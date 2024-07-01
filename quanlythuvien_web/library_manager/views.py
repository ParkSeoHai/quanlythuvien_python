from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse

import uuid
import json

# Import user dto
from library_manager.dtos.UserDto import UserDto
from library_manager.dtos.AdminDto import AdminDto
from library_manager.dtos.PhieunhapDto import PhieunhapDto
from library_manager.dtos.BookDto import BookDto

# Default view for login page
def index(request):
    template = loader.get_template('login.html')
    return HttpResponse(template.render())

# Login post request
def loginPost(request):
    if request.method == 'POST':
        # Get email and password from request
        email = request.POST.get('email')
        password = request.POST.get('password')
        # Create user dto
        user = UserDto(email=email, password=password)
        # Response from login function
        response = user.login()

        # If login success
        if response.status is True:
            # Set user id session
            request.session['id_user'] = response.data
            # Redirect to home page
            return HttpResponseRedirect(reverse('home'))
        else:
            # Redirect to login page
            return HttpResponseRedirect(reverse('main'))

# Get user from session
def get_user(request):
    # Get user id session
    id_user = request.session.get('id_user')
    # If user is not logged in, redirect to login page
    if id_user is None:
        return HttpResponseRedirect(reverse('main'))
    else:
        # Get user by id
        response = AdminDto.get_user_by_id(id_user)
        return response.data if response.data else None

# View for home page
def home(request):
    # Get user
    user = get_user(request)
    # Load home page
    template = loader.get_template('home.html')
    return HttpResponse(template.render({
        'user': user
    }, request))

# View for quanlynguoidung page
def quanlynguoidung(request):
    # Get user id session when user login
    user = get_user(request)
    # Get all users
    response = AdminDto.get_users()
    # Context for template
    context = {
        'user': user,
        'users': response.data,
    }
    # Load quanlynguoidung page
    template = loader.get_template('quanlynguoidung/index.html')
    return HttpResponse(template.render(context, request))

# Add user view
def addUser(request):
    # Get user
    user = get_user(request)
    # Load template
    template = loader.get_template('quanlynguoidung/add.html')
    return HttpResponse(template.render({
        'user': user
    }, request))

# Add user post request
def addUserPost(request):
    if request.method == 'POST':
        # Get value
        id = str(uuid.uuid4())  # Generate random id
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = '123456'     # Default password
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        role = int(request.POST.get('role'))
        gender = int(request.POST.get('gender'))
        birthday = request.POST.get('birthday')

        # Create user dto
        user = UserDto(id_user=id, name=name, email=email, password=password, role=role,
                        gender=gender, birthday=birthday, phone_number=phone, address=address)
        print(user.__dict__)

        # Response from add_user function
        response = AdminDto.add_user(user)
        if response.status is True:
            print(response.message)
            return HttpResponseRedirect(reverse('quanlynguoidung'))
        else:
            print(response.message)
            return HttpResponseRedirect(reverse('addUser'))

# Update user view
def updateUser(request, id):
    # Get user
    user = get_user(request)
    # Get user by id
    user_update = AdminDto.get_user_by_id(id).data
    # Load update user page
    template = loader.get_template('quanlynguoidung/update.html')
    return HttpResponse(template.render({
        'user': user,
        'user_update': user_update
    }, request))

# Update user post request
def updateUserPost(request):
    if request.method == 'POST':
        # Get value
        id = request.POST.get('id')
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        role = int(request.POST.get('role'))
        gender = int(request.POST.get('gender'))
        birthday = request.POST.get('birthday')

        # Create user dto
        user = UserDto(id_user=id, name=name, email=email, role=role, gender=gender,
                        birthday=birthday, phone_number=phone, address=address)
        print(user.__dict__)

        # Response from update_user function
        response = AdminDto.update_user(user)
        if response.status is True:
            print(response.message)
            return HttpResponseRedirect(reverse('quanlynguoidung'))
        else:
            print(response.message)
            return HttpResponseRedirect(reverse('updateUser', args=(id,)))

