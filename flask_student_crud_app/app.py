from flask import Flask, render_template, request, redirect, session, url_for
from models import db, Student, User

app = Flask(__name__)
app.secret_key = "secret_key"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.db'

db.init_app(app)

with app.app_context():
    db.create_all()

    # Create default admin user (run once)
    if not User.query.first():
        admin = User(username="admin", password="admin123", role="admin")
        user = User(username="user", password="user123", role="user")
        db.session.add(admin)
        db.session.add(user)
        db.session.commit()

# ?? LOGIN
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        user = User.query.filter_by(username=username, password=password).first()

        if user:
            session['user'] = user.username
            session['role'] = user.role
            return redirect('/')

        return "Invalid credentials"

    return render_template('login.html')

# ?? LOGOUT
@app.route('/logout')
def logout():
    session.clear()
    return redirect('/login')

# ?? HOME (PROTECTED)
@app.route('/')
def index():
    if 'user' not in session:
        return redirect('/login')

    students = Student.query.all()
    return render_template('index.html', students=students, role=session['role'])

# ?? ADD STUDENT (ONLY ADMIN)
@app.route('/add', methods=['POST'])
def add():
    if session.get('role') != 'admin':
        return "Access Denied"

    name = request.form['name']
    course = request.form['course']

    student = Student(name=name, course=course)
    db.session.add(student)
    db.session.commit()

    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)