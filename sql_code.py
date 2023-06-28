sql_create_groups_table = """
CREATE TABLE IF NOT EXISTS [groups] (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	name TEXT UNIQUE NOT NULL
);
"""

sql_create_teachers_table = """
CREATE TABLE IF NOT EXISTS teachers (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	fullname VARCHAR(30) NOT NULL
);
"""

sql_create_students_table = """
CREATE TABLE IF NOT EXISTS students (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	fullname VARCHAR(30) NOT NULL,
	group_id INTEGER,
	FOREIGN KEY (group_id) REFERENCES groups (id)
);
"""

sql_create_subjects_table = """
CREATE TABLE IF NOT EXISTS subjects (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	name TEXT UNIQUE NOT NULL,
	teacher_id INTEGER,
	FOREIGN KEY (teacher_id) REFERENCES teachers (id)
);
"""

sql_create_grades_table = """
CREATE TABLE IF NOT EXISTS grades (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	student_id INTEGER,
	subject_id INTEGER,
	grade INTEGER NOT NULL,
	date DATE,
	FOREIGN KEY (student_id) REFERENCES students (id),
	FOREIGN KEY (subject_id) REFERENCES subjects (id)
);
"""
