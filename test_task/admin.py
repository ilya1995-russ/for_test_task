from django.contrib import admin
from test_task.models import AuthorUser, Article

admin.site.register(AuthorUser)
admin.site.register(Article)
