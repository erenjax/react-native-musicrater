# Generated by Django 4.0.3 on 2022-03-11 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musicrater', '0006_alter_rating_username_delete_artist'),
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('album', models.CharField(max_length=100)),
                ('yearPublished', models.IntegerField()),
                ('artist', models.CharField(max_length=100)),
                ('awards', models.CharField(max_length=200)),
                ('genre', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('artist', models.CharField(max_length=100)),
                ('song', models.CharField(max_length=100)),
                ('album', models.CharField(max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='Question',
        ),
        migrations.AddField(
            model_name='rating',
            name='billboardranking',
            field=models.IntegerField(default=-1),
            preserve_default=False,
        ),
    ]
