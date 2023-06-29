-- Find the grades of students in an individual group in a particular subject

SELECT subj.name AS subject, g.name AS [GROUP], s.fullname AS student, grds.grade
	FROM grades grds
	JOIN students s ON s.id = grds.student_id
	JOIN groups g ON g.id = s.group_id
	JOIN subjects subj ON subj.id = grds.subject_id
	-- you can change the values for "g.id" and for "subj.id" to get grades for different groups in different subjects
	WHERE g.id = 1 and subj.id = 1;
