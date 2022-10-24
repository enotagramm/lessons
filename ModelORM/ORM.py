import datetime as dt
from models import *
import unittest


with con:

    students = [
        {"name": 'Max', "surname": 'Brooks', "age": 24, "city": 'Spb'},
        {"name": 'John', "surname": 'Stones', "age": 15, "city": 'Spb'},
        {"name": 'Andy', "surname": 'Wings', "age": 45, "city": 'Manhester'},
        {"name": 'Kate', "surname": 'Brooks', "age": 34, "city": 'Spb'}
        ]

    courses = [
        {"name": "python", "time_start": dt.date(2021, 7, 21), "time_end": dt.date(2021, 8, 21)},
        {"name": 'java', "time_start": dt.date(2021, 7, 13), "time_end": dt.date(2021, 8, 16)}
        ]

    student_courses = [
        {"student_id": 1, "course_id": 1},
        {"student_id": 2, "course_id": 1},
        {"student_id": 3, "course_id": 1},
        {"student_id": 4, "course_id": 2}
        ]

    if Student.table_exists() and Course.table_exists() and StudentCourse.table_exists():
        Student.drop_table()
        Course.drop_table()
        StudentCourse.drop_table()

        con.create_tables([Student, Course, StudentCourse])

        Student.insert_many(students).execute()
        Course.insert_many(courses).execute()
        StudentCourse.insert_many(student_courses).execute()

    # old_students = Student.select().where(Student.age > 30)
    # print("Старше 30-ти лет:")
    # print("TOTAL =", len(old_students), "студента")
    # for student in old_students:
    #     print(student.name, student.surname, student.age)
    #
    # courses_python = Student\
    #     .select()\
    #     .join(StudentCourse)\
    #     .where(StudentCourse.course_id == 1)
    # print('=' * 50)
    # print("Проходят курс по PYTHON:")
    # print("TOTAL =", len(courses_python), "студента")
    # for student in courses_python:
    #     print(student.name, student.surname)
    #
    # courses_python_SPB = Student\
    #     .select()\
    #     .join(StudentCourse)\
    #     .where(StudentCourse.course_id == 1, Student.city == "Spb")
    # print('=' * 50)
    # print("Проходят курс по PYTHON из Санкт-Петербурга:")
    # print("TOTAL =", len(courses_python_SPB), "студента")
    # for student in courses_python_SPB:
    #     print(student.name, student.surname, student.city)


class TestORM(unittest.TestCase):
    def test_add_student(self):
        pass

    def test_add_courses(self):
        pass

    def test_del_student(self):
        pass

    def test_add_student_courses(self):
        pass

    def test_del_student_courses(self):
        pass





