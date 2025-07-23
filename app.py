from flask import Flask, render_template, redirect, url_for, request, flash
from config import Config
from models import db, Subscriber
from forms import SubscriberForm, UpdateForm
from datetime import datetime

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

with app.app_context():
    db.create_all()

@app.route('/', methods=['GET', 'POST'])
def index():
    form = SubscriberForm()
    if form.validate_on_submit():
        new_subscriber = Subscriber(
            email=form.email.data,
            plan=form.plan.data
        )
        db.session.add(new_subscriber)
        db.session.commit()
        flash("Subscriber added!", "success")
        return redirect(url_for('index'))

    subscribers = Subscriber.query.order_by(Subscriber.subscribed_on.desc()).all()
    return render_template('index.html', form=form, subscribers=subscribers)

@app.route('/delete/<int:id>')
def delete(id):
    subscriber = Subscriber.query.get_or_404(id)
    db.session.delete(subscriber)
    db.session.commit()
    flash("Subscriber deleted!", "info")
    return redirect(url_for('index'))

@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    subscriber = Subscriber.query.get_or_404(id)
    form = UpdateForm()

    if form.validate_on_submit():
        subscriber.plan = form.plan.data
        db.session.commit()
        flash("Subscription plan updated!", "success")
        return redirect(url_for('index'))

    form.plan.data = subscriber.plan
    return render_template('update.html', form=form, subscriber=subscriber)

if __name__ == '__main__':
    app.run(debug=True)