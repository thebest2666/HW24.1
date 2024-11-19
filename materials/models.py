from django.db import models


class Course(models.Model):
    """
    Модель курса
    """
    title = models.CharField(max_length=200, verbose_name='Название курса')
    description = models.TextField(verbose_name='Описание курса')
    preview = models.ImageField(upload_to='courses', null=True, blank=True, verbose_name='Превью курса')

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'

    def __str__(self):
        return f'{self.title}'


class Lesson(models.Model):
    """
    Модель урока
    """
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='lessons', verbose_name='Курс')
    title = models.CharField(max_length=200, verbose_name='Название урока')
    description = models.TextField(verbose_name='Описание урока')
    video_url = models.CharField(max_length=250, null=True, blank=True, verbose_name='Ссылка на видео')
    preview = models.ImageField(upload_to='lessons', null=True, blank=True, verbose_name='Превью урока')

    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'

    def __str__(self):
        return f'{self.title}'
