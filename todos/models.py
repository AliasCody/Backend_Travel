'''
    "model" is the file which defines the structure of data base
'''

from django.conf import settings
from django.db import models

'''
    Django provides the class "models.Model", which contains tools for storing, deleting, and searching data.
'''

# Compares to ERD, Todo is an Entity
class Todo(models.Model):

    # title is an attribute
    title = models.CharField(max_length=255)


    '''
        - ForeignKey()
        - settings.AUTH_USER_MODEL
        - on_delete=models.CASCADE
        - related_name="todos"
    '''
    
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name = "todos"
    )

    def __str__(self):
        return self.title