# -*- coding: utf-8 -*-


import sys

from django.db import migrations, models

from cl.lib.migration_utils import load_migration_fixture


def load_fixture(apps, schema_editor):
    # Every time tests are run, the migrations are applied, importing this
    # data. Because the standard school data has more than 6,000 items, it
    # takes too long to import, and instead we import a miniature version.
    fixture = 'school_data_truncated' if 'test' in sys.argv else 'schools_data'
    load_migration_fixture(apps, schema_editor, fixture, 'people_db')

    # Do races
    load_migration_fixture(apps, schema_editor, 'races', 'people_db')


def unload_fixture(apps, schema_editor):
    """Delete everything"""
    SchoolModel = apps.get_model("people_db", "School")
    SchoolModel.objects.all().delete()

    RaceModel = apps.get_model('people_db', 'Race')
    RaceModel.objects.all().delete()


class Migration(migrations.Migration):
    dependencies = [
        ('people_db', '0002_initial_part_two'),
    ]

    operations = [
        migrations.RunPython(load_fixture, reverse_code=unload_fixture),
    ]

