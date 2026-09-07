import streamlit as st
import mysql.connector
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Shaik@Abrar12",
    database="Student_Management_System"
)

cursor=db.cursor()

st.title("Student Management System")

menu=st.sidebar.selectbox(
    "MENU",
    ["Add Student","View Students","Delete Student"]
)

#Add Student
if menu == "Add Student":
    st.header("Add Student")
    serial_no=st.number_input("Serial No")
    Roll_No=st.text_input("Roll Number")
    Name=st.text_input("Student Name")
    Branch=st.text_input("Branch")
    if st.button("Add Student"):
        query="""INSERT INTO Std (serial_no,Roll_No,Name,Branch) VALUES(%s,%s,%s,%s)"""
        cursor.execute(query,(serial_no,Roll_No,Name,Branch))
        db.commit()
        st.success("Student added successfully")

#View all students
elif menu == "View Students":
    st.header("Information of Students")
    query="""SELECT * FROM Std"""
    cursor.execute(query)
    std=cursor.fetchall()
    st.table(std)

#Delete student
elif menu == "Delete Student":
    st.header("Delete Student")
    Roll_No=st.text_input("Roll Number")
    if st.button("Delete"):
        query="""DELETE FROM Std WHERE Roll_No=%s"""
        cursor.execute(query,(Roll_No,))
        db.commit()
        st.success("Student Deleted successfully")