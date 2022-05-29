"""
@author: Alejandro Garcia
@date:   Saturday, 28 May 2022, 11:59 PM
@description: Iot I.4
"""
# Modules inclusion
from flask import Flask, request

app = Flask('__main__')
user = {
    "matricula":"111111",
    "first_name":"Alejandro",
    "last_name":"Garcia",
    "phone":"614-3936026"
}
# methods

# testing the metod get
@app.route('/', methods=['GET'])
def go_home():
    return "Bienvenido"

# doing get for the users
@app.route('/users', methods=['GET'])
def get_users():
    return user

# method POST

# save one user
@app.route('/users', methods=['POST'])
def save_user():
    user = request.json
    print(user)
    return user

# save a device 
@app.route('/devices', methods=['POST'])
def save_device():
    device = request.json
    print(device)
    return device

# calling 
if __name__ == '__main__':
    app.run(debug=True, port=5000, host='0.0.0.0')