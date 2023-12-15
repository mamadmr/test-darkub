# this file is a flask server that will be used to update nginx.conf file and restart nginx server

from flask import Flask, request, jsonify
import os
from functools import wraps

# start the nginx server
os.system("nginx")

password = "password"

def check_password(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        # check if the password is in the request
        if 'password' not in request.form:
            return jsonify({"message": "no password provided"}), 401
        
        # check if the password is correct
        if request.form['password'] == password:
            return func(*args, **kwargs)
        else:
            return jsonify({"message": "incorrect password"}), 401
    return wrapper



app = Flask(__name__)

@app.route('/server/update_password', methods=['POST'])
@check_password
def update_password():
    global password
    # check if the input has a new password
    if 'new_password' not in request.form:
        return jsonify({"message": "no new password"}), 400
    
    # update the password
    password = request.form['new_password']
    return jsonify({"message": "password updated"}), 200


@app.route('/server/update_path', methods=['POST'])
@check_password
def update_files():
    # name and path and the file should be in the request
    if 'name' not in request.form:
        return jsonify({"message": "no name provided"}), 400
    if 'path' not in request.form:
        return jsonify({"message": "no path provided"}), 400
    if 'file' not in request.files:
        return jsonify({"message": "no file provided"}), 400
    
    # get the file
    file = request.files['file']
    # get the path
    path = request.form['path']
    # get the name
    name = request.form['name']

    #make the path if it doesn't exist
    os.makedirs(path, exist_ok=True)
    # save the file
    file.save(os.path.join(path, name))

    return {"message": "files updated successfully"}, 200

@app.route('/server/restart_nginx', methods=['POST'])
@check_password
def restart_nginx():
    # restart nginx
    os.system("nginx -s reload")
    return {"message": "nginx restarted successfully"}, 200

app.run(host='127.0.0.1', port=6000, debug=True)

