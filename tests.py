import utils
import os


PATH_TO_STUDENTS = os.path.join("data", "students.json")
PATH_TO_PROFESSIONS = os.path.join("data", "professions.json")

all_students = utils.load_students(PATH_TO_STUDENTS)

all_professions = utils.load_professions(PATH_TO_PROFESSIONS)


stu = utils.get_student_by_pk(all_students, 4)
