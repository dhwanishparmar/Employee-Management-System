from database import connect_db

conn, cursor = connect_db()


# =========================
# LOAD DATA
# =========================
def load_data():
    try:
        with open("employees_500.txt", "r") as file:
            count = 0
            for line in file:
                data = line.strip().split(",")

                if len(data) != 5:
                    continue

                try:
                    cursor.execute(
                        "INSERT INTO employees VALUES (?, ?, ?, ?, ?)", data
                    )
                    count += 1
                except:
                    continue

        conn.commit()
        print(f"✅ {count} employees loaded successfully!\n")

    except FileNotFoundError:
        print("❌ employees_500.txt not found!\n")


# =========================
# ADD EMPLOYEE
# =========================
def add_employee():
    try:
        id = int(input("Enter ID: "))
        name = input("Enter Name: ")
        age = int(input("Enter Age: "))
        dept = input("Enter Department: ")
        salary = int(input("Enter Salary: "))

        cursor.execute(
            "INSERT INTO employees VALUES (?, ?, ?, ?, ?)",
            (id, name, age, dept, salary)
        )

        conn.commit()
        print("✅ Employee added!\n")

    except:
        print("❌ Error: ID may already exist or invalid input!\n")


# =========================
# VIEW EMPLOYEES
# =========================
def view_employees():
    cursor.execute("SELECT * FROM employees")
    rows = cursor.fetchall()

    if not rows:
        print("⚠️ No employees found.\n")
        return

    print("\n--- Employee List ---")
    for row in rows:
        print(row)
    print()


# =========================
# SEARCH EMPLOYEE
# =========================
def search_employee():
    try:
        id = int(input("Enter ID: "))
        cursor.execute("SELECT * FROM employees WHERE id=?", (id,))
        emp = cursor.fetchone()

        if emp:
            print("✅ Found:", emp, "\n")
        else:
            print("❌ Employee not found!\n")

    except:
        print("❌ Invalid input!\n")


# =========================
# UPDATE EMPLOYEE
# =========================
def update_employee():
    try:
        id = int(input("Enter ID: "))

        cursor.execute("SELECT * FROM employees WHERE id=?", (id,))
        if not cursor.fetchone():
            print("❌ Employee not found!\n")
            return

        name = input("New Name: ")
        age = int(input("New Age: "))
        dept = input("New Department: ")
        salary = int(input("New Salary: "))

        cursor.execute("""
        UPDATE employees
        SET name=?, age=?, department=?, salary=?
        WHERE id=?
        """, (name, age, dept, salary, id))

        conn.commit()
        print("✅ Employee updated!\n")

    except:
        print("❌ Error updating employee!\n")


# =========================
# DELETE EMPLOYEE
# =========================
def delete_employee():
    try:
        id = int(input("Enter ID: "))

        cursor.execute("SELECT * FROM employees WHERE id=?", (id,))
        if not cursor.fetchone():
            print("❌ Employee not found!\n")
            return

        cursor.execute("DELETE FROM employees WHERE id=?", (id,))
        conn.commit()
        print("✅ Employee deleted!\n")

    except:
        print("❌ Error deleting employee!\n")