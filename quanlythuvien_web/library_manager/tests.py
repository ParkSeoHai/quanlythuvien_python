from django.test import TestCase

from library_manager.dtos.UserDto import UserDto
from library_manager.dtos.AdminDto import AdminDto
from library_manager.dtos.DocgiaDto import DocgiaDto
from library_manager.dtos.ThethuvienDto import ThethuvienDto
from library_manager.dtos.PhieumuonDto import PhieumuonDto
from library_manager.dtos.PhieunhapDto import PhieunhapDto
from library_manager.dtos.BookDto import BookDto
from library_manager.dtos.CategoryDto import CategoryDto
from library_manager.dtos.PhieuhuyDto import PhieuhuyDto
from library_manager.dtos.KiemkeDto import KiemkeDto
from library_manager.dtos.CTKiemkeDto import CTKiemkeDto
from datetime import datetime

# Command test: python manage.py test -v 2 --k library_manager.tests.{className}

class LoginTest(TestCase):
    def test_case_1(self):
        user = UserDto(email='admin@gmail.com', password='123456')
        response = user.login()
        
        self.assertEqual({
            'status': response.status,
            'message': response.message
        }, {
            'status': True,
            'message': 'Đăng nhập thành công'
        })
                
    def test_case_2(self):
        user = UserDto(email='admin123@gmail.com', password='111111')
        response = user.login()
        
        self.assertEqual({
            'status': response.status,
            'message': response.message
        }, {
            'status': True,
            'message': 'Đăng nhập thành công'
        })

class Get_UsersTest(TestCase):
    def test_case_1(self):
        response = AdminDto.get_users()
        
        self.assertEqual({
            'status': response.status,
            'message': response.message
        }, {
            'status': True,
            'message': 'Get users success'
        })

class Add_UserTest(TestCase):
    def test_case_1(self):
        user = UserDto(
            id_user='1b117244-72fb-4512-966f-f03411357593',
            name='Nguyễn Văn Hải',
            email='nvhai28@gmail.com',
            password='123456',
            phone_number='0333301536',
            address='Hải Dương',
            role=0,
            gender=0,
            birthday='2003-08-02'
        )

        response = AdminDto.add_user(user)
        
        self.assertEqual({
            'status': response.status,
            'message': response.message
        }, {
            'status': True,
            'message': 'Add user success'
        })

    def test_case_2(self):
        user = UserDto(
            id_user='101c7492-fc7f-4350-913b-1bc28a8eb03f',
            name='Đỗ Minh Hiếu',
            email='admin@gmail.com',
            password='123456',
            phone_number='098277361',
            address='Hà Nội',
            role=1,
            gender=0,
            birthday='2003-10-01'
        )

        response = AdminDto.add_user(user)
        
        self.assertEqual({
            'status': response.status,
            'message': response.message
        }, {
            'status': True,
            'message': 'Add user success'
        })

class Update_UserTest(TestCase):
    def test_case_1(self):
        user = UserDto(
            id_user='237f5aac-6453-4fb4-a866-130fb399f1e9',
            name='Phan Đức Huy',
            email='huypd2@gmail.com',
            password='123456',
            phone_number='031221233',
            address='Hà Nội',
            role=0,
            gender=0,
            birthday='2003-08-02'
        )
        
        response = AdminDto.update_user(user)
        
        self.assertEqual({
            'status': response.status,
            'message': response.message
        }, {
            'status': True,
            'message': 'Update user success'
        })

    def test_case_2(self):
        user = UserDto(
            id_user='10ca6316-6151-4cd2-8afb-bea9579731bc',
            name='Nguyễn Văn Hải',
            email='hai2823@gmail.com',
            password='654321',
            phone_number='0984640915',
            address='Hải Dương',
            role=0,
            gender=0,
            birthday='2003-08-02'
        )
        
        response = AdminDto.update_user(user)
        
        self.assertEqual({
            'status': response.status,
            'message': response.message
        }, {
            'status': True,
            'message': 'Update user success'
        })

class Delete_UserTest(TestCase):
    def test_case_1(self):
        id_user = '09006e91-b68b-44f7-b6d4-f7bad61c91f1'
        response = AdminDto.delete_user(id_user)

        self.assertEqual({
            'status': response.status,
            'message': response.message
        }, {
            'status': True,
            'message': 'Delete user success'
        })

    def test_case_2(self):
        id_user = 'bbb5f608-397a-48ff-8873-e4b15f84bd29'
        response = AdminDto.delete_user(id_user)

        self.assertEqual({
            'status': response.status,
            'message': response.message
        }, {
            'status': True,
            'message': 'Delete user success'
        })

