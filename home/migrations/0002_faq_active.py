# Generated by Django 3.2 on 2023-03-19 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='faq',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]
