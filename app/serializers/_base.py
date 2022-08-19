from rest_framework import serializers


class BaseSerializer(serializers.ModelSerializer):
    """
    Base Serializer to define all base fields.
    """

    base_fields = ["id", "created_at", "updated_at", "deleted"]
