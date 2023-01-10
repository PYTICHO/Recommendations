# Generated by Django 4.1.3 on 2022-12-22 23:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testApp', '0005_remove_tovars_idtov_tovars_iddoc_tovars_kolvo_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tovars',
            options={'ordering': ('id',), 'verbose_name': 'Товар', 'verbose_name_plural': 'Товары'},
        ),
        migrations.RemoveField(
            model_name='tovars',
            name='iddoc',
        ),
        migrations.RemoveField(
            model_name='tovars',
            name='kolvo',
        ),
        migrations.RemoveField(
            model_name='tovars',
            name='summa',
        ),
        migrations.AddField(
            model_name='tovars',
            name='idtov',
            field=models.CharField(default='default', max_length=30, verbose_name='ID товара'),
        ),
        migrations.AlterField(
            model_name='tovars',
            name='name',
            field=models.CharField(default='default', max_length=400, verbose_name='Название товара'),
        ),
        migrations.CreateModel(
            name='Checks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('iddoc', models.CharField(max_length=30, verbose_name='Id Чека')),
                ('createtime', models.DateTimeField(auto_now_add=True, verbose_name='Дата')),
                ('tovars', models.ManyToManyField(to='testApp.tovars', verbose_name='Товары в чеке')),
            ],
            options={
                'verbose_name': 'Чек',
                'verbose_name_plural': 'Чеки',
                'ordering': ('createtime', 'id'),
            },
        ),
    ]
