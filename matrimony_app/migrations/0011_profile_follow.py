# Generated by Django 4.2.2 on 2023-07-27 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('matrimony_app', '0010_alter_interest_interested'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='follow',
            field=models.ManyToManyField(blank=True, related_name='interested_by', to='matrimony_app.profile'),
        ),
    ]
