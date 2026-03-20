# ============================================================
# 1. LAMBDAS
# ============================================================

print("\n========== 1. LAMBDAS ==========\n")

square = lambda x: x * x
print("[1.1 Lambda] square(5) =", square(5))

add = lambda a, b: a + b
print("[1.2 Lambda] add(3, 7) =", add(3, 7))

numbers = [1, 2, 3, 4, 5]
squares = list(map(lambda n: n ** 2, numbers))
print("[1.3 Lambda + map] squares =", squares)


# ============================================================
# 2. ARRAYS
# ============================================================

print("\n========== 2. ARRAYS ==========\n")

from array import array
import numpy as np

list1 = [1, 2, 3, 4, 6]
print("[2.1 List] list1 =", list1)

int_array = array('i', [1, 2, 3, 4, 5])
print("[2.2 array module] int_array =", int_array)

np_array = np.array([1, 2, 3, 4, 5, 6])
print("[2.3 NumPy] np_array =", np_array)

arr1 = np.array([1, 2, 3, 4])
arr2 = np.array([4, 5, 6, 7])
result = arr1 + arr2
print("[2.4 NumPy] element-wise addition =", result)

print("[2.5 NumPy] first element =", np_array[0])
print("[2.6 NumPy] slice 1:4 =", np_array[1:4])

reshaped = np.array([[1, 2, 3], [4, 5, 6]])
print("[2.7 NumPy] reshaped array:\n", reshaped)

print("[2.8 NumPy] sorted =", np.sort(np_array))
print("[2.9 NumPy] mean =", np.mean(np_array))

print("[2.10 NumPy] iteration:")
for element in np_array:
    print(" →", element)


# ============================================================
# 3. OBJECT ORIENTED PROGRAMMING
# ============================================================

print("\n========== 3. OBJECT ORIENTED PROGRAMMING ==========\n")

class MyClass:
    class_variable = "I am a class variable"

    def __init__(self, a, b):
        self.attribute1 = a
        self.attribute2 = b

    def instance_method(self):
        return f"Instance method → {self.attribute1}, {self.attribute2}"

obj = MyClass("First", "Second")
print("[3.1 OOP] instance_method =", obj.instance_method())
print("[3.2 OOP] class variable =", MyClass.class_variable)
print("[3.3 OOP] instance attribute =", obj.attribute1)


# ============================================================
# 4. SCOPE (LEGB)
# ============================================================

print("\n========== 4. SCOPE (LEGB) ==========\n")

x = 10  # Global

def outer_function():
    x = 50  # Enclosing

    def inner_function():
        x = 60  # Local
        print("[4.1 LEGB] Inner (Local) =", x)

    inner_function()
    print("[4.2 LEGB] Outer (Enclosing) =", x)

outer_function()
print("[4.3 LEGB] Global =", x)

# global keyword
global_var = "Initial"

def modify_global():
    global global_var
    global_var = "Modified globally"

modify_global()
print("[4.4 Scope] global_var =", global_var)

# nonlocal keyword
def outer():
    outer_var = 90

    def inner():
        nonlocal outer_var
        outer_var = 100

    inner()
    print("[4.5 Scope] outer_var after nonlocal =", outer_var)

outer()


# ============================================================
# 5. MODULES
# ============================================================

print("\n========== 5. MODULES ==========\n")

# mymodule.py should contain:
# def greeting(name):
#     print("Hello", name)
#
# person1 = {"name": "John", "age": 36, "country": "Norway"}

import mymodule
from mymodule import greeting
import mymodule as mx

greeting("Jonathan")
print("[5.1 Module] greeting('Jonathan') executed")

mymodule.greeting("Emmanuel")
print("[5.2 Module] greeting('Emmanuel') executed")

print("[5.3 Module] person1 age =", mymodule.person1["age"])
print("[5.4 Module alias] person1 age =", mx.person1["age"])

import platform
print("[5.5 Built-in module] OS =", platform.system())

print("[5.6 dir()] platform module contents =", dir(platform))
