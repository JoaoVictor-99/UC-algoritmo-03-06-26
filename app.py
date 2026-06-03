from flask import Flask, render_template, request
import re

app = Flask(__name__)

@app.route('/')
def formulario():
    return render_template('index.html')

@app.route('/validacao', methods=['POST'])
def validacao():

    nome = request.form.get('nome', '').strip().title()
    email = request.form.get('email', '').strip().lower()
    telefone = request.form.get('telefone', '').strip()
    cpf = request.form.get('cpf', '').strip()
    cidade = request.form.get('cidade', '').strip().title()
    estado = request.form.get('estado', '').strip().upper()
    curso = request.form.get('curso', '').strip().title()
    idade = request.form.get('idade', '').strip()
    senha = request.form.get('senha', '').strip()

    erros = []

    if not nome:
        erros.append("Preencha o nome.")
    elif len(nome) < 8:
        erros.append("Nome inválido.")

    if not email:
        erros.append("Preencha o e-mail.")
    elif '@' not in email or '.com' not in email:
        erros.append("E-mail inválido.")

    telefone = telefone.replace('(', '') \
     .replace(')', '') \
     .replace('-', '') \
     .replace(' ', '')

    if not telefone.isdigit() or len(telefone) != 11:
        erros.append("Telefone inválido.")

    cpf = cpf.replace('.', '').replace('-', '')

    if not cpf.isdigit() or len(cpf) != 11:
        erros.append("cpf inválido.")

    if not cidade or len(cidade) < 3:
        erros.append("Cidade inválida.")

    if not estado or len(estado) != 2 or not estado.isalpha():
        erros.append("Estado inválido.")

    if not curso:
        erros.append("Curso obrigatóri.")

    if not idade.isdigit():
        erros.append("Idade inválida.")
    elif int(idade) < 16:
        erros.append("Idade mínima é 16 anos.")

    possui_numero = any(caractere.isdigit() for caractere in senha)

    if len(senha) < 8 or not possui_numero:
        erros.append("Senha muito fraca.")

    if erros:
        return render_template('resultado.html',
         sucesso=False,
         erros=erros)

    dados = {
        'nome': nome,
        'email': email,
        'telefone': telefone,
        'cpf': cpf,
        'cidade': cidade,
        'estado': estado,
        'curso': curso,
        'idade': idade
    }

    return render_template('resultado.html',
      sucesso=True,
      dados=dados)

if __name__ == '__main__':
    app.run(debug=True)