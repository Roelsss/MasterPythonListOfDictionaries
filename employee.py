# List of employee dictionaries
employees = [
    {"id": 1, "name": "John Doe", "department": "Sales", "age": 30, "email": "john.doe@company.com"},
    {"id": 2, "name": "Jane Smith", "department": "Human Resources", "age": 25, "email": "jane.smith@company.com"},
    {"id": 3, "name": "Mark Johnson", "department": "IT", "age": 40, "email": "mark.johnson@company.com"},
    {"id": 4, "name": "Lisa Wong", "department": "Marketing", "age": 28, "email": "lisa.wong@company.com"},
    {"id": 5, "name": "Paul McDonald", "department": "Finance", "age": 35, "email": "paul.mcdonald@company.com"}
]

# Print employee data
for employee in employees:
    print(f"Employee ID: {employee['id']}, Name: {employee['name']}, Department: {employee['department']}, Age: {employee['age']}, Email: {employee['email']}")
