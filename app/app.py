from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():

    return "home"


@app.route('/upload', methods=['POST'])
def upload_file():
    
    return "upload"


if __name__ == '__main__':
    
    app.run(debug=True,port=8000)