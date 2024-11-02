from flask import Flask,render_template

app = Flask(__name__)

#Routes
@app.route('/')
def index():
    return render_template('index.html')

#Inicia la app en modo debug
def run_app():
    if __name__ == '__main__':
        app.run(debug=True)
run_app()