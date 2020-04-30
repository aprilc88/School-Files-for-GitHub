'''
This program demonstrates how to create pie charts with data.
Autor: April Carchedi
'''
import matplotlib.pyplot as plt

def main():
    # Lists employees.
    employees = [50, 275, 230, 250, 92, 73, 30]
    # create a list of departments for the slices.
    department = ['Marketing', 'Information Technology',
                'Management', 'Human Resources', 'Finance',
                'Supply Chain', 'Manufacturing']
    # Create pie chart from list values.
    plt.pie(employees, labels=department)

    # Create title.
    plt.title('Employees by Department')

    # Display the line graph.
    plt.show()

# Call main function.
main()
