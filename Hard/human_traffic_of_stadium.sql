# Write your MySQL query statement below
WITH t as ( SELECT t1.id, t1.visit_date, t1.people, id - row_number() OVER(ORDER BY id) as grp
          FROM Stadium t1
          WHERE people >= 100)
SELECT t.id, t.visit_date, t.people
FROM t
WHERE grp in (SELECT grp FROM t GROUP BY grp HAVING COUNT(*) >= 3)