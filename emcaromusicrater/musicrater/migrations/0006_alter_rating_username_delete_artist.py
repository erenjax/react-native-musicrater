# Generated by Django 4.0.3 on 2022-03-11 06:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musicrater', '0005_question'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rating',
            name='username',
            field=models.CharField(max_length=100),
        ),
        migrations.DeleteModel(
            name='Artist',
        ),
    ]
