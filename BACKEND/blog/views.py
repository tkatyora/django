from django.shortcuts import render

# Create your views here.
def currentBlog(request):
    return render(request, 'blog.html')

def oldBlog(request):
    return render(request, 'oldBlogs.html')


def mostLikedBlog(request):
    return render(request, 'mostLikedBlog.html')