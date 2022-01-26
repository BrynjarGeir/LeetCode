# Write your MySQL query statement below
SELECT d.name as Department, e.name as Employee, e.salary as Salary
FROM Employee e, (SELECT DepartmentId, max(Salary) as max FROM Employee GROUP BY DepartmentID) T, Department D
WHERE E.departmentId = T.departmentId AND E.salary = T.max AND E.departmentId = D.id