from flask import redirect, url_for, session, render_template
from . import main
from .forms import NameForm, SignUpForm
from .. import db

@main.route('/', methods=['GET', 'POST'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        session['name'] = form.name.data
        return redirect(url_for('main.index'))
    return render_template('index.html', form=form, name=session.get('name'))

@main.route('/sign_up', methods=['GET','POST'])
def sign_up():
    form = SignUpForm()
    if form.validate_on_submit():
        db.users.insert_one({"name": form.name.data})
        return redirect(url_for('main.index'))
    return render_template('sign_up.html', form = form)

@main.route('/test_db', methods=['GET'])
def test_db():
    coll = db['restaurants']
    restaurants = list(coll.find({"grades.score": {"$gt": 90}}))
    return render_template('db_test.html', name=session.get('name'), restaurants = restaurants)

@main.route('/logout')
def logout():
    session['name'] = None
    return redirect(url_for('main.index'))
