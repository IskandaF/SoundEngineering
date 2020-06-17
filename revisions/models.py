from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator
from tracks.models import Project,Track
from django.contrib.auth.models import User





class Revision(models.Model):
    # def __init__(self,project,track,volumechange,panningposition,eq_high,eq_middle,eq_low,distortion_changes,reverb_changes,delay_changes,additionalcomments):
        project=models.ForeignKey(Project,on_delete=models.CASCADE)
        track=models.ForeignKey(Track,on_delete=models.CASCADE)
        volumechange=models.IntegerField(default=0,verbose_name="How much you want the volume to change?",blank=True,validators=[MinValueValidator(-100),MaxValueValidator(100)])
        panningposition=models.IntegerField(default=0,verbose_name="Position of an instrument/vocal in stereo field",blank=True,validators=[MinValueValidator(-100),MaxValueValidator(100)])
        eq_high=models.IntegerField(default=0,verbose_name="How much to raise/reduce the highs?",blank=True,validators=[MinValueValidator(-100),MaxValueValidator(100)])
        eq_middle=models.IntegerField(default=0,verbose_name="How much to raise/reduce the middle?",blank=True,validators=[MinValueValidator(-100),MaxValueValidator(100)])
        eq_low=models.IntegerField(default=0,verbose_name="How much to raise/reduce the lows?",blank=True,validators=[MinValueValidator(-100),MaxValueValidator(100)])
        distortion_changes=models.IntegerField(default=0,verbose_name="How much to raise/reduce the distortion?",blank=True,validators=[MinValueValidator(-100),MaxValueValidator(100)])
        reverb_changes=models.IntegerField(default=0,verbose_name="How much to increase/reduce the reverb?",blank=True,validators=[MinValueValidator(-100),MaxValueValidator(100)])
        delay_changes=models.IntegerField(default=0,verbose_name="How much to increase/reduce the delay?",blank=True,validators=[MinValueValidator(-100),MaxValueValidator(100)])

        additionalcomments=models.TextField(default="None",verbose_name="Please leave additional comments",blank=True)
        user=models.ForeignKey(to=User, blank=True, null=True,on_delete=models.CASCADE)
    
    

# Create your models here.
