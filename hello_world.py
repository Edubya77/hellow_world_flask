from flask import Flask, render_template
from os import environ

app = Flask(__name__)

@app.route("/")
@app.route("/hello")
def say_hi():
    n = 5
    fruits = ["Apple", "Pear"]
    return render_template("hello_world.html",n=n,my_list=fruits)
            
@app.route("/hello/<name>")
def hi_person(name):
    return "Hello {}!".format(name.title())
    
@app.route("/jedi/<first_name>/<last_name>")
def jedi_name(first_name, last_name):
    return "Hello {}!".format(last_name[0:3].title()+first_name[0:2])

if __name__ == "__main__":
    app.run(host=environ['IP'],
            port=int(environ['PORT']))