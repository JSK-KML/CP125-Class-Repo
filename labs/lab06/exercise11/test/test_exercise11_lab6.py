import pytest
import importlib.util
import os

_exercise_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'exercise11.py')
_spec = importlib.util.spec_from_file_location("exercise11_lab6", _exercise_path)
_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_module)
get_student_courses = _module.get_student_courses
find_missing_courses = _module.find_missing_courses
build_student_report = _module.build_student_report
find_incomplete_students = _module.find_incomplete_students

# Tests for get_student_courses
def test_get_student_courses_multiple():
    enrollments = [("S1", "Math"), ("S1", "Physics"), ("S2", "CS")]
    assert get_student_courses(enrollments, "S1") == {"Math", "Physics"}

def test_get_student_courses_single():
    enrollments = [("S1", "Math"), ("S2", "CS")]
    assert get_student_courses(enrollments, "S1") == {"Math"}

def test_get_student_courses_with_duplicates():
    enrollments = [("S1", "Math"), ("S1", "Math"), ("S1", "Physics")]
    assert get_student_courses(enrollments, "S1") == {"Math", "Physics"}

def test_get_student_courses_none():
    enrollments = [("S2", "Math"), ("S3", "CS")]
    assert get_student_courses(enrollments, "S1") == set()

# Tests for find_missing_courses
def test_find_missing_courses_some_missing():
    completed = {"Math", "Physics"}
    required = {"Math", "Physics", "CS"}
    assert find_missing_courses(completed, required) == {"CS"}

def test_find_missing_courses_all_completed():
    completed = {"Math", "Physics", "CS"}
    required = {"Math", "Physics"}
    assert find_missing_courses(completed, required) == set()

def test_find_missing_courses_none_completed():
    completed = set()
    required = {"Math", "Physics", "CS"}
    assert find_missing_courses(completed, required) == {"Math", "Physics", "CS"}

def test_find_missing_courses_multiple_missing():
    completed = {"Math"}
    required = {"Math", "Physics", "CS", "English"}
    assert find_missing_courses(completed, required) == {"Physics", "CS", "English"}

# Tests for build_student_report
def test_build_student_report_multiple_incomplete():
    students = {"S1", "S2", "S3"}
    enrollments = [("S1", "Math"), ("S2", "Math"), ("S2", "Physics"), ("S3", "Math"), ("S3", "Physics"), ("S3", "CS")]
    required = {"Math", "Physics", "CS"}
    result = build_student_report(students, enrollments, required)
    # Returns (count, student_id) tuples sorted by count descending
    assert result == [(2, "S1"), (1, "S2")]

def test_build_student_report_all_complete():
    students = {"S1"}
    enrollments = [("S1", "Math"), ("S1", "Physics")]
    required = {"Math", "Physics"}
    assert build_student_report(students, enrollments, required) == []

def test_build_student_report_sorting():
    students = {"S1", "S2", "S3", "S4"}
    enrollments = [("S1", "Math"), ("S2", "Math"), ("S2", "Physics"), ("S3", "Math"), ("S4", "CS")]
    required = {"Math", "Physics", "CS"}
    result = build_student_report(students, enrollments, required)
    # All have 2 missing except S2 has 1, sorted descending
    assert len(result) == 4
    assert result[0][0] == 2
    assert result[1][0] == 2
    assert result[2][0] == 2
    assert result[3] == (1, "S2")

def test_build_student_report_empty_students():
    students = set()
    enrollments = []
    required = {"Math", "Physics"}
    assert build_student_report(students, enrollments, required) == []

# Tests for find_incomplete_students (integration)
def test_find_incomplete_students_standard():
    enrollments = [("S1", "Math"), ("S1", "Physics"), ("S1", "CS"), ("S2", "Math"), ("S3", "Math"), ("S3", "CS")]
    required = {"Math", "Physics", "CS"}
    result = find_incomplete_students(enrollments, required)
    # Format: (count, student_id)
    assert result == [(2, "S2"), (1, "S3")]

def test_find_incomplete_students_all_complete():
    enrollments = [("S1", "Math"), ("S1", "Physics"), ("S2", "Math"), ("S2", "Physics")]
    required = {"Math", "Physics"}
    assert find_incomplete_students(enrollments, required) == []

def test_find_incomplete_students_all_incomplete():
    enrollments = [("S1", "Math"), ("S2", "CS"), ("S3", "Physics")]
    required = {"Math", "Physics", "CS"}
    result = find_incomplete_students(enrollments, required)
    # All have 2 missing
    assert len(result) == 3
    assert all(count == 2 for count, _ in result)
    student_ids = {sid for _, sid in result}
    assert student_ids == {"S1", "S2", "S3"}

def test_find_incomplete_students_empty():
    enrollments = []
    required = {"Math", "Physics"}
    assert find_incomplete_students(enrollments, required) == []
