from flask import Flask, jsonify, request

app = Flask(__name__)

comics = []

@app.route('/')
def home():
    diccionario_envio = {
        "msg": 'Servidor funcionando correctamente, despliegue ejemplo clase.',
        "status": 200
    }
    
    return jsonify(diccionario_envio)


@app.route('/comic', methods=['POST'])
def crear_comic():
    data_comics = request.get_json()
    for comic in data_comics:
        comics.append(comic)

    return jsonify({
        "msg": 'Comics creados exitosamente',
        "status": 200
    })

@app.route('/comic', methods=['PUT'])
def actualizar_comic():
    data = request.get_json()
    id = data.get('id')
    title = data.get('title')
    copies = data.get('copies')
    available = data.get('available')


    for i in range(len(comics)):
        if comics[i].get('id') == id:
            comics[i]['title'] = title
            comics[i]['copies'] = copies

            return jsonify({
                "msg": 'Comic actualizado exitosamente',
                "status": 201
            })

    return jsonify({
        "msg": 'Comic no encontrado',
        "status": 422
    })

@app.route('/comic/<string:id>', methods=['DELETE'])
def eliminar_comic(id):

    for i in range(len(comics)):
        if comics[i].get('id') == id:
            comics.pop(i)   # 1 | 2| 3| 4
            return jsonify({
                "msg": 'Comic eliminado exitosamente',
                "status": 200
            })

    return jsonify({
        "msg": 'Comic no encontrado',
        "status": 422
    })

@app.route('/comic', methods=['GET'])
def buscar_comic():
    comics_out = []

    title = request.args.get('title')
    copies = request.args.get('copies')

    for comic in comics:
        if comic.get('title') == title or comic.get('copies') > int(copies):
            comics_out.append(comic)
            
    print(comics_out)

    if len(comics_out)>0:
        return jsonify(comics_out)

    return jsonify({
        "msg": 'No hay coincidencias encontradas',
        "status": 422
    })

@app.route('/comic/list', methods=['GET'])
def obtener_comics():

    return jsonify(
        comics
    )


if __name__ == "__main__":
    app.run(port=3004,debug=True)


