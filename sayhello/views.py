from flask import flash,redirect,url_for,render_template
from sqlalchemy import desc

from sayhello import app,db
from sayhello.forms import HelloForm
from sayhello.models import Message

@app.route('/',methods=['GET','POST'])
def index():
    db.create_all()
    form=HelloForm()
    if form.validate_on_submit():
        name=form.name.data
        body=form.body.data
        message=Message(body=body,name=name)
        db.session.add(message)
        db.session.commit()
        flash('Your Message have been sent to the word!')
        return redirect(url_for('index'))
    messages=Message.query.order_by(desc(Message.timestamp)).all()
    return render_template('index.html',form=form,messages=messages)



