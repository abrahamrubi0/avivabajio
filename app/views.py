from django.shortcuts import render


def conferencias(request):

    return render(request, 'app/conferencias_list.html')


def conferencia_view(request):

    return render(request, 'app/conferencia.html')


def blog_list(request):

    return render(request, 'app/blog_list.html')


def blog_view(request):

    return render(request, 'app/blog.html')

def contacto(request):

    return render(request, 'app/contact.html')

