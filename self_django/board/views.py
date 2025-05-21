from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from .forms import PostForm


def Post_list(request): # read
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'board/post_list.html', {'posts' : posts})

def Post_detail(request, pk): # deep read zz
    post = get_object_or_404(Post, pk = pk)
    return render(request, 'board/post_detail.html', {'post' : post})

def Post_create(request): # create 
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('post_list')
        
    else:
        form = PostForm()
    return render(request, 'board/post_form.html', {'form' : form})

def Post_edit(request, pk):
    post = get_object_or_404(Post, pk = pk)
    if request.method == 'POST':
        form = PostForm(request.POST, instance= post) # instance = post <- 기존 게시물을 수정하겠다는 의미
        if form.is_valid():
            form.save()
            return redirect('post_detail', pk = post.pk)
        
    else: 
        form = PostForm(instance= post) #get 요청이면 원래있던거 보여주기
    return render(request, 'board/post_form.html', {'form' : form})

def post_delete(request, pk):
    post = get_object_or_404(Post, pk = pk)
    if request.method == 'POST':# get 요청으로 삭제되면 안되니까
        post.delete()
        return redirect('post_list') 

    return redirect('post_detail', pk=pk)
