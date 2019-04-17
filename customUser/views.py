import os
from time import timezone

from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from django.utils.crypto import get_random_string
from django.utils.datetime_safe import datetime
from oauth2_provider.contrib.rest_framework import OAuth2Authentication
# from push_notifications.models import GCMDevice
from rest_framework import generics, status, filters, viewsets
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.parsers import MultiPartParser, FormParser, FileUploadParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.utils import json
from rest_framework.views import APIView

from customUser.models import User, Commentaire, PostStat, Message, Conversation, Category, Notification, \
    Suggest, Courses, Department, Event, Classe, Pending, Branch
from customUser.paginator import PostOffSetLimitPagination, MessagesOffSetLimitPagination
from customUser.permissions import IsAdmin, IsMe, IsMine, MyConvo, MyMsg, isStaff, IsProf
from customUser.serializers import UserSerializer, \
    CommentaireSerializer, ProfileSerializer, MessageSerializer, \
    ConversationSerializer, PostSerializer, CategorySerializer, NotifSerializer, SuggestSerializer, CoursesSerializer, \
    DepSerializer, ScheduleSerializer, EventSerializer, PostCreateSerializer, ScUserSerializer, ClasseSerializer, \
    PendingSerializer, CreateUserSerializer, FCMSerializer, ClasseSerializerMin, BranchSerializer, EventSerializerMin, \
    EventCreateSerializer


@api_view(['PATCH', 'PUT'])
@permission_classes([IsAuthenticated])
@authentication_classes([OAuth2Authentication])
def follow(request):

    followed = User.objects.get(id=request.POST.get('user_id'))

    user = request.user
    user.following.add(followed)

    followed.followers.add(request.user)

    # try:
    #
    #     device = GCMDevice.objects.get(user=followed)
    #     device.send_message(None, extra={"type": "follow",
    #                                      "user_id": user.id,
    #                                      "name": "Abonnement",
    #                                      "mass": user.first_name + " " + user.last_name + " a commencé a vous suivre",
    #                                      "timestamp": datetime.now().strftime("%Y-%m-%d'T'%H:%M:%S"),
    #                                      "image": user.picture, })
    #
    # except GCMDevice.DoesNotExist:
    #     pass

    return Response('done')


