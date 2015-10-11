# -*- coding:utf-8 -*-
from datetime import datetime_to_str
from django.http import HttpResponse
from twisted.web import http
import datetime
import json


class DatetimeEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            return datetime_to_str(obj, date_format='%Y-%m-%d %H:%M:%S')
        else:
            return json.JSONEncoder.default(self, obj)


def json_http_response(result, status=http.OK, cls=DatetimeEncoder):
    return HttpResponse(content=json.dumps(result, cls=cls, ensure_ascii=True, encoding="utf-8"),
                        mimetype="application/json; charset=UTF-8", status=status)