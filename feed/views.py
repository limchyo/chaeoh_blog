from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Article, Hashtag, Comment

# Create your views here.
def index(request):
    category = request.GET.get("category")
    hashtag = request.GET.get("hashtag")
    # request.GET은 queryDict 전체를 호출
    # request.GET.get("파라미터")는 해당 값을 가져온다
    # url을 통해 category의 값을 가져온다.

    # article_list = Article.objects.all()
    hashtag_list = Hashtag.objects.all()

    if not category and not hashtag:
        article_list = Article.objects.all()
    elif category:
        article_list = Article.objects.filter(category=category)
    else:
        article_list = Article.objects.filter(hashtag__hashtag=hashtag)

    category_list = set([
        (article.category, article.get_category_display())
        for article in article_list
    ])

    ctx = {
        "article_list" : article_list,
        "hashtag_list" : hashtag_list,
        "category_list" : category_list,
    }
    return render(request, "index.html", ctx)

def detail(request, article_id):
    article_all = Article.objects.all()
    article_detail = Article.objects.get(id=article_id)
    # comment_list = article_detail.article_comments.all()
    category_list = set([
        (article.category, article.get_category_display())
        for article in article_all
    ])
    hashtag_list = Hashtag.objects.all()

    ctx = {
        "article_detail" : article_detail,
        # "comment_list" : comment_list,
        "hashtag_list" : hashtag_list,
        "category_list" : category_list,
    }

    if request.method == "GET":
        pass

    elif request.method == "POST":
        username = request.POST.get("username")
        content = request.POST.get("content")
        Comment.objects.create(
            article=article_detail,
            username=username,
            content=content,
        )

        return HttpResponseRedirect("/{}/".format(article_id))



    return render(request, "detail.html", ctx)

def about(request):
    ctx = {}
    return render(request, "about.html", ctx)
