from django.shortcuts import render


def gallery(request):
    template_name = 'gallery/gallery.html'

    return render(request, template_name)
