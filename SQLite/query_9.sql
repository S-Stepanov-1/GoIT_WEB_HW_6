-- Find a list of the courses a particular student is taking.

SELECT s.fullname AS student, subj.name AS subject
	FROM grades g
	JOIN students s ON s.id = g.student_id
	JOIN subjects subj ON subj.id = g.subject_id
	-- WHERE s.id = 4  -- you can change "s.id" to find a list of the courses for a particular student
	GROUP BY s.id, subj.id;