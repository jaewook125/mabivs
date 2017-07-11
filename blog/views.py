from blog.models import Post
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .forms import PostForm
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def post_list(request):
    qs = Post.objects.all().order_by('-id').prefetch_related('tag_set')

    q = request.GET.get('q', '')
    if q:
        qs = qs.filter(title__icontains=q)

    paginator = Paginator(qs, 10)
    page = request.GET.get('page')
    try:
        post = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        post = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        post = paginator.page(paginator.num_pages)



    return render(request, 'blog/post_list.html',{
        'post_list' : qs,
        'post' : post,
    })


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

@login_required
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            messages.success(request, '새 포스팅을 저장했습니다.')
            return redirect(post)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

@login_required
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if post.author != request.user:
        return redirect(post)
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            messages.success(request, '포스팅을 수정 했습니다.')
            return redirect(post) # post.get_absolute_url() => post_detail
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})

@login_required
def post_delete(request, pk):
    post = Post.objects.get(pk=pk)
    if post.author != request.user:
        return redirect(post)
    post.delete()
    messages.success(request, '포스팅을 삭제 했습니다.')
    return render(request, 'blog/post_delete.html', {'post': post})


# def comment_list(request):
#     comment_list = Comment.objects.all().select_related('post')
#     return render(request, 'blog/comment_list.html',{
#         'comment_list':comment_list,
#     })
