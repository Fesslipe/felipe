from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home():
    return '''
        <html>
            <body>
                <h1>Avaliação contínua: Aula 030</h1>
                <ul>
                    <li><a href="/">Home</a></li>
                    <li><a href="/identificacao">Identificação</a></li>
                    <li><a href="/contexto_requisicao">Contexto da Requisição</a></li>
                </ul>
            </body>
        </html>
    '''

@app.route('/identificacao/<nome>/<prontuario>/<instituicao>')
@app.route('/identificacao')
def identificacao(nome="Felipe", prontuario="3020673", instituicao="IFSP"):
    return '''
        <html>
            <body>
                <h1>Avaliação contínua: Aula 030</h1>
                <h2>Aluno: {nome}</h2>
                <h2>Prontuário: {prontuario}</h2>
                <h2>Instituição: {instituicao}</h2>
                <p><a href="/">Voltar</a></p>
            </body>
        </html>
    '''.format(nome=nome, prontuario=prontuario, instituicao=instituicao)

@app.route('/contexto_requisicao')
def contexto_requisicao():
    user_agent = request.headers.get('User-Agent')
    remote_addr = request.remote_addr
    host = request.host
    return '''
        <html>
            <body>
                <h1>Avaliação contínua: Aula 030</h1>
                <h2>Seu navegador é: {user_agent}</h2>
                <h2>O IP do computador remoto é: {remote_addr}</h2>
                <h2>O host da aplicação é: {host}</h2>
                <p><a href="/">Voltar</a></p>
            </body>
        </html>
    '''.format(user_agent=user_agent, remote_addr=remote_addr, host=host)

if __name__ == '__main__':
    app.run(debug=True)
