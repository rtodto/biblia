# Generated by Django 5.1.2 on 2024-10-23 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='summary',
            field=models.TextField(default='No summary'),
        ),
    ]
