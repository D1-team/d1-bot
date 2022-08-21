from app.models.response import Response
from app.serializers.response import ResponseSerializer

IDENTIFIER = 0


def process_response_command(context, arguments) -> str:
    identifier = arguments[IDENTIFIER]
    values = arguments[1:]
    if not Response.objects.filter(identifier=identifier).exists() and values:
        data = {
            "identifier": identifier,
            "values": ' '.join(values),
            "discord_guild": context.guild.id,
            "discord_author": context.author.id,
            "discord_channel": context.channel.id,
        }
        serializer = ResponseSerializer(data=data, many=False)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return "saved"
    else:
        return Response.objects.filter(identifier=identifier).values("values").get()["values"]
