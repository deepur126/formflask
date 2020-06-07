from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hai, My first Sample page'

@app.route('/home/<string:name>')
def home(name):
    #return '''<title>My App</title>'Hai, '+name '''
    return 'Hai, '+name

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/form', methods=['GET','POST'])
def reg():
    return render_template('form.html')

if __name__ == "__main__":
    app.run(debug=True)