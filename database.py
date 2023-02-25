from sqlalchemy import create_engine
from sqlalchemy import text
#from sqlalchemy import *


#print(sqlalchemy.__version__)   #--- to print the version
#engine=create_engine("mysql+pymysql://user:pass@some_mariadb/dbname?charset=utf8mb4")    #--- SyntaxError

connection_string="mysql+pymysql://hn7vx0s04pvn9wxmp7ie:pscale_pw_xb6NpEqAKKueUCFBaujNKZHBsfITpw6okTwvBdxcM0R@ap-south.connect.psdb.cloud/joviancareers?charset=utf8mb4"

# get the attributes from the text document MySQL planetscale database connection details.txt in your laptop jovian project folder#
# get the SSL details from planetscale in main.py tab
engine=create_engine(connection_string,
    connect_args={
        "ssl": {
            "ssl_ca": "/etc/ssl/cert.pem"
               }
                }
            )


#Function to execute the query and return the jobs
def load_jobs_from_database():
  with engine.connect() as conn:
  # conn.execute just executes the query abd holds the data which, 
    # we are storing in a variable.
    connectstring = conn.execute(text("select * from jobs"))
    jobs= connectstring.all()
    print("HURRAH....MY CODE IS WORKING")
    print(jobs)
    print("THE TYPE OF jobs object is... -->",type(jobs))
    # declaring a dictionay variable
    allJobs=[]
    for ajob in jobs:
      allJobs.append(ajob)
    print("THE TYPE OF allJobs object is... -->",type(allJobs))
    #allJobs is a List
    return allJobs  


#   with engine.connect() as conn:
#   # conn.execute just executes the query abd holds the data which, 
#     # we are storing in a variable.
#     connectstring = conn.execute(text("select * from jobs"))
#     jobs= connectstring.all()
#     for job in jobs:
#       print(dict(job))

# # the type is a CursorResult
# print("The type of result is ::",type(result))

# # the type is a list
# print("The type of result.all() is ::",type(result.all()))

# print("RESULT_OUTPUT[0]",result_output[0])
# print("RESULT_OUTPUT[1]",result_output[1])
# print("Type of RESULT_OUTPUT[0]:", type(result_output[0]))
# print("Type of RESULT_OUTPUT[1]:", type(result_output[1]))


# # the output type of a sqlalchemy query  is a ROW object
# # We need to convert the SQLALCHEMY ROW Object to a Python Dict
# first_row=result_output[0]._mapping
# print("First Row Type is -->", first_row)
# print("The TYPE of First Row is ::", type(first_row))

# myoutput=[]
# for each_row in result.all():
#   myoutput.append(each_row._mapping)
# print("Stage2: Output is --> ", myoutput)

# myoutput=[]
# for each_row in result.all():
#   myoutput.append([each_row._mapping])
#   print("Stage3: Output is --> ", myoutput)