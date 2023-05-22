from .models import Member,Product
from django.shortcuts import render, redirect
from .forms import MemberForm
from django.contrib import messages 
from django.db.models import Q
from django.core.paginator import Paginator

# =============================================================================================
def main(request):
    # Get all Products to Show in HTML page
    Products = Product.objects.all()
    # paginator = Paginator(Products, 3) # Show 3 contacts per page.
    # page_number = request.GET.get('page')
    # Products = paginator.get_page(page_number)
    try:
        # if user use search filter -> search in database about Products
        if request.method == 'POST':
            name = request.POST.get('name')
            author = request.POST.get('category')

            if name:
                my_products_ids = [product['id'] for product in Product.objects.all().filter(Q(name__startswith=name)).values()]
                Products = [Product.objects.get(pk = id) for id in my_products_ids]
            if author:
                my_products_ids = [product['id'] for product in Product.objects.all().filter(Q(writer__startswith=author)).values()]
                Products = [Product.objects.get(pk = id) for id in my_products_ids]

        # Check if user is already login
        if request.session['id']:
            Name = Member.objects.get(pk = request.session['id']).name
            return render(request,'main.html',{'Name':Name,'Products' : Products})

    except KeyError:
        pass


    return render(request,'main.html',{'products' : Products})

# =============================================================================================
def product(request):
    product_id = request.GET.get('product')
    my_product = Product.objects.get(pk = product_id)
    try:
        if request.session['id']:
            member = Member.objects.get(pk = request.session['id'])
            read_before = reading.objects.filter(user = member, product = my_product)
            if not read_before:
                put_reading = reading(user = member, product = my_product)
                put_reading.save()

    except KeyError:
        pass

    return render(request, 'book.html', {'product': my_product})

# =============================================================================================
def myaccount(request):
    # Get Name to Show in HTML page and to get id of User
    id = request.session['id']

    # Check if user is already login to his account
    if id:
        # Get Email to Show in HTML page
        Name = Member.objects.get(pk = id).name
        email = Member.objects.get(pk = id).email

        # Get Products of that user from database to Show in HTML page
        id_user = request.session['id']
        my_products_ids = [product['product_id'] for product in reading.objects.all().filter(user = id_user).values()]
        Products = [Product.objects.get(pk = id) for id in my_products_ids]

        return render(request,'account.html',{'Name':Name,'email':email,'Products':Products})
    
    else:
        return redirect("/")

# =============================================================================================
def register(request):
    # Check if user wrote data 
    if request.method == "POST":

        # Get data from form
        name = request.POST.get('name')
        em = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        # Check if email is already at database if not save data.
        is_Old_User = Member.objects.filter(email = em)
        if not is_Old_User:
            if password1 == password2 != "":
                data = Member(name=name,email=em,password=password1)
                data.save()
                request.session['id'] = Member.objects.get(email = em).pk # Open new Sassion to remember user 
                return redirect("/")
            else:
                messages.warning(request,"Confirm Password not the same Password!")
                return redirect("/register")
        else:
            messages.warning(request,"This Email is registered, Do you need to login?")
            return redirect("/register")

    # Check if user is already login
    try:
        already_login = request.session['id']
        if already_login:
            return redirect("/")

    except KeyError:
        pass

    return render(request,'register.html',{'mb':MemberForm})

# =============================================================================================

def login(request):
    # Check if user wrote data 
    if request.method == 'POST':

        # Get data from form
        em =  request.POST.get('email')
        passw =    request.POST.get('password')
        isEmail = Member.objects.filter(email = em)
        isUser = Member.objects.filter(email = em, password = passw)

        # Check if user wrote valid data to login
        if isEmail:
            if isUser:
                request.session['id'] = Member.objects.get(email = em).pk # Open new Sassion to remember user 
                return redirect('/')
            else:
                messages.warning(request,"Wrong Password!")
                return redirect("/login")

        else:
            messages.warning(request,"Email not Found!")
            return redirect("/login")

    try:
        # Check if user is already login
        if request.session['id']:
            return redirect("/")

    except KeyError:
        pass
    
    return render(request, 'login.html')
# =============================================================================================

def logout(request):
    # delete sassion of user
    try:
        request.session['id'] = None
    except KeyError:
        pass
    return redirect('/')

# =============================================================================================

