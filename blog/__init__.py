# -*- coding:utf-8 -*-
from django.contrib.auth.models import AnonymousUser

def get_user_from_request(request):
    '''
    从request中获取user
    '''
    return request.user if not isinstance(request.user, AnonymousUser) else None

