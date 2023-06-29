-- -- Find the student with the highest grade point average in a particular subject

SELECT subj.name AS subject, s.fullname AS student, ROUND(AVG(g.grade), 2) AS average_grade
FROM grades AS g
JOIN students AS s ON s.id = g.student_id
JOIN subjects AS subj ON subj.id = g.subject_id
WHERE subj.id = 1 -- Here 1 means a particular subject
GROUP BY s.id
ORDER BY average_grade DESC
LIMIT 1;
