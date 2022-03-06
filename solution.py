from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/hello', methods = ['POST', 'GET'])
def index():
    if request.args.get('name'):
        return "Hello " + str(request.args.get('name'))
    return "Hello World"

#app.run(host='0.0.0.0', port=81)

@app.route('/hello-json', methods = ['POST', 'GET']) #methods??
def index2(): #func name
    return {"text": "Hello World from Dictionary"}

#app.run(host='0.0.0.0', port=81) #the same address?

@app.route('/hello-html', methods = ['POST', 'GET'])
def index3():
    return "<h1>Hello World</h1><p>Subtext</p>"

#app.run(host='0.0.0.0', port=81)

@app.route('/hello/<name>', methods = ['POST', 'GET'])
def whatevername(name):
   return 'Hello ' + str(name)


@app.route('/hello/<name>/change/<amount>', methods = ['POST', 'GET'])
def whatevername2(name, amount):
    value = 10 - int(amount)
    return 'Hello ' + str(name) + ', ' + 'your change is ' + str(value)

@app.route('/reflect', methods = ['POST', 'GET'])
def name3():
    value = request.data
    print(value)
    return "Hello " + str(value)

@app.route('/reflect/plex', methods = ['POST', 'GET'])
def name4():
    payload = request.json
    data = {}
    for key in payload:
        if type(key) == str:
            val = payload[key]
            now = "plex_" + key
            data[now] = val
    return data

@app.route('/reflect/plex/form', methods = ['POST', 'GET'])
def name5():
    payload = request.json
    final = {}
    for key in payload:
        val = payload[key]
        now = "plex_" + key
        final[now] = val
    return final

app.run(host='0.0.0.0', port=81, debug = True)