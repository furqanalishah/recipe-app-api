"""
Serializers for recipe APIs.
"""

from rest_framework import serializers

from core.models import Recipe


class RecipeSerializer(serializers.ModelSerializer):
    """Serializer for Recipe."""

    class Meta:
        model = Recipe
        fields = ["id", "title", "description", "time_minutes", "price", "link"]
        read_only_fields = ["id"]
