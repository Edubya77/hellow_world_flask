from flask import Flask
from os import environ

app = Flask(__name__)

@app.route("/")
@app.route("/hello")
def say_hi():
    return "Hello World!"

if __name__ == "__main__":
    app.run(host=environ['IP'],
            port=int(environ['PORT']))
            
@app.route("/hello/<name>")
def hi_person(name):
    return "Hello {}!".format(name.title())
    
@app.route("/jedi/<first_name>/<last_name>")
def jedi_name(first_name, last_name):
    return "Hello {}!".format(last_name[0:3].title()+first_name[0:2])