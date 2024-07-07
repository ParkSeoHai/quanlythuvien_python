
class BookDto(object):
    def __init__(self, id_sach = '', name = '', price = 0,
                quantity=1, image='', author='', id_category='',
                is_delete = 0, ngay_tao=''):
        self.id_sach = id_sach
        self.name = name
        self.price = price
        self.quantity = quantity
        self.image = image
        self.author = author
        self.is_delete = is_delete
        self.id_category = id_category
        self.ngay_tao = ngay_tao



