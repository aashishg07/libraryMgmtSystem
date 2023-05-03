from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from .models import Book


def bookView(request):
    books=Book.objects.all()
    return render(request,"books.html",{"books":books})

def addBookView(request):
    return render(request,"addBooks.html")


def addBook(request):
    if request.method=="POST":
        t=request.POST["title"]
        p=request.POST["price"]
        print(t,p)
        book=Book()
        book.title=t
        book.price=p
        book.save()
        return HttpResponseRedirect('/')
    

def editBookView(request):
    book = Book.objects.get(id = request.GET["bookid"])
    return render(request, "editBooks.html", {"book":book})


def editBook(request):
    if request.method == "POST":
        t=request.POST["title"]
        p=request.POST["price"]
        print(t,p)
        book=Book.objects.get(id=request.POST["bookid"])
        book.title=t
        book.price=p
        book.save()
        return HttpResponseRedirect('/')
    
def deleteBookView(request):
    book = Book.objects.get(id = request.GET["bookid"])
    book.delete()
    return HttpResponseRedirect('/')