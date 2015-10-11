from flask import Flask, render_template, request, redirect

app = Flask(__name__)


@app.route("/")
def index_page():
    return redirect ("/application-form")

@app.route("/application-form")
def application_form():
    return render_template("application-form.html")

@app.route("/application")
def application():
    # the request.args.get() is getting arguments from the url that the browser generated
    firstname = request.args.get("firstname")
    lastname = request.args.get("lastname")
    salary = request.args.get("salary")
    position = request.args.get("position")
    return render_template("application-response.html", 
        firstname=firstname, lastname=lastname, salary=salary, position=position)

if __name__ == "__main__":
    app.run(debug=True)
