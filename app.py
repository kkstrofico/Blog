from flask import Flask,render_template

app = Flask(__name__)

#Routes
@app.route('/')
def index():
    return render_template('index.html')

#Inicia la app en modo debug
def run_app():
    if __name__ == '__main__':# Se asegura que la app solo se ejecute en este modulo
        app.run(debug=True)
run_app()