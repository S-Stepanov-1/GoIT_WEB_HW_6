-- Find the 5 students with the highest grade point average in all subjects.

SELECT s.fullname as student, groups.name as [GROUP], ROUND(AVG(g.grade), 2) as average_grade
FROM grades AS g
JOIN students AS s ON s.id = g.student_id
JOIN groups ON groups.id = s.group_id
GROUP BY s.id
ORDER BY average_grade DESC
LIMIT 5;