# Delete user
def deleteUser(request, id):
    # Response from delete_user function
    response = AdminDto.delete_user(id)

    print(response.message)
    return HttpResponseRedirect(reverse('quanlynguoidung'))

# Search user
def searchUser(request, searchInput):
    # Get user
    user = get_user(request)
    # Response from search_user function
    response = AdminDto.search_user(searchInput)
    # Load quanlynguoidung page
    template = loader.get_template('quanlynguoidung/index.html')
    return HttpResponse(template.render({
        'user': user,
        'users': response.data
    }, request))

def quanlydanhmuc(request):
    # Get user
    user = get_user(request)
    # Load quanlydanhmuc page
    template = loader.get_template('quanlydanhmuc/index.html')
    return HttpResponse(template.render({
        'user': user
    }, request))

# hien thi view quan ly sach
def quanlysach(request):
    # Get user
    user = get_user(request)
    response = UserDto.get_books()
    context = {
        'user': user,
        'books': response.data,
    }
    # Load quanlysach page
    template = loader.get_template('quanlysach/index.html')
    return HttpResponse(template.render(
        context, request))

#xoá sách
def deleteBook(request, id_sach):
    response = AdminDto.delete_book(id_sach)
    if response.status is True:
        print(response.message)
        return HttpResponseRedirect(reverse('quanlysach'))
    else:
        print(response.message)
        return HttpResponseRedirect(reverse('quanlysach'))

#them sach
def addBook(request):
    # Get user
    user = get_user(request)
    response = AdminDto.get_categories()
    # Load template
    template = loader.get_template('quanlysach/add.html')
    return HttpResponse(template.render({
        'user': user,
        'categories': response.data,
    }, request))

# Add sach post request
def addBookPost(request):
    if request.method == 'POST':
        # Get value
        id_sach = str(uuid.uuid4())  # Generate random id
        name = request.POST.get('name')
        price = request.POST.get('price')
        quantity = request.POST.get('quantity')
        image = request.POST.get('image')
        author = request.POST.get('author')
        id_category = request.POST.get('category')
        # Create book dto
        book = BookDto(id_sach=id_sach, name=name, price=price, quantity=quantity, image=image,
                        author=author, id_category=id_category)
        print(book.__dict__)

        # Response from add_book function
        response = UserDto.add_book(book)
        if response.status is True:
            print(response.message)
            return HttpResponseRedirect(reverse('quanlysach'))
        else:
            print(response.message)
            return HttpResponseRedirect(reverse('addBook'))
        
#update sach
def updateBook(request, id_sach):
    # Get user
    user = get_user(request)
    # Get user by id
    response = AdminDto.get_categories()
    book_update = UserDto.get_bookById(id_sach).data
    # Load update user page
    template = loader.get_template('quanlysach/update.html')
    return HttpResponse(template.render({
        'user': user,
        'book_update': book_update,
        'categories': response.data,
    }, request))

# Update user post request
def updateBookPost(request):
    if request.method == 'POST':
        # Get value
        id_sach = request.POST.get('id_sach')
        name = request.POST.get('name')
        price = request.POST.get('price')
        quantity = request.POST.get('quantity')
        image = request.POST.get('image')
        author = request.POST.get('author')
        id_category = request.POST.get('category')
        # Create user dto
        book = BookDto(id_sach = id_sach,name=name, price=price, quantity=quantity, image=image,
                        author=author, id_category=id_category)
        print(book.__dict__)

        # Response from update_user function
        response = UserDto.update_book(book)
        if response.status is True:
            print(response.message)
            return HttpResponseRedirect(reverse('quanlysach'))
        else:
            print(response.message)
            return HttpResponseRedirect(reverse('updateBook', args=(id_sach,)))

#tim kiem sach
def searchBook(request, searchInput):
    # Get book
    user = get_user(request)
    # Response from search_book function
    response = UserDto.search_book(searchInput)
    # Load quanlysach page
    template = loader.get_template('quanlysach/index.html')
    return HttpResponse(template.render({
        'user': user,
        'books': response.data
    }, request))

