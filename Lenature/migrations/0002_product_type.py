# Generated by Django 5.1.3 on 2025-02-03 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Lenature', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='type',
            field=models.CharField(choices=[('face', 'Face'), ('body', 'Body')], default='face', max_length=20),
        ),
    ]
