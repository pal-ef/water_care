from flask import Flask, render_template, request, redirect, url_for, flash
from flask.wrappers import Request
from flask_mysqldb import MySQL

app = Flask(__name__)

# MYSQL CONNECTION
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'Jin'
app.config['MYSQL_PASSWORD'] = 'admin'
app.config['MYSQL_DB'] = 'h2o'
mysql = MySQL(app)

# Settings
app.secret_key = 'a_key_but_secret'

@app.route('/')
def Index():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM Participante')
    data = cur.fetchall()
    return render_template('index.htm', participantes = data)

@app.route('/registrar', methods=['POST'])
def Registro():
    if request.method == 'POST':
        localizacion = request.form['localizacion']
        correo       = request.form['correo'      ]
        cur          = mysql.connection.cursor()

        cur.execute('INSERT INTO Participante (localizacion, correo) VALUES (%s,%s)', (localizacion, correo))
        mysql.connection.commit()
        flash('Participante agregado')
        return redirect(url_for('Index'))
        

@app.route('/ingresar')
def Ingresar():
    return 'Ingresar'

@app.route('/edit/<id>')
def Get_registry(id):
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM Participante WHERE id = %s', (id))
    data = cur.fetchall()
    return render_template('edit.htm', participante = data[0])

@app.route('/update/<id>', methods=['POST'])
def Update(id):
    if request.method == 'POST':
        localizacion = request.form['localizacion']
        correo = request.form['correo']
        cur = mysql.connection.cursor()
        cur.execute("""
            UPDATE Participante
            SET localizacion = %s, correo = %s
            WHERE id = %s
        """, (localizacion,correo,id))
        mysql.connection.commit()
        flash('El participante ha sido actualizado')
        return redirect(url_for('Index'))
    

@app.route('/delete/<string:id>')
def Delete_registry(id):
    cur = mysql.connection.cursor()
    cur.execute('DELETE FROM Participante WHERE id = {0}'.format(id))
    mysql.connection.commit()
    flash('Participante ha sido removido')
    return redirect(url_for('Index'))

if __name__ == '__main__':
    app.run(port = 2077, debug = True)