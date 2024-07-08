from library_manager.dtos.UserDto import UserDto
from library_manager.dtos.DocgiaDto import DocgiaDto
from library_manager.dtos.ThethuvienDto import ThethuvienDto
from library_manager.dtos.ResponseDto import ResponseDto as Response
from library_manager.models import Users, Categories, Docgias, Thethuviens, Phieumuons, Phieuhuys, Phieunhaps, Books
from library_manager.dtos.CategoryDto import CategoryDto


class AdminDto(UserDto):
    def __init__(self):
        super().__init__()

    def check_nameCategory(name):
        category = Categories.objects.filter(name=name).first()
        return True if category else False

    def add_category(CategoryDto: CategoryDto):
        try:
            is_category = AdminDto.check_nameCategory(CategoryDto.name)

            if is_category is True:
                return Response(False, 'Category name already exists', None)
            else:
                # Add category to database
                category = Categories(id_category=CategoryDto.id_category, name=CategoryDto.name,
                                      description=CategoryDto.description, is_delete=CategoryDto.is_delete)
                category.save()
                return Response(True, 'Add category success', category.id_category)
        except Exception as e:
            print(e)
            return Response(False, e.__str__(), None)

    def update_category(categoryDto: CategoryDto):
        try:
            category = Categories.objects.filter(id_category=categoryDto.id_category).first()

            if category.name == categoryDto.name:
                category.name = categoryDto.name
                category.description = categoryDto.description
                category.is_delete = categoryDto.is_delete
                category.save()
                return Response(True, 'Update category success', category.id_category)
            else:
                is_category = AdminDto.check_nameCategory(categoryDto.name)
                if is_category is True:
                    return Response(False, 'Category name already exists', None)
                else:
                    category.name = categoryDto.name
                    category.description = categoryDto.description
                    category.is_delete = categoryDto.is_delete
                    category.save()
                    return Response(True, 'Update category success', category.id_category)
        except Exception as e:
            print(e)
            return Response(False, e.__str__(), None)

    def delete_category(id):
        try:
            category = Categories.objects.filter(id_category=id).first()
            book = Books.objects.filter(id_category=id).first()
            if book:
                category.is_delete = 1;
                category.save()
                return Response(True, 'Delete category success', None)
            else:
                category.delete()
                return Response(True, 'Delete category success', None)
        except Exception as e:
            print(e)
            return Response(False, e.__str__(), None)
        
    def search_category(searchCategory:str):
        try:
            # Search user by name or email or phone or address
            categories = (Categories.objects.filter(name__icontains=searchCategory) |
                          Categories.objects.filter(description__icontains=searchCategory))
            return Response(True, f'Tìm thấy {len(categories)} kết quả', categories)
        except Exception as e:
            print(e)
            return Response(False, e.__str__(), None)

    def get_category_by_id(id):
        try:
            category = Categories.objects.filter(id_category=id).first()
            return Response(True, 'Get user success', category)
        except Exception as e:
            print(e)
            return Response(False, e.__str__(), None)
        
    def get_categories():
        try:
            categories = Categories.objects.filter(is_delete=0)
            return Response(True, 'Get categories success', categories)
        except Exception as e:
            print(e)
            return Response(False, e.__str__(), None)
        
    def add_user(userDto: UserDto):
        try:
            # Check if user exists in database by email
            is_user = UserDto.check_email(userDto.email)

            if is_user is True:
                return Response(False, 'This email already exists', None)
            else:
                # Add user to database
                user = Users(id_user=userDto.id_user, name=userDto.name, email=userDto.email,
                        password=userDto.password, role=userDto.role, gender=userDto.gender,
                        birthday=userDto.birthday, phone_number=userDto.phone_number,
                        address=userDto.address, is_delete=userDto.is_delete)
                user.save()
                return Response(True, 'Add user success', user.id_user)
        except Exception as e:
            print(e)
            return Response(False, e.__str__(), None)
    
    def update_user(userDto: UserDto):
        try:
            # Check if user exists in database by id
            user = Users.objects.filter(id_user=userDto.id_user).first()
            if user:
                # Check if email exists in database
                if user.email != userDto.email:
                    is_user = UserDto.check_email(userDto.email)
                    if is_user is True:
                        return Response(False, 'This email already exists', None)
                    user.email = userDto.email

                # Update user
                user.name = userDto.name
                user.role = userDto.role
                user.gender = userDto.gender
                user.birthday = userDto.birthday
                user.phone_number = userDto.phone_number
                user.address = userDto.address
                user.save()
                return Response(True, 'Update user success', user.id_user)
            else:
                return Response(False, 'User not found', None)
        except Exception as e:
            print(e)
            return Response(False, e.__str__(), None)
    
    def delete_user(id):
        try:
            user = Users.objects.filter(id_user=id).first()
            if user is not None:
                # Get data phieumuon, phieuhuy, phieunhap, if data empty then delete
                phieumuons = Phieumuons.objects.filter(id_user=user)
                phieuhuys = Phieuhuys.objects.filter(id_user=user)
                phieunhaps = Phieunhaps.objects.filter(id_user=user)
                # Change is_delete to 1
                if len(phieumuons) > 0 or len(phieuhuys) > 0 or len(phieunhaps) > 0:
                    user.is_delete = 1
                    user.save()
                    return Response(True, 'Change status is_delete = 1', user.id_user)
                else:
                    # Delete user
                    user.delete()
                    return Response(True, 'Delete user success', user.id_user)
            else:
                return Response(False, 'User not found', None)
        except Exception as e:
            print(e)
            return Response(False, e.__str__(), None)
    
    def search_user(searchInput: str):
        try:
            # Search user by name or email or phone or address
            users = (Users.objects.filter(name__icontains=searchInput) | Users.objects.filter(email__icontains=searchInput) |
                    Users.objects.filter(phone_number__icontains=searchInput) |
                    Users.objects.filter(address__icontains=searchInput)) & (Users.objects.filter(is_delete=0))
            return Response(True, f"Tìm thấy {len(users)} kết quả", users)
        except Exception as e:
            print(e)
            return Response(False, e.__str__(), None)
    
    def get_users():
        try:
            users = Users.objects.filter(is_delete=0)
            return Response(True, 'Get users success', users)
        except Exception as e:
            print(e)
            return Response(False, e.__str__(), None)

    def get_user_by_id(id):
        try:
            user = Users.objects.filter(id_user=id).first()
            if user is None:
                return Response(False, 'User not found', user)
            
            return Response(True, 'Get user success', user)
        except Exception as e:
            print(e)
            return Response(False, e.__str__(), None)
    
    def add_thethuvien(ttv: ThethuvienDto):
        try:
            # Add the thu vien
            thethuvien = Thethuviens(id_the=ttv.id_the, type=ttv.type, ngay_tao=ttv.ngay_tao, ngay_het_han=ttv.ngay_het_han,
                                     ghi_chu=ttv.ghi_chu, id_docgia=ttv.id_docgia, is_delete=ttv.is_delete)
            thethuvien.save()
            return Response(True, "Tạo thẻ thư viện thành công", thethuvien.id_the)
        except Exception as e:
            print(e)
            return Response(False, e.__str__(), None)

    def get_thethuviens():
        try:
            thethuviens = Thethuviens.objects.filter(is_delete=0)
            return Response(True, 'Get thethuviens success', thethuviens)
        except Exception as e:
            print(e)
            return Response(False, e.__str__(), None)
    
    def get_thethuvien_by_id(id):
        try:
            ttv = Thethuviens.objects.filter(id_the=id).first()
            if ttv is None:
                return Response(False, 'Thethuvien not found', None)

            return Response(True, f'Get thethuvien success. {ttv.id_the}', ttv)
        except Exception as e:
            print(e)
            return Response(False, e.__str__(), None)

    def get_info_docgiaById_the(id):
        try:
            ttv = Thethuviens.objects.filter(id_the=id).first()
            if ttv is None:
                return Response(False, "Thethuvien not found", None)
            else:
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
                    'hoten': ttv.id_docgia.name,
                    'type': ttv.type,
                    'ngay_het_han': ttv.ngay_het_han,
                    'books': books
                }
                return Response(True, 'Get info success', data)
        except Exception as e:
            return Response(False, e.__str__(), None)

    def check_email_docgia(email):
        try:
            docgia = Docgias.objects.filter(email=email).first()
            return True if docgia else False
        except Exception as e:
            print(e)
            return False

    def add_docgia(docgiaDto: DocgiaDto, ttv: ThethuvienDto):
        try:
            # Check email exits
            is_email = AdminDto.check_email_docgia(docgiaDto.email)
            if is_email is True:
                return Response(False, "Email is already exist", None)
            
            # Add docgia
            docgia = Docgias(id_docgia=docgiaDto.id_docgia, name=docgiaDto.name, email=docgiaDto.email,
                             gender=docgiaDto.gender, birthday=docgiaDto.birthday, phone_number=docgiaDto.phone_number,
                             address=docgiaDto.address, ngay_tao=docgiaDto.ngay_tao, is_delete=docgiaDto.is_delete)
            docgia.save()

            # Add the thu vien
            ttv.id_docgia = docgia
            AdminDto.add_thethuvien(ttv)
            return Response(True, "Tạo mới độc giả thành công", None)
        except Exception as e:
            print(e)
            return Response(False, e.__str__(), None)
        
    def update_docgia(docgiaDto: DocgiaDto, ttv: ThethuvienDto):
        try:
            # Find thethuvien by id_the
            thethuvien = Thethuviens.objects.filter(id_the=ttv.id_the).first()
            if thethuvien is None:
                return Response(False, "Thethuvien not found", None)
            # Find docgia by id
            docgia = Docgias.objects.filter(id_docgia=thethuvien.id_docgia.id_docgia).first()
            if docgia is None:
                return Response(False, "Docgia not found", None)
            
            # Check email new
            if docgia.email != docgiaDto.email:
                is_email = AdminDto.check_email_docgia(docgiaDto.email)
                if is_email is True:
                    return Response(False, "Email is already exist", None)
                docgia.email = docgiaDto.email

            # Update thethuvien
            thethuvien.type = ttv.type
            thethuvien.ngay_tao = ttv.ngay_tao
            thethuvien.ngay_het_han = ttv.ngay_het_han
            thethuvien.ghi_chu = ttv.ghi_chu
            thethuvien.save()

            # Update docgia
            docgia.name = docgiaDto.name
            docgia.gender = docgiaDto.gender
            docgia.birthday = docgiaDto.birthday
            docgia.phone_number = docgiaDto.phone_number
            docgia.address = docgiaDto.address
            docgia.save()

            return Response(True, "Update docgia success", docgia.id_docgia)
        except Exception as e:
            print(e)
            return Response(False, e.__str__(), None)

    def delete_docgia(id_the):
        try:
            # Find thethuvien by id_the
            ttv = Thethuviens.objects.filter(id_the=id_the).first()
            if ttv is None:
                return Response(False, "Thethuvien not found", None)
            # Find docgia by id
            docgia = Docgias.objects.filter(id_docgia=ttv.id_docgia.id_docgia).first()
            if docgia is None:
                return Response(False, "Docgia not found", None)
            
            # Get data phieumuon, if data empty then delete
            phieumuons = Phieumuons.objects.filter(id_the=ttv)
            if len(phieumuons) == 0:
                # Delete docgia, thethuvien
                ttv.delete()
                docgia.delete()
                return Response(True, "Delete docgia success", docgia.id_docgia)
            
            # Update thethuvien is_delete = 1
            ttv.is_delete = 1
            ttv.save()
            # Update docgia is_delete = 1
            docgia.is_delete = 1
            docgia.save()
            return Response(True, "Change status is_delete = 1", docgia.id_docgia)
        except Exception as e:
            print(e)
            return Response(False, e.__str__(), None)
            
    def search_docgia(searchInput):
        try:
            # Search user by name or email or phone or address
            docgias = (Docgias.objects.filter(name__icontains=searchInput) |
                        Docgias.objects.filter(email__icontains=searchInput) |
                        Docgias.objects.filter(phone_number__icontains=searchInput) |
                        Docgias.objects.filter(address__icontains=searchInput)) & (Docgias.objects.filter(is_delete=0))
            # Get thethuvien from docgias search
            thethuviens = []
            for docgia in docgias:
                ttv = Thethuviens.objects.filter(id_docgia=docgia).first()
                thethuviens.append(ttv)

            return Response(True, f"Tìm thấy {len(docgias)} kết quả", thethuviens)
        except Exception as e:
            print(e)
            return Response(False, e.__str__(), None)
