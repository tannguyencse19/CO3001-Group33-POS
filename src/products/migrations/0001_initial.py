# Generated by Django 3.2.8 on 2021-10-17 12:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('phone', models.IntegerField()),
                ('email', models.CharField(blank=True, db_column='Email', max_length=20, null=True)),
                ('level', models.CharField(blank=True, db_column='Level', default='Đồng', max_length=8)),
                ('totalorder', models.IntegerField(blank=True, db_column='TotalOrder', default=0)),
                ('totalpay', models.IntegerField(blank=True, db_column='TotalPay', default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_column='Name', max_length=10, unique=True)),
                ('num_size', models.IntegerField(blank=True, db_column='Num_Size', default=1)),
                ('remain', models.FloatField(default=100)),
                ('price', models.IntegerField(db_column='Price')),
            ],
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=10, null=True)),
                ('username', models.CharField(max_length=10, unique=True)),
                ('password', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.IntegerField(blank=True, default=0)),
                ('reserve', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='products.customer')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('starttime', models.DateTimeField(blank=True, null=True)),
                ('endtime', models.DateTimeField(blank=True, null=True)),
                ('note', models.CharField(blank=True, max_length=20, null=True)),
                ('status', models.IntegerField(blank=True, default=0)),
                ('totalprice', models.IntegerField(blank=True, default=0)),
                ('id_cus', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.customer')),
                ('id_place', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.place')),
            ],
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('evaluate', models.IntegerField()),
                ('comment', models.CharField(blank=True, db_column='Comment', max_length=20, null=True)),
                ('id_cus', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.customer')),
                ('id_order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.order')),
            ],
        ),
        migrations.CreateModel(
            name='Food_Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.IntegerField(blank=True, default=1)),
                ('quantity', models.IntegerField(blank=True, default=1)),
                ('id_food', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='products.food')),
                ('id_order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.order')),
            ],
            options={
                'unique_together': {('id_food', 'id_order')},
            },
        ),
    ]
