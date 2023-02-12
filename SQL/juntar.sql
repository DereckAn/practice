SELECT Student.Student_ID, Student.Student_Name, Count(Idclass) AS [Total class]
FROM Student JOIN Adios ON Student.Student_ID = Adios.Student_ID
GROUP BY Student.Student_ID, Student.Student_Name;
