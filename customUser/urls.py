"""test2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

from customUser.views import UserList, DetailsView, follow, unfollow, \
    CommentCreateView, CommentDetailsView, \
    UpdateProfile, \
    Profile, CreateMessageView, CreateUserView, GetConversation, GetAllConversation, SeenMessage, \
    CategoryCreateView, PostCreateView, PostUpdateView, PostDetailsView, OwnPostsList, UserPostsList, MainFeed, \
    CategoryPostList, like, unlike, UserNotifsView, UserSuggestionsView, MyCoursesView, UserCoursesView, \
    DepCoursesView, AddCourseFile, AddPicPost, CategoryListView, \
    PostCommentsView, DepartmentDetails, ClasseDetails, MainCoursesFeed, like_cours, unlike_cours, CoursCommentsView, \
    CommentCoursCreateView, AllEventsView, EventView, OwnEventsList, UserEventsList, MainFeedEvents, \
    EventCreateView, participate_event, unparticipate_event, CoursListView, AddProfilePic, \
    AddCoverPic, UserFollowers, UserFollowing, CreateFCMView, see_notifs, \
    Test, ClasseStudents, DepStudents, BranchStudents, DepBranches, BranchClasses, CategoryPubListView, \
    CategoryEvnListView, AddPicEvent, EventUpdateView, UpdatePicPost

urlpatterns = [

    url(r'^user/(?P<pk>[0-9]+)/$', UserList.as_view(), name="get_user"),  #
    url(r'^profile_update/$', UpdateProfile.as_view(), name="updateprofile"),
    url(r'^users/$', DetailsView.as_view(), name="all_users"),
    url(r'^signup/$', CreateUserView.as_view(), name="all_users"),  #
    url(r'^profile/$', Profile.as_view(), name="profile"),  #


    url(r'^follow/', follow, name="follow"),
    url(r'^unfollow/', unfollow, name="unfollow"),


    url(r'^create_comment/$', CommentCreateView.as_view(), name="create"),  #
    url(r'^comment/(?P<pk>[0-9]+)/update/$', CommentDetailsView.as_view(), name="details"), #


    url(r'^create_comment_cours/$', CommentCoursCreateView.as_view(), name="create"),  #

 #   url(r'postcreate/$', PostStatCreateView.as_view(), name="create"),
 #   url(r'postupdate/(?P<pk>[0-9]+)/$', PostStatUpdateView.as_view(), name="details"),
 #   url(r'post/(?P<pk>[0-9]+)/$', PostStatDetailsView.as_view(), name="details"),

 #   url(r'ownpost/$', OwnPostList.as_view(), name="ownpost"),
 #   url(r'userposts/(?P<pk>[0-9]+)/$', UserPostList.as_view(), name="user_post"),
 #   url(r'feed/$', FollowedFeed.as_view(), name="follow_feed"),




    url(r'^conversation/(?P<pk>[0-9]+)/$', GetConversation.as_view(), name="conversation"),  #
    url(r'^conversations/$', GetAllConversation.as_view(), name="all_conversation"),   #

    url(r'^message/$', CreateMessageView.as_view(), name="message"),  #
    url(r'^seen/(?P<pk>[0-9]+)/$', SeenMessage.as_view(), name="seen"),

    url(r'^seen_notifs/$', see_notifs, name="see_notifs"),



    url(r'^create_post/$', PostCreateView.as_view(), name="create"),
    url(r'^create_post_pic/$', AddPicPost.as_view(), name="upload_pic"),
    url(r'^create_event_pic/$', AddPicEvent.as_view(), name="upload_event_pic"),
    url(r'^post/(?P<pk>[0-9]+)/update/$', PostUpdateView.as_view(), name="details"),
    url(r'^post/(?P<pk>[0-9]+)/update_pic/$', UpdatePicPost.as_view(), name="details"),
    url(r'^event/(?P<pk>[0-9]+)/update/$', EventUpdateView.as_view(), name="details"),
    url(r'^event/(?P<pk>[0-9]+)/update_pic/$', EventUpdateView.as_view(), name="details"),

    url(r'^post/(?P<pk>[0-9]+)/$', PostDetailsView.as_view(), name="details"),

    url(r'^post/(?P<pk>[0-9]+)/comments/$', PostCommentsView.as_view(), name="details"),    #
    url(r'^cours/(?P<pk>[0-9]+)/comments/$', CoursCommentsView.as_view(), name="cour_comments"),  #


    url(r'^profile_posts/$', OwnPostsList.as_view(), name="ownpost"),   #
    url(r'^user/(?P<pk>[0-9]+)/posts/$', UserPostsList.as_view(), name="user_post"),    #
    url(r'^feed/$', MainFeed.as_view(), name="follow_feed"),    #
    url(r'^coursfeed/$', MainCoursesFeed.as_view(), name="follow_cours_feed"),  #

    url(r'^allcours/$', CoursListView.as_view(), name="allcours"),  #



    url(r'^feed/events/$', MainFeedEvents.as_view(), name="follow_feed"), ##
    url(r'^allevents/$', AllEventsView.as_view(), name="allevents"), ##
    url(r'^event/(?P<pk>[0-9]+)/$', EventView.as_view(), name="event"), ##
    url(r'^profile/events/$', OwnEventsList.as_view(), name="myevents"),    ##
    url(r'^user/(?P<pk>[0-9]+)/events/$', UserEventsList.as_view(), name="user_events"),    ##
    url(r'^create/event/$', EventCreateView.as_view(), name="school_events"),   ##

    url(r'^participate/', participate_event, name="participate"),  ##
    url(r'^unparticipate/', unparticipate_event, name="unparticipate"), ##




    url(r'^create_category/$', CategoryCreateView.as_view(), name="createcat"),
    url(r'^category/(?P<pk>[0-9]+)/posts/$', CategoryPostList.as_view(), name="catposts"),  #
    url(r'^categories/$', CategoryListView.as_view(), name="listcat"),  #
    url(r'^categories_pub/$', CategoryPubListView.as_view(), name="listcat"),  #
    url(r'^categories_event/$', CategoryEvnListView.as_view(), name="listcat"),  #


    url(r'^like/', like, name="like"),  #
    url(r'^unlike/', unlike, name="unlike"),    #


    url(r'^like_cours/', like_cours, name="like_cours"),  #
    url(r'^unlike_cours/', unlike_cours, name="unlike_cours"),  #



    url(r'^department/(?P<pk>[0-9]+)/$', DepartmentDetails.as_view(), name="dep_details"),  #
    url(r'^department/(?P<pk>[0-9]+)/students/$', DepStudents.as_view(), name="dep_details"),  #
    url(r'^department/(?P<pk>[0-9]+)/branches/$', DepBranches.as_view(), name="dep_details"),  #
    url(r'^branch/(?P<pk>[0-9]+)/students/$', BranchStudents.as_view(), name="dep_details"),  #
    url(r'^branch/(?P<pk>[0-9]+)/classes/$', BranchClasses.as_view(), name="dep_details"),  #
    url(r'^classe/(?P<pk>[0-9]+)/$', ClasseDetails.as_view(), name="classe_details"),   #
    url(r'^classe/(?P<pk>[0-9]+)/students/$', ClasseStudents.as_view(), name="classe_details"),   #





    url(r'^notifications/$', UserNotifsView.as_view(), name="my_notifs"),

    url(r'^profile/suggestions/$', UserSuggestionsView.as_view(), name="get_suggestion"),



    url(r'^upload/cours/$', AddCourseFile.as_view(), name="upload_cours"),

    url(r'^profile/cours/$', MyCoursesView.as_view(), name="my_courses"),   #
    url(r'^user/(?P<pk>[0-9]+)/cours/$', UserCoursesView.as_view(), name="user_courses"),   #


    url(r'^user/(?P<pk>[0-9]+)/followers/$', UserFollowers.as_view(), name="user_followers"),
    url(r'^user/(?P<pk>[0-9]+)/following/$', UserFollowing.as_view(), name="user_following"),

    url(r'^departement/(?P<pk>[0-9]+)/cours/$', DepCoursesView.as_view(), name="dep_courses"),


    url(r'^update_profile_pic/$', AddProfilePic.as_view(), name="upload_prof_pic"),

    url(r'^update_cover_pic/$', AddCoverPic.as_view(), name="upload_cover_pic"),

    url(r'^create_fcm/$', CreateFCMView.as_view(), name="fcm"),

    url(r'^test/$', Test, name="test"),
]
