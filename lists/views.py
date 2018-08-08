from django.shortcuts import redirect,render
from django.http import HttpResponse
from lists.models import Item
# Create your views here.
#home_page = None
def home_page(request):
    if request.mothod == 'POST':
        Item.objects.create(text=request.POST['item_text'])
        return redirect('/')

    return render(request, 'home.html')
