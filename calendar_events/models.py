from django.db import models

class Event(models.Model):
    name=models.CharField(max_length=300,null=False,blank=False)
    creator = models.ForeignKey("user.User",on_delete=models.CASCADE, related_name="creator")
    dt_time = models.DateTimeField(null=False,blank=False)
    guests = models.ManyToManyField(to="user.User", related_name="guests")

    def add_guest(self,guest):
        self.guests.add(guest)
        self.save()