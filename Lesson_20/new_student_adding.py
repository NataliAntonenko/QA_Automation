import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
# Імпортуємо класи та об'єкт Base з твого нового файлу models.py
from models import Student, Course, Base

# Налаштування шляху до тієї ж бази, яку ми створили раніше
db_path = os.path.abspath("my_students.db")
engine = create_engine(f'sqlite:///{db_path}')

# Створюємо сесію
Session = sessionmaker(bind=engine)
session = Session()


def add_new_data():
    try:
        # 1. Знаходимо курс (наприклад, "Python Automation")
        target_course = session.query(Course).filter_by(title="Python Automation").first()

        if target_course:
            # 2. Створюємо студента
            new_student = Student(name="Наталія QA")

            # 3. Прив'язуємо до курсу
            new_student.courses.append(target_course)

            session.add(new_student)
            session.commit()
            print(f"✅ Студент {new_student.name} успішно доданий на курс {target_course.title}!")
        else:
            print("❌ Курс не знайдено. Перевір назву в базі через DBeaver.")

    except Exception as e:
        session.rollback()
        print(f"❌ Помилка: {e}")
    finally:
        session.close()


if __name__ == "__main__":
    add_new_data()