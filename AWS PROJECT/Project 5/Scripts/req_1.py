query = '''
WITH CTE1 AS(
    SELECT
*,
COUNT(ballnumber)/6 as maiden
WHERE extra_type IN ('NA') AND total_run = 0
GROUP BY id, bowler
FROM table
),
WITH CTE2 AS(
SELECT
*,
COUNT(*) as dots,
WHERE total_run = 0
GROUP BY id,bowler
FROM CTE1
),
WITH CTE3 AS(
SELECT 
*,
bowler as Player,
COUNT(DISTINCT overs) as Ov,
SUM(total_run) as Runs,
SUM(CASE WHEN kind IN ("caught","caught and bowled","stumped","bowled","lbw") THEN 1 ELSE 0 END) AS Wickets, 
CASE WHEN Wickets > 0 THEN (COUNT(DISTINCT overs)*6/Wickets) ELSE 0 END AS SR,
CASE WHEN battingteam = team1 THEN team1 ELSE team2 END as Against,

WHERE extra_type IN ('byes', 'legbyes', 'penalty')
FROM CTE2
)



'''