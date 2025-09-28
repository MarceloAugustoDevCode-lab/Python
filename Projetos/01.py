import tkinter as tk
from tkinter import messagebox, filedialog
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import schedule
import time
import threading
import os


class InstagramAutomation:
    def __init__(self, root):
        self.root = root
        self.root.title("Automação de Postagem no Instagram")
        self.root.geometry("400x300")

        # Variáveis para armazenar dados
        self.username = tk.StringVar()
        self.password = tk.StringVar()
        self.file_path = tk.StringVar()
        self.hour = tk.StringVar(value="14")  # Hora padrão (ex: 14 para 14:00)
        self.minute = tk.StringVar(value="00")  # Minuto padrão
        self.caption = tk.StringVar(value="Post automático! #instagram")

        self.driver = None
        self.scheduled_job = None

        self.create_widgets()

    def create_widgets(self):
        # Usuário
        tk.Label(self.root, text="Usuário do Instagram:").pack(pady=5)
        tk.Entry(self.root, textvariable=self.username, width=30).pack()

        # Senha
        tk.Label(self.root, text="Senha:").pack(pady=5)
        tk.Entry(self.root, textvariable=self.password, show="*", width=30).pack()

        # Caminho do arquivo
        tk.Label(self.root, text="Caminho do arquivo (imagem/vídeo):").pack(pady=5)
        tk.Entry(self.root, textvariable=self.file_path, width=30).pack()
        tk.Button(self.root, text="Selecionar Arquivo", command=self.select_file).pack(pady=5)

        # Horário
        tk.Label(self.root, text="Hora (HH):").pack(pady=5)
        tk.Entry(self.root, textvariable=self.hour, width=10).pack()
        tk.Label(self.root, text="Minuto (MM):").pack(pady=5)
        tk.Entry(self.root, textvariable=self.minute, width=10).pack()

        # Legenda
        tk.Label(self.root, text="Legenda (opcional):").pack(pady=5)
        tk.Entry(self.root, textvariable=self.caption, width=30).pack()

        # Botão para agendar
        tk.Button(self.root, text="Agendar Postagem", command=self.schedule_post, bg="green", fg="white").pack(pady=20)

    def select_file(self):
        file_path = filedialog.askopenfilename(
            title="Selecione o arquivo para postar",
            filetypes=[("Imagens", "*.jpg *.jpeg *.png"), ("Vídeos", "*.mp4 *.mov"), ("Todos", "*.*")]
        )
        if file_path:
            self.file_path.set(file_path)

    def login_instagram(self):
        try:
            # Configurações do Chrome
            chrome_options = Options()
            chrome_options.add_argument("--no-sandbox")
            chrome_options.add_argument("--disable-dev-shm-usage")
            # chrome_options.add_argument("--headless")  # Descomente para rodar em background (sem janela visível)

            self.driver = webdriver.Chrome(options=chrome_options)
            driver = self.driver
            wait = WebDriverWait(driver, 10)

            # Acessar Instagram
            driver.get("https://www.instagram.com/accounts/login/")

            # Aguardar e preencher usuário
            username_field = wait.until(EC.presence_of_element_located((By.NAME, "username")))
            username_field.send_keys(self.username.get())

            # Preencher senha
            password_field = driver.find_element(By.NAME, "password")
            password_field.send_keys(self.password.get())

            # Clicar em login
            login_button = driver.find_element(By.XPATH, "//button[@type='submit']")
            login_button.click()

            # Aguardar redirecionamento (pular "Salvar login?" se aparecer)
            time.sleep(5)
            if "checkpoint" in driver.current_url or "salvar" in driver.page_source.lower():
                # Simular cliques para pular telas de confirmação (ajuste conforme necessário)
                try:
                    not_now_button = wait.until(
                        EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Not Now')]")))
                    not_now_button.click()
                except:
                    pass

            print("Login realizado com sucesso!")
            return True
        except Exception as e:
            messagebox.showerror("Erro no Login", f"Falha no login: {str(e)}")
            return False

    def post_to_instagram(self):
        if not self.driver:
            if not self.login_instagram():
                return

        driver = self.driver
        wait = WebDriverWait(driver, 10)

        try:
            # Ir para página inicial e clicar no botão de criar post (+)
            driver.get("https://www.instagram.com/")
            time.sleep(3)

            # Clicar no ícone de + (criar post)
            create_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[@aria-label='New post']")))
            create_button.click()

            # Selecionar mídia
            media_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@accept='image/*,video/*']")))
            media_button.send_keys(os.path.abspath(self.file_path.get()))

            # Aguardar upload e prosseguir
            time.sleep(5)
            next_button = driver.find_element(By.XPATH, "//div[text()='Next']")
            next_button.click()

            # Próximo passo (filtros, etc.) - pular
            time.sleep(2)
            next_button = driver.find_element(By.XPATH, "//div[text()='Next']")
            next_button.click()

            # Adicionar legenda
            caption_field = wait.until(
                EC.presence_of_element_located((By.XPATH, "//textarea[@aria-label='Write a caption...']")))
            caption_field.send_keys(self.caption.get())

            # Compartilhar
            share_button = driver.find_element(By.XPATH, "//div[text()='Share']")
            share_button.click()

            time.sleep(5)
            print("Postagem realizada com sucesso!")
            messagebox.showinfo("Sucesso", "Postagem agendada e realizada!")

            # Fechar navegador
            driver.quit()
            self.driver = None

        except Exception as e:
            messagebox.showerror("Erro na Postagem", f"Falha na postagem: {str(e)}")
            if self.driver:
                self.driver.quit()
                self.driver = None

    def schedule_post(self):
        try:
            hour = int(self.hour.get())
            minute = int(self.minute.get())
            if not (0 <= hour <= 23 and 0 <= minute <= 59):
                raise ValueError("Horário inválido!")

            # Cancelar agendamento anterior se existir
            if self.scheduled_job:
                schedule.cancel_job(self.scheduled_job)

            # Agendar a tarefa
            self.scheduled_job = schedule.every().day.at(f"{hour:02d}:{minute:02d}").do(self.run_post)

            messagebox.showinfo("Agendado", f"Postagem agendada para {hour:02d}:{minute:02d}!")

            # Iniciar thread para monitorar o schedule (em background)
            def run_scheduler():
                while True:
                    schedule.run_pending()
                    time.sleep(60)  # Verifica a cada minuto

            scheduler_thread = threading.Thread(target=run_scheduler, daemon=True)
            scheduler_thread.start()

        except ValueError as e:
            messagebox.showerror("Erro", str(e))

    def run_post(self):
        # Executar a postagem em uma thread separada para não bloquear GUI
        post_thread = threading.Thread(target=self.post_to_instagram)
        post_thread.start()


if __name__ == "__main__":
    root = tk.Tk()
    app = InstagramAutomation(root)
    root.mainloop()