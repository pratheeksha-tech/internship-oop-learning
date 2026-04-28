from flask import Flask, render_template

app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return render_template('home.html')

# Dashboard route with dynamic data
@app.route('/dashboard/<username>')
def dashboard(username):
    user_data = {
        "name": username,
        "role": "Intern",
        "project": "Flask Routing & Templates"
    }
    return render_template('dashboard.html', user=user_data)

if __name__ == '__main__':
    app.run(debug=True)