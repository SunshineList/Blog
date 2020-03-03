from django.shortcuts import render
from . import models


# 主页
def Blog_index(request):
    articles = models.Article.objects.all()
    return render(request, "blog/index.html", {'articles': articles})


# Blog Content
def article_page(request, article_id):
    article = models.Article.objects.get(pk=article_id)
    all_article = models.Article.objects.all()
    previous = None
    next = None
    for index, article_1 in enumerate(all_article):
        if index == 0:
            previous_index = 0
            next_index = index + 1
        elif index == len(all_article) - 1:
            previous_index = index - 1
            next_index = index
        else:
            previous_index = index - 1
            next_index = index + 1
        if str(article_1.id) == str(article_id):
            previous = all_article[previous_index]
            next = all_article[next_index]
            break

    return render(request, "blog/blog_page.html", {'article': article,
                                                   'previous': previous,
                                                   'next': next})


# Edit Blog
def edit_page(request, article_id):
    if str(article_id) == '0':
        return render(request, "blog/edit_page.html")
    else:
        article = models.Article.objects.get(pk=article_id)
        return render(request, "blog/edit_page.html", {'article': article})


# 撰写博客
def edit_action(request):
    title = request.POST.get('title', 'TITLE')
    content = request.POST.get('content', 'CONTENT')
    article_id = request.POST.get('acticle_id', '0')
    if article_id == '0':
        models.Article.objects.create(title=title, content=content)
        articles = models.Article.objects.all()
        return render(request, "blog/index.html", {'articles': articles})
    else:
        article = models.Article.objects.get(pk=article_id)
        article.title = title
        article.content = content
        article.save()
        return render(request, "blog/blog_page.html", {'article': article})


# 删除博客
def del_page(request, article_id):
    models.Article.objects.get(pk=article_id).delete()
    return render(request, "blog/Del_page.html")
