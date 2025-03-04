from django.shortcuts import render

from django.http import response, HttpResponse, HttpResponseRedirect, HttpResponseNotFound

from .models import Books


def homePageView(request):
    return HttpResponse('Hello World')

def index(request):
    books = Books.objects.filter(isArchived=False)
    return render(request, 'index.html', {'books': books})

def create(request):
    if request.method == "POST":
        book = Books()
        book.name = request.POST.get("name")
        book.author_name = request.POST.get("author_name")
        book.author_surname = request.POST.get("author_surname")
        book.price = request.POST.get("price")
        book.descripton = request.POST.get("description")
        book.quantity = request.POST.get("quantity")
        book.save()
        return HttpResponseRedirect("/")
    else:
        return render(request, "create.html" )


def edit(request, id):
    try:
        book = Books.objects.get(id=id)

        if request.method == "POST":
            book.name = request.POST.get("name")
            book.author_name = request.POST.get("author_name")
            book.author_surname = request.POST.get("author_surname")
            book.price = request.POST.get("price")
            book.descripton = request.POST.get("description")
            book.quantity = request.POST.get("quantity")
            book.save()
            return HttpResponseRedirect("/")
        else:
            return render(request, "edit.html", {"book": book})
    except Books.DoesNotExist:
        return HttpResponseNotFound("<h2>Book not found</h2>")


def delete(request, id):
        try:
            book = Books.objects.filter(id=id).update(isArchived=True)
            return HttpResponseRedirect("/")
        except Books.DoesNotExist:
            return HttpResponseNotFound("<h2>Book not found</h2>")

