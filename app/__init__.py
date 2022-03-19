from flask import Flask, render_template

def create_app():
    app = Flask(__name__)

    @app.route('/')
    def homepage():
        return render_template('index.html')

    @app.route('/about/')
    def about():
        return 'This is the about page'

    return app