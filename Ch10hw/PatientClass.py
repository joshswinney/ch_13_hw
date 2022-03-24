class Patient:

    def __init__(self, patient_id, Name, address, phone, veteran_status):
        self.__patient_id = patient_id
        self.__Name = Name
        self.__address = address
        self.__phone = phone
        self.__veteran_status = veteran_status

    def get_patient_id(self):
        return self.__patient_id

    def get_Name(self):
        return self.__Name

    def get_address(self):
        return self.__address

    def get_phone(self):
        return self.__phone

    def get_veteran_status(self):
        return self.__veteran_status