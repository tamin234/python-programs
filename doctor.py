from ast import literal_eval
import os

def check_patient():
    os.system("clear")
    f=open("database/serials.txt",'r')
    x=f.read()
    serials=literal_eval(x)
    patient_id=input(f"Enter patient's id: ")
    for patient in serials:
        if str(patient[4])==patient_id:
            print("yes, he/she is patient")
    user=input("press q for exit: ")
    if user=="q":
        menu()

def patient_info():
    os.system("clear")
    f=open("database/serials.txt",'r')
    x=f.read()
    serials=literal_eval(x)
    patient_id=int(input(f"Enter patient's id: "))
    for patient in serials:
        if patient[4]==patient_id:
            print(f"serial: {patient[0]} name: {patient[1]} gender: {patient[2]} years: {patient[3]} patient id: {patient[4]} phone: {patient[5]} date: {patient[6]}")
    user=input("press q for exit: ")
    if user=="q":
        prescription()
        
        
        
        
def medicine():
    os.system("clear")
    i=1
    medicines_list=[]
    while True:
        medi=input(f"Enter {i} No. drug name or press q for exit: ")
        if medi=="q":
            break
        quantity=input(f"Enter quantity of {medi}: ")
        i=i+1
        usetime=input("Enter how many to eat drug: ")
        medicines_list.append([medi,quantity,usetime])
    with open("database/medicine.txt","a") as f:
        f.write(str(medicines_list))
    prescription()
        
def test():
    os.system("clear")
    i=1
    test_list=[]
    while True:
        test=input(f"Enter {i} No. test name or press q for exit: ")
        if test=="q":
            break
        i=i+1
        test_list.append([test])
    with open("database/test.txt","a") as f:
        f.writelines(str(test_list))
    prescription()
    

def prescription():
    os.system("clear")
    msg='''
1. Patient Info
2. Medicines
3. Tests
4. Back
press: '''
    user=input(msg)
    if user=="1":
        patient_info()
    elif user=="2":
        medicine()
    elif user=="3":
        test()
    elif user=="4":
        menu()
    

def view_past_record():
    os.system("clear")
    patient_id=input("Enter patient id: ")
    with open("database/past_records.txt","r") as f:
        x= f.read()
        total_patients=literal_eval(x)
        for  patient in total_patients:
            if str(patient[4])==patient_id:
                print("he/she was a old patient.")
           
                
                    
    user=input("press q for exit: ")
    if user=="q":
        menu()
def menu():
    os.system("clear")
    msg='''
1.Check Patient
2.Write Prescription
3.View Past Records of a patient
4.log out
press: 
    '''
    user=input(msg)
    if user=='1':
        check_patient()
    elif user=="2":
        prescription()
    elif user=="3":
        view_past_record()
    elif user=='4':
        os.system("python3 main.py")
    
if __name__=="__main__":
    menu()
    