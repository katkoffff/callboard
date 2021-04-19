from django_filters import FilterSet
from .models import Post

class NewsFilter(FilterSet):
    class Meta:
        model = Post
        fields = {
            'to_author': ['exact'],
            'create_post': ['lt'],
                }
