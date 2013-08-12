# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#     * Rearrange models' order
#     * Make sure each model has one field with primary_key=True
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.
from __future__ import unicode_literals

from django.db import models

class Appruncount(models.Model):
    idappruncount = models.IntegerField(primary_key=True)
    pid = models.ForeignKey('Projects', db_column='pid')
    appversion = models.CharField(max_length=45L, blank=True)
    runcount = models.BigIntegerField(null=True, blank=True)
    class Meta:
        db_table = 'appruncount'

class Appstatistics(models.Model):
    idappstatistics = models.IntegerField(primary_key=True)
    iderror = models.ForeignKey('Errors', db_column='iderror')
    appversion = models.CharField(max_length=10L)
    count = models.IntegerField()
    class Meta:
        db_table = 'appstatistics'

class Comments(models.Model):
    idcomments = models.IntegerField(primary_key=True)
    iderror = models.ForeignKey('Errors', db_column='iderror')
    datetime = models.DateTimeField()
    user = models.ForeignKey('Users', db_column='user')
    comment = models.CharField(max_length=45L)
    class Meta:
        db_table = 'comments'

class Countrystatistics(models.Model):
    idcountrystatistics = models.IntegerField(primary_key=True)
    iderror = models.ForeignKey('Errors', db_column='iderror')
    countryname = models.CharField(max_length=45L)
    count = models.IntegerField()
    class Meta:
        db_table = 'countrystatistics'

class Devicestatistics(models.Model):
    iddevicestatistics = models.IntegerField(primary_key=True)
    iderror = models.ForeignKey('Errors', db_column='iderror')
    devicename = models.CharField(max_length=45L)
    count = models.IntegerField()
    class Meta:
        db_table = 'devicestatistics'

class Errors(models.Model):
    iderror = models.IntegerField(primary_key=True)
    pid = models.ForeignKey('Projects', db_column='pid')
    rank = models.IntegerField()
    autodetermine = models.IntegerField()
    status = models.IntegerField(null=True, blank=True)
    numofinstances = models.IntegerField()
    createdate = models.DateTimeField()
    lastdate = models.DateTimeField()
    callstack = models.TextField()
    errorname = models.CharField(max_length=45L)
    errorclassname = models.CharField(max_length=45L)
    linenum = models.CharField(max_length=45L)
    errorweight = models.IntegerField(null=True, blank=True)
    recur = models.IntegerField(null=True, blank=True)
    eventpath = models.TextField(blank=True)
    wifion = models.IntegerField()
    gpson = models.IntegerField()
    mobileon = models.IntegerField()
    totalmemusage = models.IntegerField()
    class Meta:
        db_table = 'errors'

class Eventpaths(models.Model):
    ideventpaths = models.IntegerField(primary_key=True)
    idinstance = models.ForeignKey('Instances', db_column='idinstance')
    datetime = models.DateTimeField(null=True, blank=True)
    classname = models.CharField(max_length=45L, blank=True)
    methodname = models.CharField(max_length=45L, blank=True)
    linenum = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = 'eventpaths'

class Instances(models.Model):
    idinstance = models.IntegerField(primary_key=True)
    iderror = models.ForeignKey(Errors, db_column='iderror')
    sdkversion = models.CharField(max_length=45L, blank=True)
    appversion = models.CharField(max_length=45L, blank=True)
    osversion = models.CharField(max_length=45L, blank=True)
    kernelversion = models.CharField(max_length=45L, blank=True)
    appmemmax = models.CharField(max_length=45L, blank=True)
    appmemfree = models.CharField(max_length=45L, blank=True)
    appmemtotal = models.CharField(max_length=45L, blank=True)
    country = models.CharField(max_length=45L, blank=True)
    datetime = models.DateTimeField(null=True, blank=True)
    locale = models.CharField(max_length=45L, blank=True)
    mobileon = models.IntegerField(null=True, blank=True)
    gpson = models.IntegerField(null=True, blank=True)
    wifion = models.IntegerField(null=True, blank=True)
    device = models.CharField(max_length=45L, blank=True)
    rooted = models.IntegerField(null=True, blank=True)
    scrheight = models.IntegerField(null=True, blank=True)
    scrwidth = models.IntegerField(null=True, blank=True)
    scrorientation = models.IntegerField(null=True, blank=True)
    sysmemlow = models.CharField(max_length=45L, blank=True)
    log_path = models.CharField(max_length=45L, blank=True)
    batterylevel = models.IntegerField(null=True, blank=True)
    availsdcard = models.IntegerField(null=True, blank=True)
    xdpi = models.FloatField(null=True, blank=True)
    ydpi = models.FloatField(null=True, blank=True)
    class Meta:
        db_table = 'instances'

class Osstatistics(models.Model):
    idosstatistics = models.IntegerField(primary_key=True)
    iderror = models.ForeignKey(Errors, db_column='iderror')
    osversion = models.CharField(max_length=10L)
    count = models.IntegerField()
    class Meta:
        db_table = 'osstatistics'

class Projects(models.Model):
    pid = models.IntegerField(primary_key=True)
    apikey = models.CharField(max_length=10L, unique=True)
    platform = models.IntegerField()
    name = models.CharField(max_length=45L)
    stage = models.IntegerField()
    class Meta:
        db_table = 'projects'

class Session(models.Model):
    idsession = models.BigIntegerField(primary_key=True)
    pid = models.ForeignKey(Projects, db_column='pid')
    appversion = models.CharField(max_length=45L)
    class Meta:
        db_table = 'session'

class Sessionevent(models.Model):
    idsessionevent = models.IntegerField(primary_key=True)
    idsession = models.ForeignKey(Session, db_column='idsession')
    datetime = models.DateTimeField(null=True, blank=True)
    classname = models.CharField(max_length=45L, blank=True)
    methodname = models.CharField(max_length=45L, blank=True)
    linenum = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = 'sessionevent'

class Tags(models.Model):
    idtag = models.IntegerField(primary_key=True)
    iderror = models.ForeignKey(Errors, db_column='iderror')
    tag = models.CharField(max_length=45L)
    class Meta:
        db_table = 'tags'

class Users(models.Model):
    uid = models.IntegerField(primary_key=True)
    email = models.CharField(max_length=45L, unique=True)
    passwd = models.CharField(max_length=20L)
    nickname = models.CharField(max_length=45L)
    company = models.CharField(max_length=45L)
    image_path = models.CharField(max_length=45L, blank=True)
    class Meta:
        db_table = 'users'

class Viewer(models.Model):
    uid = models.ForeignKey(Users, db_column='uid')
    pid = models.ForeignKey(Projects, db_column='pid')
    class Meta:
        db_table = 'viewer'

