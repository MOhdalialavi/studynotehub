# Generated by Django 4.2.5 on 2023-10-13 17:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0008_rename_notes_hashtablenotes_note'),
    ]

    operations = [
        migrations.RenameField(
            model_name='hashtablenotes',
            old_name='namehash',
            new_name='not_id',
        ),
        migrations.RenameField(
            model_name='hashtablesyllabus',
            old_name='namehash',
            new_name='syl_id',
        ),
    ]
