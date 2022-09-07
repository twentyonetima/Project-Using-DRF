from rest_framework import serializers

from people.models import People


class PeopleSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = People
        fields = "__all__"

