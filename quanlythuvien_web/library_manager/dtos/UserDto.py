from library_manager.models import Users, Books, Phieunhaps, Ctphieunhaps, Categories, Phieumuons
from library_manager.dtos.ResponseDto import ResponseDto as Response

import uuid
from datetime import datetime
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
    def check_book(name):
        try:
            book = Books.objects.filter(name=name).first()
            return True if book else False
        except Exception as e:
            print(e)
            return False

    def logout(self):
        ...
    
    def change_info(self):
        ...

    def add_book(bookDto: BookDto):
        try:
            # Check if book exists in database by name
            is_book = UserDto.check_book(bookDto.name)

            if is_book is True:
                return Response(False, 'This book already exists', None)
            else:
                category = Categories.objects.filter(id_category=bookDto.id_category).first()
                # Add book to database
                book = Books(id_sach=bookDto.id_sach, name=bookDto.name, price=bookDto.price,
                             quantity=bookDto.quantity, image=bookDto.image, author=bookDto.author,
                             is_delete=bookDto.is_delete, id_category=category)
                book.save()
                return Response(True, 'Add book success', book.id_sach)
        except Exception as e:
            print(e)
            return Response(False, e.__str__(), None)

    def update_book(bookDto: BookDto):
        try:
            # Check if user exists in database by id
            category = Categories.objects.filter(id_category=bookDto.id_category).first()
            book = Books.objects.filter(id_sach=bookDto.id_sach).first()
            if book.name == bookDto.name:
                # Update user
                book.name = bookDto.name
                book.price = bookDto.price
                book.quantity = bookDto.quantity
                book.image = bookDto.image
                book.author = bookDto.author
                book.id_category = category
                book.save()
                return Response(True, 'Update book success', book.id_sach)
            else:
                is_book = UserDto.check_book(bookDto.name)
                if is_book is True:
                    return Response(False, 'Name is exists', book.id_sach)
                else:
                    book.name = bookDto.name
                    book.price = bookDto.price
                    book.quantity = bookDto.quantity
                    book.image = bookDto.image
                    book.author = bookDto.author
                    book.id_category = category
                    book.save()
                    return Response(True, 'Update book success', book.id_sach)
        except Exception as e:
            print(e)
            return Response(False, e.__str__(), None)

    def delete_book(id_sach):
        try:
            # Locate the book by its id_sach
            book = Books.objects.get(id_sach=id_sach)
            # Mark the book as deleted
            book.is_delete = 1
            book.save()
            return Response(True, 'Delete book success', None)
        except Books.DoesNotExist:
            return Response(False, 'Book not found', None)
        except Exception as e:
            print(e)
            return Response(False, str(e), None)

    def search_book(searchInput:str):
        try:
            books = (Books.objects.filter(name__icontains=searchInput) |
                     Books.objects.filter(author__icontains=searchInput))
            return Response(True, 'Search book success', books)
        except Exception as e:
            print(e)
            return Response(False, e.__str__(), None)

    
    def get_bookById(id_sach):
        try:
            book = Books.objects.filter(id_sach=id_sach).first()
            return Response(True, 'Get book success', book)
        except Exception as e:
            print(e)
            return Response(False, e.__str__(), None)

    def get_books():
        try:
            books = Books.objects.filter(is_delete = 0)
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
        try:
            phieumuons = Phieumuons.objects.all()
            return Response(True, 'Get phieumuon success', phieumuons)
        except Exception as e:
            print(e)
            return Response(False, e.__str__(), None)
    def thuhoi_phieumuon():
        ...
    def check_phieumuon():
        try:
            phieumuons = Phieumuons.objects.filter(ngay_tra='')
            for phieumuon in phieumuons:
                ngay_hen_tra = phieumuon.ngay_hen_tra
                today = datetime.now().strftime('%Y-%m-%d')

                if ngay_hen_tra and today:
                    a = datetime.strptime(ngay_hen_tra, "%Y/%m/%d")
                    b = datetime.strptime(today, "%Y-%m-%d")
                    c = (a-b).days
                phieumuon.trang_thai = int(c)
                phieumuon.save()
            phieumuonsbydate = Phieumuons.objects.filter(trang_thai__lt=5, ngay_tra= '')
            return Response(True, 'Get phieumuon success', phieumuonsbydate)
        except Exception as e:
            print(e)
            return Response(False, e.__str__(), None)

    def check_phieumuonDaTra():
        try:
            phieumuons = Phieumuons.objects.exclude(ngay_tra__exact='')
            for phieumuon in phieumuons:
                ngay_hen_tra = phieumuon.ngay_hen_tra
                ngay_tra = phieumuon.ngay_tra

                if ngay_hen_tra and ngay_tra:
                    a = datetime.strptime(ngay_hen_tra, "%Y/%m/%d")
                    b = datetime.strptime(ngay_tra, "%Y/%m/%d")
                    c = (a-b).days
                phieumuon.trang_thai = int(c)
                phieumuon.save()
            return Response(True, 'Get phieumuon success', phieumuons)
        except Exception as e:
            print(e)
            return Response(False, e.__str__(), None)
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