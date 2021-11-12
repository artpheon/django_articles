from django.shortcuts import render
from django.http import Http404, HttpResponseRedirect
from django.urls import reverse
from .models import Article, Comment

def index(request):
    latest_articles = Article.objects.order_by('-pub_date')[:5]
    return render(request, 'articles/list.html',
    {'latest_articles': latest_articles})

def detail(request, article_id):
    try:
        a = Article.objects.get(id = article_id)
        latest_comments = a.comment_set.order_by('-id')[:10]
        return render(request, 'articles/detail.html', {
            'article': a,
            'latest_comments': latest_comments
        })
    except:
        return Http404('Article not found')

def leave_comment(request, article_id):
    try:
        a = Article.objects.get( id = article_id)
        a.comment_set.create(author_name=request.POST['author_name'], comment_text=request.POST['comment_text'])
        return HttpResponseRedirect( reverse('articles:detail', args=(a.id,)) )
    except:
        return Http404('Article not found')
