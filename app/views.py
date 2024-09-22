from django.shortcuts import render
from .models import image
from .forms import image_form

def image_upload(request):
    if request.method == "POST":
        form = image_form(request.POST,request.FILES)
        if form.is_valid():
            form.save()
    form = image_form()
    img= image.objects.all()
    return render(request,"home.html",{"img":img ,"form":form})