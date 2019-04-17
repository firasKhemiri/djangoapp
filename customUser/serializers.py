import datetime
from django.contrib.auth import get_user_model
# from push_notifications.models import GCMDevice
from rest_framework import serializers

from customUser.models import User, Commentaire, PostStat, Message, Conversation, Category, Notification, \
    Suggest, Courses, Department, Event, Classe, Pending, Schedule, Notes, OtherDocs

"""
class SchoolSerializer(serializers.ModelSerializer):

    owner = serializers.ReadOnlyField(source='owner.username')
    owner_id = serializers.ReadOnlyField(source='owner.id')
    students_count = serializers.ReadOnlyField( read_only=True, source='get_students_count')
    adr = serializers.SerializerMethodField('get_address')

    students_only_count = serializers.SerializerMethodField('get_stud_only_count')
    profs_count = serializers.SerializerMethodField('get_prfs_count')
    departments_count = serializers.SerializerMethodField('get_deps_count')

    ibelong = serializers.SerializerMethodField('get_is_belong')

    user_has_school = serializers.SerializerMethodField('get_has_school')

    pending = serializers.SerializerMethodField('get_requested')


    pic_url = serializers.ReadOnlyField(source='owner.picture')
    cover_pic = serializers.ReadOnlyField(source='owner.cover_picture')

    class Meta:
        model = School
        fields = ('id','name','description','adr','owner','owner_id','students_count','students_only_count','profs_count','departments_count','pic_url','cover_pic',
                  'ibelong','user_has_school','pending')



    def get_is_belong(self, obj):
        try:
            is_belong = False
            school = obj
            me = self.context['request'].user

            if school.owner == me or me.belongsTo == school:
                is_belong = True

            return is_belong

        except IndexError:
            return None


    def get_has_school(self, obj):
        try:
            has_school = False
            me = self.context['request'].user

            if me.belongsTo != None:
                has_school = True

            return has_school

        except IndexError:
            return None



    def get_requested(self, obj):
        try:
            requested = False
            me = self.context['request'].user

            pendings = School.get_pendings(obj).all()


            for pending in pendings:
                if pending.user.id == me.id:
                    requested = True

            return requested

        except IndexError:
            return None


    def get_stud_only_count(self,obj):
        try:
            students_count = School.get_students(obj).filter(is_professor=False).count()
            return students_count

        except IndexError:
            return None

    def get_prfs_count(self,obj):
        try:
            profs = School.get_students(obj).filter(is_professor=True).count()
            return profs

        except IndexError:
            return None


    def get_deps_count(self,obj):
        try:
            deps = School.get_deps(obj).count()
            return deps

        except IndexError:
            return None



    def get_address(self,obj):
        try:
            school = obj
            adr = school.owner.location

            return adr

        except IndexError:
            return None

"""


class DepSerializer(serializers.ModelSerializer):
    students_count = serializers.ReadOnlyField(read_only=True, source='get_students_count')
    students = serializers.ReadOnlyField(read_only=True, source='get_students')
    branches = serializers.ReadOnlyField(read_only=True, source='get_dep_branches')
    branches_count = serializers.ReadOnlyField(read_only=True, source='get_dep_branches_count')

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Department
        fields = ('id', 'name', 'description', 'students_count', 'students', 'branches_count', 'branches')

        read_only_fields = ()


class DepSerializerMin(serializers.ModelSerializer):
    branches_count = serializers.ReadOnlyField(read_only=True, source='get_dep_branches_count')

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Department
        fields = ('id', 'name', 'description', 'branches_count')

        read_only_fields = ()


class BranchSerializer(serializers.ModelSerializer):
    classes_count = serializers.ReadOnlyField(read_only=True, source='get_classes_count')

    #  classes = serializers.ReadOnlyField(read_only=True, source='get_classes')
    #  students_count = serializers.ReadOnlyField(read_only=True, source='get_students_count')
    #  students = serializers.ReadOnlyField(read_only=True, source='get_students')

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Classe
        fields = ('id', 'name', 'description', 'classes_count')

        read_only_fields = ()


