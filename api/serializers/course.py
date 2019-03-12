from api import models

from rest_framework import serializers


class CourseSerializer(serializers.ModelSerializer):
    """
    课程序列化
    """
    level = serializers.CharField(source='get_level_display')
    class Meta:
        model = models.Course
        fields = ['id','title','course_img','level']
class CourseDetailSerializer(serializers.ModelSerializer):

    '''
    课程详情序列化
    '''
    title = serializers.CharField(source='course.title')
    img = serializers.CharField(source='course.course_img')
    level = serializers.CharField(source='course.get_level_display')
    # many to many
    recommends = serializers.SerializerMethodField()
    chapter = serializers.SerializerMethodField()

    class Meta:
        model = models.CourseDetail
        fields = ['course', 'title', 'img', 'level', 'slogon', 'why', 'recommends', 'chapter']
    def get_recommends(self,obj):
        # 获取推荐课程
        queryset = obj.recommend_courses.all()
        return [{'id': row.id, 'title': row.title} for row in queryset]

    def get_chapter(self, obj):
        # 获该课程章节,反向查询
        queryset = obj.course.chapter_set.all()

        return [{'id': row.id, 'name': row.name} for row in queryset]



