from flask import Flask, request, render_template

app = Flask(__name__)


app.static_folder = 'static'
app.config["DEBUG"] = True

@app.route('/', methods=['GET'])
def index():
    # found in ../templates/
    return render_template("index.html")