from flask import Flask, render_template,jsonify
# you can import a function from database.py to this file as a module/library
from database import load_jobs_from_database


# flask is a module
# Flask is a class within the module flask
#render_template is to render the html with templates folder

app=Flask(__name__)  #creating an object
    
# routing the main page from url to RENDER a html template
@app.route("/")  
def hello_world():
  multiplejobs=load_jobs_from_database()
# we created python list which has to be sent as data to the HTML page.
  return render_template('home.html', myJobs=multiplejobs)


if __name__=="__main__":
  print("I am inside the If Loop")
  #defining the local server to where the code needs to be run which is by default # 0.0.0.0
  app.run(host='0.0.0.0',debug=True)

#-----------------------------------------------------------
#to show the data in a direct JSON. here you are not rendering the html
# also to differentiate from a html page, we mention /api/.... 
# @app.route("/api/jobs")
# def list_jobs():
#   return jsonify(ajob)





