from flask import redirect, url_for, session, render_template
from . import main_test
from .forms import NameForm, SignUpForm
from .. import db

@main_test.route('/', methods=['GET', 'POST'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        session['name'] = form.name.data
        return redirect(url_for('main_test.index'))
    return render_template('index.html', form=form, name=session.get('name'))

@main_test.route('/sign_up', methods=['GET','POST'])
def sign_up():
    form = SignUpForm()
    if form.validate_on_submit():
        db.users.insert_one({"name": form.name.data})
        return redirect(url_for('main_test.index'))
    return render_template('sign_up.html', form = form)

@main_test.route('/test_db', methods=['GET'])
def test_db():
    coll = db['restaurants']
    restaurants = list(coll.find({"grades.score": {"$gt": 90}}))
    return render_template('db_test.html', name=session.get('name'), restaurants = restaurants)

@main_test.route('/logout')
def logout():
    session['name'] = None
    return redirect(url_for('main_test.index'))
