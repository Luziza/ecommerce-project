# Generated by Django 5.1.3 on 2024-11-19 02:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produtos', '0007_alter_avaliacao_unique_together'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='id',
        ),
        migrations.AddField(
            model_name='product',
            name='sku',
            field=models.CharField(default='default-sku', max_length=100, primary_key=True, serialize=False),
        ),
    ]
