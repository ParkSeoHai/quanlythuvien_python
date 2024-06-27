class CategoryDto(object):
    def __init__(self, id_category = '', name = '', description = '', is_delete = 0):
        self.id_category = id_category
        self.name = name
        self.description = description
        self.is_delete = is_delete