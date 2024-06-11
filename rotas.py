from flask import Flask, request, jsonify
import usuario as usuario_func

app = Flask(__name__)

@app.route('/usuarios', methods=['POST'])
def criar_usuario():
    data = request.json
    if 'nome' not in data or 'senha' not in data:
        return jsonify({'mensagem': 'Nome e senha são obrigatórios'}), 400
    novo_usuario = {'nome': data['nome'], 'senha': data['senha']}
    usuario_id = usuario_func.criar_usuario(novo_usuario)
    return jsonify({'mensagem': 'Usuário criado com sucesso', 'id': usuario_id}), 201

@app.route('/usuarios/login', methods=['POST'])
def login_usuario():
    data = request.json
    nome = data.get('nome')
    senha = data.get('senha')

    # Verificar as credenciais do usuário
    if usuario_func.verificar_credenciais(nome, senha):
        return jsonify({'mensagem': 'Login bem-sucedido'}), 200
    else:
        return jsonify({'mensagem': 'Usuário ou senha incorretos'}), 401


@app.route('/usuarios', methods=['GET'])
def listar_usuarios():
    usuarios = usuario_func.listar_usuarios()
    return jsonify(usuarios), 200

@app.route('/usuarios/<int:id>', methods=['GET'])
def ler_usuario(id):
    user = usuario_func.ler_usuario(id)
    if user:
        return jsonify(user), 200
    else:
        return jsonify({'mensagem': 'Usuário não encontrado'}), 404

@app.route('/usuarios/<int:id>', methods=['PUT'])
def atualizar_usuario(id):
    data = request.json
    if 'nome' not in data or 'senha' not in data:
        return jsonify({'mensagem': 'Nome e senha são obrigatórios'}), 400
    usuario_func.atualizar_usuario(id, data['nome'], data['senha'])
    return jsonify({'mensagem': 'Usuário atualizado com sucesso'}), 200

@app.route('/usuarios/<int:id>', methods=['DELETE'])
def deletar_usuario(id):
    usuario_func.deletar_usuario(id)
    return jsonify({'mensagem': 'Usuário deletado com sucesso'}), 200

if __name__ == '__main__':
    app.run(debug=True)