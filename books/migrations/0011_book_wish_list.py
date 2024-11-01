# Generated by Django 5.1.2 on 2024-10-24 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0010_book_quantity'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='wish_list',
            field=models.CharField(choices=[('enabled', 'Enabled'), ('disabled', 'Disabled')], default='disabled', max_length=9),
        ),
    ]
