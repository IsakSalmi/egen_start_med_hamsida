from flask import Flask, render_template,request,Response
import Magic_packet as MP

username = "isak"
password = "test123"

app = Flask(__name__,template_folder="Templates")

@app.route('/', methods=['POST'])
def index_POST():
    if request.method == "POST" and request.json == username + "/" + password:
        MP.Magic_packet()
        return Response("OK",200)
    else:
        return Response("invalid",400)

@app.route('/',methods=['GET'])
def index_GET():
    return render_template('Log_in.html')

@app.route('/Log_in',methods=['GET','POST'])
def Log_in():
    return render_template('Hemsida.html')

if __name__ == '__main__':
    app.run(host='', port='80', debug=True)