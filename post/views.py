from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import ListView
from django.views.generic.edit import UpdateView
from .models import Post
from django.utils import timezone
from .forms import PostForm
# Create your views here.

class HomePageView(ListView):
    model = Post
    template_name='home.html'


def detail_view(request, id):
    item = get_object_or_404(Post, id=id)
    context = {
        'item' : item,
    }
    return render(request, 'detail.html', context)


def add_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.pub_date = timezone.now()
            post.save()
            return redirect('detail', id=post.id)
    else:
        form = PostForm
    context = {
        'form' : form,
    }
    return render(request,'addpost.html', context)

class PostUpdateView(UpdateView):
    model = Post
    template = 'post_edit.html'
    fields = [
        'title',
        'category',
        'content',
    ]