# ===============================================
# SOAL 3: OOP, Assertions, & Exceptions
# ===============================================

# --- Custom Exceptions ---
class CapacityException(Exception):
    pass

class SchedulingConflictException(Exception):
    pass

class PrerequisiteException(Exception):
    pass


# --- Helper Function ---
def is_time_conflict(time1, time2):
    """Cek apakah dua slot waktu bertabrakan.
    Format time_slot = (hari, jam_awal, jam_akhir)
    """
    day1, start1, end1 = time1
    day2, start2, end2 = time2
    if day1 != day2:
        return False
    return not (end1 <= start2 or end2 <= start1)  # bertabrakan jika saling overlap


# --- Course Class ---
class Course:
    def __init__(self, course_id, name, capacity, time_slot, department_name, prerequisites=[]):
        self.course_id = course_id
        self.name = name
        self.capacity = capacity
        self.time_slot = time_slot
        self.department_name = department_name
        self.prerequisites = prerequisites
        self.enrolled_students = []
        self.lecturers = []

    def is_full(self):
        return len(self.enrolled_students) >= self.capacity

    def enroll_student(self, student):
        if self.is_full():
            raise CapacityException(f"Course {self.name} is at full capacity.")
        self.enrolled_students.append(student)

    def prerequisites_met(self, student_courses):
        return all(prereq in student_courses for prereq in self.prerequisites)


# --- Student Class ---
class Student:
    def __init__(self, student_id, name):
        self.student_id = student_id
        self.name = name
        self.registered_courses = []

    def enroll_in_course(self, course):
        # Cek jadwal bentrok
        for c in self.registered_courses:
            if is_time_conflict(c.time_slot, course.time_slot):
                raise SchedulingConflictException(
                    f"Scheduling conflict detected for {self.name} with course {course.name}"
                )

        # Cek prasyarat
        if not course.prerequisites_met(self.registered_courses):
            raise PrerequisiteException(f"Prerequisites not met for {course.name}.")

        # Coba daftarkan
        course.enroll_student(self)
        self.registered_courses.append(course)


# --- Lecturer Class ---
class Lecturer:
    def __init__(self, lecturer_id, name):
        self.lecturer_id = lecturer_id
        self.name = name
        self.courses_taught = []

    def assign_to_course(self, course):
        # Cek bentrok waktu dengan course lain
        for c in self.courses_taught:
            if is_time_conflict(c.time_slot, course.time_slot):
                raise SchedulingConflictException(
                    f"{self.name} already teaching a course during {course.time_slot}"
                )
        self.courses_taught.append(course)
        course.lecturers.append(self)


# --- Department Class ---
class Department:
    def __init__(self, department_name):
        self.department_name = department_name
        self.courses = []
        self.lecturers = []
        self.students = []

    def add_course(self, course):
        assert course not in self.courses, "Course already exists in the department"
        self.courses.append(course)

    def add_lecturer(self, lecturer):
        assert lecturer not in self.lecturers, "Lecturer already exists in the department"
        self.lecturers.append(lecturer)

    def add_student(self, student):
        assert student not in self.students, "Student already exists in the department"
        self.students.append(student)


# --- TEST PROGRAM SESUAI URUTAN SOAL ---
print("=== (Testing System) ===")

try:
    # 1. Department
    cs_dept = Department("Computer Science")

    # 2 & 3. Mahasiswa
    s1 = Student("1", "Mamang Diky")
    s2 = Student("2", "Mamang Andre")

    # 4. Dosen
    l1 = Lecturer("1", "Mamang Ubay S.T M.T Ph.D.")

    # 5. Course CS100
    cs100 = Course("CS100", "Basic Programming", 1, ("Monday", 10, 12), "Computer Science", [])

    # 6. Course CS101
    cs101 = Course("CS101", "Intro to Programming", 2, ("Monday", 11, 14), "Computer Science", [cs100])

    # 7. Tambahkan semua ke departemen
    cs_dept.add_course(cs100)
    cs_dept.add_course(cs101)
    cs_dept.add_student(s1)
    cs_dept.add_student(s2)
    cs_dept.add_lecturer(l1)

    # 8-10. Coba tambahkan duplikat (harus trigger assertion)
    try:
        cs_dept.add_course(cs100)
    except AssertionError as e:
        print(e)
    try:
        cs_dept.add_student(s1)
    except AssertionError as e:
        print(e)
    try:
        cs_dept.add_lecturer(l1)
    except AssertionError as e:
        print(e)

    # 11. Assign course ke dosen (cek konflik waktu)
    try:
        l1.assign_to_course(cs100)
        l1.assign_to_course(cs101)
    except SchedulingConflictException as e:
        print(e)

    # 12. Enroll CS101 ke mahasiswa id=2 (gagal karena belum ambil CS100)
    try:
        s2.enroll_in_course(cs101)
    except Exception as e:
        print(e)

    # 13. Enroll CS100 oleh mahasiswa 1 dan 2
    try:
        s1.enroll_in_course(cs100)
        s2.enroll_in_course(cs100)
    except Exception as e:
        print(e)

    # 14. Enroll CS101 oleh mahasiswa 1
    try:
        s1.enroll_in_course(cs101)
    except Exception as e:
        print(e)

    # 15. Print hasil akhir
    print("\n=== (Summary) ===")
    for c in cs_dept.courses:
        print(f"Course {c.name}: {len(c.enrolled_students)} mahasiswa, {len(c.lecturers)} dosen")

    for s in cs_dept.students:
        print(f"Student {s.name}: {len(s.registered_courses)} mata kuliah")

    for l in cs_dept.lecturers:
        print(f"Lecturer {l.name}: {len(l.courses_taught)} mata kuliah diajar")

except Exception as e:
    print("Error:", e)
