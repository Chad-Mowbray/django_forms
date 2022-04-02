from django.urls import reverse
from django.shortcuts import redirect, render
from .models import Ad
from .form import AdForm

def all_ads(request):
    ads = Ad.objects.all()
    context = {
        "ads": ads
    }
    return render(request, "ads/all.html", context)


def create_ad(request):
    if request.method == "GET":
        form = AdForm()
        return render(request, "ads/new.html", {"form":form})
    if request.method == "POST":
        form = AdForm(request.POST)
        if form.is_valid():
            form.save()
            # title = form.cleaned_data["title"]
            # content = form.cleaned_data["content"]
            # Ad.objects.create(title=title, content=content)
            return redirect(reverse("all_ads"))