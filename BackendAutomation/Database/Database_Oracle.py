import cx_Oracle
import os

# os.environ['PATH'] = "PATH/PATH2"

'''
dsn_tns = cx_Oracle.makedsn('Host Name', 'Port Number', service_name='Service Name') 
if needed, place an 'r' before any parameter in order to address special characters such as '\'.

conn = cx_Oracle.connect(user=r'User Name', password='Personal Password', dsn=dsn_tns)
if needed, place an 'r' before any parameter in order to address special characters such as '\'. For example, if your user name contains '\', you'll need to place 'r' before the user name: user=r'User Name'

'''


dsn_tns = cx_Oracle.makedsn('aws-smdqa-04.na.rtdom.net', '1522', service_name='QA203')
conn = cx_Oracle.connect(user=r'bcc', password='guesses', dsn=dsn_tns, encoding="UTF-8")


cur = conn.cursor()
QUERY_INSERT = "insert into student values (102, 'John')"
QUERY_SELECT = "select * from agency where age_code = 'AGAP01'"

cur.execute(QUERY_SELECT)

for cols in cur:
    print(cols)


cur.close()
cur.commit()

conn.close()