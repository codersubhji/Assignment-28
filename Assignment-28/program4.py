#4. Update the student name of rollno 3 with ‘Mohan’

import psycopg2

conn=psycopg2.connect(
    host='localhost',
    database='postgres',
    user='postgres',
    password='6393',
    port='5432'
    
)

creat_table='''create table student_3(
    stu_roll_no int,
    stu_name varchar(200),
    stu_add varchar(200),
    primary key (stu_roll_no)
    )
    '''
    

print("table created successfully")    

insert_table=''' insert into student_3 values 
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

update_table=''' update student_3 set stu_roll_no=106 where stu_name='ajay'

'''
cur=conn.cursor()    
cur.execute(update_table)
conn.commit()

print("update roll no in table ")