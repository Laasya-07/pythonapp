from flask import Flask
app = Flask(__name__)

@app.route('/test')

def hello():
    return "Connected to this sample application"
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001, debug=True)