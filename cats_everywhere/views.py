from .models import CatData
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Max

# Create your views here.
class CatsEveryWhereList(APIView):
    def get(self, request, format = None):
        response = Response(status = status.HTTP_200_OK, data = {})
        try:
            cats = CatData.objects.all().order_by('position')

            data = []
            if cats.exists():
                for index, cat in enumerate(cats):
                    aData = {
                        'id' : cat.id,
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

class AddDataView(APIView):
    def post(self, request, format = None):
        response = Response(status = status.HTTP_201_CREATED, data = {})
        try:
            max_position_dict = CatData.objects.aggregate(Max('position'))
            max_position = int(max_position_dict.get('position__max'))

            data = {
                'title' : request.data.get('title'),
                'image' : request.FILES.get('image'),
                'position' : max_position + 1
            }

            instance = CatData.objects.create(**data)
            response.data = {
                'id' : instance.id,
                'type' : instance.type,
                'title' : instance.title,
                'image' : instance.image.url,
                'position' : instance.position
            }

        except Exception as e:
            response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
            response.data['message'] = 'Internal Server Error'
            response.data['error'] = str(e)

        finally:
            return response

class EditDataView(APIView):
    def put(self, request, pk, format = None):
        response = Response(status = status.HTTP_200_OK, data = {})
        try:
            data = {
                'title' : request.data.get('title'),
                'image' : request.FILES.get('image'),
            }
            instance = CatData.objects.get(id = pk)

            # Update here
            instance.title = data['title']

            if data['image']:
                instance.image = data['image']
                
            instance.save()

            response.data = {
                'id' : instance.id,
                'type' : instance.type,
                'title' : instance.title,
                'image' : instance.image.url,
                'position' : instance.position
            }
        
        except CatData.DoesNotExist:
            response.status_code = status.HTTP_404_NOT_FOUND
            response.data['message'] = 'Not Found'
            response.data['error'] = 'Data Not Found!'

        except Exception as e:
            response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
            response.data['message'] = 'Internal Server Error'
            response.data['error'] = str(e)

        finally:
            return response

class UpdateCatPositionView(APIView):
    def patch(self, request, format = None):
        response = Response(status = status.HTTP_200_OK, data = {})
        try:
            ids = request.data.keys()
            cats = CatData.objects.filter(id__in = ids)

            if cats.exists():
                pass

        except Exception as e:
            response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
            response.data['message'] = 'Internal Server Error'
            response.data['error'] = str(e)

        finally:
            return response

class DeleteDataView(APIView):
    def delete(self, request, pk):
        response = Response(status = status.HTTP_200_OK, data = {})
        try:
            cat = CatData.objects.get(id = pk)
            response.data['id'] = cat.id
            cat.delete()
            response.data['message'] = 'Data deleted successfully!'
        
        except CatData.DoesNotExist:
            response.status_code = status.HTTP_404_NOT_FOUND
            response.data['message'] = 'Not Found'
            response.data['error'] = 'Data Not Found!'

        except Exception as e:
            response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
            response.data['message'] = 'Internal Server Error'
            response.data['error'] = str(e)

        finally:
            return response
