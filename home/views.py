from django.shortcuts import render

def index(request):
    """ A view to return the index page """
    return render(request, 'home/index.html')

def product_management(request):
    """ A view to display the product management page """
    products = Product.objects.all()  
    context = {'products': products}
    return render(request, 'home/product_management.html', context)

def my_profile(request):
    """ A view to display the user's profile """
    return render(request, 'home/my_profile.html')

def profile_view(request):
    """ A view to display the user's profile """
    return render(request, 'home/my_profile.html')
