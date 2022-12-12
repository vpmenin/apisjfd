from flask import Flask, make_response, jsonify,request
from bd import Carros
import mysql.connector

app = Flask(__name__)
##Para o Flask não ordenar o Json
app.config['JSON_SORT_KEYS']=False

def bd_connect():
    mydb = mysql.connector.connect(
        host='185.12.116.131',
        user='startcod_jfd',
        password='Dom250ptbr',
        database='startcod_jfd',
    )
    return mydb;

@app.route('/cursos',methods=['GET'])
def get_cursos():
    try:
        mydb = bd_connect()
    except mysql.connector.Error as e:
        cursos = list()
        cursos.append(
            {
                "id": 0,
            }
        )
        return make_response(
            jsonify(
                mensagem= e.msg,
                dados = cursos)
        )

    my_cursor = mydb.cursor()
    my_cursor.execute('SELECT * FROM cursos')
    meus_cursos = my_cursor.fetchall()

    cursos = list()
    for curso in meus_cursos:
        cursos.append(
            {
                "id": curso[0],
                "curso": curso[1],
                "datainclusao": curso[2],
                "valor": curso[3],
                "linkcurso": curso[4],
            }
        )
    my_cursor.close
    mydb.close

    return make_response(
        jsonify(
            mensagem='Lista de cursos.',
            dados = cursos)
        )

@app.route('/cursosbyid',methods=['GET'])
def get_cursosbyid():
    curso = request.json
    try:
        mydb = bd_connect()
    except mysql.connector.Error as e:
        cursos = list()
        cursos.append(
            {
                "id": 0,
            }
        )
        return make_response(
            jsonify(
                mensagem= e.msg,
                dados = cursos)
        )

    my_cursor = mydb.cursor()
    my_cursor.execute(f"SELECT * FROM cursos WHERE idcurso = '{curso['id']}'")

    meus_cursos = my_cursor.fetchall()

    cursos = list()
    for curso in meus_cursos:
        cursos.append(
            {
                "id": curso[0],
                "curso": curso[1],
                "datainclusao": curso[2],
                "valor": curso[3],
                "linkcurso": curso[4],
            }
        )
    my_cursor.close
    mydb.close

    return make_response(
        jsonify(
            mensagem='Lista de cursos.',
            dados = cursos)
        )


@app.route('/carros', methods=['POST'])
def create_carro():
    carro = request.json
    my_cursor = mydb.cursor()
    sql = f"INSERT INTO carros (marca, modelo,ano) VALUES('{carro['marca']}','{carro['modelo']}','{carro['ano']}')"
    print(sql)
    my_cursor.execute(sql)
    mydb.commit()
     
    return make_response(
        jsonify(
            mensagem='Automóvel cadastrado!',
            carro=carro
            )
    )

@app.route('/carros', methods=['DELETE'])
def delete_carro():
    carro = request.json
    my_cursor = mydb.cursor()
    sql = f"DELETE FROM carros WHERE id = '{carro['id']}'"
    my_cursor.execute(sql)
    mydb.commit()
     
    return make_response(
        jsonify(
            mensagem='Automóvel deletado!',
            carro=carro
            )
    )

@app.route('/carros', methods=['PUT'])
def update_carro():
    carro = request.json
    my_cursor = mydb.cursor()
    sql = f"UPDATE carros SET marca= '{carro['marca']}' WHERE id = '{carro['id']}'"
    print(sql)
    my_cursor.execute(sql)
    mydb.commit()
     
    return make_response(
        jsonify(
            mensagem='Automóvel alterado!',
            carro=carro
            )
    )

app.run()

