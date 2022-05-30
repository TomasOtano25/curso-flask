from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hola():
    mensaje = 'Hola Mundo con Flask'

    return render_template('index.html', msm=mensaje)


@app.route('/blogs')
def blog():
    b1 = Blog('Que es Python?', 'Descripcion de Blog 1')

    b2 = Blog('Que es Flask?', 'Descripcion de Blog 2')

    blogs = [b1, b2]

    return render_template('blog.html', blogs=blogs)


class Blog:
    def __init__(self, titulo, desc):
        self.titulo = titulo
        self.desc = desc


# python .\hola.py
if __name__ == '__main__':
    app.run(debug=True)
