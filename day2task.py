#Day 2 Task 

# -------------------
# Task 1: List
# -------------------
movies = ["Leo", "Jailer", "Avatar", "Titanic", "KGF"]

print(movies[0])      # first movie
print(movies[-1])     # last movie

movies.append("RRR")  # add movie
movies.pop(1)         # remove second movie

movies.sort()
print(movies)

print(len(movies))
print("Titanic" in movies)


# -------------------
# Task 2: Tuple
# -------------------
cities = ("Chennai", "Delhi", "Mumbai", "Bangalore", "Hyderabad")

print(cities[1])
print(cities[3])

# cities[0] = "Pune"
# ❌ Cannot change tuple because it is fixed (immutable)

a, b, c, d, e = cities
print(a, b, c, d, e)

temp = list(cities)
temp.append("Pune")
cities = tuple(temp)
print(cities)


# -------------------
# Task 3: Dictionary
# -------------------
student = {
    "name": "Hema",
    "age": 21,
    "grade": "A",
    "city": "Arni"
}

print(student.keys())
print(student.values())
print(student.items())

student["grade"] = "A+"
student["email"] = "selvi@gmail.com"

del student["city"]

print(student)


# -------------------
# Task 4: Set
# -------------------
week1 = {"Maths", "Python", "Physics"}
week2 = {"Python", "AI", "ML"}

print(week1 | week2)   # union
print(week1 & week2)   # common
print(week1 - week2)   # difference

week1.add("Stats")
week2.remove("AI")

print("Python" in week1)


# -------------------
# Task 5: Functions
# -------------------
def greet(name):
    print("Hello", name)

def add(a, b):
    return a + b

def max_num(a, b, c):
    return max(a, b, c)

def even(n):
    return n % 2 == 0

greet("Selvi")
print(add(5, 10))
print(max_num(1, 9, 3))
print(even(4))


# -------------------
# Task 6: Default
# -------------------
def introduce(name, lang="Python"):
    print(name, "is learning", lang)

introduce("Hema")
introduce("Hema", "SQL")

def discount(price, d=10):
    return price - price*d/100

print(discount(1000))


# -------------------
# Task 7: if else
# -------------------
num = int(input("Enter number: "))

if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")


# -------------------
# Task 8: Loop
# -------------------
for i in range(1, 21):
    print(i)

for i in range(1, 51):
    if i % 2 == 0:
        print(i)

fruits = ["Apple", "Mango", "Banana"]
for i in range(len(fruits)):
    print(i, fruits[i])
