import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd

st.title("Employees Management System Using Streamlit")

selected = option_menu(
    None,
    ["Add", "Display", "Search"],
    icons = ['plus', 'window', 'filter'],
    menu_icon="cast",
    default_index=0,
    orientation="horizontal",
    key="menu"
)


def Add():
    # Number of employees to add
    num_employees = st.number_input("Enter how many employees you want to add:", min_value=1, step=1, key="num_employees_input")
    
    # Collect employee data in a list of dictionaries
    employee_data = []

    for i in range(num_employees):
        st.write(f"### Employee {i + 1}")
        emp_id = st.text_input(f"Employee ID {i + 1}:", key=f"emp_id_{i}")
        emp_name = st.text_input(f"Employee Name {i + 1}:", key=f"emp_name_{i}")
        emp_salary = st.text_input(f"Employee Salary {i + 1}:", key=f"emp_salary_{i}")

        # Only add employee data if all fields are filled
        if emp_id and emp_name and emp_salary:
            try:
                emp_salary = float(emp_salary)  # Ensure salary is a valid number
                employee_data.append({"emp_id": emp_id, "emp_name": emp_name, "emp_salary": emp_salary})
                st.success(f"Employee {i + 1} details recorded!")
            except ValueError:
                st.error(f"Invalid salary for Employee {i + 1}. Please enter a numeric value.")
        else:
            st.warning(f"Please complete all fields for Employee {i + 1}.")

    # Button to save all entered employee data
    if st.button("Save All Employees to File"):
        if employee_data:
            with open("employees.txt", "a") as file:
                for emp in employee_data:
                    file.write(f"{emp['emp_id']},{emp['emp_name']},{emp['emp_salary']}\n")
            st.success("All employees added successfully!")
        else:
            st.error("No employee data to save. Please complete all fields.")

def Display():
    try:
        data = pd.read_csv("employees.txt", delimiter=",", names=["emp_id", "emp_name", "emp_salary"])
        st.dataframe(data, use_container_width=True)
    except FileNotFoundError:
        st.error("No employees found.")

def Search():
    emp_id = st.text_input("Enter Employee ID to search:", key="search_emp_id_input")
    if emp_id:
        found = False
        try:
            with open("employees.txt", "r") as file:
                for line in file:
                    current_emp_id, emp_name, emp_salary = line.strip().split(',')
                    if emp_id == current_emp_id:
                        st.success(f"Employee found: {emp_name}, Salary: {emp_salary}")
                        found = True
                        break
            if not found:
                st.error("Employee not found.")
        except FileNotFoundError:
            st.error("No employees found.")
    
    
if selected == "Add":
    Add()
elif selected == "Display":
    Display()
elif selected == "Search":
    Search()






