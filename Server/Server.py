from flask import Flask, render_template,request

app = Flask(__name__,template_folder="Templates")

@app.route('/')
def index():
    return render_template('Log_in.html')

@app.route('/validate/', methods=['POST'])
def validate():
    if request.method == "POST":
        print("test")
    return render_template('Hemsida.html')
if __name__ == '__main__':
    app.run(host='192.168.1.136', port='80', debug=True)# mapping 