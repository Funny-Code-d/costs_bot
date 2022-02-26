from flask import Flask, jsonify, request
app = Flask(__name__)

unit =     {
        "user_id" : 1,
        "first_name" : "Denis",
        "last_name" : "Sosnin"
    }

return_dict = [
    {
        "user_id" : 1,
        "first_name" : "Denis",
        "last_name" : "Sosnin"
    },
    {
        "user_id" : 2,
        "first_name" : "Sasha",
        "last_name" : "Sanina"
    }
]


@app.route('/api/v1/user/settings/', methods=['GET'])
def get_user():
    return jsonify(return_dict)

@app.route('/api/v1/user/settings/', methods=['POST'])
def create_user():
    getting_data = request.json
    
    return_dict.append(getting_data)
    return jsonify(return_dict)


@app.route("/", methods=["GET"])
def index():
    return "<h1>REST API информационной системы учёта расходов</h1><p>Owner by Sosnin Denis</p>"

if __name__ == '__main__':
    app.run()