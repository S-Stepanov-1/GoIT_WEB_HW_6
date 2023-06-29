-- Find the average score of groups in a particular subject

SELECT g.name AS [group], subj.name AS subject, ROUND(AVG(grd.grade), 2) AS average_grade
	FROM groups g
	JOIN students s ON s.group_id = g.id
	JOIN grades grd ON grd.student_id = s.id
	JOIN subjects subj ON subj.id = grd.subject_id
	GROUP BY g.id, subj.id;
