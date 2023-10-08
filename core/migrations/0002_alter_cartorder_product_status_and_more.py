# Generated by Django 4.1.7 on 2023-10-03 22:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartorder',
            name='product_status',
            field=models.CharField(choices=[('procrss', 'Processing'), ('shipped', 'Shipped'), ('delivered', 'Delivered')], default='processing', max_length=30),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_status',
            field=models.CharField(choices=[('in_review', 'In_Review'), ('draft', 'Draft'), ('rejected', 'Rejected'), ('published', 'Published'), ('disabled', 'Disabled')], default='in_review', max_length=10),
        ),
        migrations.AlterField(
            model_name='productreview',
            name='rating',
            field=models.IntegerField(choices=[(3, '★★★☆☆'), (5, '★★★★★'), (1, '★☆☆☆☆'), (2, '★★☆☆☆'), (4, '★★★★☆')], default=None),
        ),
    ]