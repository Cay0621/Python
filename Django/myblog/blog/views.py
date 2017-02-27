from django.shortcuts import render
from django.http import HttpResponse

from . import models

# Create your views here.
# 每一个响应对应一个函数，函数必须返回一个响应
# 函数必须存在一个参数，一般约定为request
# 每个函数对应一个url
def index(request):
    # return HttpResponse("Hello world!")
    # 第三个参数为传给前端页面的数值
    
    # 获取主键为1的对象
    # article = models.Article.objects.get(pk = 1)
    # return render(request, 'blog/index.html', {'hello': 'Hello Blog!','article' : article})
    
    # 获取所有的article列表
    articles = models.Article.objects.all()
    return render(request, 'blog/index.html', {'articles' : articles})
    
    
def article_page(request, article_id):
    article = models.Article.objects.get(pk=article_id)
    return render(request, 'blog/article_page.html', {'article':article})

def edit_page(request, article_id):
    if str(article_id) == '0':
        return render(request, 'blog/edit_page.html')
    
    article = models.Article.objects.get(pk=article_id)
    return render(request, 'blog/edit_page.html', {'article':article})

def edit_action(request):
    # title = request.POST['title']
    # 为了防止request请求中没有title的请求参数，建议使用以下代码
    title = request.POST.get('title', 'TITLE')
    content = request.POST.get('content', 'CONTENT')
    article_id = request.POST.get('article_id', '0')
    if article_id == '0':
        # 返回主页
        models.Article.objects.create(title=title, content=content)
        articles = models.Article.objects.all()
        return render(request, 'blog/index.html', {'articles' : articles})
    
    else:
        article = models.Article.objects.get(pk = article_id)
        article.title = title
        article.content = content
        article.save()
        return render(request, 'blog/article_page.html', {'article':article})
    