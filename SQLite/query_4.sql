-- Find the average score on the stream (across the entire grade table).
SELECT ROUND(AVG(grade), 2) AS total_avg_grade
	FROM grades;