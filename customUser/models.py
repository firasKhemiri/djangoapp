import os
import urllib.request

from decimal import Decimal
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import m2m_changed
from django.utils.crypto import get_random_string
from rest_framework.exceptions import ValidationError



class Department(models.Model):
    name = models.CharField(max_length=255, blank=False, unique=True)
    description = models.CharField(max_length=255, blank=False, unique=True)


    def __str__(self):
        return self.name

    def get_dep_students(self):
        try:
            return self.dep_branches.model.get_students(Branch.get)
        except IndexError:
            return None

    def get_students_count(self):
        try:
            return self.dep_branches.branch_classes.class_students.count()
        except IndexError:
            return None

    def get_dep_courses(self):
        try:
            return self.dep_courses
        except IndexError:
            return None

    def get_dep_branches(self):
        try:
            return self.dep_branches
        except IndexError:
            return None


class Branch(models.Model):
    name = models.CharField(max_length=255, blank=False, unique=True)
    description = models.CharField(max_length=255, blank=False, unique=True)

    department = models.ForeignKey(Department, related_name='dep_branches', blank=True, null=True,
                                   on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_students_count(self):
        try:
            return self.branch_classes.class_students.count()
        except IndexError:
            return None

    def get_students(self):
        try:
            return self.branch_classes.class_students
        except IndexError:
            return None

    def get_classes_count(self):
        try:
            return self.branch_classes.count()
        except IndexError:
            return None

    def get_classes(self):
        try:
            return self.branch_classes
        except IndexError:
            return None


class Classe(models.Model):
    name = models.CharField(max_length=255, blank=False, unique=True)
    description = models.CharField(max_length=255, blank=False, unique=False)
    year = models.IntegerField(blank=False, null=True)

    branch = models.ForeignKey(Branch, related_name='branch_classes', blank=True, null=True,
                                   on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_students_count(self):
        try:
            return self.class_students.count()
        except IndexError:
            return None

    def get_students(self):
        try:
            return self.class_students
        except IndexError:
            return None


class Conversation(models.Model):
    users = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        verbose_name='Users',
        related_name='conversations')

    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-pk',)
        verbose_name = 'Conversation'
        verbose_name_plural = 'Conversations'

    def __str__(self):
        return '{}'.format(self.pk)

    def get_last_message(self):
        try:
            return self.messages.order_by('-id')[0]
        except IndexError:
            return None

    def get_convo_id(self):
        try:
            return self.id
        except IndexError:
            return None

    def get_seen(self):
        try:
            if not self.messages.order_by('-id')[0].seen:
                return False
            else:
                return True
        except IndexError:
            return None

    def get_all_messages(self):
        try:
            return self.messages.order_by('-id').all()
        except IndexError:
            return None


class Message(models.Model):
    sender = models.ForeignKey(settings.AUTH_USER_MODEL,
                               related_name='sender',
                               on_delete=models.CASCADE)

    reciever = models.ForeignKey(settings.AUTH_USER_MODEL,
                                 related_name='reciever',
                                 on_delete=models.CASCADE)

    content = models.TextField(max_length=6255, blank=False, unique=False)

    date_created = models.DateTimeField(auto_now_add=True)

    conversation = models.ForeignKey(Conversation, verbose_name='Conversation',
                                     related_name='messages',
                                     on_delete=models.CASCADE)

    seen = models.BooleanField(default=False)


class User(AbstractUser):
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birthdate = models.DateField(null=True, blank=False)
    gender = models.CharField(max_length=6, blank=True)
    picture = models.CharField(max_length=255, blank=True)
    cover_picture = models.CharField(max_length=255, blank=True)

    phone = models.CharField(max_length=8, blank=True)

    following = models.ManyToManyField('self', related_name="who_follows", symmetrical=False, blank=True)
    followers = models.ManyToManyField('self', related_name="who_is_followed", symmetrical=False, blank=True)

    is_admin = models.BooleanField(default=False)

    is_professor = models.BooleanField(default=False)

    is_social = models.BooleanField(default=False)

    first_social = models.BooleanField(default=True)

    classe = models.ForeignKey(Classe, related_name='class_students', blank=True, null=True, on_delete=models.CASCADE)

    AbstractUser._meta.get_field('email')._unique = True

    #   AbstractUser._meta.get_field('email').null = False


    class Meta:
        db_table = 'auth_user'

    def conversation_changed(sender, **kwargs):
        if kwargs['instance'].users.count() > 2:
            raise ValidationError("You can only assign two users")

    m2m_changed.connect(conversation_changed, sender=Conversation.users.through)

    def get_conversations(self):
        try:
            return self.conversations
        except IndexError:
            return None

    def get_unseen_conv(self):
        try:
            return Conversation.get_seen(self.conversations)
        except IndexError:
            return None

    def get_posts(self):
        try:
            return self.user_post
        except IndexError:
            return None

    def get_notifs(self):
        try:
            return self.notifications
        except IndexError:
            return None

    def get_suggestions(self):
        try:
            return self.suggest
        except IndexError:
            return None

    def get_following_count(self):
        try:
            return self.following.count()
        except IndexError:
            return None

    def get_followers_count(self):
        try:
            return self.followers.count()
        except IndexError:
            return None

    def get_following(self):
        try:
            return self.following.all()
        except IndexError:
            return None

    def get_followers(self):
        try:
            return self.followers.all()
        except IndexError:
            return None

    def get_full_name(self):
        try:
            return self.first_name + ' ' + self.last_name
        except IndexError:
            return None


def save_profile(backend, user, response, *args, **kwargs):
  #  user.gender = response['gender']

    # user.birthdate= datetime.datetime.strptime(response['birthday'], '%m/%d/%Y').strftime('%Y-%m-%d')
    user.is_social = True

    if user.first_social:

        user.picture = response['picture']['data']['url']

        username = user.username
        if not os.path.exists('static/' + username + '/profle_pic/'):
            os.makedirs('static/' + username + '/profle_pic/')

        unique_id = get_random_string(length=12)

        urllib.request.urlretrieve(user.picture,
                                   'static/' + username + '/profle_pic/' + unique_id + '.jpg')

        user.picture = 'static/' + username + '/profle_pic/' + unique_id + '.jpg'

        user.first_social = False

    user.save()


class Commentaire(models.Model):
    comment = models.CharField(max_length=255, blank=False)

    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    owner = models.ForeignKey(settings.AUTH_USER_MODEL,
                              related_name='post',
                              on_delete=models.CASCADE)

    def __str__(self):
        """Return a human readable representation of the model instance."""
        return "{}".format(self.comment)


class Post(models.Model):
    name = models.CharField(max_length=255, blank=True, unique=False)
    description = models.CharField(max_length=10255, blank=True, unique=False)

    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        """Return a human readable representation of the model instance."""
        return "{}".format(self.name)

    class Meta:
        abstract = True


class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.CharField(max_length=10255, blank=True, unique=False)

    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    pic_url = models.CharField(max_length=255, unique=False, blank=True)

    is_event = models.BooleanField(default=False)

    creator = models.ForeignKey(settings.AUTH_USER_MODEL,
                                related_name='created_category',
                                on_delete=models.CASCADE,
                                null=True)

    def __str__(self):
        return self.name

    def get_posts(self):
        try:
            return self.CategoryPost.order_by('-id')
        except IndexError:
            return None

    def get_posts_count(self):
        try:
            return self.CategoryPost.count()
        except IndexError:
            return None

    def get_events_count(self):
        try:
            return self.CategoryEvent.count()
        except IndexError:
            return None

class PostStat(Post):
    picture_url = models.CharField(max_length=200, blank=True)
    is_picture = models.BooleanField(default=False)

    category = models.ForeignKey(Category,
                                 related_name='CategoryPost',
                                 on_delete=models.CASCADE)

    owner = models.ForeignKey(settings.AUTH_USER_MODEL,
                              related_name='user_post',
                              on_delete=models.CASCADE)

    likes = models.ManyToManyField(User, related_name="likes", symmetrical=False, blank=True)
    comments = models.ManyToManyField(Commentaire, related_name="comments", symmetrical=False, blank=True)

    def __str__(self):
        """Return a human readable representation of the model instance."""
        return "{}".format(self.name)

    def get_likes_count(self):
        try:
            return self.likes.count()
        except IndexError:
            return None

    def get_comments_count(self):
        try:
            return self.comments.count()
        except IndexError:
            return None

    def get_comments(self):
        try:
            return self.comments.order_by('-id').all()
        except IndexError:
            return None





class Event(Post):
    participants = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        verbose_name='User',
        related_name='events', blank=True)

    picture_url = models.CharField(max_length=200, blank=True)
    is_picture = models.BooleanField(default=False)

    location = models.CharField(max_length=255, blank=True, unique=False)

    date_beg = models.DateTimeField()
    date_end = models.DateTimeField()

    owner = models.ForeignKey(settings.AUTH_USER_MODEL,
                              related_name='user_events',
                              on_delete=models.CASCADE)


    is_limited = models.BooleanField(default=False)
    max_limit = models.IntegerField(blank=True, null=True)

    lat = models.DecimalField(max_digits=10, decimal_places=8, default=Decimal(0.00))
    lng = models.DecimalField(max_digits=10, decimal_places=8, default=Decimal(0.00))


    category = models.ForeignKey(Category,
                                 related_name='CategoryEvent',
                                 on_delete=models.CASCADE,null=True, blank=True)

    def __str__(self):
        """Return a human readable representation of the model instance."""
        return "{}".format(self.name)

    def get_particip_count(self):
        try:
            return self.participants.count()
        except IndexError:
            return None

    def get_participants(self):
        try:
            return self.participants
        except IndexError:
            return None



