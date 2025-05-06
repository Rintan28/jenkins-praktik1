from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Halo dari Jenkins Multibranch Pipeline RaWRrr!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)