from django.db import models

class Record(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    meet_subject = models.CharField(max_length=200)
    organizer = models.CharField(max_length=100)
    participants = models.TextField()
    meet_date = models.DateField(auto_now=True)
    start_time = models.TimeField(auto_now=True)
    end_time = models.TimeField(auto_now=True)
   

    def __str__(self):
        return(f"{self.meet_subject} {self.organizer}")
