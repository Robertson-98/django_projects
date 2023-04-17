
from django.shortcuts import render
from .models import Post

# Create your views here.      

def posts_list(request):
    queryset = Post.objects.all()
    return render(request, 'listing.html', {'posts':queryset})

"REST"
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Post
from .serializers import PostSerializers


@api_view(['GET'])
def post_list_api_view(request):
    queryset = Post.objects.all()
    serializer = PostSerializers(queryset, many=True)  
    return Response(serializer.data)

@api_view(['GET'])
def post_details(request, id):
    post = get_object_or_404(Post, id=id)
    serializer = PostSerializers(post)
    return Response(serializer.data)

@api_view(['POST'])
def create_post(request):
    serializer = PostSerializers(data=request.data)
    serializer .is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data, status=201)


@api_view(['DELETE'])
def delete_post(request, id):
    post = get_object_or_404(Post, id=id)
    post.delete()
    return Response(status=204)



@api_view(['PATCH'])
def update_post(request, id):
    post = get_object_or_404(Post, id=id)
    serializer = PostSerializers(post, data=request.data, partial=True)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data, status=201)





# @api_view(['PUT'])
# def update_post(request, id):
#     post = get_object_or_404(Post, id=id)
#     serializer = PostSerializers(post, data=request.data)
#     serializer.is_valid(raise_exception=True)
#     serializer.save()
#     return Response(serializer.data, status=201)





# @api_view(['PUT', 'PATCH'])
# def update_post(request, id):
#     post = get_object_or_404(Post, id=id)
#     partial =  True if request.method == 'PATCH' else False
#     serializer = PostSerializers(post, data=request.data, partial=partial)
#     serializer.is_valid(raise_exception=True)
#     serializer.save()
#     return Response(serializer.data, status=201)
