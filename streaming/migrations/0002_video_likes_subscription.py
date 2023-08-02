# Generated by Django 4.1.7 on 2023-03-16 08:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("streaming", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="video",
            name="likes",
            field=models.ManyToManyField(
                related_name="post_likes", to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.CreateModel(
            name="Subscription",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "auth",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "subscribed_to",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="streaming.video",
                    ),
                ),
            ],
        ),
    ]