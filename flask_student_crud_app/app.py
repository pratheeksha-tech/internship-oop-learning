from flask import Flask, render_template, request, redirect, url_for
from models import db, Student
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)

# Create DB
with app.app_context():
    db.create_all()

# READ (Home)
@app.route('/')
def index():
    students = Student.query.all()
    return render_template('index.html', students=students)

# CREATE
@app.route('/add', methods=['GET', 'POST'])
def add_student():
    if request.method == 'POST':
        try:
            name = request.form['name']
            course = request.form['course']

            if name == "" or course == "":
                return "Fields cannot be empty"

            student = Student(name=name, course=course)
            db.session.add(student)
            db.session.commit()

            return redirect(url_for('index'))

        except Exception as e:
            return f"Error occurred: {str(e)}"

    return render_template('add.html')

# UPDATE
@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_student(id):
    student = Student.query.get_or_404(id)

    if request.method == 'POST':
        try:
            student.name = request.form['name']
            student.course = request.form['course']

            db.session.commit()
            return redirect(url_for('index'))

        except Exception as e:
            return f"Update error: {str(e)}"

    return render_template('edit.html', student=student)

# DELETE
@app.route('/delete/<int:id>')
def delete_student(id):
    try:
        student = Student.query.get_or_404(id)
        db.session.delete(student)
        db.session.commit()
        return redirect(url_for('index'))

    except Exception as e:
        return f"Delete error: {str(e)}"

if __name__ == '__main__':
    app.run(debug=True)