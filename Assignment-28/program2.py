# 2. Insert records for 4 students.

import psycopg2

conn=psycopg2.connect(
    host='localhost',
    database='postgres',
    user='postgres',
    password='6393',
    port='5432'
)

creaate_query=""" create table student_2 (
        stu_roll int , 
        stu_name varchar(200),
        stu_add varchar(200)
        )
"""

print("table successful created ")


insert_table=""" insert into student_2 values
      (101,'Rahul','kanpu'),
      (102,'ajay','Mumbai'),
      (103,'arvind','Bhopal'),
      (104,'amit','naraini'),
      (105,'aniket','fatehpur'),
      (106,'anuj','jhansi')


"""
cur=conn.cursor()
cur.execute(insert_table)
conn.commit()

print("insert table successfully")

























# import psycopg2

# conn=psycopg2.connect(
#     host='localhost',
#     database='postgres',
#     user='postgres',
#     password='6393',
#     port='5432'
# )


# creat_query= '''create table student (
#      stu_roll_no int , 
#      stu_name varchar(200), 
#      stu_course varchar(200))
#      '''




# print("table successful created")

# insert_query='''insert into student values(01,'subhash kumar','Computer science'),(02,'Shalvi','MBA'),(03,'Arvind kumar','Social science'),(04,'Rahul kumar',' science')'''
# cur=conn.cursor()
# cur.execute(insert_query)
# conn.commit()
# print("vlaue insert successful")