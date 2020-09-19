from rest_framework import serializers
from factors.models import Factors

class FactorsSerializer(serializers.ModelSerializer):
    class Meta:
        model =  Factors
        #fields = ('id', 'user','tss','ctl','atl','tbs','date')
        fields = ('__all__')