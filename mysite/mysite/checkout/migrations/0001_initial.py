# Generated by Django 3.2.2 on 2021-05-29 10:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('product', '0002_productvar'),
    ]

    operations = [
        migrations.CreateModel(
            name='Checkout',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='CheckoutLine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField()),
                ('checkout', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lines', to='checkout.checkout')),
                ('variant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.productvariant')),
            ],
        ),
    ]
