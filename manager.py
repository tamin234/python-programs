
from datetime import date
from random import randint
from ast import literal_eval
import os
def taking_serial():
    records_of_patient=[]
    sl=0
    os.system("clear")
    while True:
        sl=sl+1
        print("="*40)
        patient_name=input("patient Name or press q for exit: ")
        if patient_name =='q':
            break
        phone=input("enter patient phone: ")
        serial_date=date.today()
        male_female=input('press 1 for male\npress 2 for female\nEnter: ')
        gender="Male" if male_female=="1" else "female"
        ps_age=input("patient age: ")
        ftime=serial_date.strftime('%Y/%m/%d')
        patient_id=randint(1000,9999)
        records_of_patient.append([sl,patient_name,gender,ps_age,patient_id,phone,ftime])
    with open("database/serials.txt","w") as f:
        f.writelines(str(records_of_patient))
        
    with open("database/past_records.txt",'r') as f:
        x=f.read()
        if x:
            old_ls=literal_eval(x)
        else:
            old_ls=[]
    with open("database/past_records.txt",'w') as f:
        old_ls=old_ls+records_of_patient
        f.writelines(str(old_ls))
    menu()
    
    
    
def view_serial():
    os.system("clear")
    with open("database/serials.txt",'r') as f:
        x=f.read()
        pasients=literal_eval(x)
        print()
    for y in pasients:
        print(f"sl: {y[0]}, patient name: {y[1]}, gander: {y[2]}, age: {y[3]}, id: {y[4]}, phone: {y[5]}, date:{y[6]}\n")
    m=input("press q for back: ")
    if m=="q":
        menu()



def add_new_drug():
    os.system("clear")
    
    
    with open("database/drugs.txt","r") as file:
        drug=file.read()
    if drug:
        drug_list=literal_eval(drug)
    else:
        drug_list=[]
    while True:
        drug_name=input("add drug name or press q for exit: ")
        if drug_name=="q":
            break
        quantity_of_drug=input(f"Quantity of {drug_name}: ")
        price=input(f"price of {drug_name}: ")
        expired_date=input("expired date(dd/mm/yy): ")
        a=[drug_name,price,expired_date,quantity_of_drug]
        drug_list.append(a)
    with open("database/drugs.txt","w") as f:
        f.write(str(drug_list))
    manage_drug_menu()
    
    

def view_all_drugs():
    os.system("clear")
    with open("database/drugs.txt","r") as f:
        drugs=f.read()
        drugs_ls=literal_eval(drugs)
        sl=1
        for a in drugs_ls:
            print(f"sl: {sl} Drug name: {a[0]} price: {a[1]} quantity: {a[3]} expired date: {a[2]}")
            sl=sl+1
    user=input("press q for exit: ")
    if user=="q":
        manage_drug_menu()
        
        
        
def update_stock():
    os.system("clear")
    with open("database/drugs.txt","r") as f:
        drugs=f.read()
        drugs_list=literal_eval(drugs)
        print("All drugs: ")
        i=1
        for x in drugs_list:
            print(f"sl: {i} name: {x[0]} price: {x[1]} quantity: {x[3]} expired date: {x[2]} \n")
            i=i+1
    indx=int(input("Enter the serial for update drugs: "))-1
    for x in drugs_list:
        if drugs_list[indx]==x:
            name=input("new name of the drug: ")
            price=input(f"price of {name}")
            quantity=input(f"Quantity of {name}: ")
            exp_date=input(f"expired date of {name} (yy/mm/dd): ")
            x[0]=name
            x[1]=price
            x[2]=exp_date
            x[3]=quantity
    with open("database/drugs.txt","w") as f:
        f.writelines(str(drugs_list))
    # for x in drugs_list:
    #     print(f"sl: {x[0]} name: {x[1]}  price: {x[2]}  expired date: {x[3]} ")
    user=input("update successfully\npress q for exit: ")
    if user=="q":
        manage_drug_menu()
   

def delete_drug():
    os.system("clear")
    with open("database/drugs.txt","r") as f:
        drugs=f.read()
        drugs_list=literal_eval(drugs)
        print("All drugs: ")
        sl=1
        for x in drugs_list:
            print(f"sl: {sl} name: {x[0]} quantity: {x[3]} price: {x[1]} expired date: {x[2]} \n")
            sl=sl+1
    indx=int(input("enter the serial of drug which you want to remove: "))-1
    for i in drugs_list:
        if drugs_list[indx]==i:
            print(f"{i[0]} deleted")
            index=drugs_list.index(i)
            drugs_list.pop(index)
    with open("database/drugs.txt","w") as f:
        f.write(str(drugs_list))

    user=input("press q for exit: ")
    if user=="q":
        manage_drug_menu()
        
        

def sell_drug():
    os.system("clear")

    # read medicine list
    with open("database/medicine.txt", "r") as f:
        medicines = literal_eval(f.read())

    # read drug stock
    with open("database/drugs.txt", "r") as f:
        drugs = literal_eval(f.read())

    sold_items = []
    unsold_items = []

    for medicine in medicines:
        found = False
        for drug in drugs:
            if drug[0] == medicine[0]:
                drug[3] = int(drug[3]) - int(medicine[1])
                print(f"{medicine[0]} sold {medicine[1]} pieces")
                sold_items.append(medicine)
                found = True
                break

        if not found:
            unsold_items.append(medicine)

    # save unsold medicines
    if unsold_items:
        print("We don't have:", unsold_items)
        with open("database/unsold.txt", "w") as f:
            f.write(str(unsold_items))
    else:
        with open("database/medicine.txt", "w") as f:
            f.write("")

    # update drug stock
    with open("database/drugs.txt", "w") as f:
        f.write(str(drugs))

    a = input("press q for exit: ")
    if a == "q":
        menu()
        
def manage_drug_menu():
    os.system("clear")
    msg="""
    1. Add New Drug
    2. View All Drugs
    3. Update Stock
    4. Delete Drug
    5. Back
    press: """
    user=input(msg)
    if user=="1":
        add_new_drug()
    elif user=="2":
        view_all_drugs()
    elif user=="3":
        update_stock()
    elif user=="4":
        delete_drug()
    elif user=="5":
        menu()


def menu():
    os.system("clear")
    msg='''
    1. Take Serial
    2. View Serials
    3. Manage Drugs
    4. drug sales
    5. Logout
    press: '''
    user=input(msg)
    if user=="1":
        taking_serial()
    elif user=="2":
        view_serial()
    elif user=="3":
        manage_drug_menu()
    elif user=="4":
        sell_drug()
    elif user=="5":
        os.system("python3 main.py")

if __name__=="__main__":

    menu()