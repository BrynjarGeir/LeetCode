# Write your MySQL query statement below
SELECT *
FROM Cinema
WHERE id mod 2 != 0 AND description != 'boring'
ORDER BY rating desc