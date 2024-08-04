from flask import Flask, render_template, request, redirect, url_for, flash 
import sqlite3 as sql 

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'

@app.route("/")
@app.route("/index")
def index():
    conn = sql.connect('datebase/Banco_dados.db')
    conn.row_factory = sql.Row
    cur =conn.cursor() 
    cur.execute('SELECT * FROM Usuario')
    data = cur.fetchall()
    
    return render_template("index.html", datas=data)


@app.route("/add_user", methods=["POST", "GET"])
def add_user():
    if request.method == "POST":
        nome = request.form['nome']
        idade = request.form['idade']
        rua = request.form['rua']
        cidade = request.form['cidade']
        numero = request.form['numero']
        estado = request.form['estado']
        email = request.form['email']
        conn =  sql.connect('datebase/Banco_dados.db')
        cur = conn.cursor()
        cur.execute("""INSERT INTO Usuario(
        nome, idade, rua, cidade, numero, estado, email
        ) values (?,?,?,?,?,?,?)
        """, (nome, idade, rua, cidade, numero, estado, email))
        conn.commit()
        flash("Dado cadastrado","success")
        return redirect(url_for("index"))
    return render_template("add_user.html")

@app.route("/edit_user/<string:id>", methods=["POST", "GET"])
def edit_user(id):
    if request.method == "POST":
        nome = request.form['nome']
        idade = request.form['idade']
        rua = request.form['rua']
        cidade = request.form['cidade']
        numero = request.form['numero']
        estado = request.form['estado']
        email = request.form['email']
        conn = sql.connect('datebase/Banco_dados.db')
        cur = conn.cursor()  
        cur.execute("""UPDATE Usuario SET 
            nome=?, idade=?, rua=?, cidade=?, numero=?,
            estado=?, email=? WHERE id=?
            """,(nome, idade, rua, cidade, numero, estado, email, id)
        )
        conn.commit()
        flash("Dados atualizados", "success")
        return redirect(url_for("index"))
    
    conn = sql.connect('datebase/Banco_dados.db')
    conn.row_factory = sql.Row
    cur =conn.cursor()
    cur.execute("SELECT * FROM Usuario WHERE id=?",(id,))
    data = cur.fetchone()
    return render_template("edit_user.html", datas=data)


@app.route("/delete_user/<string:id>", methods=['GET'])
def delete_user(id):
    conn = sql.connect("datebase/banco_dados.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM Usuario WHERE id=?", (id,))
    conn.commit()
    flash("Dados deletados", "warning")
    return redirect(url_for("index"))

if __name__ == '__main__':
    app.run(debug=True)
    