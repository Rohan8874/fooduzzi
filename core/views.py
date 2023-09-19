from django.shortcuts import redirect, render
from core.forms import UserRegisterForm
from django.contrib.auth import login, authenticate
from django.contrib import messages
from core.models import User, Product, CartOrder, Category, Vandor, CartOrderItems, ProductImages, ProductReview, Wishlist, Address
from fooduzzi.core.admin import ProductAdmin


def index(request):
    products = Product.objects.all()

    context = {
        "products": products
    }
    return render(request, 'core/index.html')

def register_view(request):

    if request.method == "POST":
        form = UserRegisterForm(request.POST or None)
        if form.is_valid():
            new_user = form.save()
            username = form.cleaned_data.get("username")
            messages.success(request, f"Hey {username}, Your account was created successfully")
            new_user = authenticate(username=form.cleaned_data['email'],
                                    password=form.cleaned_data['password1']
            )
            login(request, new_user)
            return redirect("core:index")
    else:
        form = UserRegisterForm()
    
    context = {
        'form': form,
    }

    return render(request, "core/sign-up.html", context)
