from django.test import TestCase

from library_manager.dtos.UserDto import UserDto
from library_manager.dtos.AdminDto import AdminDto
from library_manager.dtos.DocgiaDto import DocgiaDto
from library_manager.dtos.ThethuvienDto import ThethuvienDto
from library_manager.dtos.PhieumuonDto import PhieumuonDto
from library_manager.dtos.PhieunhapDto import PhieunhapDto
from library_manager.dtos.BookDto import BookDto

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
