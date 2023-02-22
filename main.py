from flask import Flask, render_template, jsonify
# flask is a module
# Flask is a class within the module flask
#render_template is to render the html with templates folder

app=Flask(__name__)  #creating an object

JOBS=[
  {
    'id':1,
    'title':'Senior Developer',
    'location':'Hyderabad',
    'salary':'Rs.11,00,000/-'
  },
  {
    'id':2,
    'title':'Data Analyst',
    'location':'Mumbai',
    'salary':'Rs.2,00,000/-'
  },
  {
    'id':3,
    'title':'Data Scientist',
    'location':'Gurugram',
    'salary':'Rs.5,55,400/-'
  },
  {
    'id':4,
    'title':'Project Manager',
    'location':'Gift City',
    'salary':'Rs.55,22,000'
  },
  {
    'id':5,
    'title':'Database Developer',
    'location':'Sanfrancisco USA',
    'salary':'$.12,67,320/-'
  }
]

@app.route("/")  # routing the main page from url to RENDER a htmpl template
def hello_world():
  # we created python list which has to be sent as data to the HTML page.
 return render_template('home.html', myJobs=JOBS)

#to show the data in a direct JSON. here you are not rendering the html
# also to differentiate from a html page, we mention /api/.... 
@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)

if __name__=="__main__":
  print("I am inside the If Loop")
  #defining the local server to where the code needs to be run which is by default 0.0.0.0
  app.run(host='0.0.0.0',debug=True)
