from rest_framework import serializers
from .models import Question, Answear


class AnswearSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answear
        fields = [
            "id",
            "answear",
            "is_correct",
        ]


class RandomQuizSerializer(serializers.ModelSerializer):
    answear = AnswearSerializer(many=True, read_only=True)

    class Meta:
        model = Question
        fields = ["title", "answear"]
