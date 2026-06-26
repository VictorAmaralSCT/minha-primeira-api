from flask import Flask, jsonify, request

app = Flask(__name__)


alunos = [
    {"id": 1, "nome": "Ana", "curso": "Técnico em Informática"},
    {"id": 2, "nome": "Bruno", "curso": "Técnico em Desenvolvimento de Sistemas"},
    {"id": 3, "nome": "Carla", "curso": "Técnico em Informática"}
]

tarefas = [
    {
        "id": 1,
        "titulo": "Estudar Flask",
        "descricao": "Criar minha primeira API",
        "concluida": False
    },
    {
        "id": 2,
        "titulo": "Fazer Exercicios",
        "descricao": "Praticar endpoints da API",
        "concluida": False
    }
]


@app.route('/', methods=['GET'])
def home():
    return jsonify({
        "message": "Minha primeira API está funcionando",
        "status": "ok"
                    })


@app.route('/health', methods=['GET'])
def health():
    return jsonify({
        "status": "ok",
        "mensagem": "API está saudável e funcionando"
    })


@app.route('/alunos', methods=['GET'])
def listar_alunos():
    return jsonify(alunos)


@app.route('/alunos/<int:id>', methods=['GET'])
def buscar_aluno(id):
    for aluno in alunos:
        if aluno["id"] == id:
            return jsonify(aluno)

    return jsonify({"erro": "Aluno não encontrado"}), 404


@app.route('/tarefas', methods=['GET'])
def listar_tarefas():
    return jsonify(tarefas)


@app.route('/tarefas/<int:id>', methods=['GET'])
def buscar_tarefa(id):
    for tarefa in tarefas:
        if tarefa["id"] == id:
            return jsonify(tarefa)

    return jsonify({"erro": "Tarefa não encontrada"}), 404


@app.route('/tarefas', methods=['POST'])
def criar_tarefa():
    dados = request.get_json()

    if not dados:
        return jsonify({"erro": "Nenhum dado foi enviado"}), 400

    if "titulo" not in dados or "descricao" not in dados:
        return jsonify({"erro":" Os campos 'titulo' e 'descricao' são obrigatórios"}), 400

    nova_tarefa={
        "id": len(tarefas)+1,
        "titulo": dados["titulo"],
        "descricao": dados["descricao"],
        "concluida": False
    }
    tarefas.append(nova_tarefa)
    print(nova_tarefa)
    return jsonify(nova_tarefa), 201


if __name__ == '__main__':
    app.run(debug=True)