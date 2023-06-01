# Generated by Django 4.2.1 on 2023-05-31 22:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='trainee_info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trainee_name', models.CharField(max_length=20)),
                ('trainee_email', models.EmailField(max_length=100)),
                ('password', models.CharField(max_length=16)),
            ],
        ),
    ]
