from django.db import models


class Category(models.Model):
    category_name = models.CharField(
        'Category',
        null=True,
        blank=True,
        max_length=50
    )

    def __str__(self):
        return self.category_name

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class Note(models.Model):
    category = models.ForeignKey(
        Category,
        null=True,
        blank=True,
        related_name='category_to_note',
        on_delete=models.PROTECT
    )

    note_body = models.TextField(
        'Note',
        null=False,
        blank=False
    )

    created_date = models.DateTimeField(
        "Created",
        auto_now=False,
        auto_now_add=True
    )

    updated_date = models.DateTimeField(
        "Updated",
        auto_now=True,
        auto_now_add=False
    )

    def __str__(self):
        return "Note № %s" % self.pk

    class Meta:
        verbose_name = 'Note'
        verbose_name_plural = 'Notes'
