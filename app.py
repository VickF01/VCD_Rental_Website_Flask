import os
import pdfkit
from flask import Flask, render_template, request, flash, redirect, session, make_response
from model import Database
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed, FileRequired
from wtforms import StringField, IntegerField, SelectField, SubmitField, TextAreaField
from wtforms.validators import InputRequired, Length
from werkzeug.utils import secure_filename
from jinja2 import Environment, PackageLoader
from flask_sqlalchemy import SQLAlchemy
from model_sqlalchemy import User
from flask_mail import Mail, Message
from datetime import datetime



app = Flask(__name__)
app.secret_key = '@#$123456&*()'
app.config['SECRET_KEY'] = '@#$123456&*()'
app.config['UPLOAD_FOLDER'] = os.path.realpath('.') + '/static/files'
app.config['MAX_CONTENT_PATH'] = 10000000
app.config['SQLALCHEMY_DATABASE_URI'] = \
    'mysql://root:''@localhost/db_kelompok5'
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = True
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
db = Database()
alchemy = SQLAlchemy(app)

# class untuk form
class MyForm(FlaskForm): 
    title = StringField('Title', validators=[InputRequired()])  
    description = TextAreaField('Description', validators=[InputRequired(), Length(max=1000)])
    stock = IntegerField('Stock', validators=[InputRequired()])
    price = IntegerField('Price', validators=[InputRequired()])
    image = FileField('Image', validators=[FileRequired(), FileAllowed(['jpg', 'jpeg', 'png'], 'Images only!')]) 
    genre = SelectField('Genre', choices=[('COMEDY', 'Comedy'), ('FANTASY', 'Fantasy'), ('HORROR', 'Horror')])
    submit = SubmitField('Submit')

# formatting price ke Rp
def format_price(value):
    if value is not None:
        return f'Rp. {value:,.0f},-'

# formatting price ke Rp (singkat)
def format_price2(value):
    if value is not None:
        if abs(value) >= 1e9:
            return f'Rp. {value/1e9:.2f}B'
        elif abs(value) >= 1e6:
            return f'Rp. {value/1e6:.2f}M'
        elif abs(value) >= 1e3:
            return f'Rp. {value/1e3:.2f}k'
        else:
            return f'Rp. {value:,.0f}'
    return 'N/A'

env = Environment(loader=PackageLoader(__name__, 'templates'))
env.filters['format_price'] = format_price
env.filters['format_price2'] = format_price2

# routing website
@app.route('/')
def index():
    return render_template('index.html', homeactive = True)

@app.route('/data')
def data():
    data = db.read(None)
    app.jinja_env.filters['format_price'] = format_price

    return render_template('data.html', dataactive = True, data=data)

@app.route('/browse')
def browse():
    data = db.read(None)
    app.jinja_env.filters['format_price2'] = format_price2

    return render_template('browse.html', browseactive = True, data=data)

@app.route('/profile')
def profile():
    if session.get('email'):
        email = session['email']
        role = session['role']
        user = db.readUser(email)
        data = db.readUserTransaction(email)
        admindata = db.readTransaction()
        app.jinja_env.filters['format_price'] = format_price
        return render_template('profile.html', profileactive = True, login = True, user = user, data = data, role = role, admindata = admindata)
    else:
        return render_template('profile.html', profileactive = True, login = False)

@app.route('/about')
def about():
    return render_template('about.html', aboutactive = True)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        if db.checkUser(request.form):
            query = User(request.form['email'], request.form['name'], request.form['password'], request.form['role'])
            alchemy.session.add(query)
            alchemy.session.commit()
            flash('Registration Successful! Please Login Now!')
            return redirect('/login')
        else:
            flash('Email is invalid or already taken!')
            return redirect('/register')

    return render_template('register.html', profileactive = True)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        if db.checkLogin(request.form):
            session['email'] = email
            session['name'] = db.getUsername(email)
            session['role'] = db.readRole(email)
            return redirect('/')
        else:
            flash('Username or Password Incorrect!')
            return redirect('/login')

    return render_template('login.html', profileactive = True)

@app.route('/logout')
def logout():
    session.pop('email', None)
    session.pop('role', None)

    return redirect('/')

@app.route('/dataentry', methods =['GET', 'POST'])
def dataentry():
    form = MyForm(request.form)

    return render_template('dataentry.html', dataentryactive = True, form=form)

@app.route('/insert', methods=['POST'])
def insert():
    form = MyForm(request.form)
    if request.method == 'POST':
        f = request.files['image']
        filename = secure_filename(f.filename)
        data = request.form.to_dict()
        data['image'] = filename
        try:
            f.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            flash('File Berhasil Diupload')
            if db.create(data):
                flash('Input success')
                return redirect('/browse')
            else:
                flash('Input failed')
                return redirect('/insert')
        except Exception as e:
            flash('File Gagal Diupload: ' + str(e))

    return render_template('dataentry.html', dataentryactive=True, form=form)

@app.route('/editvcd/<int:id>')
def editvcd(id):
    session['idvcd'] = id

    return redirect('/edit')

