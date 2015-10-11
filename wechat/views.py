# -*- coding:utf-8 -*-
from django.http import HttpResponse, HttpResponseBadRequest

import hashlib
import settings

def get_wechat_view(request):
	signature = request.GET.get('signature', '')
	timestamp = request.GET.get('timestamp', '')
	nonce = request.GET.get('nonce', '')
	echostr = request.GET.get('echostr', '')

	ori_str = ''.join(sorted([settings.WECHAT_TOKEN,timestamp,nonce]))
	print signature, hashlib.sha1(ori_str).hexdigest()
	if hashlib.sha1(ori_str).hexdigest() == signature:
		return HttpResponse(content=echostr)
	else:
		return HttpResponseBadRequest()
