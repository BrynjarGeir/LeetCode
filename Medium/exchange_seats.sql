# Write your MySQL query statement below
SELECT IF(id < (SELECT count(*) from Seat), IF(id mod 2 = 0, id-1, id+1), IF(id mod 2 = 0, id-1, id)) as id, student
FROM Seat
ORDER BY id ASC