-- script that lists all records with score >= 10 in table second_table database
-- hbtn_0c_0 in the server
SELECT `score`, `name`
FROM `second_table`
WHERE `score` >= 10
ORDER BY `score` DESC;