from flask import Flask, render_template
# flask is a module
# Flask is a class within the module flask
#render_template is to render the html with templates folder

app=Flask(__name__)  #creating an object
@app.route("/")  # routing the main page from url to beyond ""/""
def hello_world():
 return render_template('home.html')

if __name__=="__main__":
  print("I am inside the If Loop")
  #defining the local server to where the code needs to be run which is by default 0.0.0.0
  app.run(host='0.0.0.0',debug=True)
