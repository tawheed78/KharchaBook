# Generated by Django 4.1.7 on 2023-03-14 11:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='expense',
            name='profile',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='expenses', to='home.profile'),
            preserve_default=False,
        ),
    ]
