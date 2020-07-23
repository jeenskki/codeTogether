from django.contrib import admin
# from .models import Answer


class BoardAdmin(admin.ModelAdmin):
    list_display = ('title', 'writer', )

# admin.site.register(Board, BoardAdmin)


#admin화면에서 나타나는 게시판 목록
# 게시판 목록은 제목과 작성자가 나타남