class BranchSerializerMin(serializers.ModelSerializer):
    classes_count = serializers.ReadOnlyField(read_only=True, source='get_classes_count')

    #  classes = serializers.ReadOnlyField(read_only=True, source='get_classes')
    #  students_count = serializers.ReadOnlyField(read_only=True, source='get_students_count')
    #  students = serializers.ReadOnlyField(read_only=True, source='get_students')

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Classe
        fields = ('id', 'name', 'description', 'classes_count')

        read_only_fields = ()


class ClasseSerializer(serializers.ModelSerializer):
    students_count = serializers.ReadOnlyField(read_only=True, source='get_students_count')
    #  students = serializers.ReadOnlyField(read_only=True, source='get_students')

    branch = BranchSerializer(read_only=True)

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Classe
        fields = ('id', 'name', 'description', 'students_count', 'branch')

        read_only_fields = ()


class ClasseSerializerMin(serializers.ModelSerializer):
    students_count = serializers.ReadOnlyField(read_only=True, source='get_students_count')
    #  students = serializers.ReadOnlyField(read_only=True, source='get_students')

    branch = BranchSerializerMin(read_only=True)

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Classe
        fields = ('id', 'name', 'description', 'students_count', 'year', 'branch')

        read_only_fields = ()


class UserSerializer(serializers.ModelSerializer):
    classe = ClasseSerializerMin(read_only=True)
    followers_count = serializers.ReadOnlyField(read_only=True, source='get_followers_count')
    following_count = serializers.ReadOnlyField(read_only=True, source='get_following_count')

    # unssen_count = serializers.SerializerMethodField('get_unseen_conversations')



    ifollow = serializers.SerializerMethodField('get_is_following')

    messages_count = serializers.SerializerMethodField('get_mess_counts')
    messages_ids = serializers.SerializerMethodField('get_mess_ids')
    convo_id = serializers.SerializerMethodField('get_covo_id')

    notifs_count = serializers.SerializerMethodField('get_notifs_counts')

    my_id = serializers.SerializerMethodField('_user')

    birthdate = serializers.DateField(format="%d/%m/%Y")

    class Meta:
        model = get_user_model()
        exclude = ('is_staff', 'is_active', 'date_joined',
                   'last_login', 'user_permissions', 'groups', 'is_superuser')

        read_only_fields = ('followers', 'following')

        extra_kwargs = {'password': {'write_only': True}}

    def _user(self, obj):
        user = self.context['request'].user.id

        return user

    def get_notifs_counts(self, obj):
        user = self.context['request'].user
        count = 0

        for i in User.get_notifs(user).all():
            if (i.seen == False):
                count = count + 1

        return count

    def get_mess_counts(self, obj):
        user = self.context['request'].user
        count = 0

        for i in User.get_conversations(user).all():
            if ((Conversation.get_last_message(i).seen == False) and (
                        Conversation.get_last_message(i).reciever == user)):
                count = count + 1

        return count

    #    return User.get_conversations(user).all().count()


    def get_mess_ids(self, obj):
        user = self.context['request'].user

        tup = ()

        if (User.get_conversations(user).all().count() > 0):
            for i in User.get_conversations(user).all():
                if ((Conversation.get_last_message(i).seen == False) and (
                            Conversation.get_last_message(i).reciever == user)):
                    tup2 = (Conversation.get_last_message(i).sender_id,)
                    tup = tup + tup2
        return tup

    def get_covo_id(self, obj):
        user = self.context['request'].user

        tup = 0

        if (User.get_conversations(user).all().count() > 0):
            for i in User.get_conversations(user).all():
                if (Conversation.get_last_message(i).reciever == obj) or (
                            Conversation.get_last_message(i).sender == obj):
                    tup = Conversation.get_convo_id(i)
                    break
        return tup

    def get_is_following(self, obj):
        try:
            is_following = False
            user = obj.id

            me = self.context['request'].user
            following = me.following.all()

            for user_id in following:
                if user == user_id.id:
                    is_following = True

            return is_following

        except IndexError:
            return None