class Search_UserTest(TestCase):
    def test_case_1(self):
        search_input = 'Nguyen Hai'
        response = AdminDto.search_user(search_input)

        self.assertEqual({
            'status': response.status,
            'message': response.message
        }, {
            'status': True,
            'message': 'Tìm thấy 10 kết quả'
        })

class Get_DocgiasTest(TestCase):
    def test_case_1(self):
        response = AdminDto.get_thethuviens()
        
        self.assertEqual({
            'status': response.status,
            'message': response.message
        }, {
            'status': True,
            'message': 'Get thethuviens success'
        })

class Get_Info_DocgiaTest(TestCase):
    def test_case_1(self):
        id_the = '20240204'
        response = AdminDto.get_thethuvien_by_id(id_the)
        
        self.assertEqual({
            'status': response.status,
            'message': response.message
        }, {
            'status': True,
            'message': 'Get thethuvien by id success'
        })

    def test_case_2(self):
        id_the = '20240427'
        response = AdminDto.get_thethuvien_by_id(id_the)
        
        self.assertEqual({
            'status': response.status,
            'message': response.message
        }, {
            'status': True,
            'message': 'Get thethuvien by id success'
        })

class Add_DocgiaTest(TestCase):
    def test_case_1(self):
        docgia = DocgiaDto(
            id_docgia='237f5aac-6453-4fb4-a866-130fb399f1e9',
            name='Nguyễn Văn A',
            email='nva2321@gmail.com',
            address='Hà Nội',
            gender=0,
            phone_number='031221233',
            birthday='2003-08-02',
            ngay_tao='2024-07-08'
        )

        ttv = ThethuvienDto(
            id_the='20248912', type=0, ngay_tao='2024-07-08', ngay_het_han='2028-07-08'
        )

        response = AdminDto.add_docgia(docgia, ttv)
        
        self.assertEqual({
            'status': response.status,
            'message': response.message
        }, {
            'status': True,
            'message': 'Tạo mới độc giả thành công'
        })

    def test_case_2(self):
        docgia = DocgiaDto(
            id_docgia='05a5f636-8110-4084-b2b4-e9ddcd437f90',
            name='Nguyen Van C',
            email='nvc2024@gmail.com',
            address='Hà Nội',
            gender=1,
            phone_number='031221233',
            birthday='2003-08-02',
            ngay_tao='2024-06-08'
        )

        ttv = ThethuvienDto(
            id_the='20249921', type=1, ngay_tao='2024-06-08', ngay_het_han='2028-06-08'
        )

        response = AdminDto.add_docgia(docgia, ttv)
        
        self.assertEqual({
            'status': response.status,
            'message': response.message
        }, {
            'status': True,
            'message': 'Tạo mới độc giả thành công'
        })

class Update_DocgiaTest(TestCase):
    def test_case_1(self):
        docgia = DocgiaDto(
            id_docgia='237f5aac-6453-4fb4-a866-130fb399f1e9',
            name='Nguyễn Thị H',
            email='nvh2321@gmail.com',
            address='Hà Nội',
            gender=1,
            phone_number='031221233',
            birthday='2003-08-02',
            ngay_tao='2024-07-08'
        )

        ttv = ThethuvienDto(
            id_the='20248212', type=0, ngay_tao='2024-07-08', ngay_het_han='2028-07-08'
        )

        response = AdminDto.update_docgia(docgia, ttv)
        
        self.assertEqual({
            'status': response.status,
            'message': response.message
        }, {
            'status': True,
            'message': 'Update docgia success'
        })

    def test_case_2(self):
        docgia = DocgiaDto(
            id_docgia='b518c625-49f3-4b90-b865-50cdd1edc4c2',
            name='Nguyễn Văn C',
            email='nvc@gmail.com',
            address='Hà Nội',
            gender=1,
            phone_number='031227827',
            birthday='2003-08-02',
            ngay_tao='2024-07-08'
        )

        ttv = ThethuvienDto(
            id_the='20241947', type=1, ngay_tao='2024-07-08', ngay_het_han='2028-07-08'
        )

        response = AdminDto.update_docgia(docgia, ttv)
        
        self.assertEqual({
            'status': response.status,
            'message': response.message
        }, {
            'status': True,
            'message': 'Update docgia success'
        })

