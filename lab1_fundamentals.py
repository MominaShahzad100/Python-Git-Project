
# 1. Variables and Data Types
student_name = "Momina Shahzad"  # String
num_samples = 100                 # Integer
learning_rate = 0.01             # Float
is_trained = True                # Boolean

print("--- 1. Variables and Data Types ---")
print(f"Student Name: {student_name} (Type: {type(student_name)})")
print(f"Num Samples: {num_samples} (Type: {type(num_samples)})")
print(f"Learning Rate: {learning_rate} (Type: {type(learning_rate)})")
print(f"Is Trained: {is_trained} (Type: {type(is_trained)})\n")


# 2. Arithmetic, Relational, and Logical Operators
a = 15
b = 4

print("--- 2. Operators ---")
print(f"Arithmetic: {a} + {b} = {a + b}, {a} * {b} = {a * b}, {a} / {b} = {a / b}")
print(f"Relational: {a} > {b} is {a > b}, {a} == {b} is {a == b}")
print(f"Logical: ({a} > 10) and ({b} < 5) is {(a > 10) and (b < 5)}\n")


# 3. Conditional Statements (if-else)
score = 85
print("--- 3. Conditional Statements ---")
if score >= 90:
    grade = "A+"
elif score >= 80:
    grade = "A"
else:
    grade = "B"
print(f"Score: {score} -> Grade: {grade}\n")


# 4. Loops (for and while)
print("--- 4. Loops ---")
print("For Loop (Processing iterations):")
for i in range(1, 4):
    print(f"  Iteration {i}")

print("While Loop (Countdown):")
count = 3
while count > 0:
    print(f"  Countdown: {count}")
    count -= 1
print()


# 5. Functions
def calculate_loss(y_true, y_pred):
    """Calculates Absolute Error Loss"""
    loss = abs(y_true - y_pred)
    return loss

print("--- 5. Functions ---")
actual = 10.0
predicted = 8.5
error = calculate_loss(actual, predicted)
print(f"Actual: {actual}, Predicted: {predicted} -> Loss: {error}\n")


# 6. Lists and Basic Operations
dataset = [12.5, 45.0, 78.2, 23.4, 89.1]
print("--- 6. Lists & List Operations ---")
print(f"Original List: {dataset}")

dataset.append(99.9)             # Append
print(f"After Append: {dataset}")

dataset.sort()                   # Sort
print(f"Sorted List: {dataset}")

sliced_data = dataset[1:4]       # Slicing
print(f"Sliced List (index 1 to 3): {sliced_data}")