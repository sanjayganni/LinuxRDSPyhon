from pymysql import connections
import os
import boto3
from config import *

app = Flask(__name__)

bucket = custombucket
region = customregion

db_conn = connections.Connection(
    host=mysqldbemployee.cmyrfs8fssae.ap-south-1.rds.amazonaws.com,
    port=3306,
    user=mysqldbadmin,
    password=admin1234,
    db=mysqldbemployee

)
output = {}
table = 'employee'

@app.route("/", methods=['GET', 'POST'])
def home():
    return render_template('GetEmp.html')

@app.route("/Getamp", methods=['POST'])
def Getemp():
    Empl_id = request.form['Empid']
    select_sql = "select Emp_fname, Emp_lname from employee where Emp_id= Empid"
    sql_cursor = mysql.connection.cursor()
    result_value = sql_cursor.execute(select_sql)
#    if result_value > 0 
    emp_details = cur.fetchall()
    Emplid    = emp_details.Emp_id
    Emplfname = emp_details.Emp_fname 
    Emplname =  emp_details.Emp_lname 
              
    except Exception as e:
    return str(e)

    finally:
        cursor.close()

    print("all modification done...")
    return render_template('GetEmpOutput.html',Empid=Emplid,Empfname=Emplfname,Empname=Emplname)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)