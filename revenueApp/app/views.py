import traceback
from django.http import HttpResponse
from django.http.response import JsonResponse
from django.db.models import Sum
from django.db.models.functions import TruncHour, TruncDay
from rest_framework import generics, status
from app.models import Company, RevenueDetails
from app.serializers import CompanySerializer, RevenueSerializer, TotalSalesSerializer, SalesRequestSerializer


def ping(request):
    """
    Implemented to check server health
    """
    return HttpResponse("All good", status=200)


class TotalSales(generics.GenericAPIView):
    """
    Get Total sales for branch id
    """

    def get(self, request, **kwargs):
        try:
            path = request.get_full_path().lower()
            serializer = SalesRequestSerializer(data=request.GET)
            response_dict = dict()
            if serializer.is_valid():
                # adding neccessary filter for query operation
                filter_dict = dict(
                    company__branch_id=serializer.validated_data.get('branch_id'),
                    updated_date__range=(
                        serializer.validated_data.get('start'),
                        serializer.validated_data.get('end'))
                )
                
                queryset = RevenueDetails.objects.filter(**filter_dict)
                event_time = TruncDay('updated_date') if path.startswith('/sales/daily') else TruncHour('updated_date')

                queryset = queryset.annotate(
                        event_time=event_time
                    ).values('event_time').annotate(
                        total_sales=Sum('total')
                    ).values('event_time', 'total_sales')
                serializer = TotalSalesSerializer(queryset, many=True)
                
                # response construction
                response_dict.update(message="Total sales found", data=serializer.data)
                if not serializer.data:
                    response_dict.update(message="There were no sales during that period",
                    data=serializer.data)
                return JsonResponse(response_dict, safe=False ,status=status.HTTP_200_OK)
            return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception:
            print(traceback.format_exc())
            return JsonResponse({"message": "Something went wrong"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class RevenueList(generics.ListCreateAPIView):
    """
    List all Revenue or create a new revenue
    """
    queryset = RevenueDetails.objects.all()
    serializer_class = RevenueSerializer


class RevenueDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Get, update and delete individual revenue
    """

    queryset = RevenueDetails.objects.all()
    serializer_class = RevenueSerializer


class CompanyList(generics.ListCreateAPIView):
    """
        List all company or create a new company
    """
    queryset = Company.objects.all()
    serializer_class = CompanySerializer


class CompanyDetail(generics.RetrieveUpdateDestroyAPIView):
    """
        Get, Update or delete a company instance
    """
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
