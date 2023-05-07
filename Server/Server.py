from flask import Flask,render_template
app = Flask(__name__,template_folder="../templates")

@app.route("/test")
def test():
    return "Healthy"
@app.route("/", methods=['GET', 'POST'])
def index():
    return render_template("index.html")

@app.route("/addemployee", methods=['POST'])
def addemployee():
    pass


if __name__ == "__main__":
    app.run(debug=True)
