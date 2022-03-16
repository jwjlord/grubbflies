from django.db import models

class Story(models.Model):
    def __str__(id):
        return f"Story ID {id}"
    pass
    
class Player(models.Model):
    username = models.CharField(max_length=25)
    story = models.ForeignKey(Story, on_delete=models.CASCADE)
    def __str__(self):
        return self.username

# segments are ordered by their primary keys

class Segment(models.Model):
    contents = models.CharField(max_length=1000)
    author = models.ForeignKey(Player, on_delete=models.CASCADE)
    story = models.ForeignKey(Story, on_delete=models.CASCADE)
    is_complete = models.BooleanField()
    def __str__(self):
        return f"{Story.id}: {Player.username}"
    