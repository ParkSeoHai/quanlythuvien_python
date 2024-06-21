from library_manager.models import Users
from library_manager.dtos.ResponseDto import ResponseDto as Response

class UserDto(object):
    def __init__(self, id_user = '', name = '', email ='',
                password = '', role = 1, gender = 0, birthday = '',
                phone_number = '', address = ''):
        self.id_user = id_user
        self.name = name
        self.email = email
        self.password = password
        self.role = role
        self.gender = gender
        self.birthday = birthday
        self.phone_number = phone_number
        self.address = address
    
    def login(self):
        try:
            user = Users.objects.filter(email=self.email, password=self.password).first()
            if user:
                return Response(True, 'Login success', user.id_user)
            else:
                return Response(False, 'Login failed', None)
        except Exception as e:
            print(e)
            return Response(False, e.__str__(), None)

    def register(self):
        ...

    def check_email(email):
        try:
            user = Users.objects.filter(email=email).first()
            return True if user else False
        except Exception as e:
            print(e)
            return False

    def logout(self):
        ...
    
    def change_info(self):
        ...

    def add_book():
        ...
    
    def update_book():
        ...
    
    def delete_book():
        ...

    def search_book():
        ...
    
    def get_books():
        ...
    
    def get_phieumuonbytrangthai():
        ...
    
    def add_phieumuon():
        ...
    
    def update_phieumuon():
        ...

    def delete_phieumuon():
        ...
    
    def search_phieumuon():
        ...
    
    def get_phieumuons():
        ...

    def thuhoi_phieumuon():
        ...
    
    def nhap_sach():
        ...
    
    def huy_sach():
        ...

    def thongkesach():
        ...
    
    def kiemke():
        ...