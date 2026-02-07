SQL Notes 
#NOTE: Why i am uploading here the sql notes because when we work in company in actual projects then in ml pipelines there we mostly do our work with the help of commands so we must learn this 
#also right 
# ============================================
# SQL BASICS - CLEAN NOTES
# ============================================



"""
INSERTING DATA
--------------
"""
# Single row:
# INSERT INTO student VALUES (1, "Aman", 26);
# INSERT INTO student VALUES (2, "Rahul", 34);

# Multiple rows at once:
# INSERT INTO student (id, name, age) 
# VALUES 
#   (3, "Karan", 21),
#   (4, "Arjun", 22),
#   (5, "Ram", 23);

"""
VIEWING DATA
------------
"""
# SELECT * FROM student;

"""
============================================
SQL COMMAND TYPES (Quick Reference)
============================================
DDL: CREATE, ALTER, RENAME, TRUNCATE, DROP
DML: INSERT, UPDATE, DELETE
DQL: SELECT
DCL: GRANT, REVOKE
TCL: COMMIT, ROLLBACK
"""

"""
============================================
BEST PRACTICES
============================================
"""
# Use IF NOT EXISTS to avoid errors:
# CREATE DATABASE IF NOT EXISTS college;
# DROP DATABASE IF EXISTS temp1;
# DROP TABLE IF EXISTS student;

# View all databases/tables:
# SHOW DATABASES;
# SHOW TABLES;

"""
============================================
PRACTICE EXAMPLE - Employee Table
============================================
"""
# CREATE TABLE employee (
#   id INT PRIMARY KEY,
#   name VARCHAR(50),
#   salary INT NOT NULL
# );

# INSERT INTO employee (id, name, salary)
# VALUES
#   (1, "Adam", 25000),
#   (2, "Bob", 30000),
#   (3, "Casey", 40000);

# SELECT * FROM employee;

"""
KEY POINTS TO REMEMBER
----------------------
✓ Order matters when inserting values
✓ Always use semicolons after statements
✓ PRIMARY KEY ensures unique IDs
✓ NOT NULL means field is mandatory
✓ VARCHAR(50) means text up to 50 characters
✓ Column format: column_name data_type constraint
"""
# ONE MORE THING THERE IS TWO WAY TO MAKE A PRIMARY KEY IS WE ALREADY SEE SECOND IS PRIMARY KEY(id) & 
# we also make the combination to primary key but the thing is they both make the cunique combination right 
# Let See Full version of a exampler code 
"""
create table c(
  id int primary key ,
  Name Varchar(40),
  age int not null
);
/* From This way also we use the insert to put the values right */
insert into c
(id,name,age)
Values
(101,"karan",21),
(102,"Arjun",22),
(103,"Bhisma",23);

/*insert into employe values(1,"Khiladi",21);*/
insert into c values(2,"Akshay",22);
insert into c values(3,"Khiladi",21);
insert into c values(4,"Akshay",22);

select * from c;
"""

# Move to Next thing that is Our Keys Right so there are two keys Ist one is Priary key that we see in uppper code 
# And second one is Foreign key in which a cokumnns or set of columsn in a table that refers to the primary key
# if i take an exmaple then let assume there is a two tables ist is  student and second is city both hve their own primary key right 
# now in city primary key that is id 1 2 3 pune mumbai delhi so thistable also present in our student table in a colun that is cityid and city 
# now this will duplicately  right there in student table tthats why it called as foreign key because the primary key convert into foreign when comes in relation betweeen both ok.

