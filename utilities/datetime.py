# -*- coding:utf-8 -*-
import time
import datetime

FORMAT_DATE_WITHOUT_SEPARATOR = '%Y%m%d'
FORMAT_DATETIME_WITHOUT_SEPARATOR = '%Y%m%d%H%M%S'
FORMAT_DATE = '%Y-%m-%d'
FORMAT_MONTH = '%Y-%m'
FORMAT_DATETIME = '%Y-%m-%d %H:%M:%S'

def str_to_datetime(date_str, date_format=FORMAT_DATETIME):
    '''
        convert date string ('2011-01-12') into {@see datetime}
    '''
    date = datetime.datetime.strptime(date_str, date_format)
    return date

def str_to_date(date_str, date_format=FORMAT_DATE):
    '''
        convert date string ('2011-01-12') into {@see date}
    '''
    date = time.strptime(date_str, date_format)
    return datetime.date(* date[:3])

def datetime_to_str(date, date_format=FORMAT_DATE):
    '''
        convert {@see datetime} into date string ('2011-01-12') 
    '''
    return date.strftime(date_format)

def date_to_str(date, date_format=FORMAT_DATE):
    '''
        convert {@see date} into date string ('2011-01-12') 
    '''
    return date.strftime(date_format)

def date_to_datetime(date):
    '''
        convert {@see date} into datetime
    '''
    return datetime.datetime(date.year, date.month, date.day)

def generate_timestamp():
    """
        Get seconds since epoch (UTC).
    """
    return int(time.time())
