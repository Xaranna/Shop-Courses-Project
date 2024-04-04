from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from .models import Course, Cart
from django.contrib.auth.decorators import login_required


def index(request):
    courses = Course.objects.all()
    return render(request, 'shop/courses.html', {'courses': courses})


def single_course(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    return render(request, 'shop/single_course.html', {'course': course})

@login_required
def cart_add(request, course_id):
    course = Course.objects.get(id=course_id)
    cart = Cart.objects.filter(user=request.user, course=course)

    if not cart.exists():
        Cart.objects.create(user=request.user, course=course, quantity=1)
    else:
        cart = cart.first()
        cart.quantity += 1
        cart.save()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

@login_required
def cart_remove(request, cart_id):
    cart = Cart.objects.get(id=cart_id)
    cart.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))