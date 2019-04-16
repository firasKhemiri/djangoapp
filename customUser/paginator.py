from rest_framework.pagination import LimitOffsetPagination


class PostOffSetLimitPagination(LimitOffsetPagination):
    default_limit = 12
    max_limit = 16





class MessagesOffSetLimitPagination(LimitOffsetPagination):
    default_limit = 30
    max_limit = 40
