from rest_framework import serializers
from .models import User, ResumeModel, ReferenceUser


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password('password')
        instance.save()
        return instance


class ResumeSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = ResumeModel
        fields = ("id", "user", "skill", "experience", "cv")
        # fields = "__all__"


class ReferenceSerializer(serializers.ModelSerializer):
    # references = serializers.SerializerMethodField()
    #
    # def _get_reference_user(self, obj):       #try recursive logic
    #     return obj.reference_by
    #     _get_reference_user()

    # reference_by = serializers.HyperlinkedIdentityField(view_name='User-detail', read_only=True)

    username = serializers.StringRelatedField(read_only=True)
    reference_by = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = ReferenceUser
        fields = ['username', 'reference_by']
        # depth = 1
