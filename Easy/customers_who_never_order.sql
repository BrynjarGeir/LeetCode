# Write your MySQL query statement below
SELECT A.name as Customers
FROM Customers A
LEFT JOIN Orders B on A.id = B.CustomerId
WHERE B.CustomerId is Null