@api_view(['PATCH', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
@authentication_classes([OAuth2Authentication])
def unfollow(request):
    user = request.POST.get('user_id')
    request.user.following.remove(User.objects.get(id=user))

    User.objects.get(id=user).followers.remove(request.user)

    return Response('done unfollow')



@api_view(['PATCH', 'PUT'])
@permission_classes([IsAuthenticated])
@authentication_classes([OAuth2Authentication])
def see_notifs(request):

    notifs = request.user.get_notifs().all()

    for i in notifs:
        i.seen = True
        Notification.save(i)

    return Response('done')



class UserList(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_classes = [OAuth2Authentication]
    permission_classes = [IsAuthenticated]


class DetailsView(generics.ListCreateAPIView):
    authentication_classes = [OAuth2Authentication]
    permission_classes = [IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = UserSerializer

    filter_backends = (filters.SearchFilter,)
    search_fields = ('username', 'email', 'first_name', 'last_name')
    pagination_class = MessagesOffSetLimitPagination

    def get_queryset(self):
        return User.objects.filter(is_admin=False).all()


class CreateUserView(generics.CreateAPIView):
    authentication_classes = []
    permission_classes = []
    serializer_class = CreateUserSerializer


class CreateeFCMView(generics.CreateAPIView):
    authentication_classes = []
    permission_classes = []
    serializer_class = FCMSerializer

#
# class CreateFCMView(APIView):
#     authentication_classes = [OAuth2Authentication]
#     permission_classes = [IsAuthenticated]
#
#     def post(self, request, format=None):
#         fcm = FCMSerializer(data=request.data)
#         reg = self.request.POST.get('registration_id')
#
#         try:
#
#             for i in GCMDevice.objects.filter(user=self.request.user):
#                 GCMDevice.delete(i)
#
#             dev = GCMDevice.objects.all().get(registration_id=reg)
#
#             if fcm.is_valid():
#                 dev.active = True
#                 dev.application_id = "my_fcm_app"
#                 dev.user=self.request.user
#                 dev.name = self.request.user.username
#                 dev.cloud_message_type = "FCM"
#
#                 GCMDevice.save(dev)
#             return Response("done", status=status.HTTP_201_CREATED)
#
#         except GCMDevice.DoesNotExist:
#             pass
#
#         if fcm.is_valid():
#             fcm.save(active = True ,application_id = "my_fcm_app", user=self.request.user, name = self.request.user.username, cloud_message_type = "FCM" ,)
#             return Response(fcm.data, status=status.HTTP_201_CREATED)
#
#
#         else:
#             return Response(fcm.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def get_queryset(self):
#         return GCMDevice.objects.filter(user=self.request.user.id).all()
#

class UpdateProfile(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = CreateUserSerializer
    authentication_classes = [OAuth2Authentication]
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user


class Profile(generics.ListAPIView):
    serializer_class = UserSerializer
    authentication_classes = [OAuth2Authentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return User.objects.filter(id=self.request.user.id).all()


"""
class FollowedFeed(generics.ListAPIView):
    serializer_class = PostStatSerializer
    authentication_classes = [OAuth2Authentication]
    permission_classes = [IsAuthenticated]

    pagination_class = PostOffSetLimitPagination

    def get_queryset(self):
        user = self.request.user
        following = user.following.all()

        users_ids = [follow.id for follow in following]
        posts = PostStat.objects.filter(owner_id__in=users_ids).order_by('date_created').reverse()

        return posts

class OwnPostList(generics.ListAPIView):
    serializer_class = PostStatSerializer
    authentication_classes = [OAuth2Authentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        posts = PostStat.objects.filter(owner=user).order_by('date_created').reverse()

        return posts


class UserPostList(generics.ListAPIView):
    serializer_class = PostStatSerializer
    authentication_classes = [OAuth2Authentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = User.objects.get(pk=self.kwargs.get('pk'))
        posts = PostStat.objects.filter(owner=user).order_by('date_created').reverse()

        return posts
"""


class CommentCreateView(generics.CreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = Commentaire.objects.all()
    serializer_class = CommentaireSerializer
    authentication_classes = [OAuth2Authentication]
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        """Save the post data when creating a new bucketlist."""
        user = self.request.user
        post_id = self.request.POST.get('post_id')
        comment = serializer.save(owner=user)

        post = PostStat.objects.get(id=post_id)

        post.comments.add(comment)

        # try:
        #
        #     device = GCMDevice.objects.get(user=post.owner)
        #     device.send_message(None, extra={"type": "other",
        #                                      "post_id": post_id,
        #                                      "name": "commentaire",
        #                                      "mass": user.first_name + " " + user.last_name + " a commenté votre publication",
        #                                      "timestamp": datetime.now().strftime("%Y-%m-%d'T'%H:%M:%S"),
        #                                      "image": user.picture, })
        #
        # except GCMDevice.DoesNotExist:
        #     pass


class CommentCoursCreateView(generics.CreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = Commentaire.objects.all()
    serializer_class = CommentaireSerializer
    authentication_classes = [OAuth2Authentication]
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        """Save the post data when creating a new bucketlist."""
        user = self.request.user
        post_id = self.request.POST.get('id')
        comment = serializer.save(owner=user)

        cours = Courses.objects.get(id=post_id)
        cours.comments.add(comment)

        #
        # try:
        #
        #     device = GCMDevice.objects.get(user=cours.owner)
        #     device.send_message(None, extra={"type": "other",
        #                                      "post_id": post_id,
        #                                      "name": "commentaire",
        #                                      "mass": user.first_name + " " + user.last_name + " a commenté votre publication",
        #                                      "timestamp": datetime.now().strftime("%Y-%m-%d'T'%H:%M:%S"),
        #                                      "image": user.picture, })
        #
        # except GCMDevice.DoesNotExist:
        #     pass


class CommentDetailsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Commentaire.objects.all()
    serializer_class = CommentaireSerializer
    authentication_classes = [OAuth2Authentication]
    permission_classes = [IsAuthenticated]


class PostCommentsView(generics.ListAPIView):
    queryset = Commentaire.objects.all()
    serializer_class = CommentaireSerializer
    authentication_classes = [OAuth2Authentication]
    permission_classes = [IsAuthenticated]

    pagination_class = MessagesOffSetLimitPagination

    def get_queryset(self):
        post = PostStat.objects.get(pk=self.kwargs.get('pk'))
        return PostStat.get_comments(post).all()


class CoursCommentsView(generics.ListAPIView):
    queryset = Commentaire.objects.all()
    serializer_class = CommentaireSerializer
    authentication_classes = [OAuth2Authentication]
    permission_classes = [IsAuthenticated]

    pagination_class = MessagesOffSetLimitPagination

    def get_queryset(self):
        post = Courses.objects.get(pk=self.kwargs.get('pk'))
        return Courses.get_comments(post).all()


"""
class PostStatCreateView(generics.ListCreateAPIView):
    queryset = PostStat.objects.all()
    serializer_class = PostStatSerializer
    authentication_classes = [OAuth2Authentication]
    permission_classes = [IsAuthenticated]

    pagination_class = PostOffSetLimitPagination

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(owner=User.objects.get(id=user.id))


class PostStatUpdateView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PostStat.objects.all()
    serializer_class = PostStatSerializer
    authentication_classes = [OAuth2Authentication]
    permission_classes = [IsAuthenticated, IsMine]


class PostStatDetailsView(generics.RetrieveAPIView):
    queryset = PostStat.objects.all()
    serializer_class = PostStatSerializer
    authentication_classes = [OAuth2Authentication]
    permission_classes = [IsAuthenticated]
"""

"""
"""



class DepartmentDetails(generics.RetrieveAPIView):
    queryset = Department.objects.all()
    serializer_class = DepSerializer
    authentication_classes = [OAuth2Authentication]
    permission_classes = [IsAuthenticated]


class ClasseDetails(generics.RetrieveAPIView):
    queryset = Classe.objects.all()
    serializer_class = ClasseSerializerMin
    authentication_classes = [OAuth2Authentication]
    permission_classes = [IsAuthenticated]



class ClasseStudents(generics.ListAPIView):
    serializer_class = UserSerializer
    authentication_classes = [OAuth2Authentication]
    permission_classes = [IsAuthenticated]

    pagination_class = MessagesOffSetLimitPagination

    def get_queryset(self):
        classe = Classe.objects.get(pk=self.kwargs.get('pk'))
        return Classe.get_students(classe).all()


class BranchClasses(generics.ListAPIView):
    serializer_class = ClasseSerializerMin
    authentication_classes = [OAuth2Authentication]
    permission_classes = [IsAuthenticated]

    pagination_class = MessagesOffSetLimitPagination

    def get_queryset(self):
        branch = Branch.objects.get(pk=self.kwargs.get('pk'))
        classes = Branch.get_classes(branch).all()

        return classes

class BranchStudents(generics.ListAPIView):
    serializer_class = UserSerializer
    authentication_classes = [OAuth2Authentication]
    permission_classes = [IsAuthenticated]

    pagination_class = MessagesOffSetLimitPagination

    def get_queryset(self):
        branch = Branch.objects.get(pk=self.kwargs.get('pk'))
        classes_dep = Branch.get_classes(branch).all()

        classes_id = [classe.id for classe in classes_dep]
        students = User.objects.filter(classe_id__in=classes_id)

        return students





class DepStudents(generics.ListAPIView):
    serializer_class = UserSerializer
    authentication_classes = [OAuth2Authentication]
    permission_classes = [IsAuthenticated]

    pagination_class = MessagesOffSetLimitPagination


    def get_queryset(self):
        dep = Department.objects.get(pk=self.kwargs.get('pk'))

        branches = Department.get_dep_branches(dep).all()

        branch_id = [branch.id for branch in branches]
        classes = Classe.objects.filter(branch_id__in=branch_id)

        classes_id = [classe.id for classe in classes]
        students = User.objects.filter(classe_id__in=classes_id)

        return students



class DepBranches(generics.ListAPIView):
    serializer_class = BranchSerializer
    authentication_classes = [OAuth2Authentication]
    permission_classes = [IsAuthenticated]

    pagination_class = MessagesOffSetLimitPagination


    def get_queryset(self):
        dep = Department.objects.get(pk=self.kwargs.get('pk'))
        branches = Department.get_dep_branches(dep).all()

        return branches


class CreateMessageView(generics.CreateAPIView):
    authentication_classes = [OAuth2Authentication]
    permission_classes = [IsAuthenticated]

    queryset = Message.objects.all()
    serializer_class = MessageSerializer

    def perform_create(self, serializer, **validated_data):

        inter = 0

        rec = self.request.POST.get('reciever')
        user = User.objects.get(id=rec)
        me = self.request.user

        for i in User.get_conversations(me).all():
            for j in User.get_conversations(user).all():
                if i.id == j.id:
                    inter = i
                    break

        if inter == 0:
            convo = Conversation.objects.create()
            convo.users.add(me, user)

            inter = convo

        inter.date_modified = datetime.now()
        inter.save()
        mess = serializer.save(sender=me, reciever=user, conversation=inter)

        # try:
        #
        #     device = GCMDevice.objects.get(user=user)
        #     device.send_message(None, extra={"type": "message", "messid": mess.id,
        #                                                                  "name": user.first_name + " " + user.last_name,
        #                                                                  "mass": self.request.POST.get('content')
        #         , "timestamp": datetime.now().strftime("%Y-%m-%d'T'%H:%M:%S") , "image": user.picture, "sender": me.id, "convo_id":Conversation.get_convo_id(inter)})
        #
        # except GCMDevice.DoesNotExist:
        #     pass



"""class GetConversation(generics.RetrieveAPIView):
    queryset = Conversation.objects.all()
    serializer_class = ConversationSerializer
    authentication_classes = [OAuth2Authentication]
    permission_classes = [IsAuthenticated, MyConvo]"""


class GetConversation(generics.ListAPIView):
    serializer_class = MessageSerializer
    authentication_classes = [OAuth2Authentication]
    permission_classes = [IsAuthenticated, MyConvo]

    pagination_class = MessagesOffSetLimitPagination

    def get_queryset(self):
        convo = Conversation.objects.get(pk=self.kwargs.get('pk'))
        return Conversation.get_all_messages(convo).all()


class GetAllConversation(generics.ListAPIView):
    queryset = Conversation.objects.all()
    serializer_class = ConversationSerializer
    authentication_classes = [OAuth2Authentication]
    permission_classes = [IsAuthenticated]

    pagination_class = MessagesOffSetLimitPagination

    def get_queryset(self):
        return User.get_conversations(self.request.user).all().order_by('-date_modified')


class GetAllConversation_count(generics.ListAPIView):
    queryset = Conversation.objects.all()
    serializer_class = ConversationSerializer
    authentication_classes = [OAuth2Authentication]
    permission_classes = [IsAuthenticated]

    pagination_class = MessagesOffSetLimitPagination

    def get_queryset(self):
        convos = User.get_conversations(self.request.user).all().order_by('-date_modified')





class SeenMessage(generics.UpdateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    authentication_classes = [OAuth2Authentication]
    permission_classes = [IsAuthenticated, MyMsg]




@api_view(['PATCH', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
@authentication_classes([OAuth2Authentication])
def unfollow(request):
    user = request.POST.get('user_id')
    request.user.following.remove(User.objects.get(id=user))

    User.objects.get(id=user).followers.remove(request.user)

    return Response('done unfollow')




class AddPicPost(generics.CreateAPIView):
    parser_classes = (MultiPartParser, FormParser)

    authentication_classes = [OAuth2Authentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, **kwargs):
        up_file = request.FILES['file']

        username = self.request.user.username
        if not os.path.exists('static/' + username + '/posts/'):
            os.makedirs('static/' + username + '/posts/')

        unique_id = get_random_string(length=12)

        if os.path.exists('static/' + username + '/posts/' + unique_id + up_file.name):
            return Response("name exists", status=status.HTTP_400_BAD_REQUEST)

        destination = open('static/' + username + '/posts/' + unique_id + up_file.name, 'wb+')
        for chunk in up_file.chunks():
            destination.write(chunk)
            destination.close()

        serializer = PostCreateSerializer(data=self.request.data)

        cat_id = self.request.POST.get('cat_id')
        category = Category.objects.get(id=cat_id)

        name = self.request.POST.get('name')

        if serializer.is_valid():
            serializer.save(picture_url='static/' + username + '/posts/' + unique_id + up_file.name,
                            owner=self.request.user, category=category, name=name, is_picture=True)

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)





class UpdatePicPost(generics.UpdateAPIView):
    parser_classes = (MultiPartParser, FormParser)

    queryset = PostStat.objects.all()
    serializer_class = PostSerializer

    authentication_classes = [OAuth2Authentication]
    permission_classes = [IsAuthenticated]

    def update(self, request, *args, **kwargs):

        instance = self.get_object()

        up_file = request.FILES['file']

        username = self.request.user.username
        if not os.path.exists('static/' + username + '/posts/'):
            os.makedirs('static/' + username + '/posts/')

        unique_id = get_random_string(length=12)

        if os.path.exists('static/' + username + '/posts/' + unique_id + up_file.name):
            return Response("name exists", status=status.HTTP_400_BAD_REQUEST)

        destination = open('static/' + username + '/posts/' + unique_id + up_file.name, 'wb+')
        for chunk in up_file.chunks():
            destination.write(chunk)
            destination.close()

        instance = PostStat.objects.get(pk=self.kwargs.get('pk'))

     #   serializer = PostCreateSerializer(data=self.request.data)

        cat_id = self.request.POST.get('cat_id')
        category = Category.objects.get(id=cat_id)
        name = self.request.POST.get('name')

        instance.category = category
        instance.picture_url = 'static/' + username + '/posts/' + unique_id + up_file.name
        instance.owner = self.request.user
        instance.name = name
        instance.is_picture = True

        instance.save()


        return Response("done", status=status.HTTP_201_CREATED)







class AddPicEvent(generics.CreateAPIView):
    parser_classes = (MultiPartParser, FormParser)

    authentication_classes = [OAuth2Authentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, **kwargs):
        up_file = request.FILES['file']

        username = self.request.user.username
        if not os.path.exists('static/' + username + '/posts/'):
            os.makedirs('static/' + username + '/posts/')

        unique_id = get_random_string(length=12)

        if os.path.exists('static/' + username + '/posts/' + unique_id + up_file.name):
            return Response("name exists", status=status.HTTP_400_BAD_REQUEST)

        destination = open('static/' + username + '/posts/' + unique_id + up_file.name, 'wb+')
        for chunk in up_file.chunks():
            destination.write(chunk)
            destination.close()

        serializer = EventCreateSerializer(data=self.request.data)

        cat_id = self.request.POST.get('cat_id')
        category = Category.objects.get(id=cat_id)

        name = self.request.POST.get('name')
        description = self.request.POST.get('desc')
        date_beg = self.request.POST.get('date_beg')
        date_end = self.request.POST.get('date_end')
        loc = self.request.POST.get('location')
        max_limit = self.request.POST.get('max_limit')
        is_limited = self.request.POST.get('is_limited')
        lat = self.request.POST.get('lat')
        lng = self.request.POST.get('lng')

        if serializer.is_valid():
            serializer.save(picture_url='static/' + username + '/posts/' + unique_id + up_file.name,
                            owner=self.request.user, category=category, name=name, is_picture=True,location = loc,
                            description=description,date_beg=date_beg,date_end=date_end,
                            is_limited=is_limited,max_limit=max_limit,lat=lat,lng=lng)

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)






class UpdatePicEvent(generics.CreateAPIView):
    parser_classes = (MultiPartParser, FormParser)
    serializer_class = EventCreateSerializer

    authentication_classes = [OAuth2Authentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, **kwargs):
        up_file = request.FILES['file']

        username = self.request.user.username
        if not os.path.exists('static/' + username + '/posts/'):
            os.makedirs('static/' + username + '/posts/')

        unique_id = get_random_string(length=12)

        if os.path.exists('static/' + username + '/posts/' + unique_id + up_file.name):
            return Response("name exists", status=status.HTTP_400_BAD_REQUEST)

        destination = open('static/' + username + '/posts/' + unique_id + up_file.name, 'wb+')
        for chunk in up_file.chunks():
            destination.write(chunk)
            destination.close()

        cat_id = self.request.POST.get('cat_id')
        category = Category.objects.get(id=cat_id)

        name = self.request.POST.get('name')
        description = self.request.POST.get('desc')
        date_beg = self.request.POST.get('date_beg')
        date_end = self.request.POST.get('date_end')
        loc = self.request.POST.get('location')
        max_limit = self.request.POST.get('max_limit')
        is_limited = self.request.POST.get('is_limited')
        lat = self.request.POST.get('lat')
        lng = self.request.POST.get('lng')


        instance = Event.objects.get(pk=self.kwargs.get('pk'))

        instance.category = category
        instance.picture_url = 'static/' + username + '/posts/' + unique_id + up_file.name
        instance.owner = self.request.user
        instance.name = name
        instance.description = description
        instance.date_beg = date_beg
        instance.date_end = date_end
        instance.loc = loc
        instance.is_limited = is_limited
        instance.max_limit = max_limit
        instance.lat = lat
        instance.lng = lng
        instance.is_picture = True

        instance.save()

        return Response("done", status=status.HTTP_201_CREATED)







class AddProfilePic(generics.CreateAPIView):
    parser_classes = (MultiPartParser, FormParser)

    authentication_classes = [OAuth2Authentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, **kwargs):
        up_file = request.FILES['file']

        username = self.request.user.username
        if not os.path.exists('static/' + username + '/profle_pic/'):
            os.makedirs('static/' + username + '/profle_pic/')

        unique_id = get_random_string(length=12)

        if os.path.exists('static/' + username + '/profle_pic/' + unique_id + up_file.name):
            return Response("name exists", status=status.HTTP_400_BAD_REQUEST)

        destination = open('static/' + username + '/profle_pic/' + unique_id + up_file.name, 'wb+')
        for chunk in up_file.chunks():
            destination.write(chunk)
            destination.close()

        user = User.objects.get(id=self.request.user.id)
        user.picture = 'static/' + username + '/profle_pic/' + unique_id + up_file.name

        User.save(user)

        return Response("done")


class AddCoverPic(generics.CreateAPIView):
    parser_classes = (MultiPartParser, FormParser)

    authentication_classes = [OAuth2Authentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, **kwargs):
        up_file = request.FILES['file']

        username = self.request.user.username
        if not os.path.exists('static/' + username + '/cover_pic/'):
            os.makedirs('static/' + username + '/cover_pic/')

        unique_id = get_random_string(length=12)

        if os.path.exists('static/' + username + '/cover_pic/' + unique_id + up_file.name):
            return Response("name exists", status=status.HTTP_400_BAD_REQUEST)

        destination = open('static/' + username + '/cover_pic/' + unique_id + up_file.name, 'wb+')
        for chunk in up_file.chunks():
            destination.write(chunk)
            destination.close()

        user = User.objects.get(id=self.request.user.id)
        user.cover_picture = 'static/' + username + '/cover_pic/' + unique_id + up_file.name

        User.save(user)

        return Response("done")


class PostCreateView(generics.ListCreateAPIView):
    queryset = PostStat.objects.all()
    serializer_class = PostCreateSerializer
    authentication_classes = [OAuth2Authentication]
    permission_classes = [IsAuthenticated]

    pagination_class = PostOffSetLimitPagination

    def perform_create(self, serializer):
        user = self.request.user
        cat_id = self.request.POST.get('cat_id')
        category = Category.objects.get(id=cat_id)
        serializer.save(owner=user, category=category)


class PostUpdateView(generics.UpdateAPIView):
    parser_classes = (MultiPartParser, FormParser)

    queryset = PostStat.objects.all()
    serializer_class = PostSerializer

    authentication_classes = [OAuth2Authentication]
    permission_classes = [IsAuthenticated]

    def update(self, request, *args, **kwargs):

        instance = self.get_object()

        instance = PostStat.objects.get(pk=self.kwargs.get('pk'))

        cat_id = self.request.POST.get('cat_id')
        category = Category.objects.get(id=cat_id)
        name = self.request.POST.get('name')

        instance.category = category
        instance.owner = self.request.user
        instance.name = name

        instance.save()


        return Response("done", status=status.HTTP_201_CREATED)



class EventUpdateView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Event.objects.all()
    serializer_class = PostSerializer
    authentication_classes = [OAuth2Authentication]
    permission_classes = [IsAuthenticated, IsMine]


class PostDetailsView(generics.RetrieveAPIView):
    queryset = PostStat.objects.all()
    serializer_class = PostSerializer
    authentication_classes = [OAuth2Authentication]
    permission_classes = [IsAuthenticated]


class AllPostsView(generics.ListAPIView):
    queryset = PostStat.objects.all()
    serializer_class = PostSerializer
    authentication_classes = [OAuth2Authentication]
    permission_classes = [IsAuthenticated]

    filter_backends = (filters.SearchFilter,)
    search_fields = ('name',)


class MainFeed(generics.ListAPIView):
    serializer_class = PostSerializer
    authentication_classes = [OAuth2Authentication]
    permission_classes = [IsAuthenticated]

    pagination_class = PostOffSetLimitPagination

    def get_queryset(self):
        user = self.request.user
        following = user.following.all()

        users_ids = [follow.id for follow in following]
        users_ids = users_ids + [user.id]
        posts = PostStat.objects.filter(owner_id__in=users_ids).order_by('date_created').reverse()

     #   device = GCMDevice.objects.get(user=user)
      #  device.send_message("You've got mail",extra={"type":"notif"})

        return posts


class MainFeedEvents(generics.ListAPIView):
    serializer_class = EventSerializerMin
    authentication_classes = [OAuth2Authentication]
    permission_classes = [IsAuthenticated]

    pagination_class = PostOffSetLimitPagination

    def get_queryset(self):
        user = self.request.user
        following = user.following.all()

        users_ids = [follow.id for follow in following]
        users_ids = users_ids + [user.id]
        posts_non_expired = Event.objects.filter(date_end__gt= datetime.now()).order_by('date_beg')
    #    posts_expired = Event.objects.filter(date_end__lt= datetime.now()).order_by('date_end')

        posts = posts_non_expired.order_by('date_beg')

      #  posts = Event.objects.filter(owner_id__in=users_ids).order_by('date_beg')


        return posts


class MainCoursesFeed(generics.ListAPIView):
    serializer_class = CoursesSerializer
    authentication_classes = [OAuth2Authentication]
    permission_classes = [IsAuthenticated]

    pagination_class = PostOffSetLimitPagination

    def get_queryset(self):
        user = self.request.user
        following = user.following.all()

        users_ids = [follow.id for follow in following]
        users_ids = users_ids + [user.id]
        cours = Courses.objects.filter(owner_id__in=users_ids).order_by('date_created').reverse()

        return cours


class OwnPostsList(generics.ListAPIView):
    serializer_class = PostSerializer
    authentication_classes = [OAuth2Authentication]
    permission_classes = [IsAuthenticated]

    pagination_class = PostOffSetLimitPagination

    def get_queryset(self):
        user = self.request.user
        posts = PostStat.objects.filter(owner=user).order_by('date_created').reverse()

        return posts


class UserPostsList(generics.ListAPIView):
    serializer_class = PostSerializer
    authentication_classes = [OAuth2Authentication]
    permission_classes = [IsAuthenticated]

    pagination_class = PostOffSetLimitPagination

    def get_queryset(self):
        user = User.objects.get(pk=self.kwargs.get('pk'))
        posts = PostStat.objects.filter(owner=user).order_by('date_created').reverse()

        return posts


class CategoryCreateView(generics.CreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    authentication_classes = [OAuth2Authentication]
    permission_classes = [IsAuthenticated]

    pagination_class = PostOffSetLimitPagination

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(creator=user)


class CategoryListView(generics.ListAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    authentication_classes = [OAuth2Authentication]
    permission_classes = [IsAuthenticated]

    filter_backends = (filters.SearchFilter,)
    search_fields = ('name',)
    pagination_class = MessagesOffSetLimitPagination



class CategoryPubListView(generics.ListAPIView):
    """This class defines the create behavior of our rest api."""
    serializer_class = CategorySerializer
    authentication_classes = [OAuth2Authentication]
    permission_classes = [IsAuthenticated]

    filter_backends = (filters.SearchFilter,)
    search_fields = ('name',)
    pagination_class = MessagesOffSetLimitPagination


    def get_queryset(self):
        cats = Category.objects.filter(is_event=False)
        return cats



class CategoryEvnListView(generics.ListAPIView):
    """This class defines the create behavior of our rest api."""
    serializer_class = CategorySerializer
    authentication_classes = [OAuth2Authentication]
    permission_classes = [IsAuthenticated]

    filter_backends = (filters.SearchFilter,)
    search_fields = ('name',)
    pagination_class = MessagesOffSetLimitPagination

    def get_queryset(self):
        cats = Category.objects.filter(is_event=True)
        return cats





class CoursListView(generics.ListAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = Courses.objects.all()
    serializer_class = CoursesSerializer
    authentication_classes = [OAuth2Authentication]
    permission_classes = [IsAuthenticated]

    filter_backends = (filters.SearchFilter,)
    search_fields = ('name',)
    pagination_class = PostOffSetLimitPagination


class CategoryPostList(generics.ListAPIView):
    serializer_class = PostSerializer
    authentication_classes = [OAuth2Authentication]
    permission_classes = [IsAuthenticated]

    pagination_class = PostOffSetLimitPagination

    def get_queryset(self):
        category = Category.objects.get(pk=self.kwargs.get('pk'))
        posts = PostStat.objects.filter(category=category).order_by('date_created').reverse()

        return posts



@api_view(['PATCH'])
@permission_classes([IsAuthenticated])
@authentication_classes([OAuth2Authentication])
def like(request):
    id = request.POST.get('post_id')
    post = PostStat.objects.get(id=id)
    post.likes.add(request.user)

    # try:
    #
    #     device = GCMDevice.objects.get(user=post.owner)
    #     device.send_message(None, extra={"type": "other",
    #                                      "post_id": id,
    #                                      "name": "like",
    #                                      "mass": request.user.first_name + " " + request.user.last_name + " a aimé votre publication",
    #                                      "timestamp": datetime.now().strftime("%Y-%m-%d'T'%H:%M:%S"),
    #                                      "image": request.user.picture,})
    #
    # except GCMDevice.DoesNotExist:
    #     pass

    return Response('post liked')


@api_view(['PATCH'])
@permission_classes([IsAuthenticated])
@authentication_classes([OAuth2Authentication])
def unlike(request):
    id = request.POST.get('post_id')
    post = PostStat.objects.get(id=id)
    post.likes.remove(request.user)

    return Response('post unliked')


@api_view(['PATCH'])
@permission_classes([IsAuthenticated])
@authentication_classes([OAuth2Authentication])
def like_cours(request):
    id = request.POST.get('id')
    post = Courses.objects.get(id=id)
    post.likes.add(request.user)

    return Response('cours liked')


@api_view(['PATCH'])
@permission_classes([IsAuthenticated])
@authentication_classes([OAuth2Authentication])
def unlike_cours(request):
    id = request.POST.get('id')
    post = Courses.objects.get(id=id)
    post.likes.remove(request.user)

    return Response('cours unliked')


@api_view(['PATCH'])
@permission_classes([IsAuthenticated])
@authentication_classes([OAuth2Authentication])
def participate_event(request):

    id = request.POST.get('event_id')
    event = Event.objects.get(id=id)
    if(event.is_limited):
        if(event.get_particip_count()>= event.max_limit):
            return Response('not participated')
        else:
            event.participants.add(request.user)

            if(event.get_particip_count()>= event.max_limit):
                    participants = Event.get_participants(event).all()

               # for participant in participants:
                #    print(participant.id)

                    # try:
                    #     device = GCMDevice.objects.get(user=event.owner)
                    #
                    #     device.send_message(None, extra={"type": "event",
                    #                                      "post_id": event.id,
                    #                                      "name": "Evennement complet",
                    #                                      "mass": " Evennement " + event.name + " est complet",
                    #                                      "timestamp": datetime.now().strftime(
                    #                                          "%Y-%m-%d'T'%H:%M:%S"),
                    #                                      "image": event.picture_url, })
                    # except GCMDevice.DoesNotExist:
                    #     pass


            return Response('participated')

    else:
        event.participants.add(request.user)
        return Response('participated')



@api_view(['PATCH'])
@permission_classes([IsAuthenticated])
@authentication_classes([OAuth2Authentication])
def unparticipate_event(request):
    id = request.POST.get('event_id')
    post = Event.objects.get(id=id)
    post.participants.remove(request.user)

    return Response('unparticipated')




class UserNotifsView(generics.ListAPIView):
    serializer_class = NotifSerializer
    authentication_classes = [OAuth2Authentication]
    permission_classes = [IsAuthenticated]

    pagination_class = PostOffSetLimitPagination

    def get_queryset(self):
        user = self.request.user
        return user.get_notifs().all()



class UserSuggestionsView(generics.ListAPIView):
    """This class defines the create behavior of our rest api."""
    serializer_class = SuggestSerializer
    authentication_classes = [OAuth2Authentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return user.suggest.all()


class AddCourseFile(generics.CreateAPIView):
    parser_classes = (MultiPartParser, FormParser)

    authentication_classes = [OAuth2Authentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, **kwargs):
        up_file = request.FILES['file']

        username = self.request.user.username
        if not os.path.exists('static/' + username + '/cours'):
            os.makedirs('static/' + username + '/cours')

        unique_id = get_random_string(length=12)

        if os.path.exists('static/' + username + '/cours/' + unique_id + up_file.name):
            return Response("name exists", status=status.HTTP_400_BAD_REQUEST)

        destination = open('static/' + username + '/cours/' + unique_id + up_file.name, 'wb+')
        for chunk in up_file.chunks():
            destination.write(chunk)
            destination.close()

        serializer = CoursesSerializer(data=self.request.data)

        if (self.request.user.department is None):
            depart = None

        else:
            if (self.request.user.is_admin):
                dep = self.request.POST.get('dep_id')
                depart = Department.objects.get(id=dep)

            else:
                depart = self.request.user.department

        if serializer.is_valid():
            serializer.save(department=depart, name=up_file.name,
                            file_path='static/' + username + '/cours/' + unique_id + up_file.name,
                            owner=self.request.user)

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


        #   return Response(up_file.name, status.HTTP_201_CREATED)


class MyCoursesView(generics.ListAPIView):
    """This class defines the create behavior of our rest api."""
    #  queryset = Courses.objects.all()
    serializer_class = CoursesSerializer
    authentication_classes = [OAuth2Authentication]
    permission_classes = [IsAuthenticated]
    pagination_class = PostOffSetLimitPagination

    def get_queryset(self):
        user = self.request.user
        return user.courses.all()


class UserCoursesView(generics.ListAPIView):
    """This class defines the create behavior of our rest api."""
    #  queryset = Courses.objects.all()
    serializer_class = CoursesSerializer
    authentication_classes = [OAuth2Authentication]
    permission_classes = [IsAuthenticated]
    pagination_class = PostOffSetLimitPagination

    def get_queryset(self):
        user = User.objects.get(pk=self.kwargs.get('pk'))
        return user.courses.all()



class DepCoursesView(generics.ListAPIView):
    serializer_class = CoursesSerializer
    authentication_classes = [OAuth2Authentication]
    permission_classes = [IsAuthenticated]

    pagination_class = PostOffSetLimitPagination

    def get_queryset(self):
        department = Department.objects.get(pk=self.kwargs.get('pk'))
        courses = Department.get_dep_courses(department).all()
        return courses





class EventCreateView(generics.ListCreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    authentication_classes = [OAuth2Authentication]
    permission_classes = [IsAuthenticated]

    pagination_class = PostOffSetLimitPagination

    def perform_create(self, serializer):
        user = self.request.user
        cat_id = self.request.POST.get('cat_id')
        category = Category.objects.get(id=cat_id)

        serializer.save(owner=user, category=category)


class AllEventsView(generics.ListAPIView):
    queryset = Event.objects.all().order_by('date_beg')
    serializer_class = EventSerializerMin
    authentication_classes = [OAuth2Authentication]
    permission_classes = [IsAuthenticated]

    filter_backends = (filters.SearchFilter,)
    search_fields = ('name',)

    pagination_class = PostOffSetLimitPagination


class EventView(generics.RetrieveAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializerMin
    authentication_classes = [OAuth2Authentication]
    permission_classes = [IsAuthenticated]

    pagination_class = PostOffSetLimitPagination


class OwnEventsList(generics.ListAPIView):
    serializer_class = EventSerializer
    authentication_classes = [OAuth2Authentication]
    permission_classes = [IsAuthenticated]

    pagination_class = PostOffSetLimitPagination

    def get_queryset(self):
        user = self.request.user
        events = Event.objects.filter(owner=user).order_by('date_created').reverse()

        return events


class UserEventsList(generics.ListAPIView):
    serializer_class = EventSerializer
    authentication_classes = [OAuth2Authentication]
    permission_classes = [IsAuthenticated]

    pagination_class = PostOffSetLimitPagination

    def get_queryset(self):
        user = User.objects.get(pk=self.kwargs.get('pk'))
        events = Event.objects.filter(owner=user).order_by('date_created').reverse()

        return events




class UserFollowers(generics.ListAPIView):
    serializer_class = UserSerializer
    authentication_classes = [OAuth2Authentication]
    permission_classes = [IsAuthenticated]

    filter_backends = (filters.SearchFilter,)
    search_fields = ('username', 'email', 'first_name', 'last_name')
    pagination_class = MessagesOffSetLimitPagination

    def get_queryset(self):
        user = User.objects.get(pk=self.kwargs.get('pk'))
        followers = user.followers.all()

        return followers


class UserFollowing(generics.ListAPIView):
    serializer_class = UserSerializer
    authentication_classes = [OAuth2Authentication]
    permission_classes = [IsAuthenticated]

    filter_backends = (filters.SearchFilter,)
    search_fields = ('username', 'email', 'first_name', 'last_name')
    pagination_class = MessagesOffSetLimitPagination

    def get_queryset(self):
        user = User.objects.get(pk=self.kwargs.get('pk'))
        following = user.following.all()

        return following





@api_view(['POST'])
@permission_classes([IsAuthenticated])
@authentication_classes([OAuth2Authentication])
def Test(request):
    data = request.data["dat"]
    req = request.POST.get('https://api.coursera.org/api/courses.v1?q=search&query = machine + learning')

    json_data = json.loads(req.text)
    s=""

    for element in json_data['elements']:
         s= s + (element['name'])
    return Response (s)
