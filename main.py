#  Колун Дэнилэ 373732 (Вар. 2)
import flask
from flask import request, render_template, url_for, redirect
from flask_sqlalchemy import SQLAlchemy


app = flask.Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///telephonebook.db'
db = SQLAlchemy(app)


class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    phone = db.Column(db.String(20), nullable=False)


@app.route('/', methods=['GET', 'POST'])
def main():
    return redirect(url_for('index'))


@app.route('/addcontact', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        phone = request.form['phone']
        name = request.form['name']
        contact = Contact(name=name, phone=phone)
        db.session.add(contact)
        db.session.commit()
    contacts = Contact.query.all()
    return render_template('index.html', contacts=contacts)


@app.route('/deletecontacts')
def deletecontacts():
    db.session.query(Contact).delete()
    db.session.commit()
    return '', 204


with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run()