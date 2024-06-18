class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id

class EmployeeManager:
    def __init__(self):
        self.employees = []

    def add_employee(self, name, id):
        self.employees.append(Employee(name, id))

    def remove_employee(self, id):
        self.employees = [emp for emp in self.employees if emp.id != id]

    def display_employees(self):
        for emp in self.employees:
            print(f"ID: {emp.id}, Name: {emp.name}")

def main():
    manager = EmployeeManager()
    manager.add_employee("Alice", 1)
    manager.add_employee("Bob", 2)
    manager.display_employees()
    manager.remove_employee(1)
    manager.display_employees()

if __name__ == "__main__":
    main()
