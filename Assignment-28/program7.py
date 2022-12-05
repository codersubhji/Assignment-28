#7. Drop the student table.

import psycopg2

conn=psycopg2.connect(
    host='localhost',
    database='postgres',
    user='postgres',
    password='6393',
    port='5432'
    
)

creat_table='''create table student_5(
    stu_roll_no int,
    stu_name varchar(200),
    stu_add varchar(200),
    primary key (stu_roll_no)
    )
    '''
    
cur=conn.cursor()    
cur.execute(creat_table)
conn.commit()
print("table created successfully")    

insert_table=''' insert into student_5 values 
(1,'ajay','kanpur'),
(2,'anita','afgan'),
(3,'Mohan','ajmer'),
(4,'arnav','fatehpur'),
(5,'akas','kanpur')

'''
cur=conn.cursor()    
cur.execute(insert_table)
conn.commit()
print("table inserted")


drop_all_data='''drop table student_3'''

cur=conn.cursor()    
cur.execute(drop_all_data)
conn.commit()
print("drop table successfully ")