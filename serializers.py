from rest_framework import serializers
from .models import Products_serializers, Type_serializers

class Info_Type_serializers(serializers.ModelSerializer):
    class Meta:
        model = Type_serializers
        fields = '__all__'


class Info_Product__serializers(serializers.ModelSerializer):
    type = Info_Type_serializers()

    class Meta:
        model = Products_serializers
        fields = '__all__'

    
    
    def update(self, instance, validated_data):
        # Update the scalar fields of the instance
        instance.name = validated_data.get('name', instance.name)
        instance.price = validated_data.get('price', instance.price)
        instance.image = validated_data.get('image', instance.image)

        # Update the nested 'type' field if it is provided
        type_data = validated_data.get('type', None)
        if type_data:
            type_instance = instance.type
            type_instance.name = type_data.get('name', type_instance.name)
            type_instance.save()

        instance.save()
        return instance

    
    
    def create(self, validated_data):
        type_data = validated_data.pop('type')
        type_obj = Type_serializers.objects.create(**type_data)
        product_obj = Products_serializers.objects.create(type=type_obj, **validated_data)
        return product_obj