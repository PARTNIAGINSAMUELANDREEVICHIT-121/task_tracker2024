from django.db import models

class Task(models.Model):
    LOW = 'Низкий'
    MEDIUM = 'Средний'
    HIGH = 'Высокий'

    PRIORITY_CHOICES = [
        (LOW, 'Низкий'),
        (MEDIUM, 'Средний'),
        (HIGH, 'Высокий'),
    ]

    NEW = 'Новая'
    IN_PROGRESS = 'В прогрессе'
    DONE = 'Выполнено'
    CANCELED = 'Отменено'
    POSTPONED = 'Отложено'

    STATUS_CHOICES = [
        (NEW, 'Новая'),
        (IN_PROGRESS, 'В прогрессе'),
        (DONE, 'Выполнено'),
        (CANCELED, 'Отменено'),
        (POSTPONED, 'Отложено'),
    ]

    title = models.CharField(max_length=100)
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES, default=LOW)
    priority_color = models.CharField(max_length=20, default='black')  # Добавлено поле для цвета приоритета
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=NEW)
    status_color = models.CharField(max_length=20, default='black')  # Добавлено поле для цвета статуса

    def __str__(self):
        return self.title