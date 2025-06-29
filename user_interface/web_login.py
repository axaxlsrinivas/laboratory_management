from flask import Flask, render_template, request

app = Flask(__name__, template_folder='../ui/templates', static_folder='../ui/static')

@app.route('/', methods=['GET', 'POST'])
def login():
    message = ''
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == 'admin' and password == 'password123':
            message = 'Login successful!'
        else:
            message = 'Login failed. Please try again.'
    return render_template('login.html', message=message)

if __name__ == '__main__':
    app.run(debug=True)
