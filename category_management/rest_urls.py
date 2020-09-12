from django.conf.urls import url
from category_management.rest_views import CategoryList, FilterInvJson, DeleteCategory, GetCategory, AddCategory, \
    UpdateCategory

urlpatterns = [
    url(r'add_category/$', AddCategory.as_view(), name='delete_category'),
    url(r'^category_list/$', CategoryList.as_view(), name='category_list'),
    url(r'delete/(?P<cat_id>[0-9]+)/$', DeleteCategory.as_view(), name='delete_category'),
    url(r'get/(?P<cat_id>[0-9]+)/$', GetCategory.as_view(), name='delete_category'),
    url(r'update/(?P<cat_id>[0-9]+)/$', UpdateCategory.as_view(), name='delete_category'),

    url(r'^filter_invjson/$', FilterInvJson.as_view(), name='filter_invjson'),

]
