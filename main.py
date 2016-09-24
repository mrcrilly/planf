
from yaml import load

from flask import Flask , render_template, request, jsonify

app = Flask(__name__)
app.config["SECRET_KEY"] = "abc123"

@app.route("/data/schema.json", methods=["GET"])
def schemaSourceRoute():
    with open("static/sources/schema.json") as fd:
        return fd.read()

@app.route("/data/options.json", methods=["GET"])
def optionsSourceRoute():
    with open("static/sources/options.json") as fd:
        return fd.read()

@app.route("/data/view.json", methods=["GET"])
def viewSourceRoute():
    with open("static/sources/view.json") as fd:
        return fd.read()

@app.route("/plan", methods=["POST"])
def planRoute():
    if request.method == "POST":
        mutable_form = request.form.copy()
        for fields in mutable_form.iteritems():
            field = fields[0].replace("_", "-")
            field_type = field_name.split("-")[0]

            if field_type == "incomes":
                print "Income: %s" % fields[1]
            elif field_type == "savings":
                print "Saving: %s" % fields[1]
            elif field_type == "debts":
                print "Debt: %s" % fields[1]
            elif field_type == "expenses":
                print "Expense: %s" % fields[1]
            else:
                print "Unknown: %s" % fields[1]


        return str(mutable_form)

@app.route("/", methods=["GET"])
def indexRoute():
    return render_template("index.html")

if __name__ == "__main__":
    main()