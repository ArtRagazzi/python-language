from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .form import SignUpForm, AddBookForm
from .models import Book

# Create your views here.
def home(request):
    
    books = Book.objects.all()
    
    if(request.method == "POST"):
        username = request.POST['usuario']
        password = request.POST['senha']
        #Auth
        user = authenticate(
            request,
            username = username,
            password = password
        )
        if user is not None:
            login(request, user)
            messages.success(request, "Login foi realizado com sucesso!")
            return redirect('home')
        else:
            messages.error(request, "Erro na autenticação, tente novamente!")
            return redirect('home')
        
    else:
        return render(request, 'home.html', {'books':books})

def logout_user(request):
    logout(request)
    messages.success(request, "Logout com sucesso!")
    return redirect('home')

def register_user(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            #Auth e Login
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(
                username = username,
                password = password
            )
            login(request, user)
            messages.success(
                request,
                "Você fez o login com sucesso com o novo usuario!"
            )
            return redirect('home')
            
    else:
        form = SignUpForm()
        return render(request, 'register.html', {'form':form})
    return render(request, 'register.html', {'form':form})

def book_detail(request, id):
    if request.user.is_authenticated:
        book = Book.objects.get(id=id)
        return render(request, 'book.html', {'book':book})
    else:
        messages.error(request, 'Você preicsa estar logado!')
        return redirect('home')
    
def book_delete(request,id):
    if request.user.is_authenticated:
        book = Book.objects.get(id=id)
        book.delete()
        messages.success(request, 'Livro excluido com sucesso!')
        return redirect('home')
    else:
        messages.error(request, 'Você precisa estar logado!')
        return redirect('home')
    
    
def book_add(request):
    form = AddBookForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == "POST":
            if form.is_valid():
                form.save()
                messages.success(request, "Livro adicionado com sucesso!")
                return redirect('home')
        return render(request, 'add_book.html', {'form':form})
    else:
        messages.error(request, "Você deve estar autenticado para adicionar livros!")
        return redirect('home')
    

def update_book(request, id):
    if request.user.is_authenticated:
        book = Book.objects.get(id=id)
        form = AddBookForm(request.POST or None, instance=book)
        if form.is_valid():
            form.save()
            messages.success(request, 'Livro atualizado com sucesso!')
        return render(request, 'update_book.html', {'form':form})
    else:
        messages.error(request, "Você deve estar autenticado para adicionar livros!")
        return redirect('home')