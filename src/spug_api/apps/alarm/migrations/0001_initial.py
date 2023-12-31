# Generated by Django 3.2.20 on 2023-07-17 17:59

from django.db import migrations, models
import django.db.models.deletion
import libs.mixins
import libs.utils


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Alarm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('type', models.CharField(max_length=50)),
                ('target', models.CharField(max_length=100)),
                ('notify_mode', models.CharField(max_length=255)),
                ('notify_grp', models.CharField(max_length=255)),
                ('status', models.CharField(choices=[('1', '报警发生'), ('2', '故障恢复')], max_length=2)),
                ('duration', models.CharField(max_length=50)),
                ('created_at', models.CharField(default=libs.utils.human_datetime, max_length=20)),
            ],
            options={
                'db_table': 'alarms',
                'ordering': ('-id',),
            },
            bases=(models.Model, libs.mixins.ModelMixin),
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('desc', models.CharField(max_length=255, null=True)),
                ('contacts', models.TextField(null=True)),
                ('created_at', models.CharField(default=libs.utils.human_datetime, max_length=20)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='+', to='account.user')),
            ],
            options={
                'db_table': 'alarm_groups',
                'ordering': ('-id',),
            },
            bases=(models.Model, libs.mixins.ModelMixin),
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=20, null=True)),
                ('email', models.CharField(max_length=255, null=True)),
                ('ding', models.CharField(max_length=255, null=True)),
                ('wx_token', models.CharField(max_length=255, null=True)),
                ('qy_wx', models.CharField(max_length=255, null=True)),
                ('created_at', models.CharField(default=libs.utils.human_datetime, max_length=20)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='+', to='account.user')),
            ],
            options={
                'db_table': 'alarm_contacts',
                'ordering': ('-id',),
            },
            bases=(models.Model, libs.mixins.ModelMixin),
        ),
    ]