class Delete_DocgiaTest(TestCase):
    def test_case_1(self):
        id_the = '20242011'
        response = AdminDto.delete_docgia(id_the)

        self.assertEqual({
            'status': response.status,
            'message': response.message
        }, {
            'status': True,
            'message': 'Delete docgia success'
        })

    def test_case_2(self):
        id_the = '20240423'
        response = AdminDto.delete_docgia(id_the)

        self.assertEqual({
            'status': response.status,
            'message': response.message
        }, {
            'status': True,
            'message': 'Delete docgia success'
        })

class Search_DocgiaTest(TestCase):
    def test_case_1(self):
        search_input = 'nguyen hai'
        response = AdminDto.search_docgia(search_input)

        self.assertEqual({
            'status': response.status,
            'message': response.message
        }, {
            'status': True,
            'message': 'Tìm thấy 2 kết quả'
        })

class Get_PhieuDangMuonsTest(TestCase):
    def test_case_1(self):
        response = UserDto.get_phieumuons()

        self.assertEqual({
            'status': response.status,
            'message': response.message
        }, {
            'status': True,
            'message': 'Get phieumuon success'
        })

class Add_PhieumuonTest(TestCase):
    def test_case_1(self):
        phieumuon = PhieumuonDto(
            id_phieumuon='9a66ab24-34e1-488f-91d7-3565e3cec19f',
            ngay_tao='2024-07-05',
            ngay_hen_tra='2024-07-12',
            ghi_chu='mượn sách',
            so_luong=1,
            id_user='142dd5a8-23e1-4cef-89eb-93052f36776b',
            id_the='20240427'
        )
        ten_sach = 'Lập trình Python'

        response = UserDto.add_phieumuon(phieumuon, ten_sach)

        self.assertEqual({
            'status': response.status,
            'message': response.message
        }, {
            'status': True,
            'message': 'Add phieumuon success'
        })

    def test_case_2(self):
        phieumuon = PhieumuonDto(
            id_phieumuon='4f9bf5d6-765f-4bdb-9c33-82e5589c8b45',
            ngay_tao='2024-07-01',
            ngay_hen_tra='2024-07-08',
            ghi_chu='mượn sách',
            so_luong=1,
            id_user='142dd5a8-23e1-4cef-89eb-93052f36776b',
            id_the='20242812'
        )
        ten_sach = 'Thiết kế mạng Intranet'

        response = UserDto.add_phieumuon(phieumuon, ten_sach)

        self.assertEqual({
            'status': response.status,
            'message': response.message
        }, {
            'status': True,
            'message': 'Add phieumuon success'
        })

class Update_PhieumuonTest(TestCase):
    def test_case_1(self):
        phieumuon = PhieumuonDto(
            id_phieumuon='3f59fc7e-0437-478e-8f4a-1173ed281362',
            ngay_tao='2024-07-10',
            ngay_hen_tra='2024-07-17',
            ghi_chu='cập nhật',
            so_luong=1,
        )
        ten_sach = 'Thiết kế mạng Intranet'

        response = UserDto.update_phieumuon(phieumuon, ten_sach)

        self.assertEqual({
            'status': response.status,
            'message': response.message
        }, {
            'status': True,
            'message': 'Update phieumuon success'
        })

    def test_case_2(self):
        phieumuon = PhieumuonDto(
            id_phieumuon='262ec694-f882-434b-a9f7-6435bbf3aeb3',
            ngay_tao='2024-07-10',
            ngay_hen_tra='2024-07-17',
            ghi_chu='cập nhật 2',
            so_luong=1,
        )
        ten_sach = 'Lập trình Python'

        response = UserDto.update_phieumuon(phieumuon, ten_sach)

        self.assertEqual({
            'status': response.status,
            'message': response.message
        }, {
            'status': True,
            'message': 'Update phieumuon success'
        })

