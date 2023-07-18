import mysql.connector
from flask import Flask , request
import json

conn_db = mysql.connector.connect(host="localhost", username="root", password="Nikhil9764", database="mydb")

app = Flask(__name__)


@app.route('/add_student', methods= ['POST'])
def insert_data() :
    cursor = conn_db.cursor()

    data_obt = request.get_json()

    sql_query = "INSERT INTO mydb.student_table(Student_ID,gender,NationalITy,PlaceofBirth,StageID,GradeID,SectionID,Topic,Semester,Relation,raisedhands,VisITedResources,AnnouncementsView,Discussion,ParentAnsweringSurvey,ParentschoolSatisfaction,StudentAbsenceDays,StudentMarks,Class) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"

    value_list = (data_obt['Student_ID'], data_obt['gender'], data_obt['NationalITy'], data_obt['PlaceofBirth'],data_obt['StageID'],data_obt['GradeID'],data_obt['SectionID'],data_obt['Topic'],data_obt['Semester'],data_obt['Relation'],data_obt['raisedhands'],data_obt['VisITedResources'],data_obt['AnnouncementsView']
                  ,data_obt['Discussion'],data_obt['ParentAnsweringSurvey'],data_obt['ParentschoolSatisfaction'],data_obt['StudentAbsenceDays'],data_obt['StudentMarks'],data_obt['Class'])
    cursor.execute(sql_query, value_list)
    conn_db.commit()
    return {'id': data_obt['Student_ID']}

    cursor.close()


@app.route('/delete_student', methods=['DELETE'])
def delete_student_record():
    cursor = conn_db.cursor()

    data_obt = request.get_json()
    sid = data_obt['Student_ID']

    sel_query = "SELECT COUNT(*) FROM student_table where Student_ID = %s"
    cursor.execute(sel_query, (sid,))
    cnt = cursor.fetchone()[0]

    if cnt == 0:
        return {"error": "given student id not found"}
    else:
        del_query = "DELETE FROM student_table where Student_ID=%s"
        cursor.execute(del_query, (sid,))
        conn_db.commit()
        return {'id': data_obt['Student_ID']}

    cursor.close()


@app.route('/update_student', methods=['PUT', 'PATCH'])
def update_student_record():
    cursor = conn_db.cursor()

    data_obt = request.get_json()
    sid = data_obt['Student_ID']

    sel_query = "SELECT COUNT(*) FROM student_table where Student_ID = %s"
    cursor.execute(sel_query, (sid,))
    cnt = cursor.fetchone()[0]

    if cnt == 0:
        return {"error": "given student id not found"}

    else:
        l1=len(data_obt)
        part_query = ""
        cnt = 0
        for k,v in data_obt.items():
            if k!= "Student_ID":
              key_val = v
              part_query = part_query+str(k)+"="+ "'{}'".format(key_val)
            if cnt != l1-1 and cnt!=0:
              part_query = part_query+','
            cnt+=1

        update_query = "UPDATE student_table SET "+part_query+" "+"WHERE Student_ID=%s"
        values_list = (sid,)
        cursor.execute(update_query, values_list)
        conn_db.commit()

    return {'id': data_obt['Student_ID']}

    cursor.close()


if __name__ == '__main__':
    app.run()