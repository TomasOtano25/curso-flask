from flask import Flask

app = Flask(__name__)


@app.route('/hola')
def hola():
    return 'Hola Mundo de Flask'


# python .\hola.py
if __name__ == '__main__':
    app.run()
