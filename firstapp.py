from flask import Flask, request, render_template, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///emp.db'
db = SQLAlchemy(app)

class Empl(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    desig = db.Column(db.Text, nullable=False)
    dept = db.Column(db.String(20), nullable=False, default='N/A')
    loc = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return 'Employee ID ' + str(self.id)

@app.route('/')
@app.route('/home')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/view')
def view():
    info = Empl.query.all()
    return render_template('view.html',info=info)

@app.route('/del/<int:id>')
def delid(id):
    post = Empl.query.get_or_404(id)
    db.session.delete(post)
    db.session.commit()
    return redirect('/view')

@app.route('/view/<int:id>')
def viewid(id):
    post = Empl.query.get_or_404(id)
    return render_template('viewid.html',emp=post)

@app.route('/form', methods=['GET','POST'])
def reg():
    if request.method == 'POST':
        e_id = request.form['eid']
        e_name = request.form['ename']
        e_des = request.form['edes']
        e_dept = request.form['edept']
        e_loc = request.form['eloc']
        new_empl = Empl(id=e_id, name=e_name, desig=e_des, dept=e_dept,loc=e_loc)
        db.session.add(new_empl)
        db.session.commit()
        return redirect('/view')
    else:
        return render_template('appf.html')

if __name__ == "__main__":
    app.run(debug=True)