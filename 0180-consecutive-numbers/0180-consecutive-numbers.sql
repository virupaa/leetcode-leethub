# At last I tried this and it worked but it takes lots of processing time
# Write your MySQL query statement below
SELECT distinct Num as ConsecutiveNums
FROM Logs
WHERE (Id + 1, Num) in 
(select * from Logs) and 
(Id + 2, Num) in (select * from Logs)