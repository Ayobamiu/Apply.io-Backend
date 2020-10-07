from django.db import models
from user.models import User
from competition.models import Competition

STATUS_CHOICES = [ ('qualified', 'Qualified'),
('disqualified', 'Disqualified'),
('winner', 'Winner'),
]

class Entry(models.Model):
    first_name = models.CharField(max_length=100 , blank=True, null=True )
    last_name = models.CharField(max_length=100 , blank=True, null=True )
    applicant = models.ForeignKey(User, on_delete=models.CASCADE)
    file = models.FileField()
    status = models.CharField(max_length=100, blank=True, null=True, choices=STATUS_CHOICES )
    allowed = models.BooleanField(default=True)
    competition = models.ForeignKey(Competition,on_delete=models.CASCADE, blank=True, null=True )
    
    def __str__(self):
        return self.first_name + self.last_name