-- The average score that a particular instructor gives to a particular student !=in each course=!.

SELECT s.fullname AS student, t.fullname AS teacher, subj.name AS subject, ROUND(AVG(g.grade), 2)
	FROM grades g
	JOIN students s ON s.id = g.student_id
	JOIN subjects subj ON subj.id = g.subject_id
	JOIN teachers t ON t.id = subj.teacher_id
	WHERE t.id = 4 AND s.id = 3
	GROUP BY subj.id;