class Notification(models.Model):
    name = models.CharField(max_length=255, blank=True, unique=False)
    description = models.CharField(max_length=255, blank=True, unique=False)

    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    owner = models.ForeignKey(settings.AUTH_USER_MODEL,
                              related_name='notifs',
                              on_delete=models.CASCADE)

    is_class = models.BooleanField(default=False)
    is_depp = models.BooleanField(default=False)

    seen = models.BooleanField(default=False)

    students = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        verbose_name='students',
        related_name='notifications')

    def __str__(self):
        """Return a human readable representation of the model instance."""
        return "{}".format(self.name)


class Suggest(models.Model):
    name = models.CharField(max_length=255, blank=False, unique=False)
    description = models.CharField(max_length=255, blank=True, unique=False)

    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    owner = models.ForeignKey(settings.AUTH_USER_MODEL,
                              related_name='suggest',
                              on_delete=models.CASCADE)

    picture_url = models.CharField(max_length=200, blank=True)
    is_picture = models.BooleanField(default=False)
    is_problem = models.BooleanField(default=False)
    is_anonymous = models.BooleanField(default=False)

    def __str__(self):
        """Return a human readable representation of the model instance."""
        return "{}".format(self.name)


class Schedule(models.Model):
    name = models.CharField(max_length=255, unique=False)
    description = models.CharField(max_length=255, blank=True, unique=False)

    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    file_path = models.CharField(max_length=255, unique=False)


