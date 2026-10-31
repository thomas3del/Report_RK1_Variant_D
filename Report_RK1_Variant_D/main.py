from operator import itemgetter

# ==========================================
# 1. تعريف الكلاسات (Classes)
# ==========================================

class Teacher:
    """Преподаватель (مُدرّس) - الطرف الأول"""
    def __init__(self, id, surname, salary, course_id):
        self.id = id
        self.surname = surname
        self.salary = salary  # خاصية كمية: الراتب
        self.course_id = course_id

class Course:
    """Учебный курс (مقرر دراسي) - الطرف الثاني"""
    def __init__(self, id, name):
        self.id = id
        self.name = name

class TeacherCourse:
    """جدول الربط للعلاقة Many-to-Many"""
    def __init__(self, course_id, teacher_id):
        self.course_id = course_id
        self.teacher_id = teacher_id

# ==========================================
# 2. البيانات التجريبية (Test Data)
# ==========================================

# المقررات الدراسية
courses = [
    Course(1, 'Алгебра'),          # يبدأ بحرف А
    Course(2, 'Астрономия'),       # يبدأ بحرف А
    Course(3, 'История'),
    Course(4, 'Физика'),
    Course(5, 'Английский язык'),  # يبدأ بحرف А
]

# المُدرّسون
teachers = [
    Teacher(1, 'Иванов', 50000, 1),
    Teacher(2, 'Петров', 60000, 2),
    Teacher(3, 'Сидоров', 45000, 3),
    Teacher(4, 'Кузнецов', 70000, 4),
    Teacher(5, 'Смирнов', 55000, 5),
]

# جدول الربط Many-to-Many
teachers_courses = [
    TeacherCourse(1, 1),
    TeacherCourse(2, 2),
    TeacherCourse(3, 3),
    TeacherCourse(4, 4),
    TeacherCourse(5, 5),
    # ربط إضافي (نفس المدرس يدرّس أكثر من مقرر)
    TeacherCourse(1, 2), 
    TeacherCourse(3, 5),
]

def main():
    """الدالة الرئيسية"""

    # --- ربط البيانات One-to-Many ---
    one_to_many = [(t.surname, t.salary, c.name)
                   for c in courses
                   for t in teachers
                   if t.course_id == c.id]

    # --- ربط البيانات Many-to-Many ---
    many_to_many_temp = [(c.name, tc.course_id, tc.teacher_id)
                         for c in courses
                         for tc in teachers_courses
                         if c.id == tc.course_id]

    many_to_many = [(t.surname, t.salary, course_name)
                    for course_name, course_id, teacher_id in many_to_many_temp
                    for t in teachers if t.id == teacher_id]

    # ==========================================
    # 3. تنفيذ الاستعلامات (Вариант Д)
    # ==========================================

    print('--- Задание Д1 ---')
    # Д1: جميع المُدرّسين الذين تنتهي أسماؤهم بـ "ов" وأسماء مقرراتهم (One-to-Many)
    res_1 = [(t.surname, c.name) for t in teachers for c in courses 
             if t.course_id == c.id and t.surname.endswith('ов')]
    print(res_1)

    print('\n--- Задание Д2 ---')
    # Д2: المقررات مع متوسط راتب المُدرّسين، مرتبة حسب المتوسط
    res_2_unsorted = []
    for c in courses:
        # المُدرّسون في هذا المقرر
        c_teachers = list(filter(lambda i: i[2] == c.name, one_to_many))
        if len(c_teachers) > 0:
            # الرواتب
            c_salaries = [sal for _, sal, _ in c_teachers]
            # المتوسط (مجموع / عدد)
            avg_salary = sum(c_salaries) / len(c_salaries)
            res_2_unsorted.append((c.name, round(avg_salary, 2)))
    
    res_2 = sorted(res_2_unsorted, key=itemgetter(1), reverse=True)
    print(res_2)

    print('\n--- Задание Д3 ---')
    # Д3: المقررات التي تبدأ بحرف "А" مع المُدرّسين (Many-to-Many)
    res_3 = {}
    for c in courses:
        if c.name.startswith('А'):
            c_teachers = list(filter(lambda i: i[2] == c.name, many_to_many))
            teacher_names = [x for x, _, _ in c_teachers]
            res_3[c.name] = teacher_names
    
    print(res_3)

if __name__ == '__main__':
    main()