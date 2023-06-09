from django.db import models

# Create your models here.
class ToDo(models.Model):
    title = models.CharField(
        verbose_name ='Название',
        max_length=200,
    )
    complited = models.BooleanField(
        verbose_name='Выполненно ли',
        default=False
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    deadline = models.DateTimeField(
        verbose_name='Крайний срок'
    )

    def __str__(self) -> str:
        return self.title

#Миграции - ситема контроля версий в базе данных