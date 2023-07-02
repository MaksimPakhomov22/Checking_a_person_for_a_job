import os

import utils

PATH_TO_STUDENTS = os.path.join("data", "students.json")
PATH_TO_PROFESSIONS = os.path.join("data", "professions.json")

all_students = utils.load_students(PATH_TO_STUDENTS)

all_professions = utils.load_professions(PATH_TO_PROFESSIONS)

student_pk = int(input("Введите номер студента\n"))

stu = utils.get_student_by_pk(all_students, student_pk)

if stu is None:
    print("Нет такого студента")
    quit("")

stu_name, stu_skills = stu["full_name"], stu["skills"]

print(f"Студент {stu_name}")
print(f"Знает {', '.join(stu_skills)}")

profession_title = input("Введите профессию\n").strip().lower()
pro = utils.get_profession_by_title(all_professions, profession_title)

if pro is None:
    print("Нет такой профессии")
    quit("")

pro_skills = pro["skills"]

stats = utils.check_fitness(stu_skills, pro_skills)

has = ", ".join(stats["has"])
lacks = ", ".join(stats["lacks"])
fit_percent = stats["fit_percent"]


print(f"Пригодность {fit_percent}")
if has:
    print(f"{stu_name} знает {has}")
if lacks:
    print(f"{stu_name} не знает {lacks}")
