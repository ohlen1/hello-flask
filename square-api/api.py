from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/square/<int:num>', methods=['GET'])
def disp(num):
    return jsonify({'result': num**2})


# driver function
if __name__ == '__main__':
    app.run(debug=False)
