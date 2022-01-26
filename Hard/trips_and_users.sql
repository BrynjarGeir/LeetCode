# Write your MySQL query statement below
SELECT request_at as Day, ROUND(SUM(t.status != "completed") / COUNT(*), 2) as 'cancellation rate'
FROM Trips t
JOIN Users c ON t.client_ID = c.users_ID AND c.banned = 'No'
Join Users d On t.driver_ID = d.users_ID AND d.banned = 'No'
WHERE request_at BETWEEN '2013-10-01' AND '2013-10-03'
GROUP BY request_at