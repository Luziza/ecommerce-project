# Generated by Django 5.1.3 on 2024-11-19 01:49

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produtos', '0004_avaliacao_usuario'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='avaliacao',
            name='rating',
        ),
        migrations.AddField(
            model_name='avaliacao',
            name='nota',
            field=models.IntegerField(choices=[(1, '1 estrela'), (2, '2 estrelas'), (3, '3 estrelas'), (4, '4 estrelas'), (5, '5 estrelas')], default=3),
        ),
        migrations.AlterField(
            model_name='avaliacao',
            name='comentario',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='avaliacao',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
