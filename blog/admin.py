from django.contrib import admin
from blog.models import Post, Tag

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'author', 'title', 'tag_list' ,'content',
                    'image','created_at', 'updated_at']


    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.prefetch_related('tag_set')
        #어드민의 태그리스트 SQL을 없애주는 함수
    def tag_list(request,post):
        return ', '.join(tag.name for tag in post.tag_set.all()) #list comprehension 문법?

# @admin.register(Comment)
# class CommentAdmin(admin.ModelAdmin):
#     list_display = ['id', 'author','post_content_len']
#
#     def post_content_len(self,comment):
#         return '{}글자'.format(len(comment.post.content))
#
#     def get_queryset(self,request):
#         qs = super().get_queryset(request)
#         return qs.select_related('post')


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['name']
