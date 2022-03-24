import PatientClass as pc
import ProcedureClass as prdc

def main():

    p1 = pc.Patient(1, "Matt Jones", "123 Main st, Waco TX 76706", "254-555-7415", "TRUE")

    prdc1 = prdc.Procedure("Physical Exam", "2/15/2022", "Dr. Irvine", 250, 1)
    prdc2 = prdc.Procedure("MRI", "2/15/2022", "Dr. Hamilton", 1500, 1)
    prdc3 = prdc.Procedure("CT Scan", "2/17/2022", "Dr. Drey", 1200, 2)


    charges = 0

    print('*** Patient Bill ***')
    print('Name: ', p1.get_Name())
    print('Address: ', p1.get_address())
    print('Phone: ', p1.get_phone())
    
    print()

    print('Procedure: ', prdc1.get_prod_name())
    print('Date: ', prdc1.get_date())
    print('Practictioner: ', prdc1.get_pract())
    print('Charge: $', prdc1.get_charge)
    
    print()
    
    print('Procedure: ', prdc2.get_prod_name())
    print('Date: ', prdc2.get_date())
    print('Practictioner: ', prdc2.get_pract())
    print('Charge: $', prdc2.get_charge)
    
    print()
   
    if prdc1.get_patient_id() == p1.get_patient_id():
        charges += prdc1.get_charge()

    if prdc2.get_patient_id() == p1.get_patient_id():
        charges += prdc2.get_charge()

    if prdc3.get_patient_id() == p1.get_patient_id():
        charges += prdc3.get_charge()

    if p1.get_verteran_status() == "TRUE" or "True" or "true":
        charges *= .6

    print('Total Charges: $', charges)

main()