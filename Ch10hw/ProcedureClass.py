class Procedure:

    def __init__(self, prod_name, date, pract, charge, patient_id):
        self.__prod_name = prod_name
        self.__date = date
        self.__pract = pract
        self.__charge = int(charge)
        self.__patient_id = patient_id

    def get_prod_name(self):
        return self.__prod_name

    def get_date(self):
        return self.__date

    def get_pract(self):
        return self.__pract  

    def get_charge(self):
        return self.__charge     

    def get_patient_id(self):
        return self.__patient_id