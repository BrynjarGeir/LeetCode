# Write your MySQL query statement below
Select E.name as Employee
FROM Employee E, Employee M
WHERE E.salary > M.salary AND E.managerId = M.id