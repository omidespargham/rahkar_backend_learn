"""
This is a code example with wrong approach.
We created this code intentionally to demonstrate composite concept in the next part
"""



class Component:
    def __init__(self, name):
        self.name = name

    def display(self):
        pass

class Department(Component):
    def __init__(self, name):
        super().__init__(name)
        self.sub_departments = []
        self.employees = []

    def add(self, component):
        if isinstance(component, Department):
            self.sub_departments.append(component)
        elif isinstance(component, Employee):
            self.employees.append(component)

    def display(self):
        print(f"Department: {self.name}")
        for sub_department in self.sub_departments:
            sub_department.display()
        for employee in self.employees:
            employee.display()

class Employee(Component):
    def display(self):
        print(f"Employee: {self.name}")

# Client code
engineering = Department("Engineering")
engineering.add(Employee("John"))
engineering.add(Employee("Alice"))

sales = Department("Sales")
sales.add(Employee("Bob"))
sales.add(Employee("Carol"))

company = Department("Company")
company.add(engineering)
company.add(sales)
company.display()

"""
This is a code example with right approach. 
we used composite concept in this code to implement tree like structure
"""

class Component:
    def __init__(self, name):
        self.name = name

    def display(self, indent=0):
        pass

class Department(Component):
    def __init__(self, name):
        super().__init__(name)
        self.children = []

    def add(self, component):
        self.children.append(component)

    def remove(self, component):
        self.children.remove(component)

    def display(self, indent=0):
        print(" " * indent + f"Department: {self.name}")
        for child in self.children:
            child.display(indent + 2)

class Employee(Component):
    def display(self, indent=0):
        print(" " * indent + f"Employee: {self.name}")

# Client code
engineering = Department("Engineering")
engineering.add(Employee("John"))
engineering.add(Employee("Alice"))

sales = Department("Sales")
sales.add(Employee("Bob"))
sales.add(Employee("Carol"))

company = Department("Company")
company.add(engineering)
company.add(sales)
company.display()


# todo : Implement More example for better understanding