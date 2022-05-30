 
#serialize the data sended
 
from rest_framework import serializers
from django.core.validators import RegexValidator

class commandSerialize(serializers.Serializer):
    type=serializers.CharField(max_length=500,allow_null=True,allow_blank=True)
    name=serializers.CharField(max_length=500,allow_blank=True ,allow_null=True,required=False)
    expresion=serializers.CharField(max_length=500,required=False,allow_null=True,allow_blank=True )
    parameters=serializers.CharField(max_length=500,required=False,allow_null=True,allow_blank=True )
    
    #validate type field
    def validate_type(self, value):
        content=['os','compute']
        if value not in content   :
            raise serializers.ValidationError("Type of request have to be 'os' or 'compute'")
        return value
     
    #validate name field
    def validate_name(self, value):
        if   value.isdigit():
             raise serializers.ValidationError("name is invalid")
        return value
    
    #validate expresion field
    def validate_expresion(self, value):
        if  value.isalpha() or value.isdigit():
             raise serializers.ValidationError("expresion is invalid")
        return value
 