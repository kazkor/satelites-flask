from flask import Flask,request,render_template

app = Flask(__name__)

@app.route('/')
def home():

    data = data = {"pred": "",
                    "max": "" }
    return render_template('index.html',user_data = data)


@app.route('/upload', methods=['POST'])
def upload_file():
    
    return "upload"


if __name__ == '__main__':
    
    app.run(debug=True,port=8000)