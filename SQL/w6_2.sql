-- Marginal complexity: What data is stored in the Production.Culture table?
-- CultureId->String | Name->String | ModificaDate-> date 
SELECT * FROM Production.Culture; 

-- Give me the 10 first row in the Person.Person table
SELECT  TOP(10) * from Person.Person

-- How would you query ten first names, last names, and email addresses of the person's and email's table?
SELECT a.FirstName, a.LastName, b.EmailAddress 
FROM Person.Person a JOIN Person.EmailAddress b 
ON a.BusinessEntityID = b.BusinessEntityID;

-- I need a list of the employees with the 10 highest salaries, with their respective sales organized from highest to lowest salary, and the main items sold by each one.
SELECT top (10)
  p.FirstName + ' ' + p.LastName AS Name, 
  SUM(s.TotalDue) AS TotalSales
FROM 
  HumanResources.Employee e 
  INNER JOIN Sales.SalesPerson sp 
    ON e.BusinessEntityID = sp.BusinessEntityID 
  INNER JOIN Sales.SalesOrderHeader s 
    ON sp.BusinessEntityID = s.SalesPersonID 
  INNER JOIN Person.Person p 
    ON e.BusinessEntityID = p.BusinessEntityID
GROUP BY 
  p.FirstName, 
  p.LastName
ORDER BY 
  SUM(s.TotalDue) DESC


-- How would you be able to get each employee's password's last modification, including its name, job title. Filtered by a married marital status and male gender. Including an order from newest to oldest?

SELECT a.ModifiedDate, b.FirstName, c.JobTitle FROM Person.Password a
JOIN Person.Person b ON a.BusinessEntityID = b.BusinessEntityID
JOIN HumanResources.Employee c ON a.BusinessEntityID = c.BusinessEntityID
WHERE c.MaritalStatus = 'M' AND c.Gender = 'M'
ORDER BY a.ModifiedDate DESC;


-- Join the table Person.EmailAddress and the table Person.Pasword  in one table. The relational column is Busness entityID
SELECT 
  p.FirstName + ' ' + p.LastName AS Name, 
  e.EmailAddress, 
  pa.PasswordHash, 
  pa.PasswordSalt
FROM 
  Person.Person p 
  INNER JOIN Person.EmailAddress e 
    ON p.BusinessEntityID = e.BusinessEntityID 
  INNER JOIN Person.Password pa 
    ON p.BusinessEntityID = pa.BusinessEntityID;




-- How many tables are there in the batabase AdventureWorks2019?
SELECT COUNT(*) as [Number of Tables]
FROM information_schema.tables
WHERE table_type = 'BASE TABLE'
  AND table_catalog = 'AdventureWorks2019';


-- What is the name, schema and creation date of the Person.Person's and Person.CountryRegion's table inside the database?
SELECT 
  t.name AS TableName, 
  s.name AS SchemaName, 
  t.create_date AS CreationDate
FROM 
  sys.tables t 
  INNER JOIN sys.schemas s 
    ON t.schema_id = s.schema_id
WHERE 
  t.name IN ('Person', 'CountryRegion') 
  AND s.name = 'Person';
