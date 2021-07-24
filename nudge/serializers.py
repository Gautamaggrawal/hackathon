from django.contrib.auth import authenticate
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
from rest_framework import serializers
from django.contrib.auth import get_user_model
User = get_user_model()

class MyAuthTokenSerializer(serializers.Serializer):
    appName = serializers.CharField()

    def validate(self, attrs):
        appName = attrs.get('appName')

        if appName:
            user = User.objects.create_user()
            
        else:
            msg = _('Must include "appName".')
            raise serializers.ValidationError(msg, code='authorization')

        attrs['user'] = user
        return attrs


from .models import User, UserProfile

# class UserProfileSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = UserProfile
#         fields = ('title', 'dob')

#     def create(self, validated_data):
#         instance , created = Item.objects.get_or_create(parameter)
#         return instance
#     #     print(validated_data)
#     #     print(1/0)
#     #     title = validated_data.pop('title')
#     #     dob = validated_data.pop('dob')
#     #     user = None
#     #     request = self.context.get("request")
#     #     if request and hasattr(request, "user"):
#     #         user = request.user
#     #     x = UserProfile.objects.filter(user = user)
#     #     if x.exists():
#     #         return x.first()
#     #     else:
#     #         x = UserProfile.objects.create(user=user, title =title,dob= dob)
#     #     return p

class UserProfileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('user', 'title','dob')
        read_only_fields = ('user',)

class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    profile = UserProfileSerializer(required=True)

    class Meta:
        model = User
        fields = ('url','profile')
        # extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        profile_data = validated_data.pop('profile')
        user = None
        request = self.context.get("request")
        if request and hasattr(request, "user"):
            user = request.user
        UserProfile.objects.create(user=user, **profile_data)
        return UserProfile

    def update(self, instance, validated_data):
        profile_data = validated_data.pop('profile')
        profile = instance.profile

        instance.email = validated_data.get('email', instance.email)
        instance.save()

        profile.title = profile_data.get('title', profile.title)
        profile.dob = profile_data.get('dob', profile.dob)
        profile.save()

        return instance




from rest_framework import serializers
from .models import User, UserProfile

class UserProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserProfile
        fields = ('title',)

class UserSerializer(serializers.HyperlinkedModelSerializer):
    profile = UserProfileSerializer(required=True)

    class Meta:
        model = User
        fields = ('url', 'username', 'profile')
        extra_kwargs = {'username': {'read_only': True}}

    def create(self, validated_data):
        profile_data = validated_data.pop('profile')
        user = User.objects.create_user()
        UserProfile.objects.create(user=user, **profile_data)
        return user

    def update(self, instance, validated_data):
        # print(1/0)
        profile_data = validated_data.pop('profile')
        profile = instance.profile

        profile.title = profile_data.get('title', profile.title)
        # profile.dob = profile_data.get('dob', profile.dob)
        # profile.address = profile_data.get('address', profile.address)
        # profile.country = profile_data.get('country', profile.country)
        # profile.city = profile_data.get('city', profile.city)
        # profile.zip = profile_data.get('zip', profile.zip)
        profile.save()

        return instance