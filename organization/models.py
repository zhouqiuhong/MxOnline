from datetime import datetime

from django.db import models

# Create your models here.


class City(models.Model):
    name = models.CharField(max_length=20,verbose_name=u"城市名称")
    desc_city = models.CharField(max_length=200,verbose_name=u"城市描述")
    add_time = models.DateTimeField(default=datetime.now)

    class Meta:
        verbose_name = u"城市"
        verbose_name_plural = verbose_name


class CourseOrganization(models.Model):
    name = models.CharField(max_length=50, verbose_name=u"机构名称")
    desc_organization = models.TextField(verbose_name=u"机构描述")
    # students = models.IntegerField(default=0, verbose_name=u"学习人数")
    fav_num = models.IntegerField(default=0, verbose_name=u"收藏人数")
    image = models.ImageField(upload_to="image/%Y/%m", verbose_name=u"封面图片", max_length=200)
    click_num = models.IntegerField(default=0, verbose_name=u"点击数")
    city = models.ForeignKey(City, verbose_name=u"机构所在城市")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"课程机构"
        verbose_name_plural = verbose_name


class Teacher(models.Model):
    org = models.ForeignKey(CourseOrganization,verbose_name=u"所属机构")
    name = models.CharField(max_length=20, verbose_name=u"授课老师")
    work_year = models.IntegerField(default=0, verbose_name=u"工作年限")
    work_company = models.CharField(max_length=50, verbose_name=u"所在公司")
    work_position = models.CharField(max_length=50, verbose_name=u"公司职位")
    points = models.CharField(max_length=50, verbose_name=u"教学特点")
    fav_num = models.IntegerField(default=0, verbose_name=u"收藏人数")
    click_num = models.IntegerField(default=0, verbose_name=u"点击数")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"授课老师"
        verbose_name_plural = verbose_name