# Get book by id from javascript fetch request
def getBook(request):
    if request.method == 'GET':
        id = request.GET.get('id')
        response = UserDto.get_bookById(id[0:len(id)-1])
        # Book response
        bookResponse = {
            'id_sach': response.data.id_sach,
            'name': response.data.name,
            'price': response.data.price,
            'quantity': response.data.quantity,
            'image': response.data.image,
            'author': response.data.author,
            'is_delete': response.data.is_delete,
            'id_category': response.data.id_category_id
        }
        # Return response to javascript json serializer
        return HttpResponse(json.dumps(bookResponse), content_type='application/json')

def quanlymuontra(request):
    # Get user
    user = get_user(request)
    # Load quanlymuontra page
    template = loader.get_template('quanlymuontra/index.html')
    return HttpResponse(template.render({
        'user': user
    }, request))

def quanlytinhhinhmuontra(request):
    # Get user
    user = get_user(request)
    phieumuons = UserDto.check_phieumuon()

    # Load quanlytinhhinhmuontra page
    template = loader.get_template('quanlytinhhinhmuontra/index.html')
    return HttpResponse(template.render({
        'user': user,
        'phieumuons': phieumuons.data,
    }, request))

def quanlytinhhinhDaTra(request):
    # Get user
    user = get_user(request)
    phieumuons = UserDto.check_phieumuonDaTra()

    # Load quanlytinhhinhmuontra page
    template = loader.get_template('quanlytinhhinhmuontra/PhieuMuonDaTra.html')
    return HttpResponse(template.render({
        'user': user,
        'phieumuons': phieumuons.data,
    }, request))

# Quan ly kho sach
def quanlykhosach(request):
    # Get user
    user = get_user(request)
    # Load quanlykhosach page
    template = loader.get_template('quanlykhosach/index.html')
    return HttpResponse(template.render({
        'user': user
    }, request))

# Quan ly kho sach - nhap sach
def nhapsach(request):
    # Get user 
    user = get_user(request)
    # Get all phieu nhap
    phieunhapRes = UserDto.get_phieunhaps()
    # Context for template
    context = {
        'user': user,
        'phieunhaps': phieunhapRes.data
    }
    # Load nhapsach page
    template = loader.get_template('quanlykhosach/nhapsach/index.html')
    return HttpResponse(template.render(context, request))

# Lap phieu nhap sach view
def addPhieunhap(request):
    # Get user
    user = get_user(request)
    # Get category
    categoryRes = AdminDto.get_categories()
    # Get books
    bookRes = UserDto.get_books()
    # Context for template
    context = {
        'user': user,
        'categories': categoryRes.data,
        'books': bookRes.data
    }
    # Load addPhieunhap page
    template = loader.get_template('quanlykhosach/nhapsach/add.html')
    return HttpResponse(template.render(context, request))

# Cap nhat phieu nhap sach view
def updatePhieunhap(request, id):
    # Get user
    user = get_user(request)
    # Get phieu nhap by id
    pnRes = UserDto.get_phieunhapById(id)
    # Get ctphieunhap by id phieu nhap
    ctphieunhapRes = UserDto.get_ctphieunhapBy_PnhapId(id)
    # List books
    listBooks = []
    for ctpn in ctphieunhapRes.data:
        book = {
            'id': ctpn.id_sach_id,
            'name': ctpn.id_sach.name,
            'price': ctpn.gia_nhap,
            'quantity': ctpn.so_luong,
            'author': ctpn.id_sach.author,
            'category': {
                'id': ctpn.id_sach.id_category_id,
                'name': ctpn.id_sach.id_category.name
            }
        }
        listBooks.append(book)
    # Get categogies
    categoryRes = AdminDto.get_categories()
    # Get books
    bookRes = UserDto.get_books()
    # Context for template
    context = {
        'user': user,
        'phieunhap': pnRes.data,
        'categories': categoryRes.data,
        'books': bookRes.data,
        'listBooks': listBooks
    }
    # Load updatePhieunhap page
    template = loader.get_template('quanlykhosach/nhapsach/update.html')
    return HttpResponse(template.render(context, request))

