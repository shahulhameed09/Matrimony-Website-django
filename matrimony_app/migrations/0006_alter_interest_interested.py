# Generated by Django 4.2.2 on 2023-07-22 07:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('matrimony_app', '0005_interest'),
    ]

    operations = [
        migrations.AlterField(
            model_name='interest',
            name='interested',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='matrimony_app.profile'),
        ),
    ]
