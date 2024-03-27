-- List all recordsof second_table in MYSQL server
-- All numbers are in descending order
SELECT `score`, COUNT(*) AS `number`
FROM `second_table`
GROUP BY `score`
ORDER BY `number` DESC;
