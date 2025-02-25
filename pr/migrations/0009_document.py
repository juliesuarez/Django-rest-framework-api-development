# Generated by Django 4.2.7 on 2023-12-06 17:47

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("pr", "0008_course_staff_student_module"),
    ]

    operations = [
        migrations.CreateModel(
            name="Document",
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
                ("name", models.CharField(max_length=200)),
                ("file_type", models.FileField(upload_to="documents/")),
                ("uploaded_at", models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
