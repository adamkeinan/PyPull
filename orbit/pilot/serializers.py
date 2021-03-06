from rest_framework import serializers
from .models import Pilot, LANGUAGE_CHOICES, STYLE_CHOICES
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    pilot = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Pilot.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'pilot']
        owner = serializers.ReadOnlyField(source='owner.username')

class PilotSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(
        required=False, allow_blank=True, max_length=100)
    code = serializers.CharField(style={'base_template': 'textarea.html'})
    linenos = serializers.BooleanField(required=False)
    language = serializers.ChoiceField(
        choices=LANGUAGE_CHOICES, default='python')
    style = serializers.ChoiceField(choices=STYLE_CHOICES, default='friendly')
    owner = serializers.ReadOnlyField(source='owner.username')

    def create(self, validated_data):
        """
        Create and return a new `Pilot` instance, given the validated data.
        """
        return Pilot.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Pilot` instance, given the validated data.
        """
        instance.title = validated_data.get('title', instance.title)
        instance.code = validated_data.get('code', instance.code)
        instance.linenos = validated_data.get('linenos', instance.linenos)
        instance.language = validated_data.get('language', instance.language)
        instance.style = validated_data.get('style', instance.style)
        instance.save()
        return instance

