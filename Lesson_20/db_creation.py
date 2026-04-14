import random
import os
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship, sessionmaker, declarative_base

Base = declarative_base()

# 1. Таблиця зв'язку Many-to-Many
student_courses = Table(
    'student_courses',
    Base.metadata,
    Column('student_id', Integer, ForeignKey('students.id'), primary_key=True),
    Column('course_id', Integer, ForeignKey('courses.id'), primary_key=True)
)

# 2. Опис моделей
class Student(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    courses = relationship("Course", secondary=student_courses, back_populates="students")

class Course(Base):
    __tablename__ = 'courses'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    students = relationship("Student", secondary=student_courses, back_populates="courses")

# 3. Підключення до файлу бази даних
# Створимо новий файл 'my_students.db' у тій же папці, де лежить скрипт
db_path = os.path.abspath("my_students.db")
engine = create_engine(f'sqlite:///{db_path}')

Session = sessionmaker(bind=engine)
session = Session()

# Створюємо таблиці
Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

# 4. Наповнення
course_names = ["Python Automation", "SQL for QA", "API Testing", "Mobile Testing", "Java Basics"]
courses = [Course(title=name) for name in course_names]
session.add_all(courses)

students = [Student(name=f"Student_{i}") for i in range(1, 21)]
session.add_all(students)

session.flush()

for student in students:
    assigned = random.sample(courses, k=random.randint(1, 3))
    student.courses.extend(assigned)

session.commit()
print(f"База створена за шляхом: {db_path}")
session.close()