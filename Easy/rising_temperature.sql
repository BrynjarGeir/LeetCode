# Write your MySQL query statement below
SELECT w1.id
FROM Weather w1, Weather w2
WHERE w1.temperature > w2.temperature AND To_Days(w1.recordDate) - To_days(w2.recordDate) = 1