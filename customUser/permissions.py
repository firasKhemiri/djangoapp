from rest_framework.permissions import BasePermission
from .models import Post, User, Conversation


class Following(BasePermission):
    """Custom permission class to allow only bucketlist owners to edit them."""

    def is_following(self, request, view, obj):
        """Return True if permission is granted to the bucketlist owner."""
 #       if isinstance(obj, Post):
  #          return obj.owner == request.user.following
   #     return obj.owner == request.user.following
        return False



class IsAdmin(BasePermission):
    """Custom permission class to allow only bucketlist owners to edit them."""

    def has_permission(self, request, view):
        return request.user.is_admin


class IsProf(BasePermission):
    """Custom permission class to allow only bucketlist owners to edit them."""

    def has_permission(self, request, view):
        return request.user.is_professor or request.user.is_admin


class isStaff(BasePermission):
    """Custom permission class to allow only bucketlist owners to edit them."""


    def has_permission(self, request, view):
        return ( (request.user.is_professor) or (request.user.is_admin) )







class IsMe(BasePermission):
    """Custom permission class to allow only bucketlist owners to edit them."""

    def has_object_permission(self, request, view, obj):
        """Return True if permission is granted to the bucketlist owner."""
        if isinstance(obj, User):
            return obj == request.user
        return obj == request.user



class IsMine(BasePermission):
    """Custom permission class to allow only bucketlist owners to edit them."""

    def has_object_permission(self, request, view, obj):
        """Return True if permission is granted to the bucketlist owner."""
        if isinstance(obj, User):
            return obj.owner == request.user
        return obj.owner == request.user





class MyConvo(BasePermission):

    def has_object_permission(self, request, view, obj):

        val = False

        for i in User.get_conversations(request.user).all():
            if obj.id == i.id:
                val = True
                break
        return val


class MyMsg(BasePermission):

    def has_object_permission(self, request, view, obj):
        val= obj.sender == request.user or obj.reciever == request.user
        return val

