# Generated by Django 4.2.9 on 2024-02-11 11:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0001_initial"),
        ("main", "0003_course_code_alter_course_id"),
    ]

    operations = [
        migrations.CreateModel(
            name="Query",
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
                ("title", models.CharField(default="", max_length=200)),
                (
                    "description",
                    models.TextField(
                        blank=True, default="", max_length=1000, null=True
                    ),
                ),
                (
                    "resolution_status",
                    models.CharField(
                        choices=[
                            ("PENDING", "Pending"),
                            ("IN_PROGRESS", "In Progress"),
                            ("DECLINED", "Declined"),
                            ("RESOLVED", "Resolved"),
                        ],
                        default="PENDING",
                        max_length=1000,
                    ),
                ),
                ("date_created", models.DateTimeField(auto_now_add=True, null=True)),
                ("date_updated", models.DateTimeField(auto_now=True, null=True)),
                (
                    "author",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="queries_author",
                        to="users.imuser",
                    ),
                ),
                (
                    "submitted_by",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="queries_submitted_by",
                        to="users.imuser",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="course",
            name="date_created",
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name="course",
            name="date_updated",
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name="course",
            name="code",
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.CreateModel(
            name="QueryComment",
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
                (
                    "comment",
                    models.TextField(
                        blank=True, default="", max_length=1000, null=True
                    ),
                ),
                ("date_created", models.DateTimeField(auto_now_add=True, null=True)),
                ("date_updated", models.DateTimeField(auto_now=True, null=True)),
                (
                    "author",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="comment_author",
                        to="users.imuser",
                    ),
                ),
                (
                    "query",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="comments_query",
                        to="main.query",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="ClassSchedule",
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
                ("title", models.CharField(default="", max_length=1000)),
                ("description", models.TextField(blank=True, default="", null=True)),
                ("start_date_and_time", models.DateTimeField(blank=True, null=True)),
                ("end_date_and_time", models.DateTimeField(blank=True, null=True)),
                ("is_repeated", models.BooleanField(default=False)),
                (
                    "repeat_frequency",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                ("is_active", models.BooleanField(default=True)),
                ("venue", models.CharField(max_length=100)),
                ("date_created", models.DateTimeField(auto_now_add=True, null=True)),
                ("date_updated", models.DateTimeField(auto_now=True, null=True)),
                (
                    "cohort",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="cohort_organizer",
                        to="users.cohort",
                    ),
                ),
                (
                    "course",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="classschedule_organizer",
                        to="main.course",
                    ),
                ),
                (
                    "organizer",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="classschedule_organizer",
                        to="users.imuser",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="ClassAttendance",
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
                ("is_present", models.BooleanField(default=False)),
                ("date_created", models.DateTimeField(auto_now_add=True, null=True)),
                ("date_updated", models.DateTimeField(auto_now=True, null=True)),
                (
                    "attendee",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="classattendance_member",
                        to="users.imuser",
                    ),
                ),
                (
                    "author",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="classattendance_author",
                        to="users.imuser",
                    ),
                ),
                (
                    "class_schedule",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="classattendance_classschedule",
                        to="main.classschedule",
                    ),
                ),
            ],
        ),
    ]