import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Student, Course

# Підключення
db_path = os.path.abspath("my_students.db")
engine = create_engine(f'sqlite:///{db_path}')
Session = sessionmaker(bind=engine)
session = Session()


# 1. ОНОВЛЕННЯ (UPDATE)
def update_student_name(old_name, new_name):
    student = session.query(Student).filter_by(name=old_name).first()
    if student:
        student.name = new_name
        session.commit()
        print(f"✅ Ім'я змінено: {old_name} -> {new_name}")
    else:
        print(f"❌ Студента {old_name} не знайдено")


# 2. ВИДАЛЕННЯ СТУДЕНТА З БАЗИ (DELETE)
def delete_student(student_name):
    student = session.query(Student).filter_by(name=student_name).first()
    if student:
        session.delete(student)
        session.commit()
        print(f"🗑️ Студент {student_name} видалений з бази")
    else:
        print(f"❌ Студента {student_name} не знайдено")


# 3. ВИДАЛЕННЯ СТУДЕНТА ТІЛЬКИ З КУРСУ (Відв'язка)
def remove_student_from_course(student_name, course_title):
    student = session.query(Student).filter_by(name=student_name).first()
    course = session.query(Course).filter_by(title=course_title).first()

    if student and course:
        if course in student.courses:
            student.courses.remove(course)
            session.commit()
            print(f"➖ Студент {student_name} більше не відвідує {course_title}")
        else:
            print(f"ℹ️ Студент не був записаний на цей курс")


# --- ТЕСТУВАННЯ ---
if __name__ == "__main__":
    # Спробуємо оновити
    update_student_name("Наталія QA", "Наталія Senior QA")

    # Видалимо когось із рандомних (наприклад, Student_1)
    delete_student("Student_1")

    session.close()