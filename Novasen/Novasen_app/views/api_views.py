# Novasen_app/serializers.py
from rest_framework import serializers
from Novasen_app.models import Programas

class ProgramasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Programas
        fields = '__all__'  # O especifica los campos que necesites
