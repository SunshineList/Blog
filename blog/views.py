from django.shortcuts import render
from .models import Article
from django.contrib.auth.decorators import login_required


# 主页
def Blog_index(request):
    articles = Article.objects.all()
    return render(request, "blog/index.html", {'articles': articles})


# Blog Content
def article_page(request, article_id):
    article = Article.objects.get(pk=article_id)
    all_article = Article.objects.all()
    previous = None
    next = None
    for index, article_1 in enumerate(all_article):
        if index == 0:
            previous_index = 0
            next_index = index
        elif index == len(all_article) - 1:
            previous_index = index - 1
            next_index = index
        else:
            previous_index = index - 1
            next_index = index + 1
        if str(article_1.id) == str(article_id):
            previous = all_article[previous_index]
            next = all_article[next_index]

    return render(request, "blog/blog_page.html", {'article': article,
                                                   'previous': previous,
                                                   'next': next})


# Edit Blog
def edit_page(request, article_id):
    if str(article_id) == '0':
        return render(request, "blog/edit_page.html")
    else:
        article = Article.objects.get(pk=article_id)
        return render(request, "blog/edit_page.html", {'article': article})


# 撰写博客
def edit_action(request):
    title = request.POST.get('title')
    content = request.POST.get('content')
    article_id = request.POST.get('article_id')
    if article_id == '0':
        Article.objects.create(title=title, content=content, author=None)
        articles = Article.objects.all()
        return render(request, "blog/index.html", {'articles': articles})
    else:
        article = Article.objects.get(pk=article_id)
        article.title = title
        article.content = content
        article.save()
        return render(request, "blog/blog_page.html", {'article': article})


# 删除博客
def del_page(request, article_id):
    Article.objects.get(pk=article_id).delete()
    return render(request, "blog/Del_page.html")
