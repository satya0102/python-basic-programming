import mysql.connector
from mysql.connector import Error

class HospitalManagementSystem:
    def __init__(self):
        self.connection = None

    def connect_to_database(self):
        try:
            self.connection = mysql.connector.connect(
                host='localhost',
                database='hospital_management',
                user='root',
                password='password'
            )
            print("Connected to database successfully")
        except Error as e:
            print(f"Error connecting to database: {e}")

    def register_patient(self, name, email, phone, address):
        cursor = self.connection.cursor()
        query = "INSERT INTO patients (name, email, phone, address) VALUES (%s, %s, %s, %s)"
        cursor.execute(query, (name, email, phone, address))
        self.connection.commit()
        print("Patient registered successfully")

    def register_doctor(self, name, email, phone, specialization):
        cursor = self.connection.cursor()
        query = "INSERT INTO doctors (name, email, phone, specialization) VALUES (%s, %s, %s, %s)"
        cursor.execute(query, (name, email, phone, specialization))
        self.connection.commit()
        print("Doctor registered successfully")

    def schedule_appointment(self, patient_id, doctor_id, date, time):
        cursor = self.connection.cursor()
        query = "INSERT INTO appointments (patient_id, doctor_id, date, time) VALUES (%s, %s, %s, %s)"
        cursor.execute(query, (patient_id, doctor_id, date, time))
        self.connection.commit()
        print("Appointment scheduled successfully")

    def manage_patient_records(self, patient_id, diagnosis, treatment):
        cursor = self.connection.cursor()
        query = "INSERT INTO patient_records (patient_id, diagnosis, treatment) VALUES (%s, %s, %s)"
        cursor.execute(query, (patient_id, diagnosis, treatment))
        self.connection.commit()
        print("Patient record updated successfully")

    def manage_billing(self, patient_id, amount, payment_status):
        cursor = self.connection.cursor()
        query = "INSERT INTO bills (patient_id, amount, payment_status) VALUES (%s, %s, %s)"
        cursor.execute(query, (patient_id, amount, payment_status))
        self.connection.commit()
        print("Bill updated successfully")

    def add_disease_specialist(self, doctor_id, disease_id):
        cursor = self.connection.cursor()
        query = "INSERT INTO disease_specialists (doctor_id, disease_id) VALUES (%s, %s)"
        cursor.execute(query, (doctor_id, disease_id))
        self.connection.commit()
        print("Disease specialist added successfully")

    def add_bed(self, hospital_id, bed_type, availability):
        cursor = self.connection.cursor()
        query = "INSERT INTO beds (hospital_id, bed_type, availability) VALUES (%s, %s, %s)"
        cursor.execute(query, (hospital_id, bed_type, availability))
        self.connection.commit()
        print("Bed added successfully")

    def search_nearby_hospitals(self, location):
        cursor = self.connection.cursor()
        query = "SELECT * FROM hospitals WHERE address LIKE %s"
        cursor.execute(query, (f"%{location}%",))
        results = cursor.fetchall()
        return results

# Example usage:
hms = HospitalManagementSystem()
hms.connect_to_database()

while True:
    print("1. Register patient")
    print("2. Register doctor")
    print("3. Schedule appointment")
    print("4. Manage patient records")
    print("5. Manage billing")
    print("6. Add disease specialist")
    print("7. Add bed")
    print("8. Search nearby hospitals")
    print("9. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter patient name: ")
        email = input("Enter patient email: ")
        phone = input("Enter patient phone: ")
        address = input("Enter patient address: ")
        hms.register_patient(name, email, phone, address)
    elif choice == "2":
        name = input("Enter doctor name: ")
        email = input("Enter doctor email: ")
        phone = input("Enter doctor phone: ")
        specialization = input("Enter doctor specialization: ")
        hms.register_doctor(name, email, phone, specialization)
    elif choice == "3":
        patient_id = int(input("Enter patient ID: "))
        doctor_id = int(input("Enter doctor ID: "))
        date = input("Enter appointment date (YYYY-MM-DD): ")
        time = input("Enter appointment time (HH:MM:SS): ")
        hms.schedule_appointment(patient_id, doctor_id, date, time)
    elif choice == "4":
        patient_id = int(input("Enter patient ID: "))
        diagnosis = input("Enter diagnosis: ")
        treatment = input("Enter treatment: ")
        hms.manage_patient_records(patient_id, diagnosis, treatment)
    elif choice == "5":
        print("choice")
        