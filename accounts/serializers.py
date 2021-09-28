from rest_framework import serializers
from .models import UserProfile

class userSerializer(serializers.ModelSerializer):
    url = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model= UserProfile
        fields = '__all__'

    def get_url(self,obj):
        request = self.context.get("request")
        return obj.get_api_url()

    def validate_user(self,value):
        qs = UserProfile.objects.filter(user__iexact = value)
        if self.instance:
            qs = qs.exclude(pk=self.instance.pk)
        if qs.exists():
            raise serializers.ValidationError("Username must be unique")
        return value


class LoginSerializer(serializers.ModelSerializer):
    password= serializers.CharField(
        max_length=128, min_length=6, write_only=True
    )

    class Meta:
        model= UserProfile
        fields = ('description','password','token')

        read_only_fields= ['token']