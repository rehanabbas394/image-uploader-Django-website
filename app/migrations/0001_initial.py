# Generated by Django 5.0.2 on 2024-06-01 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='my_image')),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
