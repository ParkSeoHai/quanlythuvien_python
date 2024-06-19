from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse

# Import user dto
from library_manager.dtos.UserDto import UserDto
from library_manager.dtos.AdminDto import AdminDto

# Create your views here.
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
        # Login
        id_user = user.login()
        # If login success
        if id_user is not None:
            # Set user id session
            request.session['id_user'] = id_user
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
        user = AdminDto.get_user_by_id(id_user)
        return user if user else None

# View for home page
def home(request):
    # Get user
    user = get_user(request)
    # Load home page
    template = loader.get_template('home.html')
    return HttpResponse(template.render({
        'user': user
    }, request))

def quanlynguoidung(request):
    # Get user
    user = get_user(request)
    # Load quanlynguoidung page
    template = loader.get_template('quanlynguoidung.html')
    return HttpResponse(template.render({
        'user': user
    }, request))

def quanlydanhmuc(request):
    # Get user
    user = get_user(request)
    # Load quanlydanhmuc page
    template = loader.get_template('quanlydanhmuc.html')
    return HttpResponse(template.render({
        'user': user
    }, request))

def quanlysach(request):
    # Get user
    user = get_user(request)
    # Load quanlysach page
    template = loader.get_template('quanlysach.html')
    return HttpResponse(template.render({
        'user': user
    }, request))

def quanlymuontra(request):
    # Get user
    user = get_user(request)
    # Load quanlymuontra page
    template = loader.get_template('quanlymuontra.html')
    return HttpResponse(template.render({
        'user': user
    }, request))

def quanlytinhhinhmuontra(request):
    # Get user
    user = get_user(request)
    # Load quanlytinhhinhmuontra page
    template = loader.get_template('quanlytinhhinhmuontra.html')
    return HttpResponse(template.render({
        'user': user
    }, request))

def quanlykhosach(request):
    # Get user
    user = get_user(request)
    # Load quanlykhosach page
    template = loader.get_template('quanlykhosach.html')
    return HttpResponse(template.render({
        'user': user
    }, request))

# Logout
def logout(request):
    # Delete user id session
    del request.session['id_user']
    # Redirect to login page
    return HttpResponseRedirect(reverse('main'))