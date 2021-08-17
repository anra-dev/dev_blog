from django.db import models
from django.contrib.contenttypes.fields import GenericRelation
from django.contrib.auth import get_user_model

User = get_user_model()


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=100, unique=True)

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'
        ordering = ('name',)

    def __str__(self):
        return self.name


class PostQuerySet(models.QuerySet):
    def active(self):
        return self.filter(status__in=[Post.STATUS_PUBLISHED, Post.STATUS_ARCHIVED])

    def published(self):
        return self.filter(status=Post.STATUS_PUBLISHED)


class Post(models.Model):
    STATUS_DRAFT = 1
    STATUS_PUBLISHED = 2
    STATUS_ARCHIVED = 3
    STATUSES = (
        (STATUS_DRAFT, 'Draft'),
        (STATUS_PUBLISHED, 'Published'),
        (STATUS_ARCHIVED, 'Archived'),
    )

    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор')
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    slug = models.SlugField()
    body = models.TextField(verbose_name='Содержимое поста')
    snippet = models.TextField(verbose_name='Краткое содержание')
    banner = models.ImageField(upload_to='uploads/%Y/%m/%d/', verbose_name='Картинка-баннер', blank=True)
    preview = models.ImageField(upload_to='uploads/%Y/%m/%d/', verbose_name='Картинка-превью', blank=True)
    tags = models.ManyToManyField(Tag, verbose_name='Теги', blank=True)
    status = models.SmallIntegerField(verbose_name='Статус', choices=STATUSES)
    created_at = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='Дата изменения', auto_now=True)
    published_at = models.DateTimeField(verbose_name='Дата публикации', blank=True, null=True)
    comments = GenericRelation('comments.Comment')

    objects = PostQuerySet.as_manager()

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
        ordering = ('-created_at',)

    def __str__(self):
        return self.title

