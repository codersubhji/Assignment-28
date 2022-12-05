#10. Select all the students who are doing a specific course, eg. Python.

import psycopg2

conn=psycopg2.connect(
    host='localhost',
    database='postgres',
    user='postgres',
    password='6393',
    port='5432'
)

create_table="""create table course_4 
(c_id int , cor_name varchar(100) ,
primary key(c_id))"""
# cur=conn.cursor()
# cur.execute(create_table)
# conn.commit()

print("Table are created ")

inser_table="""insert into course_4 values
(001,'Mca'),
(002,'bca'),
(003,'Mca'),
(004,'bcom'),
(005,'Mca'),
(006,'mteck')
"""
# cur=conn.cursor()
# cur.execute(inser_table)
# conn.commit()
print("table inserted")

create_sec_table="""create table student_table_4
(stu_roll int ,
stu_name varchar(200) ,
c_id int, 
primary key (stu_roll) ,
constraint fk_coure foreign key(c_id) references course(c_id))
"""
# cur=conn.cursor()
# cur.execute(create_sec_table)
# conn.commit()
print("created second table ")

inserted_sec_table="""insert into student_table_4 values
(101,'subhash',001),
(102,'vikas',002),
(103,'arun',003),
(104,'shiva',004),
(105,'mahraj',005),
(106,'aniket',006)
"""
# cur=conn.cursor()
# cur.execute(inserted_sec_table)
# conn.commit()
print("inserted second table ")


select_same_couse_student="""select stu_name from student_table_4 where c_id=(select c_id from course_4 where cor_name = 'Mca') """
cur=conn.cursor()
cur.execute(select_same_couse_student)
conn.commit()
print("select same course student ")