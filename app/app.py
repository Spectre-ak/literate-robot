from flask import Flask,render_template, request
from flask.helpers import send_file
import run_model_memory
import uuid

app = Flask(__name__)

@app.route("/")
def helloworld():
    print(str(uuid.uuid4()))
    return render_template("uploadImage.html")

@app.route("/ru")
def helloworqld():
    return "Hello World!"

@app.route("/run")
def runModelRest():
    run_model_memory.run()
    return "running"

@app.route("/image/<name>")
def data(name):
    print(name)
    return send_file(name,mimetype='image/gif')

@app.route('/upload', methods = ['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['file']
        id=str(uuid.uuid4())
        name=id+".jpg"
        print(name)
        f.save((name))
        try:
            result=run_model_memory.run(name,id)
            #image_url="http://localhost:5000/image/"+result  #https://literate-robot.azurewebsites.net/
            image_url="https://literate-robot.azurewebsites.net/image/"+result  #
            
            return image_url
        except Exception as e:
            return "image resolution must be atleast 1280x720"


app.run(debug=True, host='0.0.0.0',port=5000)

