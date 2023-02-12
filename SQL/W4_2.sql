-- SELECT BusinessEntityID, FirstName, LastName
-- FROM Person.Person;

-- SELECT BusinessEntityID, PhoneNumber
-- FROM Person.PersonPhone;

-- SELECT A.BusinessEntityID, 
--     A.FirstName, 
--     A.LastName, 
--     b.PhoneNUmber
-- FROM Person.Person AS A LEFT JOIN Person.PersonPhone AS b
--     ON A.BusinessEntityID = b.BusinessEntityID
--     ORDER BY BusinessEntityID;



-- --------------------------------------------------------------
-- SELECT *
-- FROM Person.Person
-- ORDER BY BusinessEntityID;

-- SELECT *
-- FROM Sales.PersonCreditCard
-- ORDER BY BusinessEntityID;


-- SELECT BusinessEntityID
-- FROM Person.Person
-- WHERE PersonType <> 'IN'

-- UNION

-- SELECT BusinessEntityID
-- FROM Sales.PersonCreditCard;



-- --------------------------------------------

SELECT BusinessEntityID
FROM Person.EmailAddress
EXCEPT

SELECT BusinessEntityID
FROM Person.Password;

-- SELECT * FROM Person.EmailAddress
-- Select * FROM Person.Password