class Delete_PhieumuonTest(TestCase):
    def test_case_1(self):
        id_phieumuon = '9a66ab24-34e1-488f-91d7-3565e3cec19f'
        response = UserDto.delete_phieumuon(id_phieumuon)

        self.assertEqual({
            'status': response.status,
            'message': response.message
        }, {
            'status': True,
            'message': 'Delete phieumuon success'
        })

    def test_case_2(self):
        id_phieumuon = '3f59fc7e-0437-478e-8f4a-1173ed281362'
        response = UserDto.delete_phieumuon(id_phieumuon)

        self.assertEqual({
            'status': response.status,
            'message': response.message
        }, {
            'status': True,
            'message': 'Delete phieumuon success'
        })

class Search_PhieumuonTest(TestCase):
    def test_case_1(self):
        id_the = '2024'
        response = UserDto.search_phieumuonById_the(id_the)

        self.assertEqual({
            'status': response.status,
            'message': response.message
        }, {
            'status': True,
            'message': 'Get phieumuons success. (1 result)'
        })

class Thuhoi_PhieumuonTest(TestCase):
    def test_case_1(self):
        id_phieumuon = '61885b1f-e7ee-489f-ae91-6822300844f8'
        ngay_tra = '2024-07-09'
        ghi_chu = 'Trả đúng hạn'

        response = UserDto.thuhoi_phieumuon(id_phieumuon, ngay_tra, ghi_chu)

        self.assertEqual({
            'status': response.status,
            'message': response.message
        }, {
            'status': True,
            'message': 'Thu hồi phiếu mượn thành công'
        })
    
    def test_case_2(self):
        id_phieumuon = '7c55b32c-0500-4526-b9d0-22dd5a3c4882'
        ngay_tra = '2024-07-06'
        ghi_chu = 'Trả trễ hạn'

        response = UserDto.thuhoi_phieumuon(id_phieumuon, ngay_tra, ghi_chu)

        self.assertEqual({
            'status': response.status,
            'message': response.message
        }, {
            'status': True,
            'message': 'Thu hồi phiếu mượn thành công'
        })

class Get_phieunhapsTest(TestCase):
    def test_case_1(self):
        response = UserDto.get_phieunhaps()

        self.assertEqual({
            'status': response.status,
            'message': response.message
        }, {
            'status': True,
            'message': 'Get phieunhaps success'
        })

class Add_phieunhapTest(TestCase):
    def test_case_1(self):
        phieunhap = PhieunhapDto(
            id_phieunhap='6eba9ce9-103d-4100-bc26-a68337b6ed41',
            donvi_cungcap='Bộ giáo dục',
            ngay_nhap='2024-07-09',
            ly_do_nhap='Nhập sách 07/2024',
            id_user='142dd5a8-23e1-4cef-89eb-93052f36776b'
        )

        books = [
            BookDto(
                id_sach='df5848fb-dff4-458e-959c-2860a0c79211', name='Lập trình Python', price=250000,
                quantity=12, author='Nguyen A', id_category='fca7336d-1d2c-4dd5-9e1d-fb104fc53191',
                ngay_tao='2024-07-08'
            ),
            BookDto(
                id_sach='544e2e17-e88f-4578-b42b-7c11e88d9999', name='Quản trị mạng', price=420000,
                quantity=8, author='Nguyen B', id_category='fca7336d-1d2c-4dd5-9e1d-fb104fc53191',
                ngay_tao='2024-07-08'
            )
        ]

        response = UserDto.nhap_sach(phieunhap, books)

        self.assertEqual({
            'status': response.status,
            'message': response.message
        }, {
            'status': True,
            'message': 'Add phieunhap success'
        })
class register(TestCase):
    def test_case1(self):
        user = UserDto(email='admin@gmail.com', password='123456')
        if UserDto.check_email(user.email):
            self.assertEqual(False, True)
        else:
            response = UserDto.register(user)
            self.assertEqual({
                'status': response.status,
                'message': response.message,
            },{
                'status': True,
                'message': 'Register success',
            })
    def test_case2(self):
        user = UserDto(email='admin123@gmail.com', password='111111')
        response = UserDto.register(user)
        self.assertEqual({
            'status': response.status,
            'message': response.message,
        }, {
            'status': True,
            'message': 'Register success',
        })
