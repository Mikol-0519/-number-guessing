from django.db import models

from django.utils import timezone

class GameHistory(models.Model):
    player_name = models.CharField(max_length=50)
    attempts = models.IntegerField()
    number_to_guess = models.IntegerField()
    is_won = models.BooleanField(default=False)
    played_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.player_name} - {'Won' if self.is_won else 'Lost'} in {self.attempts} attempts"