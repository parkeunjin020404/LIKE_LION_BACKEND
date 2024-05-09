# Generated by Django 5.0.4 on 2024-05-08 12:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0005_comment_post_alter_comment_content'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='content',
            new_name='comment',
        ),
        migrations.AddField(
            model_name='comment',
            name='created_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='board.community'),
        ),
    ]