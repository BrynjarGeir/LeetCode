# Write your MySQL query statement below
SELECT Department.Name as Department, e.Name as Employee, e.Salary
FROM Employee e Inner Join Department
ON e.DepartmentID = Department.Id
WHERE (SELECT count(Distinct m.Salary) FROM Employee m where m.DepartmentId = e.DepartmentId and m.salary > e.salary) < 3