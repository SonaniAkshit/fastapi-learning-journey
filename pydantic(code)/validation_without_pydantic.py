# 1. Without any Validation
def insert_student_data(name: str, age: int):
    print(name)
    print(age)
    print("Data Inserted")

insert_student_data('john','twenty')
insert_student_data('john','30')

# Problem: age is expected as int but passing string ('twenty')
# Python does not strictly enforce types, so it will not stop this
# 'twenty' is not a valid number, can break logic later
# '30' is also string, not integer (wrong type)
# No validation to check correct data before using it

# 2. With Type Validation
def insert_student_data(name: str, age: int):
   if type(name) == str and type(age) == int:
       print(name)
       print(age)
       print("Record Inserted!")
   else:
       raise TypeError('Incorrect DataType')
       
insert_student_data('john',-30)

# This manually checks types using type(), which works for simple cases
# It will correctly raise error if wrong datatype is passed
# Not scalable because you must repeat this in every function
# Hard to maintain as project grows (code duplication)
# Not flexible (fails for subclasses, better to use isinstance)


# 3. With Data Validation

def insert_student_data(name: str, age: int):
    if age < 0:
        raise ValueError('Age Cant be negative')
    else:
        print(age)
        print(name)
        print('Inserted!')
    
       
insert_student_data('john',30)

# Checks if age is negative and raises error if so
# Works for this simple case
# Missing type validation (age could be string and still pass until comparison breaks)
# Not scalable, you’ll repeat this logic in many places
# Validation is mixed with business logic (bad design for bigger projects)