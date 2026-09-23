# main.py - Updated Version
def greet_user(name):
    print(f"Hello, {name}! Welcome to AI/ML Version Control.")

def calculate_data_size(samples, features):
    return samples * features

if __name__ == "__main__":
    greet_user("Student")
    total_elements = calculate_data_size(1000, 20)
    print(f"Total Dataset Elements: {total_elements}")