import datetime

class DocgiaDto(object):
    def __init__(self, id_docgia = '', name = '', email = '',
                gender = 0, birthday = '', phone_number = '',
                address = '', ngay_tao = ''):
        self.id_docgia = id_docgia
        self.name = name
        self.email = email
        self.gender = gender
        self.birthday = birthday
        self.phone_number = phone_number
        self.address = address
        self.ngay_tao = ngay_tao