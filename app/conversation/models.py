from django.contrib.auth.models import User
from django.db import models

from item.models import Item


class Conversation(models.Model):

    class Meta:
        ordering = ('-modified_at',)

    item = models.ForeignKey(Item, related_name='conversations', on_delete=models.CASCADE)
    members = models.ManyToManyField(User,related_name='conversations')
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)


class ConversationMessage(models.Model):

    conversation = models.ForeignKey(Item, related_name='messages', on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, related_name='created_messages', on_delete=models.CASCADE)

