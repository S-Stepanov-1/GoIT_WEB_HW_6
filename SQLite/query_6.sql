-- Find a list of students in a particular group
SELECT g.name AS [GROUP], s.fullname as student
	FROM groups g
	JOIN students s ON s.group_id = g.id
    WHERE g.id = 1  --
	ORDER BY g.id;