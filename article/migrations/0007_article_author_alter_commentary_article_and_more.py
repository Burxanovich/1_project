# Generated by Django 5.0.1 on 2024-01-23 13:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0006_content_boolean_field'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='author',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='article.author'),
        ),
        migrations.AlterField(
            model_name='commentary',
            name='article',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='article.article'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='content',
            name='article',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contents', to='article.article'),
        ),
    ]
