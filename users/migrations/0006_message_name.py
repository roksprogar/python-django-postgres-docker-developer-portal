# Generated by Django 4.1.3 on 2022-11-16 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_rename_name_message_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='name',
            field=models.CharField(blank=True, default='Rok Sprogar', max_length=200, null=True),
        ),
    ]