class addCategory(TestCase):
    def test_case1(self):
        category = CategoryDto(name='Sách Python', description='Sách về python')
        response = AdminDto.add_category(category)
        self.assertEqual({
            'status': response.status,
            'message': response.message
        }, {
            'status': True,
            'message': 'Add category success'
        })
    def test_case2(self):
        category = CategoryDto(name='Công nghệ thông tin', description='none')
        response = AdminDto.add_category(category)
        self.assertEqual({
            'status': response.status,
            'message': response.message
        }, {
            'status': True,
            'message': 'Add category success'
        })
class updateCategory(TestCase):
    def test_case1(self):
        category = CategoryDto(id_category='fca7336d-1d2c-4dd5-9e1d-fb104fc53191', name='Sách python', description='Sách về python')
        response = AdminDto.update_category(category)
        self.assertEqual({
            'status': response.status,
            'message': response.message
        },{
            'status': True,
            'message': 'Update category success'
        })

    def test_case2(self):
        category = CategoryDto(id_category='fca7336d-1d2c-4dd5-9e1d-fb104fc53191', name='Công nghệ thực phẩm', description='none')
        response = AdminDto.update_category(category)
        self.assertEqual({
            'status': response.status,
            'message': response.message
        },{
            'status': True,
            'message': 'Update category success'
        })
class deleteCategory(TestCase):
    def test_case1(self):
        id_category='fca7336d-1d2c-4dd5-9e1d-fb104fc53191'
        response = AdminDto.delete_category(id_category)
        self.assertEqual({
            'status': response.status,
        },{
            'status': True,
        })
    def test_case2(self):
        id_category='daa032-23'
        response = AdminDto.delete_category(id_category)
        self.assertEqual({
            'status': response.status,
        }, {
            'status': True,
        })
class getCategory(TestCase):
    def test_case1(self):
        categories = AdminDto.get_categories()
        self.assertEqual({
            'status': categories.status,
            'message': categories.message
        },{
            'status': True,
            'message': 'Get categories success'
        })
class getQLTHMT(TestCase):
    def test_case1(self):
        response = UserDto.check_phieumuon()
        self.assertEqual({
            'status': response.status,
            'message': response.message
        },{
            'status': True,
            'message': 'Get phieumuon success'
        })
class getThongKeNhapHuy(TestCase):
    def test_case1(self):
        response = UserDto.ThongKePhieuNhap()
        response2 = UserDto.ThongKePhieuHuy()
        self.assertEqual({
            'status': response.status,
            'message': response.message
        },{
            'status': True,
            'message': 'Thong ke thanh cong'
        })
        self.assertEqual({
            'status': response2.status,
            'message': response2.message
        }, {
            'status': True,
            'message': 'Thong ke thanh cong'
        })
class getThongKeTonKho(TestCase):
    def test_case1(self):
        response = UserDto.thongkesach()
        self.assertEqual({
            'status': response.status,
            'message': response.message
        },{
            'status': True,
            'message': 'Get books success'
        })
class searchCategory(TestCase):
    def test_case1(self):
        a = 'Công nghệ thông tin'
        response = AdminDto.search_category(a)
        self.assertEqual({
            'status': response.status,
        },{
            'status': True,
        })
    def test_case2(self):
        a = 'something'
        response = AdminDto.search_category(a)
        self.assertEqual({
            'status': response.status,
        }, {
            'status': True,
        })
class getinfoPhieuKiemKe(TestCase):
    def test_case1(self):
        id = '3679e5d4-6b48-44f9-8e81-b76a2352b944'
        response = UserDto.get_phieuKiemkeById(id)
        self.assertEqual({
            'status': response.status,
            'message': response.message
        }, {
            'status': True,
            'message': 'Get phieu kiemke by id success'
        })
    def test_case2(self):
        id = '6f73d063-8a9f-436a-8fef-72603c5d0857'
        response = UserDto.get_phieuKiemkeById(id)
        self.assertEqual({
            'status': response.status,
            'message': response.message
        }, {
            'status': True,
            'message': 'Get phieu kiemke by id success'
        })
