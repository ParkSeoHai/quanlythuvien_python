from library_manager.models import Users, Books, Phieunhaps, Ctphieunhaps, Docgias
from library_manager.models import Categories, Phieumuons, Phieuhuys, Ctphieuhuys, Thethuviens

from collections import defaultdict
import uuid
from datetime import datetime

from library_manager.dtos.ResponseDto import ResponseDto as Response
from library_manager.dtos.PhieunhapDto import PhieunhapDto
from library_manager.dtos.BookDto import BookDto
from library_manager.dtos.PhieumuonDto import PhieumuonDto
from library_manager.dtos.PhieuhuyDto import PhieuhuyDto

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
            if user is None:
                return Response(False, 'Tài khoản hoặc mật khẩu không chính xác', None)
            if user.is_delete == 1:
                return Response(False, 'Tài khoản này đã bị xóa', None)
            else:
                return Response(True, 'Đăng nhập thành công', user.id_user)
        except Exception as e:
            print(e)
            return Response(False, e.__str__(), None)

    def register(self):
        try:
            user = Users(id_user=self.id_user, name=self.name, email=self.email,
                        password=self.password, role=self.role, gender=self.gender,
                        birthday=self.birthday, phone_number=self.phone_number,
                        address=self.address, is_delete=self.is_delete)
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
    
    def change_info(self):
        ...

    def check_book(name):
        try:
            book = Books.objects.filter(name=name).first()
            return True if book else False
        except Exception as e:
            print(e)
            return False

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
                             is_delete=bookDto.is_delete, id_category=category,ngay_tao =bookDto.ngay_tao)
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
            if book is None:
                return Response(False, 'Book not found')
            return Response(True, 'Get book success', book)
        except Exception as e:
            print(e)
            return Response(False, e.__str__())

    def get_books():
        try:
            books = Books.objects.filter(is_delete=0)
            return Response(True, 'Get books success', books)
        except Exception as e:
            print(e)
            return Response(False, e.__str__(), None)
    def get_docgias():
        try:
            docgias = Docgias.objects.filter(is_delete=0)
            return Response(True, 'Get docgias success', docgias)
        except Exception as e:
            print(e)
            return Response(False, e.__str__(),None)

    def search_booksByName(name):
        try:
            books = Books.objects.filter(name__icontains=name, is_delete=0)
            return Response(True, "Get books success", books)
        except Exception as e:
            print(e)
            return Response(False, e.__str__(), None)
        
    def get_info_thethuvienById(id):
        try:
            ttv = Thethuviens.objects.filter(id_the=id).first()
            if ttv is None:
                return Response(False, "Thethuvien not found", None)
            else:
                # Get info docgia
                docgia = Docgias.objects.filter(id_docgia=ttv.id_docgia.id_docgia).first()
                # Get info phieumuons by thethuvien
                phieumuons = Phieumuons.objects.filter(id_the=ttv, trang_thai=0)
                # Get info books
                books = []
                for phieumuon in phieumuons:
                    book = {
                        'name': phieumuon.id_sach.name,
                        'price': phieumuon.id_sach.price,
                        'quantity': phieumuon.id_sach.quantity,
                        'ngay_muon': phieumuon.ngay_tao,
                        'ngay_hen_tra': phieumuon.ngay_hen_tra
                    }
                    books.append(book)
                    
                data = {
                    'hoten': docgia.name,
                    'type': ttv.type,
                    'ngay_het_han': ttv.ngay_het_han,
                    'books': books
                }
                return Response(True, 'Get info success', data)
        except Exception as e:
            return Response(False, e.__str__(), None)

    def get_phieumuonbytrangthai():
        ...
    
    def get_phieumuonById(id):
        try:
            # Get phieumuon
            phieumuon = Phieumuons.objects.filter(id_phieumuon=id).first()
            if phieumuon is None:
                return Response(False, 'Phieumuon not found', None)
            
            phieumuonResponse = {
                'id_phieumuon': phieumuon.id_phieumuon,
                'ngay_tao': phieumuon.ngay_tao,
                'ngay_hen_tra': phieumuon.ngay_hen_tra,
                'trang_thai': phieumuon.trang_thai,
                'ngay_tra': phieumuon.ngay_tra,
                'ghi_chu': phieumuon.ghi_chu,
                'so_luong': phieumuon.so_luong,
                'user': {
                    'id_user': phieumuon.id_user.id_user,
                    'name': phieumuon.id_user.name,
                    'role': phieumuon.id_user.role,
                },
                'book': {
                    'id_sach': phieumuon.id_sach.id_sach,
                    'name': phieumuon.id_sach.name,
                    'price': phieumuon.id_sach.price,
                    'quantity': phieumuon.id_sach.quantity,
                    'author': phieumuon.id_sach.author,
                    'image': phieumuon.id_sach.image,
                    'category': phieumuon.id_sach.id_category.name,
                },
                'docgia': {
                    'id_docgia': phieumuon.id_the.id_docgia.id_docgia,
                    'id_the': phieumuon.id_the.id_the,
                    'name': phieumuon.id_the.id_docgia.name,
                    'type': phieumuon.id_the.type,
                    'ngay_tao': phieumuon.id_the.ngay_tao,
                    'ngay_het_han': phieumuon.id_the.ngay_het_han,
                    'ghi_chu': phieumuon.id_the.ghi_chu,
                }
            }
            
            return Response(True, 'Get phieumuon success', phieumuonResponse)
        except Exception as e:
            return Response(False, e.__str__(), None)

    def add_phieumuon(phieumuonDto: PhieumuonDto, bookName):
        try:
            # Search book by name
            book = Books.objects.filter(name=bookName).first()
            if book is None:
                return Response(False, "Book not found", None)
            # Get user
            user = Users.objects.filter(id_user=phieumuonDto.id_user).first()
            if user is None:
                return Response(False, "User not found", None)
            # Get thethuvien
            ttv = Thethuviens.objects.filter(id_the=phieumuonDto.id_the).first()
            if ttv is None:
                return Response(False, "Thethuvien not found", None)
            # Check if docgia has phieumuons then does not add to database
            is_phieumuon = Phieumuons.objects.filter(id_the=ttv, trang_thai=0).first()
            if is_phieumuon is not None:
                return Response(False, "Add phieumuon failed because docgia has phieumuons", None)

            # Add phieumuon to database
            phieumuon = Phieumuons(id_phieumuon=phieumuonDto.id_phieumuon, ngay_tao=phieumuonDto.ngay_tao,
                                   ngay_hen_tra=phieumuonDto.ngay_hen_tra, ghi_chu=phieumuonDto.ghi_chu,
                                   trang_thai=phieumuonDto.trang_thai, ngay_tra=phieumuonDto.ngay_tra,
                                   so_luong=phieumuonDto.so_luong, id_user=user, id_sach=book, id_the=ttv,
                                   is_delete=phieumuonDto.is_delete)
            phieumuon.save()
            # Update quantity book
            book.quantity -= phieumuonDto.so_luong
            book.save()

            return Response(True, 'Add phieumuon success', phieumuon.id_phieumuon)
        except Exception as e:
            return Response(False, e.__str__(), None)
    
    def update_phieumuon(phieumuonDto: PhieumuonDto, bookName):
        try:
            # Find book by name
            book = Books.objects.filter(name=bookName).first()
            if book is None:
                return Response(False, f'Book {bookName} not found', None)
            
            # Get phieumuon by id
            phieumuon = Phieumuons.objects.filter(id_phieumuon=phieumuonDto.id_phieumuon).first()
            if phieumuon is None:
                return Response(False, 'Phieumuon not found', None)
            # Update quantity book old
            phieumuon.id_sach.quantity += phieumuon.so_luong
            phieumuon.id_sach.save()
            # Update quantity book new
            book.quantity -= phieumuonDto.so_luong
            book.save()
            # Update phieumuon
            phieumuon.id_sach = book
            phieumuon.ngay_tao = phieumuonDto.ngay_tao
            phieumuon.ngay_hen_tra = phieumuonDto.ngay_hen_tra
            phieumuon.ghi_chu = phieumuonDto.ghi_chu
            phieumuon.save()

            return Response(True, 'Update phieumuon success', phieumuon.id_phieumuon)
        except Exception as e:
            return Response(False, e.__str__(), None)

    def delete_phieumuon(id):
        try:
            # Find phieumuon
            phieumuon = Phieumuons.objects.filter(id_phieumuon=id).first()
            if phieumuon is None:
                return Response(False, "Phieumuon not found", None)
            else:
                # Update quantity book
                book = Books.objects.filter(id_sach=phieumuon.id_sach.id_sach).first()
                if book is None:
                    return Response(False, "Book not found", None)
                
                book.quantity += phieumuon.so_luong
                phieumuon.delete()
                book.save()
                return Response(True, "Delete phieumuon success", phieumuon.id_phieumuon)
        except Exception as e:
            return Response(False, e.__str__(), None)

    def search_phieumuonById_the(id_the):
        try:
            # Get thethuvien by id_the
            thethuviens = Thethuviens.objects.filter(id_the__icontains=id_the)
            if (id_the == 'all'):
                thethuviens = Thethuviens.objects.all()

            # Get phieumuon
            phieumuons = []
            for ttv in thethuviens:
                phieumuon = Phieumuons.objects.filter(id_the=ttv).first()
                # Convert to phieumuon response object
                phieumuonObject = {
                    'id_phieumuon': phieumuon.id_phieumuon,
                    'bookName': phieumuon.id_sach.name,
                    'id_the': phieumuon.id_the.id_the,
                    'docgiaName': phieumuon.id_the.id_docgia.name,
                    'ngay_tao': phieumuon.ngay_tao,
                    'ngay_hen_tra': phieumuon.ngay_hen_tra,
                    'trang_thai': phieumuon.trang_thai,
                    'so_luong': phieumuon.so_luong,
                    'userName': phieumuon.id_user.name,
                    'ghichu': phieumuon.ghi_chu
                }
                phieumuons.append(phieumuonObject)

            return Response(True, f'Get phieumuons success. ({len(phieumuons)} result)', phieumuons)
        except Exception as e:
            return Response(False, e.__str__(), None)
    
    def get_phieumuons():
        try:
            phieumuons = Phieumuons.objects.filter(trang_thai=0, is_delete=0)
            return Response(True, 'Get phieumuon success', phieumuons)
        except Exception as e:
            print(e)
            return Response(False, e.__str__(), None)
        
    def thuhoi_phieumuon(id_phieumuon, ngay_tra, ghi_chu):
        try:
            phieumuon = Phieumuons.objects.filter(id_phieumuon=id_phieumuon).first()
            if phieumuon is None:
                return Response(False, 'Phieumuon not found', None)
            
            # Update trang_thai phieumuon
            phieumuon.trang_thai = 1
            phieumuon.ngay_tra = ngay_tra
            if ghi_chu != "":
                phieumuon.ghi_chu = ghi_chu
            phieumuon.save()

            # Update quantity book
            phieumuon.id_sach.quantity += phieumuon.so_luong
            phieumuon.id_sach.save()

            return Response(True, 'Thu hồi phiếu mượn thành công', phieumuon.id_phieumuon)
        except Exception as e:
            return Response(False, e.__str__(), None)
    
    def check_phieumuon():
        try:
            phieumuons = Phieumuons.objects.filter(trang_thai=0, is_delete=0)
            return Response(True, 'Get phieumuon success', phieumuons)
        except Exception as e:
            print(e)
            return Response(False, e.__str__(), None)

    def check_phieumuonDaTra():
        try:
            phieumuons = Phieumuons.objects.filter(trang_thai=1,is_delete=0)
            return Response(True, 'Get phieumuon success', phieumuons)
        except Exception as e:
            print(e)
            return Response(False, e.__str__(), None)
    
    def get_phieunhaps():
        try:
            phieunhaps = Phieunhaps.objects.filter(is_delete=0)
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
                                    ngay_nhap=phieunhap.ngay_nhap, ly_do_nhap=phieunhap.ly_do_nhap, id_user=user,
                                    is_delete=phieunhap.is_delete)
            phieunhap.save()
            # Update book if book exits else add new book
            for bookDto in bookDtos:
                # Check book is exist by name
                book = Books.objects.filter(name=bookDto.name).first()
                if book:
                    # Update book
                    book.quantity += bookDto.quantity
                else:
                    # Get category by id
                    category = Categories.objects.filter(id_category=bookDto.id_category).first()
                    # Add new book
                    book = Books(id_sach=bookDto.id_sach, name=bookDto.name, price=bookDto.price, quantity=bookDto.quantity,
                             image=bookDto.image, author=bookDto.author, id_category=category, is_delete=bookDto.is_delete,
                             ngay_tao=bookDto.ngay_tao)
                book.save()

                # Add ctphieunhap
                ctphieunhap = Ctphieunhaps(id_ctphieunhap=str(uuid.uuid4()), id_phieunhap=phieunhap, id_sach=book,
                                           so_luong=bookDto.quantity, gia_nhap=bookDto.price)
                ctphieunhap.save()
                
            return Response(True, 'Add phieunhap success', phieunhap.id_phieunhap)
        except Exception as e:
            print(e)
            return Response(False, e.__str__(), None)
    
    def update_phieunhap(phieunhap: PhieunhapDto, bookDtos: list[BookDto], book_deletes):
        try:
            # Get user by id
            user = Users.objects.filter(id_user=phieunhap.id_user).first()
            # Update phieunhap
            phieunhap = Phieunhaps.objects.filter(id_phieunhap=phieunhap.id_phieunhap).first()
            phieunhap.donvi_cungcap = phieunhap.donvi_cungcap
            phieunhap.ngay_nhap = phieunhap.ngay_nhap
            phieunhap.ly_do_nhap = phieunhap.ly_do_nhap
            phieunhap.id_user = user
            phieunhap.save()

            # Update book if book exits else add new book
            for bookDto in bookDtos:
                # Check book is exist by name
                book = Books.objects.filter(name=bookDto.name).first()
                if book:
                    # Get ctphieunhap by id_sach and id_phieunhap, xoa so_luong nhap cu
                    ctpn = Ctphieunhaps.objects.filter(id_sach=book, id_phieunhap=phieunhap).first()
                    if ctpn:
                        book.quantity -= ctpn.so_luong

                    # Update book
                    book.quantity += bookDto.quantity
                    book.save()
                else:
                    # Get category by id
                    category = Categories.objects.filter(id_category=bookDto.id_category).first()
                    # Add new book
                    book = Books(id_sach=str(uuid.uuid4()), name=bookDto.name, price=bookDto.price, quantity=bookDto.quantity,
                             image=bookDto.image, author=bookDto.author, id_category=category, is_delete=bookDto.is_delete,
                             ngay_tao=bookDto.ngay_tao)
                book.save()

                # Update ctphieunhap if ctphieunhap exits else add new ctphieunhap
                ctphieunhap = Ctphieunhaps.objects.filter(id_sach=book, id_phieunhap=phieunhap).first()
                if ctphieunhap:
                    ctphieunhap.so_luong = bookDto.quantity
                    ctphieunhap.gia_nhap = bookDto.price
                else:
                    ctphieunhap = Ctphieunhaps(id_ctphieunhap=str(uuid.uuid4()), id_phieunhap=phieunhap, id_sach=book,
                                               so_luong=bookDto.quantity, gia_nhap=bookDto.price)
                ctphieunhap.save()
            
            # Delete ct phieunhap
            for book_delete in book_deletes:
                book = Books.objects.filter(id_sach=book_delete).first()
                ctphieunhap = Ctphieunhaps.objects.filter(id_sach=book, id_phieunhap=phieunhap).first()
                UserDto.delete_ctphieunhap(ctphieunhap.id_ctphieunhap)
            
            return Response(True, 'Update phieunhap success', phieunhap.id_phieunhap)
        except Exception as e:
            print(e)
            return Response(False, e.__str__(), None)

    def delete_phieunhap(id):
        try:
            phieunhap = Phieunhaps.objects.filter(id_phieunhap=id).first()
            if phieunhap is None:
                return Response(False, 'Phieunhap not found', None)
            
            # If phieunhap exist then delete ct phieunhap
            ctpns = Ctphieunhaps.objects.filter(id_phieunhap=phieunhap)
            for ctpn in ctpns:
                print(ctpn.id_ctphieunhap)
                UserDto.delete_ctphieunhap(ctpn.id_ctphieunhap)

            phieunhap.delete()
            return Response(True, 'Delete phieunhap success', phieunhap.id_phieunhap)
        except Exception as e:
            print(e)
            return Response(False, e.__str__(), None)

    def search_phieunhap_by_date(dateFrom, dateTo):
        try:
            phieunhaps = Phieunhaps.objects.filter(ngay_nhap__gte=dateFrom, ngay_nhap__lte=dateTo, is_delete=0)
            return Response(True, 'Search phieunhap by date success', phieunhaps)
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

    def delete_ctphieunhap(id):
        try:
            ctpn = Ctphieunhaps.objects.filter(id_ctphieunhap=id).first()

            if ctpn is None:
                print('Ctphieunhap not found')
                return Response(False, 'Ctphieunhap not found', None)
            
            # Update quantity book
            book = Books.objects.filter(id_sach=ctpn.id_sach.id_sach).first()
            book.quantity -= ctpn.so_luong
            book.save()

            # Delete ct phieunhap
            ctpn.delete()
            print(f'Delete Ctphieunhap success. {book.name}')
            return Response(True, 'Delete Ctphieunhap success', id)
        except Exception as e:
            print(e)
            return Response(False, e.__str__(), None)

    def get_ctphieuhuyBy_PhuyId(id_phieuhuy):
        try:
            ctphs = Ctphieuhuys.objects.filter(id_phieuhuy=id_phieuhuy)
            return Response(True, 'Get ctphieuhuys success', ctphs)
        except Exception as e:
            return Response(False, e.__str__())

    def search_phieuhuy_by_date(dateFrom, dateTo):
        try:
            phieuhuys = Phieuhuys.objects.filter(ngay_huy__gte=dateFrom, ngay_huy__lte=dateTo, is_delete=0)
            return Response(True, 'Search phieuhuy by date success', phieuhuys)
        except Exception as e:
            print(e)
            return Response(False, e.__str__())

    def get_phieuhuys():
        try:
            phieuhuys = Phieuhuys.objects.filter(is_delete=0)
            return Response(True, 'Get phieuhuys success', phieuhuys)
        except Exception as e:
            return Response(False, e.__str__())
        
    def get_books_all():
        try:
            books = Books.objects.all()
            return Response(True, 'Get all books success', books)
        except Exception as e:
            return Response(False, e.__str__())

    def huy_sach(phieuhuyDto: PhieuhuyDto, ctphieuhuys):
        try:
            # Get user by id
            user = Users.objects.filter(id_user=phieuhuyDto.id_user).first()
            if user is None:
                return Response(False, 'User not found')
            
            # Add phieunhap
            phieuhuy = Phieuhuys(
                id_phieuhuy=phieuhuyDto.id_phieuhuy,
                ngay_huy=phieuhuyDto.ngay_huy,
                id_user=user,
                is_delete=phieuhuyDto.is_delete
            )
            phieuhuy.save()
            # Add ctphieuhuy
            for ct in ctphieuhuys:
                # Get book by id
                book = Books.objects.filter(id_sach=ct['id_sach']).first()
                if book is None:
                    return Response(False, 'Book not found')
                # Update quantity book
                book.quantity -= ct['so_luong']
                # Add ctphieuhuy
                ctphieuhuy = Ctphieuhuys(
                    id_ctphieuhuy=ct['id_ctphieuhuy'],
                    id_phieuhuy=phieuhuy,
                    id_sach=book,
                    so_luong=ct['so_luong'],
                    ly_do_huy=ct['ly_do_huy']
                )
                ctphieuhuy.save()
                book.save()
            return Response(True, 'Add phieuhuy success', phieuhuy.id_phieuhuy)
        except Exception as e:
            return Response(False, e.__str__())

    def get_phieuhuyById(id):
        try:
            phieuhuy = Phieuhuys.objects.filter(id_phieuhuy=id).first()
            if phieuhuy is None:
                return Response(False, 'Phieuhuy not found', id)
            return Response(True, 'Get phieuhuy success', phieuhuy)
        except Exception as e:
            return Response(False, e.__str__())

    def update_phieuhuy(phieuhuyDto: PhieuhuyDto, ctphieuhuys, ctph_deletes):
        try:
            # Update phieuhuy
            phieuhuy = Phieuhuys.objects.filter(id_phieuhuy=phieuhuyDto.id_phieuhuy).first()
            if phieuhuy is None:
                return Response(False, 'Phieuhuy not found', phieuhuyDto.id_phieuhuy)
            phieuhuy.ngay_huy = phieuhuyDto.ngay_huy
            phieuhuy.save()
            # Update ctphieuhuy
            for ctph in ctphieuhuys:
                # Get ctph by id_phieuhuy & id_sach
                ctphieuhuy = Ctphieuhuys.objects.filter(id_phieuhuy=phieuhuy.id_phieuhuy,
                                                        id_sach=ctph['id_sach']).first()
                # Get book by id
                book = Books.objects.filter(id_sach=ctph['id_sach']).first()
                if book is None:
                    return Response(False, f'Book not found, id: {ctph['id_sach']}')
                
                if ctphieuhuy is None:
                    # Add new ctphieuhuy
                    ctphieuhuy = Ctphieuhuys(
                        id_ctphieuhuy=ctph['id_ctphieuhuy'],
                        id_sach=book,
                        id_phieuhuy=phieuhuy,
                        so_luong=ctph['so_luong'],
                        ly_do_huy=ctph['ly_do_huy']
                    )
                    # Update quantity
                    book.quantity -= ctphieuhuy.so_luong
                else:
                    # Update quantity book
                    book.quantity += ctphieuhuy.so_luong - ctph['so_luong']
                    ctphieuhuy.so_luong = ctph['so_luong']
                    ctphieuhuy.ly_do_huy = ctph['ly_do_huy']
                # Update ctphieuhuy & book
                ctphieuhuy.save()
                book.save()

            # Delete ctphieuhuys
            for id_ctph in ctph_deletes:
                # Get ctph
                ctphieuhuy = Ctphieuhuys.objects.filter(id_ctphieuhuy=id_ctph).first()
                if ctphieuhuy is None:
                    return Response(False, f'Ctphieuhuy not found, id: {id_ctph}')
                else:
                    # Update quantity book
                    ctphieuhuy.id_sach.quantity += ctphieuhuy.so_luong
                    ctphieuhuy.id_sach.save()
                    ctphieuhuy.delete()
                    
            return Response(True, 'Update phieuhuy success', phieuhuy.id_phieuhuy)
        except Exception as e:
            return Response(False, e.__str__())

    def delete_phieuhuy(id):
        try:
            # Get phieuhuy by id
            phieuhuy = Phieuhuys.objects.filter(id_phieuhuy=id).first()
            if phieuhuy is None:
                return Response(False, 'Phieuhuy not found')
            # Delete ctphieuhuy
            ctphieuhuys = Ctphieuhuys.objects.filter(id_phieuhuy=phieuhuy)
            for ct in ctphieuhuys:
                # Update quantity book
                book = Books.objects.filter(id_sach=ct.id_sach.id_sach).first()
                book.quantity += ct.so_luong
                book.save()
                ct.delete()

            phieuhuy.delete()
            return Response(True, 'Delete phieuhuy success', id)

        except Exception as e:
            return Response(False, e.__str__())

    def thongkesach():
        try:
            tksach = Books.objects.filter(quantity__gt=0)
            return Response(True, 'Get books success', tksach)
        except Exception as e:
            print(e)
            return Response(False, e.__str__(), None)
        
    def searchSachTK(inputSearch:str):
        try:
            tksach = Books.objects.filter(name__icontains = inputSearch, quantity__gt=0)
            return Response(True, 'Search books success', tksach)
        except Exception as e:
            print(e)
            return Response(False, e.__str__(), None)
        
    def kiemke():
        ...

    #thong ke
    def ThongKePhieuNhap():
        try:
            current_year = datetime.now().year
            # Lấy tất cả các phiếu nhập
            phieunhaps = Phieunhaps.objects.filter(is_delete=0, ngay_nhap__startswith=f'{current_year}-')

            # Khởi tạo từ điển để lưu trữ tổng số lượng
            monthly_stats = defaultdict(lambda: {'total_quantity': 0})

            for phieunhap in phieunhaps:
                # Chuyển đổi chuỗi ngày tháng sang đối tượng datetime
                ngay_nhap = datetime.strptime(phieunhap.ngay_nhap, "%Y-%m-%d")
                month = ngay_nhap.month

                # Lấy các chi tiết phiếu nhập tương ứng
                ctphieunhaps = Ctphieunhaps.objects.filter(id_phieunhap=phieunhap)

                for ctphieunhap in ctphieunhaps:
                    monthly_stats[month]['total_quantity'] += ctphieunhap.so_luong

            # Chuyển đổi dữ liệu từ từ điển sang danh sách để dễ sử dụng trong JavaScript
            quantity_data = [monthly_stats[month]['total_quantity'] for month in range(1, 13)]

            return Response(True, "Thong ke thanh cong", quantity_data)
        except Exception as e:
            print(e)
            return Response(False, e.__str__(), None)

    def ThongKePhieuHuy():
        try:
            current_year = datetime.now().year
            # Lấy tất cả các phiếu hủy
            phieuhuys = Phieuhuys.objects.filter(ngay_huy__startswith=f"{current_year}-",is_delete=0)

            # Khởi tạo từ điển để lưu trữ tổng số lượng
            monthly_stats = defaultdict(lambda: {'total_quantity': 0})

            for phieuhuy in phieuhuys:
                # Chuyển đổi chuỗi ngày tháng sang đối tượng datetime
                ngay_huy = datetime.strptime(phieuhuy.ngay_huy, "%Y-%m-%d")
                month = ngay_huy.month

                # Lấy các chi tiết phiếu nhập tương ứng
                ctphieuhuys = Ctphieuhuys.objects.filter(id_phieuhuy=phieuhuy)

                for ctphieuhuy in ctphieuhuys:
                    monthly_stats[month]['total_quantity'] += ctphieuhuy.so_luong

            # Chuyển đổi dữ liệu từ từ điển sang danh sách để dễ sử dụng trong JavaScript
            quantity_data = [monthly_stats[month]['total_quantity'] for month in range(1, 13)]

            return Response(True, "Thong ke thanh cong", quantity_data)
        except Exception as e:
            print(e)
            return Response(False, e.__str__(), None)