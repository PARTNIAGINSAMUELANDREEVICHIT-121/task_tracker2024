# Generated by Django 5.0.2 on 2024-03-04 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task_tracker', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='priority_color',
            field=models.CharField(default='black', max_length=20),
        ),
        migrations.AddField(
            model_name='task',
            name='status_color',
            field=models.CharField(default='black', max_length=20),
        ),
        migrations.AlterField(
            model_name='task',
            name='priority',
            field=models.CharField(choices=[('Низкий', 'Низкий'), ('Средний', 'Средний'), ('Высокий', 'Высокий')], default='Низкий', max_length=10),
        ),
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.CharField(choices=[('Новая', 'Новая'), ('В прогрессе', 'В прогрессе'), ('Выполнено', 'Выполнено'), ('Отменено', 'Отменено'), ('Отложено', 'Отложено')], default='Новая', max_length=20),
        ),
    ]