class addPhieuKiemke(TestCase):
    def test_case1(self):
        kiemke = KiemkeDto(id_kiemke='6f73d063-8a9f-436a-8fef-72603c5d0857', ngay_tao='2024-07-10’', ly_do='Kiểm kê tháng 7', file_kiemke='url', id_user='142dd5a8-23e1-4cef-89eb-93052f36776b')
        ctkiemke = [CTKiemkeDto(id_ctkiemke='bfa46093-8781-4b2e-8164-3f446338ff69', id_sach='7b357d38-8ed7-4cda-838d-55135c843e61', so_luong_bandau=10, so_luong_kiemke=8),
                    CTKiemkeDto(id_ctkiemke='73ba9cac-5989-483d-9ee2-7fe1be59d0ed', id_sach='2291e033-baf1-44de-94d6-40bf94e91e35', so_luong_bandau=15 , so_luong_kiemke=16 )]
        response = UserDto.kiemke(kiemke, ctkiemke)
        self.assertEqual({
            'status': response.status,
            'message': response.message
        },{
            'status': True,
            'message': 'Add phieu kiemke success'
        })
class gethistoryKiemke(TestCase):
    def test_case1(self):
        response = UserDto.get_phieuKiemkes()
        self.assertEqual({
            'status': response.status,
            'message': response.message
        },{
            'status': True,
            'message': 'Get phieu kiemkes success'
        })
class getCTPhieuHuy(TestCase):
    def test_case1(self):
        id = '891cbb1f-0bea-453c-a783-2a10e0aeef90'
        response = UserDto.get_ctphieuhuyBy_PhuyId(id)
        self.assertEqual({
            'status': response.status,
            'message': response.message
        }, {
            'status': True,
            'message': 'Get ctphieuhuys success'
        })
    def test_case2(self):
        id = 'usu29x3f-074b-498a-b6e0-628765df9089'
        response = UserDto.get_ctphieuhuyBy_PhuyId(id)
        self.assertEqual({
            'status': response.status,
            'message': response.message
        }, {
            'status': True,
            'message': 'Get ctphieuhuys success'
        })
class searchPhieuHuy(TestCase):
    def test_case1(self):
        date_from = '2024-07-01'
        date_to = '2024-07-03'
        a = datetime.strptime(date_from, '%Y-%m-%d')
        b = datetime.strptime(date_to, '%Y-%m-%d')
        response = UserDto.search_phieuhuy_by_date(a, b)
        self.assertEqual({
            'status': response.status,
            'message': response.message
        }, {
            'status': True,
            'message': 'Search phieuhuy by date success'
        })
class deletePhieuHuy(TestCase):
    def test_case1(self):
        id = '2cee2d3f-074b-498a-b6e0-628765df9089'
        response = UserDto.delete_phieuhuy(id)
        self.assertEqual({
            'status': response.status,
            'message': response.message
        },  {
            'status': True,
            'message': 'Delete phieuhuy success'
        })
    def test_case2(self):
        id = 'usu29x3f-074b-498a-b6e0-628765df9089'
        response = UserDto.delete_phieuhuy(id)
        self.assertEqual({
            'status': response.status,
            'message': response.message
        },  {
            'status': True,
            'message': 'Delete phieuhuy success'
        })
class addPhieuHuy(TestCase):
    def test_case1(self):
        ngayhuy='2024-07-09'
        a = datetime.strptime(ngayhuy, '%Y-%m-%d')
        phieuhuy = PhieuhuyDto(id_phieuhuy='3df400bc-78ad-4d7d-ae5a-10ac3589f6f3', ngay_huy=a, id_user='142dd5a8-23e1-4cef-89eb-93052f36776b')
        ctphieuhuy = [
                        {
                            'id_ctphieuhuy' : '142dd5a8-23e1-4cef-89eb-93052f36776b',
                            'id_sach' : '7b357d38-8ed7-4cda-838d-55135c843e61',
                            'so_luong' : 1,
                            'ly_do_huy' : 'Sách bị cháy'
                        },
                        {
                            'id_ctphieuhuy': 'f519c434-6db5-4cab-ad5b-393560caee77',
                            'id_sach': '2291e033-baf1-44de-94d6-40bf94e91e35',
                            'so_luong': 3,
                            'ly_do_huy': 'Sách bị hỏng'
                        }
                    ]
        response = UserDto.huy_sach(phieuhuy, ctphieuhuy)
        self.assertEqual({
            'status': response.status,
            'message': response.message
        }, {
            'status': True,
            'message': 'Add phieuhuy success'
        })
    def test_case2(self):
        ngayhuy='2024-07-09'
        a = datetime.strptime(ngayhuy, '%Y-%m-%d')
        phieuhuy = PhieuhuyDto(id_phieuhuy='4234e4a1-b88d-4b29-bb75-32cc335bb727', ngay_huy=a, id_user='c2a320e5-eb4e-4570-bfa0-0d300fdcf723')
        ctphieuhuy = [
                        {
                            'id_ctphieuhuy' : '2c1cb904-1f55-4128-a79d-1ee8246dff7f',
                            'id_sach' : '7b357d38-8ed7-4cda-838d-55135c843e61',
                            'so_luong' : 1,
                            'ly_do_huy' : 'Sách bị cháy'
                        },
                        {
                            'id_ctphieuhuy': 'f519c434-6db5-4cab-ad5b-393560caee77',
                            'id_sach': '2291e033-baf1-44de-94d6-40bf94e91e35',
                            'so_luong': 3,
                            'ly_do_huy': 'Sách bị hỏng'
                        }
                    ]
        response = UserDto.huy_sach(phieuhuy, ctphieuhuy)
        self.assertEqual({
            'status': response.status,
            'message': response.message
        }, {
            'status': True,
            'message': 'Add phieuhuy success'
        })
