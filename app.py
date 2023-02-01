from flask import Flask, render_template
from controllers.library_controller import library_blueprint

app = Flask(__name__)

app.register_blueprint(library_blueprint)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)