from django.shortcuts import render,redirect,HttpResponse
from customer.models import Contact,Category,SubCategory,Product,addCart
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login ,logout


# ? Common things
cat=Category.objects.all();
subcat=SubCategory.objects.all();
# print(cat)
context = {'cat':cat,'subcat':subcat}



# Create your views here.

def base(request):
    return render(request,'customer/base.html',context)

def index(request):
    product=Product.objects.all()
    context.update({'product':product})
    return render(request,'customer/index.html',context)

def About(request):
    return render(request,'customer/aboutUs.html',context)

def contact(request):
    if request.method == 'POST':
        name = request.POST['customerName']
        email = request.POST['customerEmail']
        sub = request.POST['contactSubject']
        desc = request.POST['contactMessage']
        print(name,email,sub,desc)
        contact=Contact(name=name,email=email,sub=sub,desc=desc)
        contact.save()
        messages.success(request,"Your Response Has been saved!")      
        return redirect(index)  
    return render(request,'customer/contactUs.html',context)

def register(request):
    if request.method == "POST":
        email = request.POST['email']
        username = request.POST['username']
        name = request.POST['name']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
        
        print(email,username,name,pass1,pass2)

        # check for errorneous input
        if len(username)>10:
            messages.error(request, " Your user name must be under 10 characters")
            return redirect('register')

        if not username.isalnum():
            messages.error(request, " User name should only contain letters and numbers")
            return redirect('index')
        
        if (pass1!= pass2):
             messages.error(request, " Passwords do not match")
             return redirect('index')
        

        myuser = User.objects.create_user(username,email,pass1)
        myuser.first_name = name
        myuser.save()
        messages.success(request, "Account Created Successfully!")
        return redirect(register)
    return render(request,'customer/register.html',context)

def loginPage(request):
        if request.method == "POST":
            loginusername = request.POST['loginusername']
            loginpassword = request.POST['loginpassword']
            print(loginusername,loginpassword)
            user=authenticate(username=loginusername,password=loginpassword)
            if user is not None:
                login(request,user)
                messages.success(request,"Successfully Logged In!")
            else:
                messages.error(request,"Invalid Credentials")
        return render(request,'customer/login.html',context)
    
def logoutPage(request):
        logout(request)
        return redirect('index')


def shop(request):
    return render(request,'customer/shop.html',context)

def category(request):
    context = {}
    return render(request,'customer/category.html',context)

def product(request,slug):
    product = Product.objects.filter(name=slug).first()
    print(product)
    context.update({'product':product})
    return render(request,'customer/product.html',context)

def checkout(request):
    return render(request, 'customer/checkout.html',context)

def wish(request):
    return render(request, 'customer/wish.html',context)


def search(request):
    if request.method == 'GET':
        search = request.GET['search']
        if len(search) > 70:
            messages.error(request, "Enter a Valid Keyword to Search")
            product = Product.objects.none()            
        else:
            productName=Product.objects.filter(name__icontains=search)
            productContent=Product.objects.filter(srtdesc__icontains=search)
            allProducts=productName.union(productContent)
        if allProducts.count() == 0:
            messages.warning(request, "Search Results not found.")
        context.update({'allProducts':allProducts,'search':search})
    return render(request,'customer/search.html',context)


def addCart(request):
    return render(request, 'customer/addCart.html',context)
