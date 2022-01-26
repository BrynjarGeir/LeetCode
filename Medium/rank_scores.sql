# Write your MySQL query statement below
SELECT A.Score, count(distinct B.score) as 'Rank'
FROM Scores A JOIN Scores B ON A.Score <= B.score
GROUP BY A.id
ORDER BY A.Score desc