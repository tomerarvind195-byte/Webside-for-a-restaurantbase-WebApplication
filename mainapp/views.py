from django.shortcuts import render, HttpResponse,redirect
from .models import Order
# Create your views here.
def index(request):
   #return HttpResponse("this is homepage")
   return render(request,"index.html")

def about(request):
    return render(request,"about.html")

def services(request):
    return render(request,"services.html")
from .models import ContactMessage

def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        subject = request.POST.get("subject")
        message = request.POST.get("message")

        ContactMessage.objects.create(
            name=name,
            email=email,
            subject=subject,
            message=message
        )

        return render(request, "contact.html", {"success": True})

    return render(request, "contact.html")


def add_to_cart(request, item):
    cart = request.session.get('cart', [])
    cart.append(item)
    request.session['cart'] = cart
    return redirect('/')





def cart(request):
    return render(request, 'cart.html')

from .models import Feedback

def feedback(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        rating = request.POST.get("rating")
        message = request.POST.get("message")

        Feedback.objects.create(
            name=name,
            email=email,
            rating=rating,
            message=message
        )

        return render(request, "feedback.html", {"success": True})

    return render(request, "feedback.html")

def order_now(request, item, qty=1):
    return render(request, "order.html", {
        "item": item,
        "qty": qty
    })


def place_order(request):
    if request.method == "POST":
        item = request.POST.get("item")
        qty = request.POST.get("qty")
        name = request.POST.get("name")
        email = request.POST.get("email")
        address = request.POST.get("address")
        phone = request.POST.get("phone")

        Order.objects.create(
            item=item,
            quantity=qty,
            name=name,
            email=email,
            address=address,
            phone=phone
        )

        return redirect("/")   # homepage redirect

    return redirect("/") # GET request aaye to home


def order_success(request):
    order = request.session.get("order")
    return render(request, "success.html", {"order": order})
    