# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-10 15:23
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0015_add_receipt_to_reimbursement'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='reimbursement',
            options={'ordering': ['-issue_date']},
        ),
    ]
