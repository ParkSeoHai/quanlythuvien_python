from django.test import TestCase, tag

from library_manager.dtos.UserDto import UserDto

# Command test: python manage.py test --k --tag={name}

class TestFunction(TestCase):
    @tag('login')
    def test_login(self):
        user = UserDto(email='admin4444@gmail.com', password='123456')
        response = user.login()
        
        self.assertEqual({
            'status': response.status,
            'message': response.message
        }, {
            'status': True,
            'message': 'Đăng nhập thành công'
        })
        