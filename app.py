from flask import Flask, render_template,jsonify
#flask is a module and Flask is a #class within the module
#render_template is used to render an html template using flask

app = Flask(__name__)
#app is an object of the class Flask

job = [
  {
    'id': 1,
    'title': 'Data Analyst',
    'location': 'Bengaluru, India',
    'salary': 'Rs. 10,00,000'
  },
  {
    'id': 2,
    'title': 'Data Scientist',
    'location': 'Delhi, India',
    'salary': 'Rs. 15,00,000'
  },
  {
    'id': 3,
    'title': 'Frontend Engineer',
    'location': 'Remote',
    'salary': 'Rs. 12,00,000'
  },
  {
    'id': 4,
    'title': 'Backend Engineer',
    'location': 'San Francisco, USA',
    'salary': '$150,000'
  }
]

@app.route("/")
#used to set route ,i.e, the url at which this page is to be rendered


def hello_world():
  return render_template('home.html',jobs = job)

@app.route("/jobs")
def list_jobs():
  return jsonify(job)


#when we use python app.py, __name__ is set to __main__
if __name__ == "__main__":
  app.run(host="0.0.0.0", debug=True)