# Nhap sach post request
def nhapsachPost(request):
    if request.method == 'POST':
        # Get value
        data = request.POST.get('data')
        data = json.loads(data)
        # Create phieu nhap dto
        phieunhap = PhieunhapDto(
            id_phieunhap=str(uuid.uuid4()),
            donvi_cungcap=data['dvcc'],
            ngay_nhap=data['ngaynhap'],
            ly_do_nhap=data['lydo'],
            id_user=request.session.get('id_user')
        )
        
        # Create list book dto
        books = []
        for book in data['books']:
            book = BookDto(
                id_sach=str(uuid.uuid4()),
                name=book['name'],
                price=float(book['price']),
                quantity=int(book['quantity']),
                image='https://plus.unsplash.com/premium_photo-1667251760532-85310936c89a?q=80&w=1887&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D',
                author=book['author'],
                id_category=book['category']['id']
            )
            books.append(book)
        
        # Response from nhap_sach function
        responseDto = UserDto.nhap_sach(phieunhap, books)
        print(responseDto.message)

        response = {
            'status': responseDto.status,
            'message': responseDto.message,
            'data': responseDto.data
        }
        # Return response to javascript json serializer
        return HttpResponse(json.dumps(response), content_type='application/json')

# Update phieu nhap
def updatePhieunhapPost(request):
    if request.method == 'POST':
        # Get value
        data = request.POST.get('data')
        data = json.loads(data)

        print(data)

        # Create phieu nhap dto
        pn = PhieunhapDto(
            id_phieunhap=data['id_phieunhap'],
            donvi_cungcap=data['dvcc'],
            ngay_nhap=data['ngaynhap'],
            ly_do_nhap=data['lydo'],
            id_user=request.session.get('id_user')
        )
        
        # Create list book dto
        books = []
        for book in data['books']:
            book = BookDto(
                id_sach=book['id'],
                name=book['name'],
                price=float(book['price']),
                quantity=int(book['quantity']),
                image='https://plus.unsplash.com/premium_photo-1667251760532-85310936c89a?q=80&w=1887&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D',
                author=book['author'],
                id_category=book['category']['id']
            )
            books.append(book)

        # Get book deletes
        book_deletes = data['book_deletes']

        # Response from nhap_sach function
        responseDto = UserDto.update_phieunhap(pn, books, book_deletes)
        print(responseDto.message)

        response = {
            'status': responseDto.status,
            'message': responseDto.message,
            'data': responseDto.data
        }

        # Return response to javascript json serializer
        return HttpResponse(json.dumps(response), content_type='application/json')

# Delete phieu nhap
def deletePhieunhap(request, id):
    # Response from delete_phieunhap function
    response = UserDto.delete_phieunhap(id)
    
    print(response.message)
    return HttpResponseRedirect(reverse('nhapsachIndex'))

# Search phieu nhap by date
def searchPhieunhapByDate(request, dateFrom, dateTo):
    # Get user
    user = get_user(request)
    # Response from search_phieunhap_by_date function
    response = UserDto.search_phieunhap_by_date(dateFrom, dateTo)
    # Context for template
    context = {
        'user': user,
        'phieunhaps': response.data,
        'dateFrom': dateFrom,
        'dateTo': dateTo
    }
    # Load nhapsach page
    template = loader.get_template('quanlykhosach/nhapsach/index.html')
    return HttpResponse(template.render(context, request))

# Info phieu nhap sach view
def infoPhieunhap(request, id):
    # Get user
    user = get_user(request)
    # Get phieu nhap by id
    phieunhapRes = UserDto.get_phieunhapById(id)
    # Get ctphieunhap by id phieu nhap
    ctphieunhapRes = UserDto.get_ctphieunhapBy_PnhapId(id)
    # Context for template
    context = {
        'user': user,
        'phieunhap': phieunhapRes.data,
        'ctphieunhaps': ctphieunhapRes.data
    }
    # Load infoPhieunhap page
    template = loader.get_template('quanlykhosach/nhapsach/info.html')
    return HttpResponse(template.render(context, request))

# Logout
def logout(request):
    # Delete user id session
    if 'id_user' in request.session:
        del request.session['id_user']
    # Redirect to login page
    return HttpResponseRedirect(reverse('main'))