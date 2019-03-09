from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer,BrowsableAPIRenderer
from rest_framework.versioning import QueryParameterVersioning,URLPathVersioning

class CourseView(APIView):
    versioning_class = URLPathVersioning
    renderer_class = [JSONRenderer,BrowsableAPIRenderer]
    def get(self,request,*args,**kwargs):

        ret = {
            'code':1000,
            'data':[
                {
                    "id": 1, "title": 'python全栈'
                },
                {
                    "id": 2, "title": 'Linux运维'
                },
                {
                    "id": 3, "title": '金融分析'
                },
            ]
        }
        return Response(ret)