class getPhieuHuy(TestCase):
    def test_case1(self):
        response = UserDto.get_phieuhuys()
        self.assertEqual({
            'status': response.status,
            'message': response.message
        }, {
            'status': True,
            'message': 'Get phieuhuys success'
        })
class getPhieuNhapByID(TestCase):
    def test_case1(self):
        id = 'bda84d7d-9e34-4335-a5c2-9ac7392ce0ff'
        rp = UserDto.get_phieunhapById(id)
        self.assertEqual({
            'status': rp.status,
            'message': rp.message
        }, {
            'status': True,
            'message': 'Get phieunhap success'
        })
    def test_case2(self):
        id = '0c197c30-77d5-4f7e-82ca-686a8cfddb47'
        rp = UserDto.get_phieunhapById(id)
        self.assertEqual({
            'status': rp.status,
            'message': rp.message
        }, {
            'status': True,
            'message': 'Get phieunhap success'
        })
class searchPhieuNhap(TestCase):
    def test_case1(self):
        date_from = '2024-07-01'
        date_to = '2024-07-03'
        a = datetime.strptime(date_from, '%Y-%m-%d')
        b = datetime.strptime(date_to, '%Y-%m-%d')
        response = UserDto.search_phieunhap_by_date(a,b)
        self.assertEqual({
            'status': response.status,
            'message': response.message
        }, {
            'status': True,
            'message': 'Search phieunhap by date success'
        })
class deletePhieuNhap(TestCase):
    def test_case1(self):
        id = '6eba9ce9-103d-4100-bc26-a68337b6ed41'
        response = UserDto.delete_phieunhap(id)
        self.assertEqual({
            'status': response.status,
            'message': response.message
        }, {
            'status': True,
            'message': 'Delete phieunhap success'
        })
    def test_case2(self):
        id = '7490a0d2-adde-4ca4-8cc8-c1978522ad7c'
        response = UserDto.delete_phieunhap(id)
        self.assertEqual({
            'status': response.status,
            'message': response.message
        }, {
            'status': True,
            'message': 'Delete phieunhap success'
        })
class updatePhieuNhap(TestCase):
    def test_case1(self):
        ngay_nhap = '2024-06-09'
        ngay_tao = '2024-07-08'
        a = datetime.strptime(ngay_nhap, '%Y-%m-%d')
        b = datetime.strptime(ngay_tao, '%Y-%m-%d')
        phieunhap = PhieunhapDto(id_phieunhap='6eba9ce9-103d-4100-bc26-a68337b6ed41', donvi_cungcap='Bộ giáo dục', ngay_nhap=a, ly_do_nhap='Nhập sách 06/2024', id_user='‘142dd5a8-23e1-4cef-89eb-93052f36776b')
        book = [BookDto(id_sach='df5848fb-dff4-458e-959c-2860a0c79211', name='Lập trình Python', price=25000, quantity=10, author='Nguyen A', id_category='fca7336d-1d2c-4dd5-9e1d-fb104fc53191', ngay_tao=b, )]
        bookdelete = '544e2e17-e88f-4578-b42b-7c11e88d9999'
        response = UserDto.update_phieunhap(phieunhap, book , bookdelete)
        self.assertEqual({
            'status': response.status,
            'message': response.message
        },{
            'status': True,
            'message': 'Update phieunhap success'
        })
