from django.db.models import Q
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post
# Create your views here.


def index(request):
    posts = Post.objects.all()
    context = {'posts':posts}
    return render(request, 'index.html', context)


class ProductDetailView(DetailView):
    model = Post
    template_name = 'detail.html'


class ProductSearchView(ListView):
    model = Post
    paginate_by = 4
    template_name = 'search.html'
    context_object_name = 'posts'

    def get_queryset(self):
        queryset = Post.objects.all()
        query_obj = self.request.GET.get('key')
        if query_obj:
            queryset = Post.objects.filter(
                Q(title__icontains=query_obj) | Q(course__icontains=query_obj)
            )
        return queryset
