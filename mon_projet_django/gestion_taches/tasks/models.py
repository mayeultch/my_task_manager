from django.db import models
from django.contrib.auth.models import User  # Pour associer les tâches à un utilisateur

class Task(models.Model):
    STATUS_CHOICES = [
        ('pending', 'En attente'),
        ('in_progress', 'En cours'),
        ('completed', 'Terminée'),
    ]
    
    title = models.CharField(max_length=200)  # Titre de la tâche
    description = models.TextField(blank=True)  # Description optionnelle
    created_at = models.DateTimeField(auto_now_add=True)  # Date de création
    due_date = models.DateTimeField(null=True, blank=True)  # Date limite
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')  # Statut de la tâche
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Lien avec l'utilisateur qui a créé la tâche

    def __str__(self):
        return self.title
