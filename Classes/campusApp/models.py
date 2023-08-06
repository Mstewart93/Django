from django.db import models

# Create your models here.
class UniversityCampus(models.Model):
    Name = models.CharField(max_length=60, default="",blank=True,null=False)
    State = models.CharField(max_length=2,default="",blank=True,null=False)
    Campus_ID= models.IntegerField(default="",blank=True,null=False)
    class Meta:
        verbose_name_plural = "University Campus"
    def __str__(self):
    #returns input value of the title and instructor name
    #feild as a tuple to display in the browser instead of the defautl title
        display_campus = '{0.Name}: {0.State}'
        return display_campus.format(self)

#create model manager
object = models.Manager()
 #display the name without the extra s, 

    