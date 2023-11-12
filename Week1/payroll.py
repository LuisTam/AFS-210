class Employee:
    def __init__(self, first_name, last_name, employee_id, hourly_pay):
        self.first_name = first_name
        self.last_name = last_name
        self.employee_id = employee_id
        self.hourly_pay = hourly_pay

    def pay(self, hours_worked):
        if hours_worked <= 40:
            total_pay = self.hourly_pay * hours_worked
        else:
            regular_pay = self.hourly_pay * 40
            overtime_pay = (hours_worked - 40) * 1.5 * self.hourly_pay
            total_pay = regular_pay + overtime_pay

        return total_pay

# Prompt user for employee information
first_name = input("Enter employee's first name: ")
last_name = input("Enter employee's last name: ")
employee_id = int(input("Enter employee ID: "))
hourly_pay = float(input("Enter employee's hourly pay: "))

# Create an instance of the Employee class
employee = Employee(first_name, last_name, employee_id, hourly_pay)

# Prompt user for hours worked
hours_worked = float(input("Enter hours worked for the week: "))

# Calculate and display the total pay
total_pay = employee.pay(hours_worked)
print(f"\nEmployee: {employee.first_name} {employee.last_name}")
print(f"Total Pay for the Week: ${total_pay:.2f}")
