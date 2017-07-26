from django.contrib import admin
from blog.models import Post, Tag, Notice, Comment
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    list_display = ['id', 'author', 'title', 'tag_list' ,'content',
                    'image','created_at', 'updated_at']


    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.prefetch_related('tag_set')
        #어드민의 태그리스트 SQL을 없애주는 함수
    def tag_list(request,post):
        return ', '.join(tag.name for tag in post.tag_set.all()) #list comprehension 문법?

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['id', 'author','post_content_len','comment_content_len']

    def post_content_len(self,comment):
        return '{}글자'.format(len(comment.post.content))

    def comment_content_len(self,comment):
        return '{}글자'.format(len(comment.message))

    def get_queryset(self,request):
        qs = super().get_queryset(request)
        return qs.select_related('post')


@admin.register(Notice)
class NoticeAdmin(admin.ModelAdmin):
    list_display = ['id', 'author', 'title', 'content' ,'image', 'created_at','updated_at']

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['name']
