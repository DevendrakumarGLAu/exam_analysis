from django.db import models

class Exam(models.Model):
    exam_name = models.CharField(max_length=100)
    exam_date = models.DateField()
    total_marks = models.IntegerField()

    def __str__(self):
        return self.exam_name

    class Meta:
        db_table = 'my_exam_table'  # Custom table name
