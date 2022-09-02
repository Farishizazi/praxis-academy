import mysql.connector

conn = {
  'user': 'root',
  'password': 'password',
  'host': '192.168.155.222',
  'database': 'employees',
  'raise_on_warnings': True
}

cn_employ = mysql.connector.connect(**conn)

cn.close()