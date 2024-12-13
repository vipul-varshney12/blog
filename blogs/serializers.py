from rest_framework import serializers
from .models import BlogPost, Comment, Category, Tag, Profile
from django.core.exceptions import ValidationError
from datetime import datetime

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'

class BlogPostSerializer(serializers.ModelSerializer):
    categories = serializers.PrimaryKeyRelatedField(many=True, queryset=Category.objects.all())
    tags = serializers.PrimaryKeyRelatedField(many=True, queryset=Tag.objects.all())

    class Meta:
        model = BlogPost
        fields = '__all__'

    def validate_title(self, value):
        if not value.strip():
            raise serializers.ValidationError("Title cannot be empty.")
        return value

    def validate_content(self, value):
        if not value.strip():
            raise serializers.ValidationError("Content cannot be empty.")
        return value

    def validate(self, attrs):
        if 'creator' in attrs and attrs['creator'] is None:
            raise serializers.ValidationError("Creator must be set.")
        return attrs

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

    def validate_content(self, value):
        if not value.strip():
            raise serializers.ValidationError("Comment content cannot be empty.")
        return value

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'

    def validate_phone(self, value):
        if not value.isdigit() or len(value) < 10:
            raise serializers.ValidationError("Phone number must be numeric and at least 10 digits long.")
        return value

    def validate_email(self, value):
        from django.core.exceptions import ValidationError
        from django.utils.translation import gettext_lazy as _
        if Profile.objects.filter(email=value).exists():
            raise ValidationError(_("Email is already in use."))
        return value
