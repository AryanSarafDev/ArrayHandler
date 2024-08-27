import json
import arraymod
from flask import Flask, request
from flask_session import Session


app = Flask(__name__)
send = list()
data = dict()


# @app.route('/')
# def index():
#     return json.dumps({'name': [1,2],
#                        })
# app.run()
@app.route('/test', methods=['GET', 'POST'])
def index():
    data = json.loads(request.get_data(), strict=False)
    array = data["1"]
    p = arraymod.player()
    print(data["2"])
    apple = list()

    exec('''
exec(data["2"])

        ''')
    return apple


app.debug = True
app.run()




j