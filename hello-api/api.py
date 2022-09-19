from flask import Flask, jsonify, request

app = Flask(__name__)
previous_name = None


@app.route("/hello", methods=["GET", "POST"], )
def home():
    args = request.args
    name = args.get('name')

    global previous_name
    if request.method == "GET":
        if name:
            if previous_name is None:
                message = "Hello "+name
            else:
                message = "Hello "+name+", previously known as "+previous_name
            previous_name = name
        else:
            if previous_name is not None:
                message = "Hello "+previous_name
            else:
                message = "Hello world"
        return jsonify({'message': message})
    elif request.method == "POST":
        json_input = request.get_json(silent=False)
        if "name" not in json_input:
            return "Bad method", 400
        set_previous_name(json_input["name"])
        return jsonify({"response": "OK"})


def set_previous_name(name: str):
    global previous_name
    previous_name = name


# driver function
if __name__ == '__main__':
    app.run(debug=False)
