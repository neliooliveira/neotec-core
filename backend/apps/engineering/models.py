from django.db import models
from core.models import BaseModel

class Engineering(BaseModel):
    """Engineering disciplines."""
    DISCIPLINE_CHOICES = [('hardware', 'Hardware'), ('firmware', 'Firmware'), ('software', 'Software'), ('mechanics', 'Mechanics'), ('3d_print', '3D Printing'), ('cnc', 'CNC'), ('pcb', 'PCB'), ('documentation', 'Documentation')]
    name = models.CharField(max_length=255, choices=DISCIPLINE_CHOICES)
    project = models.ForeignKey('projects.Project', on_delete=models.CASCADE, related_name='engineering')
    description = models.TextField(blank=True)
    class Meta:
        verbose_name_plural = 'Engineering'
    def __str__(self):
        return f"{self.project} - {self.get_name_display()}"
