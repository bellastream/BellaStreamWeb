# -*- coding:utf-8 -*-

import os

from django.db import models
from django.db.models.fields.files import ImageFieldFile
from PIL import Image

from settings import MEDIA_ROOT


UPLOAD_ROOT = 'photos'

def make_thumb(image, size=750):
    pixbuf = Image.open(image)
    width, height = pixbuf.size

    if width > size:
        delta = width / size
        height = int(height / delta)
        pixbuf.thumbnail((size, height), Image.ANTIALIAS)

        return pixbuf


class PhotoStream(models.Model):
    image = models.ImageField(upload_to=UPLOAD_ROOT)
    thumb = models.ImageField(upload_to=UPLOAD_ROOT, blank=True, null=True, verbose_name="小尺寸图")
    name = models.CharField(max_length=50, blank=True, null=True, verbose_name="照片名")
    place = models.CharField(max_length=50, blank=True, null=True, verbose_name="地点")
    keywords = models.CharField(max_length=500, blank=True, null=True, verbose_name="关键字")
    abstract = models.TextField(default="", blank=True, null=True, verbose_name="说明")
    time = models.DateTimeField(auto_now_add=True, verbose_name="拍摄时间")
    upload_time = models.DateTimeField(auto_now_add=True, verbose_name="上传时间")

    def __unicode__(self):
        return self.name

    def save(self):
        base, ext = os.path.splitext(os.path.basename(self.image.path))
        relate_thumb_path = os.path.join(UPLOAD_ROOT, base + '_thumb' + ext)
        thumb_pix = make_thumb(self.image)
        thumb_pix.save(os.path.join(MEDIA_ROOT, relate_thumb_path))
        self.thumb = ImageFieldFile(self, self.thumb, relate_thumb_path)
        super(PhotoStream, self).save()
