from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__, template_folder='../ui/templates', static_folder='../ui/static')

@app.route('/', methods=['GET', 'POST'])
def login():
    message = ''
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == 'admin' and password == 'password123':
            return redirect(url_for('items_list'))
        else:
            message = 'Login failed. Please try again.'
    return render_template('login.html', message=message)

@app.route('/items')
def items_list():
    # Example items data
    items = [
        {'id': 1, 'name': 'Beaker', 'category': 'Glassware', 'quantity': 20},
        {'id': 2, 'name': 'Test Tube', 'category': 'Glassware', 'quantity': 50},
        {'id': 3, 'name': 'Microscope', 'category': 'Equipment', 'quantity': 5},
        {'id': 4, 'name': 'Bunsen Burner', 'category': 'Equipment', 'quantity': 10},
    ]
    return render_template('items_list.html', items=items)

@app.route('/items-ui')
def items_ui():
    return render_template('items_ui.html')

if __name__ == '__main__':
    app.run(debug=True)
