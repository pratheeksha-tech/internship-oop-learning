from flask import Flask, render_template, request, redirect, session, url_for
from config import Config
from models import db, User, Student
from functools import wraps

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)

with app.app_context():
    db.create_all()

# ---------------- LOGIN REQUIRED ----------------
def login_required(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        if 'user_id' not in session:
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return wrapper

# ---------------- REGISTER ----------------
@app.route('/', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        existing = User.query.filter_by(username=username).first()
        if existing:
            return "User already exists"

        user = User(username=username, password=password)
        db.session.add(user)
        db.session.commit()

        return redirect(url_for('login'))

    return render_template('register.html')

# ---------------- LOGIN ----------------
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        user = User.query.filter_by(username=username, password=password).first()

        if user:
            session['user_id'] = user.id
            session['role'] = user.role
            return redirect(url_for('index'))
        else:
            return "Invalid credentials"

    return render_template('login.html')

# ---------------- LOGOUT ----------------
@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))

# ---------------- DASHBOARD ----------------
@app.route('/index')
@login_required
def index():
    students = Student.query.all()
    return render_template('index.html', students=students)

# ---------------- ADD ----------------
@app.route('/add', methods=['GET', 'POST'])
@login_required
def add():
    if request.method == 'POST':
        student = Student(
            name=request.form['name'],
            course=request.form['course']
        )
        db.session.add(student)
        db.session.commit()
        return redirect(url_for('index'))

    return render_template('add.html')

# ---------------- EDIT ----------------
@app.route('/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit(id):
    student = Student.query.get(id)

    if request.method == 'POST':
        student.name = request.form['name']
        student.course = request.form['course']
        db.session.commit()
        return redirect(url_for('index'))

    return render_template('edit.html', student=student)

# ---------------- RUN ----------------
if __name__ == "__main__":
    app.run(debug=True)