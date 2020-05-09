from django.shortcuts import render
from django.utils import timezone
from .models import Post, Category
from django.views import generic  # 追記
from django.shortcuts import render, get_object_or_404

def post_list(request):
    posts = Post.objects.order_by('published_date')
    allcategory = Category.objects.all()
    categories = Category.objects.all()
    return render(request, 'blog/post_list.html', {'allcategory': allcategory, 'posts': posts, 'categories': categories})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def category(request, category):
    allcategory = Category.objects.all()
    category = Category.objects.get(name=category)
    post = Post.objects.filter(category=category)
    return render(request, 'blog/post_list.html',
                   {'allcategory': allcategory, 'category': category, 'posts': post})



# class IndexView(generic.ListView):
#     model = Post
#     template_name = 'blog/post_list.html'
#     def get_queryset(self):
#         queryset = Post.objects.order_by('-id')
#         return queryset



# class CategoryView(generic.ListView):
#     model = Post
#     template_name = 'blog/post_list.html'
#     def get_queryset(self):
#         category = Category.objects.get(name=self.kwargs['category'])
#         queryset = Post.objects.order_by('-id').filter(category=category)
#         return queryset
#     """ アクセスされた値を取得し辞書に格納 """
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['category_key'] = self.kwargs['category']
#         return context