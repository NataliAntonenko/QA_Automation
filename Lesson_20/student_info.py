import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
# Імпортуємо моделі з твого файлу models.py
from models import Student, Course

# 1. Налаштовуємо підключення (те саме, що було раніше)
db_path = os.path.abspath("my_students.db")
engine = create_engine(f'sqlite:///{db_path}')

# 2. Створюємо сесію (це саме той 'session', якого не вистачало)
Session = sessionmaker(bind=engine)
session = Session()


def get_student_info(student_name):
    # 3. Шукаємо студента
    student = session.query(Student).filter_by(name=student_name).first()

    if student:
        print(f"--- Інформація про студента: {student.name} ---")
        if student.courses:
            for course in student.courses:
                print(f"Записаний(а) на курс: {course.title}")
        else:
            print("Студент ще не записаний на жоден курс.")
    else:
        print(f"Студента з ім'ям '{student_name}' не знайдено.")


def get_course_info(course_title):
    # 4. Шукаємо курс
    course = session.query(Course).filter_by(title=course_title).first()

    if course:
        print(f"\n--- Студенти на курсі: {course.title} ---")
        if course.students:
            for st in course.students:
                print(f"Студент: {st.name}")
        else:
            print("На цей курс ще ніхто не записався.")
    else:
        print(f"Курс '{course_title}' не знайдено.")


# --- ЗАПУСК ПЕРЕВІРКИ ---
if __name__ == "__main__":
    get_student_info("Наталія QA")
    get_course_info("Python Automation")

    session.close()