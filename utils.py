import json


def load_students(path):
    with open(path, "r", encoding="utf-8") as file:
        data = json.load(file)
        return data


def load_professions(path):
    with open(path, "r", encoding="utf-8") as file:
        data = json.load(file)
        return data


def get_student_by_pk(students, pk):
    for stu in students:
        if stu["pk"] == pk:
            return stu


def get_profession_by_title(professions, title):
    for pro in professions:
        if pro["title"].lower() == title:
            return pro


def check_fitness(student_skills, profession_skills):
    stu_skill_set = set(student_skills)
    pro_skill_set = set(profession_skills)

    has = pro_skill_set.intersection(stu_skill_set)
    lacks = pro_skill_set.difference(stu_skill_set)
    fit_percent = round(len(has) / len(pro_skill_set) * 100)
    return {
        "has": has,
        "lacks": lacks,
        "fit_percent": fit_percent,
    }