@app.route('/edit', methods=['GET', 'POST'])
def edit():
    form = MyForm(request.form)
    id = session['idvcd']
    data = db.read(id)
    if request.method == 'POST':
        if 'image' in request.files:
            f = request.files['image']
            if f.filename != '':
                filename = secure_filename(f.filename)
                modified_data = request.form.to_dict()
                modified_data['image'] = filename
                f.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            else:
                modified_data = request.form.to_dict()
                modified_data['image'] = db.readImage(id)
            if db.update(id, modified_data):
                flash('Data successfully updated')
                return redirect('/browse')
            else: 
                flash('Data update failed')
                return redirect('/edit')

    return render_template('edit.html', data = data, form = form)

@app.route('/delete/<int:id>')
def delete(id):
    if db.delete(id):
        flash('Data Berhasil Dihapus')
        return redirect('/browse')
    else:
        flash('Data Gagal Dihapus')
        return redirect('/browse')

@app.route('/detailvcd/<int:id>')
def detailvcd(id):
    session['idvcd'] = id
    
    return redirect('/detail')

@app.route('/detail')
def detail():
    id = session['idvcd']
    data = db.read(id)
    stock = db.getStock(id)
    session.pop('idvcd', None)
    app.jinja_env.filters['format_price'] = format_price
    if stock > 0:
        outofstock = False
    else:
        outofstock = True

    return render_template('details.html', data=data, outofstock=outofstock)

@app.route('/email', methods=['GET', 'POST'])
def email():
    alluser = db.readUserEmail(None)
    emailuser = db.readUserEmail(session['email'])
    filtered_alluser = [user for user in alluser if user[0] not in [email[0] for email in emailuser]]
    # bvwqxoadvjevmtoh
    if request.method == 'POST':
        print("request.form", request.form)
        email = request.form['email']
        password = request.form['password']
        to = request.form['emailkepada']
        subject = request.form['subject']
        message = request.form['isiemail']
        app.config['MAIL_USERNAME'] = email
        app.config['MAIL_PASSWORD'] = password
        if to == 'all':
            allemail=[]
            for i in filtered_alluser:
                allemail.append(i[0])
            pesan = Message(subject, sender=email, recipients=allemail)
            pesan.body = message
        else:
            pesan = Message(subject, sender=email, recipients=[to])
            pesan.body = message
        try:
            mail = Mail(app)
            mail.connect()
            mail.send(pesan)
            flash('Email has been successfully sent to '+ to)
            return redirect('/email')
        except:
            flash('Email has been unsuccessfully sent to '+ to)
            return redirect('/email')
    return render_template('email.html', emailactive = True, filtered_alluser=filtered_alluser, emailuser=emailuser)



@app.route('/bookvcd/<int:id>')
def bookvcd(id):
    session['idvcd'] = id
    return redirect('/book') 

@app.route('/notlogged')
def notlogged():
    flash('Please login into your account first')
    return redirect('/login') 

@app.route('/book')
def book():
    id = session['idvcd']
    data = db.read(id)
    title = db.selectTitle(id)
    price = db.getPrice(id)
    session.pop('idvcd', None)
    app.jinja_env.filters['format_price'] = format_price
    return render_template('book.html', data=data, title=title, price=price)

@app.route('/confirmorder/<int:id>')
def confirmorder(id):
    email = session['email']
    name = db.getUsername(email)
    title = db.selectTitle(id)
    price = db.getPrice(id)
    date = datetime.now().strftime('%d %B %Y')
    image = db.getImage(id)
    current_stock = db.getStock(id)
    if db.makeTransaction(title, price, name, image, date, email, id):
        new_stock = current_stock - 1
        db.stockUpdate(id, new_stock)
        flash('Transaction Success')
        return redirect('/browse')
    else:
        flash('Transaction Failed')
        return redirect('/browse')

@app.route('/returnvcd/<int:id>')
def returnvcd(id):
    vcd_id = db.getVcdId(id)
    current_stock = db.getStock(vcd_id)
    if db.returnTransaction(id):
        new_stock = current_stock + 1
        db.stockUpdate(vcd_id, new_stock)
        flash('Return Success')
        return redirect('/profile')
    else:
        flash('Return Failed')
        return redirect('/profile')

@app.route('/deletetransaction/<int:id>')
def deletetransaction(id):
    if db.deleteTransaction(id):
        flash('Data has been deleted')
        return redirect('/profile')
    else:
        flash('Data deletion failed')
        return redirect('/profile')
    
@app.route('/transpdf')
def transpdf():
    data = db.readTransaction()
    app.jinja_env.filters['format_price'] = format_price
    rendered = render_template('layoutpdf.html', data = data)
    config = pdfkit.configuration(wkhtmltopdf='C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe')
    pdf = pdfkit.from_string(rendered, configuration=config, options ={"enable-local-file-access":""})
   
    
    response = make_response(pdf)
    response.headers['Content-Type'] = 'application/pdf'
    response.headers['Content-Disposition'] = 'attachment; filename=report.pdf'
    return response

if __name__ == '__main__':
    app.run(debug = True)