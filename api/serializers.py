from rest_framework import serializers
from test_task.models import Article


class ArticleSerializer(serializers.Serializer):
    heading = serializers.CharField(max_length=220)
    description = serializers.CharField(max_length=220)
    art_type = serializers.CharField(max_length=220)
    author_id = serializers.IntegerField()

    def create(self, validated_data):
        return Article.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.heading = validated_data.get('heading', instance.heading)
        instance.description = validated_data.get(
            'description', instance.description)
        instance.art_type = validated_data.get('art_type', instance.art_type)
        instance.author_id = validated_data.get(
            'author_id', instance.author_id)

        instance.save()
        return instance
