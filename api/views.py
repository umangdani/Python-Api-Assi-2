from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view,authentication_classes
from rest_framework.response import Response
from ApiApp.serializers import *
from django.views.decorators.csrf import csrf_exempt
from ApiApp.models import *
from rest_framework.authentication import TokenAuthentication


# Create your views here.


@csrf_exempt
@api_view(['GET'])
def discussion_list(request):
	discussion_list = Discussion.objects.filter(discussion_type__in = ['article', 'question'])
    serializer = DiscssionsSerializer(discussion_list, many=True)
    return Response(serializer, status=status.HTTP_200_OK)
							

@csrf_exempt
@api_view(['POST'])
def comment_create(request):
	if request.user.is_authenticated():
		owner = request.user
		data = request.data
		data['added_by'] = owner.id
		serializer = CommentSerializer(data=data)
		if serializer.is_valid():
			d_id = request.data['discussion']
			comment = Comment.objects.all().filter(discussion=d_id, added_by=owner.id).exists()
			if comment == True:
				return Response({'error': 'Already comment.'}, status=status.HTTP_200_OK)
			else:
				obj = Discussion.objects.get(id=d_id)
				dis_list = Discussion.objects.filter(added_by=owner.id)
				if obj in dis_list:
					return Response({'error': 'You can not many comment .'}, status=status.HTTP_200_OK)
				else:
					serializer.save()
					return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
	else:
		return Response({'error': 'You are not authenticated'}, status=status.HTTP_200_OK)




@api_view(['GET'])
def discussion_search(request):
    serializer = SearchDiscssionsSerializer(data=request.GET)
    if serializer.is_valid():
        try:
            title = serializer.validated_data['title']
            search_detail = Discussion.objects.filter(title__icontains=title)
            data = DiscssionsSerializer(search_detail, many=True)
            return Response(data.data, status=status.HTTP_200_OK)
        except:
            return Response({'error': 'Discussion is not found'}, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




	# if request.user.is_authenticated():
	# 	owner = request.user
	# 	data = request.data
	# 	data['added_by'] = owner.id
	# 	serializer = CommentSerializer(data=data)
	# 	if serializer.is_valid():
	# 		d_id = request.data['discussion']
	# 		comment = Comment.objects.all().filter(discussion=d_id, added_by=owner.id).exists()
	# 		if comment == True:
	# 			return Response({'error': 'Already comment.'}, status=status.HTTP_200_OK)
	# 		else:
	# 			obj = Discussion.objects.get(id=d_id)
	# 			dis_list = Discussion.objects.filter(added_by=owner.id)
	# 			if obj in dis_list:
	# 				return Response({'error': 'You can not many comment .'}, status=status.HTTP_200_OK)
	# 			else:
	# 				serializer.save()
	# 				return Response(serializer.data, status=status.HTTP_201_CREATED)
	# 	return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
	# else:
	# 	return Response({'error': 'You are Not authenticated'}, status=status.HTTP_200_OK)



	# serializer = DiscssionsSerializer(data=request.GET)
 #    if serializer.is_valid():
 #        try:
 #            title = serializer.validated_data['title']
 #            search_detail = Discussion.objects.filter(title__icontains=title)
 #            data = listDiscssionsserializer(search_detail, many=True)
 #            return Response(data.data, status=status.HTTP_200_OK)
 #        except:
 #            return Response({'error': 'Not found'}, status=status.HTTP_400_BAD_REQUEST)
 #    else:
 #        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


