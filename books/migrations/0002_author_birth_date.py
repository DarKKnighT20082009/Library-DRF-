# Generated by Django 5.0.4 on 2024-04-25 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='birth_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]