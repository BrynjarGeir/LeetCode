# Write your MySQL query statement below
SELECT distinct(A.email)
FROM Person A, Person B
WHERE A.id > B.id AND A.email = B.email