from flask import Flask
app=Flask(__name__)
@app.route("/")
def hello_world():
 return "Hello Sumanth"

if __name__=="__main__":
  print("I am inside the If Loop")
  app.run(host='0.0.0.0',debug=True)
