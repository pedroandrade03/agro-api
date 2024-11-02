from rest_framework import serializers


class CitySerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=100);
    
    class Meta:
        fields = "__all__"
