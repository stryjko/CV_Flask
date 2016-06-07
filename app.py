"""Main application"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    """Render cv page"""
    return render_template('main.html')

@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page"""
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True)
