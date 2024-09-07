from .models import CatData
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
class CatsEveryWhereList(APIView):
    def get(self, request, format = None):
        response = Response(status = status.HTTP_200_OK, data = {})
        try:
            cats = CatData.objects.all()

            data = []
            if cats.exists():
                for cat in cats:
                    aData = {
                        'type' : cat.type,
                        'title' : cat.title,
                        'image' : cat.image.url,
                        'position' : cat.position
                    }
                    data.append(aData)
            response.data = data

        except Exception as e:
            response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
            response.data['message'] = 'Internal Server Error'
            response.data['error'] = str(e)

        finally:
            return response

