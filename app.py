from flask import Flask, render_template
#flask is a module and Flask is a #class within the module
#render_template is used to render an html template using flask

app = Flask(__name__)
#app is an object of the class Flask

@app.route("/")
#used to set route ,i.e, the url at which this page is to be rendered


def hello_world():
  return render_template('home.html')


#when we use python app.py, __name__ is set to __main__
if __name__ == "__main__":
  app.run(host="0.0.0.0", debug=True)