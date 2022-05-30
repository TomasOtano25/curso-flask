from flask import Flask

app = Flask(__name__)


@app.route('/')
def hola():
    return '<h1>Hola Mundo de Flask</h1>'


# python .\hola.py
if __name__ == '__main__':
    app.run(debug=True)
