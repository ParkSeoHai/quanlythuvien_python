from library_manager.models import Users, Books, Phieunhaps, Ctphieunhaps, Categories
from library_manager.dtos.ResponseDto import ResponseDto as Response

import uuid

from library_manager.dtos.PhieunhapDto import PhieunhapDto
from library_manager.dtos.BookDto import BookDto

class UserDto(object):
    def __init__(self, id_user = '', name = '', email ='',
                password = '', role = 1, gender = 0, birthday = '',
                phone_number = '', address = '', is_delete = 0):
        self.id_user = id_user
        self.name = name
        self.email = email
        self.password = password
        self.role = role
        self.gender = gender
        self.birthday = birthday
        self.phone_number = phone_number
        self.address = address
        self.is_delete = is_delete
    
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
        try:
            user = Users(id_user=self.id_user, name=self.name, email=self.email,
                        password=self.password, role=self.role, gender=self.gender,
                        birthday=self.birthday, phone_number=self.phone_number, address=self.address, is_delete=self.is_delete)
            user.save()
            return Response(True, 'Register success', user.id_user)
        except Exception as e:
            print(e)
            return Response(False, e.__str__(), None)

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
    
    def get_bookById(id_sach):
        try:
            book = Books.objects.filter(id_sach=id_sach).first()
            return Response(True, 'Get book success', book)
        except Exception as e:
            print(e)
            return Response(False, e.__str__(), None)

    def get_books():
        try:
            books = Books.objects.all()
            return Response(True, 'Get books success', books)
        except Exception as e:
            print(e)
            return Response(False, e.__str__(), None)
    
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
    
    def get_phieunhaps():
        try:
            phieunhaps = Phieunhaps.objects.all()
            return Response(True, 'Get phieunhaps success', phieunhaps)
        except Exception as e:
            print(e)
            return Response(False, e.__str__(), None)

    def nhap_sach(phieunhap: PhieunhapDto, bookDtos: list[BookDto]):
        try:
            # Get user by id
            user = Users.objects.filter(id_user=phieunhap.id_user).first()
            # Add phieunhap
            phieunhap = Phieunhaps(id_phieunhap=phieunhap.id_phieunhap, donvi_cungcap=phieunhap.donvi_cungcap,
                                    ngay_nhap=phieunhap.ngay_nhap, ly_do_nhap=phieunhap.ly_do_nhap, id_user=user)
            phieunhap.save()
            # Update book if book exits else add new book
            for bookDto in bookDtos:
                # Check book is exist by name
                book = Books.objects.filter(name=bookDto.name).first()
                if book:
                    # Update book
                    book.quantity += bookDto.quantity
                    book.save()
                else:
                    # Get category by id
                    category = Categories.objects.filter(id_category=bookDto.id_category).first()
                    # Add new book
                    bookNew = Books(id_sach=bookDto.id_sach, name=bookDto.name, price=bookDto.price, quantity=bookDto.quantity,
                             image=bookDto.image, author=bookDto.author, active=bookDto.active, id_category=category)
                    bookNew.save()
            # Add ctphieunhap
            for bookDto in bookDtos:
                # Get book by name
                book = Books.objects.filter(name=bookDto.name).first()

                ctphieunhap = Ctphieunhaps(id_ctphieunhap=str(uuid.uuid4()), id_phieunhap=phieunhap, id_sach=book,
                                           so_luong=bookDto.quantity, gia_nhap=bookDto.price)
                ctphieunhap.save()
            return Response(True, 'Nhap sach thanh cong', phieunhap.id_phieunhap)
        except Exception as e:
            print(e)
            return Response(False, e.__str__(), None)
    
    def get_phieunhapById(id):
        try:
            pn = Phieunhaps.objects.filter(id_phieunhap=id).first()
            return Response(True, 'Get phieunhap success', pn)
        except Exception as e:
            print(e)
            return Response(False, e.__str__(), None)
    
    def get_ctphieunhapBy_PnhapId(id_phieunhap):
        try:
            ctpns = Ctphieunhaps.objects.filter(id_phieunhap=id_phieunhap)
            return Response(True, 'Get ctphieunhaps success', ctpns)
        except Exception as e:
            print(e)
            return Response(False, e.__str__(), None)

    def huy_sach():
        ...

    def thongkesach():
        ...
    
    def kiemke():
        ...