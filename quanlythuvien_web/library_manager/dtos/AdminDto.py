from library_manager.dtos.UserDto import UserDto
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
    
    def add_user(self):
        ...
    
    def update_user(self):
        ...
    
    def delete_user(self):
        ...
    
    def search_user(self):
        ...
    
    def get_users(self):
        ...

    def get_user_by_id(id):
        user = Users.objects.filter(id_user=id).first()
        return user if user else None