class Notes(models.Model):
    name = models.CharField(max_length=255, unique=False)
    description = models.CharField(max_length=255, blank=True, unique=False)

    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)


    file_path = models.CharField(max_length=255, unique=False)


class OtherDocs(models.Model):
    name = models.CharField(max_length=255, unique=False)
    description = models.CharField(max_length=255, blank=True, unique=False)

    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)


    file_path = models.CharField(max_length=255, unique=False)


class Courses(models.Model):
    name = models.CharField(max_length=255, unique=False)
    description = models.CharField(max_length=255, blank=True, unique=False)

    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    file_path = models.CharField(max_length=255, unique=True)

    owner = models.ForeignKey(settings.AUTH_USER_MODEL,
                              related_name='courses',
                              on_delete=models.CASCADE)

    department = models.ForeignKey(Department, related_name='dep_courses', blank=True, null=True,
                                   on_delete=models.CASCADE)

    likes = models.ManyToManyField(User, related_name="cours_likes", symmetrical=False, blank=True)
    comments = models.ManyToManyField(Commentaire, related_name="cours_comments", symmetrical=False, blank=True)

    def __str__(self):
        """Return a human readable representation of the model instance."""
        return "{}".format(self.name)

    def get_likes_count(self):
        try:
            return self.likes.count()
        except IndexError:
            return None

    def get_comments_count(self):
        try:
            return self.comments.count()
        except IndexError:
            return None

    def get_comments(self):
        try:
            return self.comments.order_by('-id').all()
        except IndexError:
            return None


class Pending(models.Model):

    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             related_name='user',
                             on_delete=models.CASCADE)

    is_professor = models.BooleanField(default=False, unique=False)

    classe = models.ForeignKey(Classe,
                               related_name='classe',
                               on_delete=models.CASCADE,
                               blank=True,
                               null=True)

    department = models.ForeignKey(Department,
                                   related_name='dep',
                                   on_delete=models.CASCADE,
                                   blank=True,
                                   null=True )

    message = models.TextField(max_length=6255, blank=True, unique=False, null=True)

    accepted = models.BooleanField(default=False, unique=False)

    date_created = models.DateTimeField(auto_now_add=True)
