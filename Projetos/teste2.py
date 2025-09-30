

from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'sua_chave_secreta_aqui'  # Use uma chave forte e secreta!

# Dados de produtos (substitua por seus produtos)
produtos = {
    'prod_01': {'nome': 'Produto Incrível 1', 'preco': 50.00, 'imagem': 'produto1.jpg'},
    'prod_02': {'nome': 'Produto Incrível 2', 'preco': 75.50, 'imagem': 'produto2.jpg'},
}

@app.route('/')
def index():
    return render_template('index.html', produtos=produtos)

@app.route('/produto/<id_produto>')
def produto(id_produto):
    produto_selecionado = produtos.get(id_produto)
    if not produto_selecionado:
        return "Produto não encontrado", 404
    return render_template('product.html', produto=produto_selecionado)

# Lógica de carrinho (Adicionar, remover, etc.)
@app.route('/adicionar-carrinho/<id_produto>')
def adicionar_carrinho(id_produto):
    if 'carrinho' not in session:
        session['carrinho'] = {}

    produto_selecionado = produtos.get(id_produto)
    if produto_selecionado:
        carrinho = session['carrinho']
        if id_produto in carrinho:
            carrinho[id_produto]['quantidade'] += 1
        else:
            carrinho[id_produto] = produto_selecionado
            carrinho[id_produto]['quantidade'] = 1
        session.modified = True  # Marca a sessão como modificada

    return redirect(url_for('ver_carrinho'))

@app.route('/carrinho')
def ver_carrinho():
    carrinho = session.get('carrinho', {})
    total = sum(item['preco'] * item['quantidade'] for item in carrinho.values())
    return render_template('cart.html', carrinho=carrinho, total=total)

# Lógica de checkout e pagamento
@app.route('/checkout', methods=['GET', 'POST'])
def checkout():
    if request.method == 'POST':
        # Aqui você integraria com uma API de pagamento real (como Stripe ou Mercado Pago)
        # Para o seu caso, pode ser apenas uma confirmação simples.
        return render_template('checkout_sucesso.html')

    return render_template('checkout.html')

if __name__ == '__main__':
    app.run(debug=True)