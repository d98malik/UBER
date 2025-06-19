from flask import Flask,request, render_template
from account_handling import Account

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("signup.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/passenger", methods = ["POST"])
def passenger_account():
    name = request.form["name"]
    email = request.form["email"]
    password = request.form["password"]

    info = {"name": name,
            "_id": email,
            "password": password
            }
    p_a = Account("passengers")
    p_a.create_account(info)    
    return render_template("login.html")

@app.route("/driver", methods = ["POST"])
def driver_account():
    name = request.form["name"]
    email = request.form["email"]
    password = request.form["password"]
    v_number = request.form["vehicle number"]
    l_number = request.form["license number"]

    info = {"name": name,
            "_id": email,
            "password": password,
            "v_number": v_number,
            "v_licence": l_number
            }
    p_a = Account("drivers")
    p_a.create_account(info)    
    return render_template("login.html")



if __name__ == "__main__":
    app.run(debug=True)
