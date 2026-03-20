# -----------------------------------------
# Task 1: Tuples for student information
# -----------------------------------------
print("1. Create tuples to store student information (name, age, grade).")

student1 = ("Alice", 20, "A")
student2 = ("Bob", 22, "B")
student3 = ("Charlie", 19, "A")

students = (student1, student2, student3)

print("\nAll Students:")
for s in students:
    print(s)


# -----------------------------------------
# Task 2: Tuple methods
# -----------------------------------------
print("\n2. Use tuple methods to count and index elements.")

print("Number of students:", len(students))
print("Index of Bob's record:", students.index(student2))


# -----------------------------------------
# Task 3: Sets for IDs and courses
# -----------------------------------------
print("\n3. Create sets to store unique student IDs and courses.")

student_ids = {101, 102, 103}
courses = {"Math", "Science", "History"}

print("Student IDs:", student_ids)
print("Courses:", courses)


# -----------------------------------------
# Task 4: Set operations
# -----------------------------------------
print("\n4. Perform set operations like union, intersection, and difference.")

student_ids.update({104, 105})
print("Updated IDs:", student_ids)

completed_courses = {"Math", "History"}

# -------------------------
# UNION
# -------------------------
union_result = courses | completed_courses
print("\nUnion:", union_result)

print("Visualisation:")
print("courses:            Math   Science   History")
print("completed_courses:  Math             History")
print("result:             Math   Science   History")


# -------------------------
# INTERSECTION
# -------------------------
intersection_result = courses & completed_courses
print("\nIntersection:", intersection_result)

print("Visualisation:")
print("courses:            Math   Science   History")
print("completed_courses:  Math             History")
print("shared:             Math   History")


# -------------------------
# DIFFERENCE
# -------------------------
difference_result = courses - completed_courses
print("\nDifference (remaining):", difference_result)

print("Visualisation:")
print("courses:            Math   Science   History")
print("completed_courses:  Math             History")
print("remaining:                  Science")


# -------------------------
# SYMMETRIC DIFFERENCE
# -------------------------
sym_diff_result = courses ^ completed_courses
print("\nSymmetric Difference:", sym_diff_result)

print("Visualisation:")
print("courses:            Math   Science   History")
print("completed_courses:  Math             History")
print("remove shared:             Science")
print("result:             Math? No → only unique items")
print("final:              Science")


# -----------------------------------------
# Task 5: Frozen sets
# -----------------------------------------
print("\n5. Use frozen sets to create immutable sets of student data.")

immutable_courses = frozenset(["Math", "Science", "History"])
immutable_student = frozenset(student1)

print("Frozen set of courses:", immutable_courses)
print("Frozen set of student1:", immutable_student)

# Attempting to modify a frozen set will raise an error:
immutable_courses.add("Biology")  # AttributeError
