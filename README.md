# rest framework + vue projection
# 1. 渲染器
规定页面显示的效果
# 2. 版本 
原理：要了解使用：
## 2.1. 添加配置
### 2.1.1. 添加配置
				REST_FRAMEWORK = {
					
					.... 
					
					'DEFAULT_VERSIONING_CLASS':'rest_framework.versioning.URLPathVersioning',
					'ALLOWED_VERSIONS':['v1','v2'], # 允许的版本
					'VERSION_PARAM':'version', # 参数
					'DEFAULT_VERSION':'v1', # 默认版本
					....
				}
### 2.1.2 设置路由 
urls.py:

	urlpatterns = [
	    #url(r'^admin/', admin.site.urls),
		    url(r'^api/(?P<version>\w+)/', include('api.urls')),
		]
				
api/urls.py :

		urlpatterns = [
		    url(r'^course/$', course.CourseView.as_view()),
			]
			
### 2.1.3. 获取版本 
request.version 获取版本  
			
	
# 3. vue+rest framework
## 3.1 vue: 
- 路由 + 组件 
- axios发送ajax请求
- that 
## 3.2 api:
- 跨域: 
(1)域名不同
(2)端口不同 
- cors:
本质设置响应头

			#允许你的域名来获取我的数据
			response['Access-Control-Allow-Origin'] = "*"

			# 允许你携带Content-Type请求头
			response['Access-Control-Allow-Headers'] = "Content-Type"

			# 允许你发送DELETE,PUT
			response['Access-Control-Allow-Methods'] = "DELETE,PUT"
			
			
			
# 4. 序列化
	- source
	- method 
# 5.推荐课程，用户拦截,拦截器
## 5.1 VUE:
- 课程列表：this.$axios + this 
- 课程详细：this.$axios + this 
- 用户登录：
    - this.$axios
	- this 
	- 跨域简单和复杂请求
	- vuex做全局变量
	- vuex-cookies 
- 微职位 
	- 拦截器
	- 携带token 
			
PS: api可以同一放在store中保存
			
## 5.2 API:
- 课程列表 
    - 序列化：source='get_level_display'
- 课程详细：
    - 序列化：source='get_level_display'
    - 序列化：method
- 用户登录 
    - update_or_create
- 微职位 
    - 认证组件 
			
- 关联组件：
    - 版本
    - 解析器
    - 渲染器
    - 序列化 
    - 认证组件 
    - 视图 
    - 路由 