# encoding: utf-8
__author__ = 'sunwei'
__date__ = '2018/5/9 上午10:11'

import xadmin

from .models import CityDict, CourseOrg, Teacher


# 机构所属城市名后台管理器
class CityDictAdmin(object):
    list_display = ['name', 'desc', 'add_time']
    search_fields = ['name', 'desc']
    list_filter = ['name', 'desc', 'add_time']


# 机构课程信息管理器
class CourseOrgAdmin(object):
    list_display = ['name', 'desc','category',  'click_nums', 'fav_nums','add_time' ]
    search_fields = ['name', 'desc','category',  'click_nums', 'fav_nums']
    list_filter = ['name', 'desc', 'category', 'click_nums', 'fav_nums','city__name','address','add_time']


class TeacherAdmin(object):
    list_display = ['name', 'org', 'work_years', 'work_company','add_time']
    search_fields = ['org', 'name', 'work_years', 'work_company']
    list_filter = ['org__name', 'name', 'work_years', 'work_company','click_nums', 'fav_nums', 'add_time']


xadmin.site.register(CityDict, CityDictAdmin)
xadmin.site.register(CourseOrg, CourseOrgAdmin)
xadmin.site.register(Teacher, TeacherAdmin)
