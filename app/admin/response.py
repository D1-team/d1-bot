from django.contrib import admin

from app.models.response import Response


@admin.register(Response)
class ResponseAdmin(admin.ModelAdmin):
    search_fields = (
        "identifier",
        "values",
    )

    fields = [field.name for field in Response._meta.fields]

    list_display = (
        "identifier",
        "values",
        "discord_guild",
        "discord_author",
        "discord_channel"
    )

    readonly_fields = ["id", "created_at", "updated_at"]