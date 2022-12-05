"""8. Create Courses table (cid, cname) where cid is a primary key and Student table
(rollno, name, cid) where rollno is a primary key and cid is a foreign key."""

import psycopg2

conn=psycopg2.connect(
    host='localhost',
    database='postgres',
    user='postgres',
    password='6393',
    port='5432'
)

create_table="""create table course 
(c_id int , cor_name varchar(100) ,
primary key(c_id))"""


print("Table are created ")

inser_table="""insert into course values
(001,'Mca'),
(002,'bca'),
(003,'bba'),
(004,'bcom'),
(005,'llb'),
(006,'mteck')
"""
# cur=conn.cursor()
# cur.execute(inser_table)
# conn.commit()
print("table inserted")

create_sec_table="""create table student_table
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

inserted_sec_table="""insert into student_table values
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

# update_collom="""update student_table set c_id= 001 """

# # cur=conn.cursor()
# # cur.execute(update_collom)
# # conn.commit()
# print("updated table ")

# drop_table="""drop table student_table"""

# cur=conn.cursor()
# cur.execute(drop_table)
# conn.commit()
# print("drop table ")




