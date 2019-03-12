from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer
from rest_framework.versioning import QueryParameterVersioning, URLPathVersioning
from rest_framework.viewsets import ViewSetMixin

from api import models
from rest_framework import serializers

from api.auth.auth import ApiAuth
from api.serializers.course import CourseSerializer, CourseDetailSerializer


class CourseView(ViewSetMixin, APIView):
    # versioning_class = URLPathVersioning
    # renderer_class = [JSONRenderer, BrowsableAPIRenderer]

    # def get(self, request, *args, **kwargs):
    #
    #     ret = {'code': 1000, 'data': None}
    #
    #     print(ret)
    #     try:
    #         queryset = models.Course.objects.all()
    #         ser = CourseSerializer(instance=queryset,many=True)
    #         ret['data'] = ser.data
    #     except Exception as e:
    #         ret['code'] = 1001
    #         ret['error'] = '获取课程失败'
    #
    #     return Response(ret)
    def list(self, request, *args, **kwargs):
        '''
        课程列表接口
        :param request:
        :param args:
        :param kwargs:
        :return:
        '''
        ret = {'code': 1000, 'data': None}

        try:
            queryset = models.Course.objects.all()
            ser = CourseSerializer(instance=queryset, many=True)
            ret['data'] = ser.data
        except Exception as e:
            ret['code'] = 1001
            ret['error'] = '获取课程失败'

        return Response(ret)

    def retrieve(self, request, *args, **kwargs):
        """
        课程详细接口
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        ret = {'code': 1000, 'data': None}

        try:
            # 课程ID=2
            pk = kwargs.get('pk')

            # 课程详细对象
            obj = models.CourseDetail.objects.filter(course_id=pk).first()

            ser = CourseDetailSerializer(instance=obj, many=False)

            ret['data'] = ser.data

        except Exception as e:
            ret['code'] = 1001
            ret['error'] = '获取课程失败'

        return Response(ret)

class MicroView(APIView):
    authentication_classes = [ApiAuth,]
    # versioning_class = URLPathVersioning
    def get(self,request,*args,**kwargs):
        ret = {'code':1000,'title':'微职位'}
        return Response(ret)



