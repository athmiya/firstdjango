from django.shortcuts import render,redirect
from .forms import BookForms,ModelBookForms,SearchForm
from home.models import Book
#from django.utils import timezone 
from django.contrib import messages
# Create your views here.
def form_view(request):
    #context = None
    msg=''
    if request.method =='POST':
        form = BookForms(request.POST)
        if form.is_valid():
            book = Book.objects.create(
                name=form.cleaned_data.get('name'),
                purchase_date=form.cleaned_data.get('pur_date'),
                #genre=form.cleaned_data.get('genre'),
                author=form.cleaned_data.get('author')
            )
            book.save()
            msg = 'Book Added Successfully!!'
        else:
            msg = form.errors
#  book= Book.objects.all()
#  book=Book.objects.filter(name='',purchase_date='')
    else:
       form=BookForms()    
    return render(request,'forms.html',{"msg":msg,"forms":form})

#def model_view(request):
  #context = None
  # msg=''
   # if request.method =='POST':
    #  form = ModelBookForms(request.POST)
     # if form.is_valid():
      #  form.save()
        
        
       # msg = 'Book Added Successfully!!'
      #else:
       #   msg = form.errors
 
    #else:
     #  form=ModelBookForms()    
      # return render(request,'forms.html',{"msg":msg,"forms":form})

def html_form(request):
  value=''
  if request.method == 'POST':
    value = request.POST.get('name')
    return render(request,'values.html',{'values':value})
  else:
      value='wrong input'
  return render(request,'myproject.html',{ 'values':value})


def booksearch(request):
  if request.method == 'POST':
    form = SearchForm(request.POST)
    if form.is_valid():
      q = form.cleaned_data.get('q')
    #  book = Book.objects.filter(name__contains=q)
    return render(request,'showtables.html',{'book':book})
  else:
    form = SearchForm()
    book = Book.objects.all()
  return render(request,'showtables.html',{'book':book,'form':form})

def deletebook(request,id):
  book = Book.objects.get(id=id)
  messages.success(request,'Deleted #'+str(id)+'Succeessfully!!')
  #messages.success(request,'Deleted Successfully!!')
  book.delete()
  return redirect('/')


def editbook(request,id):
  book = Book.objets.get(id = id)
  if request.method  == 'POST':
    form = ModelBookForms(request.POST)
    if form.is_valid():
      form.save()
      messages.success(request,'Book Updated Successfully!!')
      return redirect('/')
  else:
    form = ModelBookForms(instance=book)
  return render(request,'editbook.html',{'form':form})
#Email",widget=forms.EmailInput(attrs=
 #    {'placeholder':'ac@mail.com','class':'form-control'}))