from flask import Flask, request
import json

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def hello_world():
    data = {}
    if request.method == 'POST':
        data = request.json
        print(data)
    return json.dumps(data)


if __name__ == '__main__':
    app.run()
