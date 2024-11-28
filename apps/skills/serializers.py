from rest_framework import serializers

from apps.skills.models import SkillProgress


class SkillProgressSerializer(serializers.ModelSerializer):
    class Meta:
        model = SkillProgress
        fields = [
            'skill',
            'experience'
        ]
