from flask import Flask,render_template, request
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

@app.route('/upload', methods = ['GET', 'POST'])
def upload_file():
   if request.method == 'POST':
      f = request.files['file']
      name=str(uuid.uuid4())+".jpg"
      print(name)
      f.save((name))
      image=run_model_memory.run(name)
      res={"data":image}
      return res

app.run(debug=True, host='0.0.0.0',port=5000)

