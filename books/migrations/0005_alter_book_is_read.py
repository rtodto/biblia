# Generated by Django 5.1.2 on 2024-10-23 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0004_alter_book_is_read'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='is_read',
            field=models.CharField(choices=[('yes', 'Yes'), ('no', 'No')], default='no', max_length=3, verbose_name='Finished'),
        ),
    ]
