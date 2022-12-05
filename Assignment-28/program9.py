#9. Insert data in both the tables.

import psycopg2

conn=psycopg2.connect(
    host='localhost',
    database='postgres',
    user='postgres',
    password='6393',
    port='5432'
)

create_table="""create table course_2 
(c_id int , cor_name varchar(100) ,
primary key(c_id))"""
cur=conn.cursor()
cur.execute(create_table)
conn.commit()

print("Table are created ")

inser_table="""insert into course_2 values
(001,'Mca'),
(002,'bca'),
(003,'bba'),
(004,'bcom'),
(005,'llb'),
(006,'mteck')
"""
cur=conn.cursor()
cur.execute(inser_table)
conn.commit()
print("table inserted")

create_sec_table="""create table student_table_2
(stu_roll int ,
stu_name varchar(200) ,
c_id int, 
primary key (stu_roll) ,
constraint fk_coure foreign key(c_id) references course(c_id))
"""
cur=conn.cursor()
cur.execute(create_sec_table)
conn.commit()
print("created second table ")

inserted_sec_table="""insert into student_table_2 values
(101,'subhash',001),
(102,'vikas',002),
(103,'arun',002),
(104,'shiva',003),
(105,'mahraj',004),
(106,'aniket',005)
"""
cur=conn.cursor()
cur.execute(inserted_sec_table)
conn.commit()
print("inserted second table ")