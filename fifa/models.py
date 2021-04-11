from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Club(models.Model):
    name = models.CharField()


class Player(models.Model):
    PREFERRED_FOOT_CHOICES = [
        ('L', 'Left'),
        ('R', 'Right'),
    ]

    POSITION_CHOICES = [
        ('LS', 'Left Striker'),
        ('ST', 'Striker'),
        ('RS', 'Right Striker'),
        ('LW', 'Left Winger'),
        ('LF', 'Left Forward'),
        ('CF', 'Center Forward'),
        ('RF', 'Right Forward'),
        ('RW', 'Right Winger'),
        ('LM', 'Left Midfielder'),
        ('LAM', 'Left Attacking Midfielder'),
        ('LDM', 'Left Defensive Midfielder'),
        ('LCM', 'Left Center Midfielder'),
        ('CAM', 'Center Attacking Midfielder'),
        ('CDM', 'Center Defensive Midfielder'),
        ('CM', 'Center Midfielder'),
        ('RCM', 'Right Center Midfielder'),
        ('RDM', 'Right Defensive Midfielder'),
        ('RAM', 'Right Attacking Midfielder'),
        ('RM', 'Right Midfielder'),
        ('LWB', 'Left Wingback'),
        ('LB', 'Left Back'),
        ('LCB', 'Left Center Back'),
        ('CB', 'Center Back'),
        ('RCB', 'Right Center Back'),
        ('RB', 'Right Back'),
        ('RWB', 'Right Wingback'),
        ('GK', 'Goalkeeper'),
    ]

    name = models.CharField()
    age = models.IntegerField()
    nationality = models.CharField()
    overall = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(99)])
    potential = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(99)])
    club = models.ForeignKey(Club, on_delete=models.DO_NOTHING)
    value = models.IntegerField()
    preferred = models.CharField(max_length=1, choices=PREFERRED_FOOT_CHOICES)
    international_reputation = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    weak_foot = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    skill_moves = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    position = models.CharField(max_length=3, choices=POSITION_CHOICES)
    jersey_number = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(99)])
    joined = models.DateField()
    loaned_from = models.ForeignKey(Club, on_delete=models.DO_NOTHING)
    contract_valid_until = models.DateField()
    height = models.IntegerField()
    weight = models.IntegerField()
