from django.shortcuts import render
from imageuploaderapp.forms import ImageForm
from imageuploaderapp.models import ImageUploader

# Create your views here.


def homepage(request):
    if request.method == "POST":
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    img_form = ImageForm()
    all_img = ImageUploader.objects.all()
    return render(request, 'home.html', {'image_form': img_form,
                                         'images': all_img})
