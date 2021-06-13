from flask import Flask
import run_model_memory

app = Flask(__name__)

@app.route("/")
def helloworld():
    return "Hello World!"

@app.route("/ru")
def helloworqld():
    return "Hello World!"

@app.route("/run")
def runModelRest():
    run_model_memory.run()
    return "running"

app.run(debug=True, host='0.0.0.0',port=5000)

