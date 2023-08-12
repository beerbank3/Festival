# Generated by Django 4.2.2 on 2023-08-11 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Festival',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contentid', models.CharField(max_length=10)),
                ('contenttypeid', models.CharField(max_length=2)),
                ('title', models.CharField(max_length=200)),
                ('createdtime', models.CharField(max_length=14)),
                ('modifiedtime', models.CharField(max_length=14)),
                ('tel', models.CharField(max_length=20)),
                ('telname', models.CharField(max_length=50)),
                ('homepage', models.URLField()),
                ('booktour', models.TextField(blank=True)),
                ('firstimage', models.URLField()),
                ('firstimage2', models.URLField()),
                ('cpyrhtDivCd', models.CharField(max_length=10)),
                ('areacode', models.CharField(max_length=5)),
                ('sigungucode', models.CharField(max_length=5)),
                ('cat1', models.CharField(max_length=10)),
                ('cat2', models.CharField(max_length=10)),
                ('cat3', models.CharField(max_length=10)),
                ('addr1', models.CharField(max_length=200)),
                ('addr2', models.CharField(max_length=100)),
                ('zipcode', models.CharField(max_length=10)),
                ('mapx', models.CharField(max_length=20)),
                ('mapy', models.CharField(max_length=20)),
                ('mlevel', models.CharField(max_length=2)),
                ('overview', models.TextField()),
            ],
        ),
    ]
