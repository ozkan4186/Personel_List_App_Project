from rest_framework import serializers

from .models import Department,Personnel

class DepartmentSerializer(serializers.ModelSerializer):

        personnel_count = serializers.SerializerMethodField()  
        class Meta:
            model = Department
            fields="__all__"

        def get_personnel_count(self,obj):
            return obj    
