from flask import Flask, render_template, request
from flask_mysqldb import MySQL

app = Flask("__name__")

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'fatec'
app.config['MYSQL_DB'] = 'jean'

mysql = MySQL(app)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/quemsomos")
def quemsomos():
    return render_template("quemSomos.html")

@app.route("/contato", methods=['GET', 'POST'])
def contato():
    if request.method == 'POST':
        email = request.form['email']
        assunto = request.form['assunto']
        descricao = request.form['descricao']

        cur = mysql.connection.cursor()
        cur.execute('INSERT INTO contato(email, assunto, descricao) VALUES (%s, %s, %s)', (email, assunto, descricao))

        mysql.connection.commit()

        cur.close()

        return render_template('usuarios.html')

    return render_template('contato.html')

@app.route('/usuarios')
def usuarios():
    cur = mysql.connection.cursor()

    usuarios = cur.execute('SELECT * FROM contato')

    if usuarios > 0:
        usuariosDetails = cur.fetchall()


    return render_template('usuarios.html', usuariosDetails=usuariosDetails)

    if __name__ == '__main__':
        app.run()