""" 
Next topic is constraint specify rules for data in table like not null unique etc.
Unique 
primary key 
foreign key  isme kya hai ki like syntax iska yeh hai ki sabse pehle table create kerte hain ham 
create table temp(
 cust_id # yaha pe new talbe yani kii current table ki primary key id dalenge 
 Foreign key (cust_id) references customer(id) # ab yaha pe hamne dusri table ka refernce liya hai 
)
# and vo dusri table purani hamari pehles e exist kerti hogi right t uski customer id ko ham hamara new table temp me leke jauenge and cust_id hamrai new table ki foriegn key and customer(id) is primary key 

# Code of imoplementing the foriegn key table with help of parent and child table 

create table customer (
  id int primary key,
  name avrchar(40)
);

insert into 
customer(id,name)
values 
(1,"jkausdfbiasujbd"),
(2,"ianenfin"),
(3,"ikanisdogn"),
(4,"ionasgb");


create table temp(
  order_id int primary key,
  cust_id int,
  foreign key (cust_id) references customer(id)
);
insert into temp 
values
(101,1),
(102,1),
(103,1),
(104,1);

select * from customer;
select * from temp;


create table emp1(
  id int primary key,
  salary int default 23000);
 
 insert into emp1(id)  values(101);

  select * from emp1;
  -- Now there is two more thing that comes  in our check so let craeat a table infromation 
  create table information(
    id int primary key ,
    city varchar(30),
    age int ,
    constraint age_check check(age>=18 And city="Delhi")
  );
  -- And here if we want to apply the check conditon at the point like below given way so we also do this
  Create Table newtable(
    age int check (age>=18) 

"""
# Slect command in detail so let starts: 1. if we want to select particular row and columnn then 
"""
create table c(
  id int primary key ,
  Name Varchar(40),
  age int not null
);
/* From This way also we use the insert to put the values right */
insert into c
(id,name,age)
Values
(101,"karan",21),
(102,"Arjun",22),
(103,"Bhisma",23);


select * from c;
-- here we see how we use select to select the particular things right like we only want to see the names of the table information so then 
select name from c; -- This will print only name and similarly if we want to print two things at one time and more than two also so then the same pattern which is below given is follow like how :
select name , age from c;
select distinct name from c ; --prints only unnique name not duplicate 
"""
# where clause 
"""
select * from c where age>22; -- so here where clause works simply 
select *from c where name="karan";  -- here only the name karan will be print because there is no another karan in this table 
likewise we also do this 
select age from c where age>22; -- so this is only print the age not the all infromation ok 
"""
# Now there is also opeartors okey 
"""
important operator and , or and means both condition true then print in  or one is true and one false that okey 
between select * from student where marks between 40 and 90 ; -- it also print 80 and 90
In opeartor select * from student where city in ("delhi" , "Mumbai")  in IN operator if the cities are found in these delhi and mumbai it will print the all data of those students 
Not operator Select * from student where city not in ("delhi" , "Mumbai") Not negative niklata hai matlab reverse kerna hota jab condition ko .
Limit Clause 
Select * from student LIMIT 3 ; it means we only show the ist 3 data of the students 
select* from students were marks >70 ; 
LIMIT 3; it gives only 3 students liiewise only 3 whose marks are greater than 70 okey isntead there are 100 students whose numbers are greater than70 but limit only print its limit value data like here is 3.
 
 Next is Order by clause  ( in ascending and descending order arrangement )
 select * from student 
 order by marks DESC;
 Limit 3;

 Now one more thing let suppose we found out the top 3 marks from last but we dont know which marks is highest so we simply apply order by desc clause it convert into descending and then appy limit 3 ; simple 
 """ 
 #Aggregate functions -> Like sum() max() count()  let me show you the syntax 
 #select count(id) 
 #From  customer;    it count the all id and give it to us like in upper code where we make temp and customer table there we apply this syntax it returns the 4 simply because id total count are 4 
 """
 create table customer (
  id int primary key,
  name avrchar(40),
 marks int not null
);

insert into 
customer(id,name,marks)
values 
(1,"jkausdfbiasujbd",100),
(2,"ianenfin",44),
(3,"ikanisdogn",99),
(4,"ionasgb",80);


create table temp(
  order_id int primary key,
  cust_id int,
  foreign key (cust_id) references customer(id)
);
insert into temp 
values
(101,1),
(102,1),
(103,1),
(104,1);

select * from customer;
select * from temp;
select * from customer 
order by id >2 DESC;
select max(marks) 
From  customer;
select min(marks) 
From  customer;
select avg(marks) 
From  customer;
"""
# Next is group by clause 
"""
Basically in this what we do we make group like let suppose we make a group on the basis 
of city and we want that print the total students in every grouped city from student table
right so what we do 

select  city , count(rollno)   -- we find in the basis of roll no right 
from student 
group by city 

select city , avg(marks)
from student
group by city ;
# let see a code of it again same code we use like in upper one we use so 

create table customer (
  id int primary key,
  city avrchar(40),
  marks int not null

);

insert into 
customer(id,city,marks)
values 
(1,"jkausdfbiasujbd",100),
(2,"ianenfin",44),
(3,"ikanisdogn",99),
(4,"ionasgb",80);


create table temp(
  order_id int primary key,
  cust_id int,
  foreign key (cust_id) references customer(id)
);
insert into temp 
values
(101,1),
(102,1),
(103,1),
(104,1);

select * from customer;
select * from temp;
select * from customer 
order by id >2 DESC;
select avg(marks) 
From  customer;
select city , avg(marks)
from customer
group by city ;


"""
# Having clause 
"""
create table customer (
  id int primary key,
  city avrchar(40),
  marks int not null

);

insert into 
customer(id,city,marks)
values 
(1,"jkausdfbiasujbd",100),
(2,"ianenfin",44),
(3,"ikanisdogn",99),
(4,"ionasgb",80);


create table temp(
  order_id int primary key,
  cust_id int,
  foreign key (cust_id) references customer(id)
);
insert into temp 
values
(101,1),
(102,1),
(103,1),
(104,1);

select * from customer;
select * from temp;
select * from customer 
order by id >2 DESC;
select avg(marks) 
From  customer;
select city , avg(marks)
from customer
group by city 
having max(marks)>70;

"""
# order to write these all comands in a way so the order is 
"""
select column(s)
from table_name
where condition 
group by column(s)
having condition
order by column(s) ASC;
"""
