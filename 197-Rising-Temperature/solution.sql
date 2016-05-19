# Write your MySQL query statement below
SELECT W2.Id
FROM Weather AS W1, Weather AS W2
WHERE julianday(W1.Date) - julianday(W2.Date) = -1 AND W1.Temperature < W2.Temperature;