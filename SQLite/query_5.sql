-- Find what courses a particular instructor is reading

SELECT t.fullname, s.name AS subject
	FROM teachers t
	JOIN subjects s ON s.teacher_id = t.id
	ORDER BY t.id;