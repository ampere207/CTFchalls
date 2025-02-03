from flask import Flask, request, make_response

app = Flask(__name__)

@app.route('/')
def home():
    cookie = request.cookies.get('auth')
    if cookie == "admin":
        return "Congratulations! Here is your flag: FLAG{cookie_monster_hacked}", 200
    return "Access Denied! Try modifying the cookie.", 403

@app.route('/login')
def login():
    resp = make_response("You are now logged in as guest!")
    resp.set_cookie("auth", "guest")
    return resp

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
