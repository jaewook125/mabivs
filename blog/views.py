from blog.models import Post, Notice, Comment
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.http import HttpResponse
from .forms import PostForm, CommentForm
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def prologue(request):
    return render(request, 'blog/prologue.html', {})


@login_required
def post_list(request):
    qs = Post.objects.all().order_by('-id').prefetch_related('tag_set')

    q = request.GET.get('q', '')
    if q:
        qs = qs.filter(title__icontains=q)

    paginator = Paginator(qs, 10)
    page = request.GET.get('page',1)
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

@login_required
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    form = CommentForm(request.POST or None)

    post.count += 1
    post.save()
    if form.is_valid():
        comment = form.save(commit=False)
        comment.author = request.user
        comment.post = post
        comment.save()
        messages.success(request, '댓글이 작성 됐습니다.')
        return redirect(request.path)
    return render(request, 'blog/post_detail.html', {
                                    'post': post,
                                    'form': form,
                                    })

@login_required
def comment_delete(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    html = "<html><body>다른 사용자의 덧글입니다.</body></html>"
    if comment.author != request.user:
        return HttpResponse(html)
    comment.delete()
    messages.success(request, '댓글을 삭제 했습니다.')
    return render(request, 'blog/comment_delete.html', {'comment': comment})

@login_required
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = Post(**form.cleaned_data)
            post.author = request.user
            post.save()
            messages.success(request, '새 포스팅을 저장했습니다.')
            return redirect(post)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form,})

@login_required
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if post.author != request.user:
        return redirect(post)
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = Post(**form.cleaned_data)
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


def notice_list(request):
    qs = Notice.objects.all().order_by('-id')

    q = request.GET.get('q', '')
    if q:
        qs = qs.filter(title__icontains=q)

    paginator = Paginator(qs, 10)
    page = request.GET.get('page',1)
    try:
        notice = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        notice = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        notice = paginator.page(paginator.num_pages)

    return render(request, 'blog/notice_list.html',{
        'notice_list' : qs,
        'notice' : notice,
    })


def notice_view(request, pk):
    notice = get_object_or_404(Notice, pk=pk)
    return render(request, 'blog/notice_view.html', {'notice': notice})


def comment_list(request):
    qs = Comment.objects.all().order_by('-id').select_related('post')

    paginator = Paginator(qs, 5)
    page = request.GET.get('page',1)
    try:
        comment = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        comment = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        comment = paginator.page(paginator.num_pages)
    return render(request, 'blog/post_detail.html',{
        'comment_list':qs,
        'comment':comment,
    })
