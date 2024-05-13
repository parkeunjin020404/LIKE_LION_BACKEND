from django.shortcuts import render
from .models import Community
from .serializers import CommunitySerializer
from .serializers import CommunityDetailSerializer
from .serializers import CommentRequestSerializer
from .serializers import CommentResponseSerializer
from .serializers import CommunitySerializer2
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Comment
# Create your views here.
@api_view(['GET', 'POST'])
def community_list(request):
	if request.method == 'GET':
		communitys = Community.objects.all()
		serializer = CommunitySerializer(communitys, many=True)
		return Response(serializer.data, status=status.HTTP_200_OK)
	elif request.method == 'POST':
		serializer = CommunitySerializer2(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status = status.HTTP_201_CREATED)
	return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def community_detail(request, pk):
    try:
        community = Community.objects.get(pk=pk)
        if request.method == 'GET':
            serializer = CommunityDetailSerializer(community)
            return Response(serializer.data, status=status.HTTP_200_OK)
        elif request.method == 'PUT':
            serializer = CommunitySerializer2(community, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(status=status.HTTP_400_BAD_REQUEST)
        elif request.method == 'DELETE':
            community.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
    except Community.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
def create_comment(request, post_id):
    community = Community.objects.get(pk=post_id)
    serializer = CommentRequestSerializer(data=request.data) # 들어오는 데이터를 시리얼라이저로 보냄
    if serializer.is_valid():
        new_comment = serializer.save(post=community)
        response = CommentResponseSerializer(new_comment) # 응답용 시리얼라이저에 데이터 보냄
        return Response(response.data, status=status.HTTP_201_CREATED)

@api_view(['GET'])
def get_comments(request, post_id):
    community = Community.objects.get(pk=post_id)
    comments = Comment.objects.filter(post=community)
    serializer = CommentResponseSerializer(comments, many=True) # 응답용 시리얼라이저에 데이터 보냄
    return Response(serializer.data, status=status.HTTP_200_OK)