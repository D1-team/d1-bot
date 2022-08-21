from app.models.response import Response
from app.serializers._base import BaseSerializer


class ResponseSerializer(BaseSerializer):
    """
    ResponseSerializer to define fields used in the Response model.
    """

    class Meta:
        """
        Serializer Meta class
        """

        model = Response
        fields = [field.name for field in Response._meta.fields]
