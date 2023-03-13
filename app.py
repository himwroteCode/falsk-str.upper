from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/home')
def home():
    return render_template("home page.html")

@app.route('/')
def index():
    return render_template("form.html")
    

@app.route('/uppercase')
def uppercase():
    strings_param = request.args.get('strings')
    
    strings = strings_param.split(',')
    upper_strings = [s.strip().upper() for s in strings]
    
    message = "The uppercase strings are: " + ", ".join(upper_strings)
    
    return message


@app.route("/hello")
def hello():
    return "hello users"

    
if __name__ == "__main__":
    app.run()
