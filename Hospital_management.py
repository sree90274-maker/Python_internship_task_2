patients = []
appointments = []
doctors = ['Dr.usha', 'Dr.Durga']
#Register Patient
def required_details():
    patient_name = input("Enter Patient Name: ")
    patient_age = int(input("Enter Patient Age: "))
    patient_gender = input("Enter Patient Gender: ")
    patient_weight = int(input("Enter Patient Weight: "))
    patient_disease = input("Enter Patient Disease: ")
    patient_address = input("Enter Patient Address: ")
    patient_appointment = input("Enter Appointment Time: ")
    print(f"\n{'GOVERNMENT HOSPITAL':^80}")
    print(f"{'12-25, CHILAKAVARIPALLI, CTM, MADANAPALLE, A.P 517319':^80}")
    print(f"{str(doctors):^80}")
    print("_" * 80)
    print("Patient Name:", patient_name)
    print("Patient Age:", patient_age)
    print("Patient Gender:", patient_gender)
    print("Patient Weight:", patient_weight)
    print("Patient Disease:", patient_disease)
    print("Patient Address:", patient_address)
    print("Appointment Time:", patient_appointment)
    print("\nPatient Registered Successfully!\n")
required_details()
#Schedule Appointment
def schedule_appointment():
    name = input("Enter Patient Name: ")
    time = input("Enter Appointment Time: ")
    appointments.append({"name": name,"time": time})
    print("Appointment Scheduled Successfully")
#Assign Doctor
def assign_doctor():
    name = input("Enter Patient Name: ")
    print("\nAvailable Doctors:")
    for doctor in doctors:
        print(doctor)
    doctor_name = input("Choose Doctor: ")
    print("\nDoctor Assigned Successfully")
    print("Patient:",name)
    print("Doctor:",doctor_name)
#Calculate Hospital Bill
def calculate_bill():
    consultation_fee = 500
    medicine_fee = int(input("Enter Medicine Fee: "))
    test_fee = int(input("Enter Test Fee: "))
    total_bill = consultation_fee + medicine_fee + test_fee
    print("\n----- BILL -----")
    print("Consultation Fee:",consultation_fee)
    print("Medicine Fee:",medicine_fee)
    print("Test Fee:",test_fee)
    print("Total Bill:",total_bill)
calculate_bill()
while True:
    print("\n===== HOSPITAL MANAGEMENT SYSTEM =====")
    print("1.Register Patient")
    print("2.Schedule Appointment")
    print("3.Assign Doctor")
    print("4.Calculate Bill")
    print("5.Exit")
    menu=int(input("Enter Choice: "))
    if menu==1:
        required_details()
    elif menu==2:
        schedule_appointment()
    elif menu==3:
        assign_doctor()
    elif menu==4:
        calculate_bill()
    elif menu==5:
        print("Thank You")
        break
    else:
        print("Invalid Choice")
