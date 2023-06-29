-- Find the average score that a particular teacher gives in his or her subjects.

SELECT t.fullname AS teacher, s.name AS subject, ROUND(AVG(g.grade), 2)
	FROM teachers t
	LEFT JOIN subjects s ON s.teacher_id = t.id
	JOIN grades g ON g.subject_id = s.id
	GROUP BY s.id
	ORDER BY t.id;