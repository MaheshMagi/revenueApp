from django.db.models.fields import DateTimeField
from app.models import Company, RevenueDetails
from rest_framework import serializers

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ['id','branch_name', 'branch_id', 'created_date']

class RevenueSerializer(serializers.ModelSerializer):
    updated_date = serializers.DateTimeField(format="%d/%m/%y %H:%M")
    class Meta:
        model = RevenueDetails
        fields = ['id','company', 'receipt', 'updated_date', 'total']

class TotalSalesSerializer(serializers.Serializer):
    event_time = serializers.DateTimeField()
    total_sales = serializers.FloatField()

class SalesRequestSerializer(serializers.Serializer):
    start = serializers.DateField(format="%Y-%m-%d", required=False)
    end = serializers.DateField(format="%Y-%m-%d", required=False)
    branch_id = serializers.CharField()

    def validate(self, data):
        if data.get('end') < data.get('start'):
            raise serializers.ValidationError("End date is lesser than start date.")
        return data

    def validate_branch_id(self, data):
        company_details = Company.objects.filter(branch_id=data).exists()
        if not company_details:
            raise serializers.ValidationError("Branch id does not exist")
        return data


