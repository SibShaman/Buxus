from flask import Flask
from datetime import datetime
from flask import render_template
from jinja2 import Template
from os import environ

app = Flask(__name__)


@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'html/index.html',
        title='Buxus',
        year=datetime.now().year,
    )


@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'html/about.html',
        title='О нас',
        year=datetime.now().year,
        message='Your application description page.'
    )


@app.route('/price')
def price():
    """Renders the about page."""
    return render_template(
        'html/price.html',
        title='Цены',
        year=datetime.now().year,
        message='Your application description page.'
    )


@app.route('/portfolio')
def portfolio():
    """Renders the about page."""
    return render_template(
        'html/portfolio.html',
        title='Портфолио',
        year=datetime.now().year,
        message='Your application description page.'
    )


@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'html/contact.html',
        title='Контакты',
        year=datetime.now().year,
        message='Your contact page.'
    )


if __name__ == '__main__':
    app.run()
