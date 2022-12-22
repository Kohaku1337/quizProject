# Generated by Django 4.1.4 on 2022-12-22 18:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=4096)),
                ('visible', models.BooleanField(default=False)),
                ('max_points', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=4096)),
                ('points', models.FloatField()),
                ('lock_other', models.BooleanField(default=False)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='quiz.question')),
            ],
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('choice', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='quiz.choice')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='quiz.question')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
