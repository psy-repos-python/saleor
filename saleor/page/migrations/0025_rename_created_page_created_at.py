# Generated by Django 3.2.12 on 2022-04-14 10:25

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("page", "0024_alter_pagetranslation_language_code"),
    ]

    operations = [
        migrations.RenameField(
            model_name="page",
            old_name="created",
            new_name="created_at",
        ),
    ]
