from django.contrib import admin
from .models import Post

# register our models so they appear on admin page

admin.site.register(Post)
