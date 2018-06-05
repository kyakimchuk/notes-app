from django.db import models


class Note(models.Model):
    note_text = models.TextField(verbose_name='Заметка')

    # def __str__(self):
    #     return self.name
