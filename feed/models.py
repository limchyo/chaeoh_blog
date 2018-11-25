from django.db import models

# Create your models here.
class Hashtag(models.Model):
    hashtag = models.CharField(max_length=50)

    def __str__(self):
        return self.hashtag

class Article(models.Model):
    DEVELOPMNET = "dv"
    PERSONAL = "ps"
    CATEGORY_CHOICES = (
        (DEVELOPMNET, "development"),
        (PERSONAL, "personal"),
    )

    title = models.CharField(max_length=200)
    small_title = models.CharField(max_length=150, null=True)
    content = models.TextField()
    category = models.CharField(
        max_length=2,
        choices=CATEGORY_CHOICES,
        default=DEVELOPMNET,
    )

    hashtag = models.ManyToManyField(Hashtag)

    def __str__(self):
        return self.title

class Comment(models.Model):
    article = models.ForeignKey(
        Article,
        related_name="article_comments",
        on_delete=models.CASCADE
    )
    username = models.CharField(max_length=50)
    content = models.CharField(max_length=200)
    approved_comment = models.BooleanField(default=False)

    def __str__(self):
        return "({}) {}".format(self.article.title, self.content)
