from library_manager.dtos.UserDto import UserDto
from library_manager.dtos.ResponseDto import ResponseDto as Response
from library_manager.models import Users

class AdminDto(UserDto):
    def __init__(self):
        super().__init__()

    def add_category(self):
        ...
    
    def update_category(self):
        ...
    
    def delete_category(self):
        ...

    def search_category(self):
        ...
    
    def get_categories(self):
        ...
    
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
                        birthday=userDto.birthday, phone_number=userDto.phone_number, address=userDto.address)
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
                else:
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
            if user:
                user.delete()
                return Response(True, 'Delete user success', None)
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
                    Users.objects.filter(address__icontains=searchInput))
            return Response(True, 'Search user success', users)
        except Exception as e:
            print(e)
            return Response(False, e.__str__(), None)
    
    def get_users():
        try:
            users = Users.objects.all()
            return Response(True, 'Get users success', users)
        except Exception as e:
            print(e)
            return Response(False, e.__str__(), None)

    def get_user_by_id(id):
        try:
            user = Users.objects.filter(id_user=id).first()
            return Response(True, 'Get user success', user)
        except Exception as e:
            print(e)
            return Response(False, e.__str__(), None)