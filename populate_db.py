import csv
import mysql.connector

db_conn = mysql.connector.connect(host="localhost", username="root", password="", database="mydb")

c1 = db_conn.cursor()

csv_file_path = 'Student_original.csv'

table_name = 'student_table'

with open(csv_file_path, 'r') as file:
    csv_reader = csv.reader(file)

    header = next(csv_reader)

    insert_sql = "INSERT INTO {} ({}) VALUES ({})".format(table_name, ", ".join(header), ", ".join(['%s']*len(header)))

    for row in csv_reader:
        c1.execute(insert_sql, row)
        db_conn.commit()

c1.close()
db_conn.close()
    
