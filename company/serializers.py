from rest_framework import serializers


class CldrSerializer(serializers.Serializer):
    id = serializers.CharField()
    date = serializers.CharField()
    open = serializers.CharField()
    high = serializers.CharField()
    low = serializers.CharField()
    close = serializers.CharField()
    adjclose = serializers.CharField()
    volume = serializers.CharField()

class DocuSerializer(serializers.Serializer):
    id = serializers.CharField()
    date = serializers.CharField()
    open = serializers.CharField()
    high = serializers.CharField()
    low = serializers.CharField()
    close = serializers.CharField()
    adjclose = serializers.CharField()
    volume = serializers.CharField()

class PdSerializer(serializers.Serializer):
    id = serializers.CharField()
    date = serializers.CharField()
    open = serializers.CharField()
    high = serializers.CharField()
    low = serializers.CharField()
    close = serializers.CharField()
    adjclose = serializers.CharField()
    volume = serializers.CharField()

class PinsSerializer(serializers.Serializer):
    id = serializers.CharField()
    date = serializers.CharField()
    open = serializers.CharField()
    high = serializers.CharField()
    low = serializers.CharField()
    close = serializers.CharField()
    adjclose = serializers.CharField()
    volume = serializers.CharField()

class RunSerializer(serializers.Serializer):
    id = serializers.CharField()
    date = serializers.CharField()
    open = serializers.CharField()
    high = serializers.CharField()
    low = serializers.CharField()
    close = serializers.CharField()
    adjclose = serializers.CharField()
    volume = serializers.CharField()

class ZmSerializer(serializers.Serializer):
    id = serializers.CharField()
    date = serializers.CharField()
    open = serializers.CharField()
    high = serializers.CharField()
    low = serializers.CharField()
    close = serializers.CharField()
    adjclose = serializers.CharField()
    volume = serializers.CharField()

class ZuoSerializer(serializers.Serializer):
    id = serializers.CharField()
    date = serializers.CharField()
    open = serializers.CharField()
    high = serializers.CharField()
    low = serializers.CharField()
    close = serializers.CharField()
    adjclose = serializers.CharField()
    volume = serializers.CharField()
