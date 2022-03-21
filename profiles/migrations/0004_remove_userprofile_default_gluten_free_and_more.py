# Generated by Django 4.0.2 on 2022-03-16 08:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('profiles', '0003_userprofile_default_country'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='default_gluten_free',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='default_nut_free',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='default_vegan',
        ),
        migrations.CreateModel(
            name='UserPreferences',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('default_gluten_free', models.BooleanField(default=False)),
                ('default_nut_free', models.BooleanField(default=False)),
                ('default_vegan', models.BooleanField(default=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]