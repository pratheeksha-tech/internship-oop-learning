from flask import Flask, render_template, request

app = Flask(__name__)

# In-memory history (last 5 calculations)
history = []

@app.route('/')
def home():
    return render_template('index.html', history=history)

@app.route('/calculate', methods=['POST'])
def calculate():
    num1 = float(request.form['num1'])
    num2 = float(request.form['num2'])
    operation = request.form['operation']

    if operation == 'add':
        result = num1 + num2
    elif operation == 'sub':
        result = num1 - num2
    elif operation == 'mul':
        result = num1 * num2
    elif operation == 'div':
        result = num1 / num2 if num2 != 0 else "Cannot divide by zero"
    else:
        result = "Invalid operation"

    # store history
    history.append(f"{num1} {operation} {num2} = {result}")

    # keep only last 5
    if len(history) > 5:
        history.pop(0)

    return render_template('result.html', result=result)

# dynamic greeting route
@app.route('/greet/<name>')
def greet(name):
    return f"Hello {name}, welcome to Flask application!"

if __name__ == '__main__':
    app.run(debug=True)