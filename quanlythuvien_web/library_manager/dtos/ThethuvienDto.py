
class ThethuvienDto(object):
    def __init__(self, id_the = '', type = 1, ngay_tao = '',
                ngay_het_han = '', ghi_chu = '', id_docgia = '', is_delete = 0):
        self.id_the = id_the
        self.type = type
        self.ngay_tao = ngay_tao
        self.ngay_het_han = ngay_het_han
        self.ghi_chu = ghi_chu
        self.id_docgia = id_docgia
        self.is_delete = is_delete
