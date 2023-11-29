import json


def load_students():
    """
    Loads list of students from a file
    :return:
    """
    with open('data/students.json') as f:
        data = json.load(f)
        return data


def load_professions():
    """
    Loads list of professions from a file
    :return:
    """
    with open('data/professions.json') as f:
        data = json.load(f)
        return data


def get_student_by_pk(pk):
    """
    Gets student data by his primary key
    Returns None if not found
    :param pk:
    :return:
    """
    students = load_students()
    for student in students:
        if student.get('pk') == pk:
            return student


def get_profession_by_title(title):
    """
    Gets profession data by its title
    Returns None if not found
    :param title:
    :return:
    """
    professions = load_professions()
    for profession in professions:
        if profession.get('title').lower() == title.lower():
            return profession


def check_suitability(student, profession):
    """
    Returns student's profile dictionary
    :param student:
    :param profession:
    :return:
    """

    skills_present = set(student.get('skills'))
    skills_required = set(profession.get('skills'))

    has = skills_required.intersection(skills_present)
    lacks = skills_required.difference(skills_present)
    fit_percent = round(len(has) / len(skills_required) * 100)

    result = {
        'has': list(has),
        'lacks': list(lacks),
        'fit_percent': fit_percent
    }

    return result
