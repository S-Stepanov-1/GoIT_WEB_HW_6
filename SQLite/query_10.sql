-- A list of courses that a particular student is taught by a particular teacher.

SELECT s.fullname AS student, t.fullname AS teacher, subj.name AS subject
	FROM grades g
	JOIN students s ON s.id = g.student_id
	JOIN subjects subj ON subj.id = g.subject_id
	JOIN teachers t ON t.id = subj.teacher_id
	-- change "s.id" and "t.id" to find a list of subjects that a particular student is taught by a particular instructor
--	WHERE s.id = 1 AND t.id = 1
	GROUP BY s.id, t.id, subj.id;