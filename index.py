from flask import Flask, request, render_template, redirect, flash, session, send_from_directory
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = '{SGBD}://{usuario}:{senha}@{servidor}/{database}'.format(
        SGBD='mysql',
        usuario='root',
        senha='123',
        servidor='localhost',
        database='webrotas'
    )

app.config['SECRET_KEY'] = '123'
db = SQLAlchemy(app)


class clientes(db.Model):
    user = db.Column(db.String(30), nullable=False)
    password = db.Column(db.String(15))
    confirmPassword = db.Column(db.String(15))
    email = db.Column(db.String(20))
    dateBirthday = db.Column(db.Date)
    cpf = db.Column(db.String(11), primary_key=True, nullable=False)


@app.route('/')
def home():
    return render_template("ExemploNovo.html")

@app.route('/PaginaCadastro', methods=['GET', 'POST'])
def PaginaCadastro():
    return render_template("PaginaCadastro.html")


@app.route('/Cadastrar', methods=['GET', 'POST'])
def Cadastrar():
    if request.method == 'POST':
        user = request.form['user']
        password = request.form['password']
        confirmPassword = request.form['confirmPassword']
        email = request.form['email']
        dateBirthday = request.form['dateBirthday']
        cpf = request.form['cpf']
        
        if not(user and password and confirmPassword and email and dateBirthday and cpf):
            flash("Erro ao cadastrar, Existem campos vazios!",'error')
            return redirect("/PaginaCadastro")
        
        if (len(user) > 30 or len(password) > 15 or len(confirmPassword) > 15 or len(email) > 20 or len(cpf) > 11):
            flash("Erro ao cadastrar, algum dos campos passou do tamanho excedido!",'error')
            return redirect("/PaginaCadastro")

        if(password != confirmPassword):
            flash("Erro ao cadastrar, senha e confirmação de senha estão diferentes!",'error')
            return redirect("/PaginaCadastro")

                
        new_user = clientes(user=user, password=password, confirmPassword=confirmPassword, email=email, dateBirthday=dateBirthday, cpf=cpf)
        db.session.add(new_user)
        db.session.commit()

        flash("Cadastro realizado com sucesso!",'sucess')
        return redirect("/ExemploNovo")

    return render_template("PaginaCadastro.html")

@app.route('/ExemploNovo', methods=['GET', 'POST'])
def ExemploNovo():
    return render_template("ExemploNovo.html")

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = request.form['user']
        password = request.form['password']
        cliente = clientes.query.filter_by(user=user, password=password).first()
        if cliente:
            session['user'] = cliente.user  # Armazena o nome do usuário na sessão
            return redirect('/MainPage')
        else:
            flash('Credenciais inválidas. Tente novamente.', 'error')
            return redirect('/ExemploNovo')
    return render_template('ExemploNovo.html')


@app.route('/MainPage', methods=['GET', 'POST'])
def MainPage():
    return render_template("MainPage.html")

@app.route('/static/<path:filename>')
def serve_static(filename):
    return send_from_directory('static', filename)

@app.route('/returnPaginaLogin', methods=['GET', 'POST'])
def returnPaginaLogin():
    return redirect('/ExemploNovo')

if __name__ == "__main__":
    app.run(debug=True)