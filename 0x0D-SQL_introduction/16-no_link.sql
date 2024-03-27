-- List all records of second_table in MYSQL server
-- All records are in descending order
SELECT `score`, `name`
FROM `second_table`
GROUP BY `name` != ""
ORDER BY `score` DESC;
