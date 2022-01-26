# Write your MySQL query statement below
SELECT DISTINCT(num) as ConsecutiveNums
FROM (SELECT num, 
      case
        when @record = num then @count :=@count + 1
        when @record <> @record:=num then @count:=1 end as n
      from 
        Logs, (select @count:=0,@record:=(select num from Logs limit 0,1)) r
      ) a
      Where a.n >= 3