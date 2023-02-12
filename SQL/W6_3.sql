DROP TABLE IF EXISTS Student;

CREATE TABLE Student (
   Student_ID INT PRIMARY KEY NOT NULL,
   Student_Name VARCHAR(30) NOT NULL
)

INSERT INTO Student (Student_ID, Student_Name)
VALUES (1, 'Edie Rodgers'),
       (2, 'Koa Larsen'),
       (5, 'Zahrah Mathis'),
       (6, 'Ameer Silva')