class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        exclude = ('is_staff', 'is_active', 'date_joined',
                   'last_login', 'user_permissions', 'groups', 'is_superuser')

        read_only_fields = ('followers', 'following')

        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            username=validated_data['username'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            birthdate=validated_data['birthdate'],

            #  birthdate = datetime.datetime.strptime(validated_data['birthday'], '%d/%m/%Y').strftime('%Y-%m-%d')

        )

        user.set_password(validated_data['password'])
        user.save()

        return user


class MinUserSerializer(serializers.ModelSerializer):
    ifollow = serializers.SerializerMethodField('get_is_following')

    def get_is_following(self, obj):
        try:
            is_following = False
            user = obj.id

            me = self.context['request'].user
            following = me.following.all()

            for user_id in following:
                if user == user_id.id:
                    is_following = True

            return is_following

        except IndexError:
            return None

    class Meta:
        model = get_user_model()

        fields = ('id', 'first_name', 'last_name', 'picture', 'is_social', 'ifollow')


class ScUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()

        fields = (
            'id', 'first_name', 'last_name', 'picture', 'is_social', 'classe', 'is_professor', 'is_admin')


class ProfileSerializer(serializers.ModelSerializer):
    current_user = serializers.SerializerMethodField('_user')

    def _user(self, obj):
        user = self.context['request'].user
        return user

    class Meta:
        model = get_user_model()
        exclude = ('is_staff', 'is_active', 'date_joined',
                   'last_login', 'user_permissions', 'groups', 'is_superuser',)

        extra_kwargs = {'password': {'write_only': True}}



class CategorySerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""
    # creator = serializers.ReadOnlyField(source='creator.username')
    creator = MinUserSerializer(read_only=True)


    num_posts = serializers.ReadOnlyField(read_only=True, source='get_posts_count')
    num_events = serializers.ReadOnlyField(read_only=True, source='get_events_count')

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Category
        fields = ('id', 'name', 'description', 'creator', 'date_created', 'date_modified', 'pic_url','is_event','num_events','num_posts')
        read_only_fields = ('date_created', 'date_modified')




class CommentaireSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""
    owner = MinUserSerializer(read_only=True)

    my_id = serializers.SerializerMethodField('_user')

    def _user(self, obj):
        user = self.context['request'].user.id
        return user

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Commentaire
        fields = ('id', 'comment', 'owner', 'date_created', 'date_modified', 'my_id')
        read_only_fields = ('date_created', 'date_modified')


"""
class PostStatSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')


    class Meta:
        model = PostStat
        fields = ('id','name', 'owner', 'date_created', 'date_modified','likes','comments')
        read_only_fields = ('date_created', 'date_modified')

"""


class MessageSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""
    conversation = serializers.ReadOnlyField(source='conversation.id')
    sender = serializers.ReadOnlyField(source='sender.id')

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Message
        fields = ('id', 'sender', 'reciever', 'content', 'date_created', 'conversation', 'seen')


class ConversationSerializer(serializers.ModelSerializer):
    message = MessageSerializer(read_only=True, source='get_last_message')

    my_id = serializers.SerializerMethodField('_user')

    users = MinUserSerializer(read_only=True, many=True)

    def _user(self, obj):
        user = self.context['request'].user.id
        return user

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Conversation
        fields = ('id', 'users', 'message', 'my_id', 'date_created', 'date_modified')
        read_only_fields = ('date_created', 'date_modified')


class PostSerializer(serializers.ModelSerializer):
    owner = MinUserSerializer()
    category = CategorySerializer()
    category_name = serializers.ReadOnlyField(source='category.name')
    num_likes = serializers.ReadOnlyField(read_only=True, source='get_likes_count')
    num_comments = serializers.ReadOnlyField(read_only=True, source='get_comments_count')
    is_liked = serializers.SerializerMethodField('get_is_post_liked')

    my_id = serializers.SerializerMethodField('_user')

    def _user(self, obj):
        user = self.context['request'].user.id
        return user

    def get_is_post_liked(self, obj):
        try:
            is_liked = False
            users = obj.likes.all()
            user = [user.id for user in users]
            user_id = self.context['request'].user.id

            for user in users:
                if user.id == user_id:
                    is_liked = True

            return is_liked

        except IndexError:
            return None

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = PostStat
        fields = ('id', 'name', 'description', 'owner', 'category', 'date_created', 'date_modified', 'likes', 'comments'
                  , 'is_picture', 'picture_url', 'is_liked', 'num_likes', 'num_comments', 'my_id','category_name')

        read_only_fields = ('date_created', 'date_modified')

class PostCreateSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    category = serializers.ReadOnlyField(source='category.id')

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = PostStat
        fields = ('id', 'name', 'description', 'owner', 'category', 'date_created', 'date_modified', 'likes', 'comments'
                  , 'is_picture', 'picture_url')

        read_only_fields = ('date_created', 'date_modified')

class EventCreateSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    category = serializers.ReadOnlyField(source='category.id')

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Event
        fields = ('id', 'name', 'description', 'owner', 'category', 'date_created', 'date_modified', 'date_beg', 'date_end','location'
                  , 'is_picture', 'picture_url','is_limited','max_limit','lat','lng')



        read_only_fields = ('date_created', 'date_modified')

class CategoryPostsSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""
    creator = serializers.ReadOnlyField(source='creator.username')
    posts = PostSerializer(many=True, read_only=True, source='get_posts')

    class Meta:
        model = Category
        fields = ('id', 'name', 'description', 'posts', 'creator', 'date_created', 'date_modified')
        read_only_fields = ('date_created', 'date_modified')


class NotifSerializer(serializers.ModelSerializer):
    #  owner = serializers.ReadOnlyField(source='owner.name')
    owner = ScUserSerializer(read_only=True)

    # student = serializers.ReadOnlyField(source='students.username

    class Meta:
        model = Notification
        fields = ('id', 'name', 'owner', 'description', 'students', 'date_created', 'date_modified')
        read_only_fields = ('date_created', 'date_modified', 'owner', 'students',)


class SuggestSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Suggest
        fields = ('id', 'name', 'description', 'owner', 'date_created', 'date_modified',
                  'is_picture', 'picture_url', 'is_problem', 'is_anonymous')
        read_only_fields = ('date_created', 'date_modified')


class CoursesSerializer(serializers.ModelSerializer):
    owner = MinUserSerializer(read_only=True)
    department = serializers.ReadOnlyField(source='department.name')

    num_likes = serializers.ReadOnlyField(read_only=True, source='get_likes_count')
    num_comments = serializers.ReadOnlyField(read_only=True, source='get_comments_count')
    is_liked = serializers.SerializerMethodField('get_is_post_liked')

    def get_is_post_liked(self, obj):
        try:
            is_liked = False
            users = obj.likes.all()
            user = [user.id for user in users]
            user_id = self.context['request'].user.id

            for user in users:
                if user.id == user_id:
                    is_liked = True

            return is_liked

        except IndexError:
            return None

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Courses
        fields = ('id', 'name', 'description', 'owner', 'date_created', 'date_modified', 'file_path', 'department',
                  'is_liked', 'num_likes', 'num_comments')

        read_only_fields = ('date_created', 'date_modified', 'file_path', 'name', 'department')


class ScheduleSerializer(serializers.ModelSerializer):
    creator = serializers.ReadOnlyField(source='creator.name')

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Schedule
        fields = ('id', 'name', 'description', 'creator', 'date_created', 'date_modified', 'file_path')
        read_only_fields = ('date_created', 'date_modified', 'file_path', 'name', 'creator')


class NotesSerializer(serializers.ModelSerializer):
    creator = serializers.ReadOnlyField(source='creator.name')

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Notes
        fields = ('id', 'name', 'description', 'creator', 'date_created', 'date_modified', 'file_path')
        read_only_fields = ('date_created', 'date_modified', 'file_path', 'name', 'creator')


class OtherDocsSerializer(serializers.ModelSerializer):
    creator = serializers.ReadOnlyField(source='creator.name')

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = OtherDocs
        fields = ('id', 'name', 'description', 'creator', 'date_created', 'date_modified', 'file_path')
        read_only_fields = ('date_created', 'date_modified', 'file_path', 'name', 'creator')


class EventSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""
    owner = MinUserSerializer(read_only=True)

    category = CategorySerializer(read_only=True)

    participants = MinUserSerializer(read_only=True, many=True)
    is_participated = serializers.SerializerMethodField('get_is_particip')

    particip_count = serializers.ReadOnlyField(read_only=True, source='get_particip_count')

    my_id = serializers.SerializerMethodField('_user')

    get_particip_follow = serializers.SerializerMethodField('get_particip_follo',read_only=True)


    def _user(self, obj):
        user = self.context['request'].user.id
        return user

    def get_is_particip(self, obj):
        try:
            is_particip = False
            users = obj.participants.all()
            user = [user.id for user in users]
            user_id = self.context['request'].user.id

            for user in users:
                if user.id == user_id:
                    is_particip = True

            return is_particip

        except IndexError:
            return None

    def get_particip_follo(self, obj):
        try:
            user = self.context['request'].user
            following = user.following.all()
            participants = Event.get_participants(obj).all()

            var = [x for x in following if x in participants]

            return ScUserSerializer(var, many=True).data

        except IndexError:
            return None



    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Event
        fields = (
            'id', 'name', 'description', 'owner', 'date_created', 'date_modified', 'participants', 'date_beg',
            'date_end',
            'picture_url', 'is_picture',
            'is_participated', 'location', 'my_id', 'particip_count','category','lat','lng','get_particip_follow','is_limited','max_limit')

        read_only_fields = ('date_created', 'date_modified', 'is_participated')




class EventSerializerMin(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""
    owner = MinUserSerializer(read_only=True)

    category = CategorySerializer()

    is_participated = serializers.SerializerMethodField('get_is_particip')

    particip_count = serializers.ReadOnlyField(read_only=True, source='get_particip_count')

    my_id = serializers.SerializerMethodField('_user')

    get_particip_follow = serializers.SerializerMethodField('get_particip_follo',read_only=True)

    get_is_limit = serializers.SerializerMethodField('get_is_limit_reached',read_only=True)

    def _user(self, obj):
        user = self.context['request'].user.id
        return user


    def get_is_limit_reached(self, obj):
        if(obj.is_limited == True):
            if(Event.get_particip_count(obj)>= obj.max_limit):
                return True
            else:
                return False

        else:
            return False

    def get_is_particip(self, obj):
        try:
            is_particip = False
            users = obj.participants.all()
            user = [user.id for user in users]
            user_id = self.context['request'].user.id

            for user in users:
                if user.id == user_id:
                    is_particip = True

            return is_particip

        except IndexError:
            return None

    def get_particip_follo(self, obj):
        try:
            user = self.context['request'].user
            following = user.following.all()
            participants = Event.get_participants(obj).all()

            var = [x for x in following if x in participants]

            return ScUserSerializer(var, many=True).data

        except IndexError:
            return None



    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Event
        fields = (
            'id', 'name', 'description', 'owner', 'date_created', 'date_modified', 'date_beg',
            'date_end',
            'picture_url', 'is_picture',
            'is_participated', 'location', 'my_id', 'particip_count','category','lat','lng','get_particip_follow','get_is_limit','is_limited','max_limit')

        read_only_fields = ('date_created', 'date_modified', 'is_participated')


class PendingSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""

    # user_name = serializers.ReadOnlyField( read_only=True, source='get_full_name')
    classe = serializers.ReadOnlyField(source='classe.name')
    department = serializers.ReadOnlyField(source='department.name')
    user = MinUserSerializer(read_only=True)

    class Meta:
        model = Pending
        fields = ('id', 'user', 'date_created', 'is_professor', 'classe', 'department', 'message', 'accepted')
        read_only_fields = ('date_created',)

#
# class FCMSerializer(serializers.ModelSerializer):
#     owner = MinUserSerializer(read_only=True)
#
#     class Meta:
#         """Meta class to map serializer's fields with the model fields."""
#         model = GCMDevice
#         exclude = ('cloud_message_type',)
