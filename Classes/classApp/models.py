from django.db import models

# Create your models here.
class UniversityClasses(models.Model):
    title= models.CharField(max_length=60, default="",blank=True,null=False)
    course_number= models.IntegerField(default="",blank=True,null=False)
    Instructor_name= models.CharField(max_length=60,default="",blank=True,null=False)
    duration= models.FloatField(null=True, blank=True,default=None)
    class Meta:
        verbose_name_plural = "University Classes"
    def __str__(self):
    #returns input value of the title and instructor name
    #feild as a tuple to display in the browser instead of the defautl title
        display_course = '{0.title}: {0.Instructor_name}'
        return display_course.format(self)
#create model manager
object = models.Manager()

#display the object output values in the form of a string

#remove the added 's' that Django adds to the model name 
