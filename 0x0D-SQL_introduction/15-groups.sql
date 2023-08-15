-- script that ists the number of records with ame score in the table
-- second_table of the database hbtn_0c_0 in the server
SELECT `score`, COUNT(*) AS `number`
FROM `second_table`
GROUP BY `score`
ORDER BY `number` DESC;
