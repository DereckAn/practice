DROP TABLE IF EXISTS Adios;

-- class history
CREATE TABLE Adios (
   Student_ID INT NOT NULL,
   Idclass INT NOT NULL,
   Semester VARCHAR(30)
)

INSERT INTO Adios (Student_ID, Idclass, Semester)
VALUES (1, 3001, 'Spring 2019'),
       (1, 2001, 'Fall 2019'),
       (2, 1004, 'Spring 2019'),
       (2, 3002, 'Fall 2019'),
       (3, 2001, 'Fall 2018'),
       (6, 1001, 'Spring 2018'),
       (5, 1001, 'Fall 2019');