
from flask_appbuilder.models.sqla.interface import SQLAInterface
from flask_babel import lazy_gettext as _
from wtforms.validators import DataRequired
from myapp import app, appbuilder
from wtforms import StringField, SelectField
from flask_appbuilder.fieldwidgets import BS3TextFieldWidget, Select2Widget
from myapp.forms import MyBS3TextAreaFieldWidget,MySelect2Widget
from flask_appbuilder import expose, BaseView
from .baseApi import MyappModelRestApi
from flask import g, redirect, url_for

from myapp.models.model_lyctest import Lyctest
conf = app.config
logging = app.logger


##  定义数据表视图
# class Model1_ModelView(MyappModelView):
#     datamodel = SQLAInterface(Model1)
##  添加model的前后端
# appbuilder.add_view(baseview=Model1_ModelView, name="视图1", icon='fa-list',category='菜单1', category_icon='fa-window-maximize')


# 定义数据表视图
# class Model1_ModelView_Api(MyappModelRestApi):
#     datamodel = SQLAInterface(Model1)
#     route_base = '/model2/api'
# # 添加model的纯后端接口
# appbuilder.add_api(Model1_ModelView_Api)


class Lyctest_ModelView_base():
    label_title='数据标注功能'
    datamodel = SQLAInterface(Lyctest)
    # base_permissions = ['can_add','can_show','can_edit','can_list','can_delete']
    base_permissions = ['can_add', 'can_edit']   # 这边对应的是每一条数据的操作

    base_order = ("id", "desc")  
    order_columns=['id']

    # add_columns = ['test_name','test_num'] 
    # show_columns = ['id','test_name','test_num']
    # search_columns=['test_name','test_num',]
    spec_label_columns = {
        "test_name": "测试名字",
        "test_num": "测试数量",
        "des": "描述"
    }

    # cols_width = {
    #     "test_name": {"type": "ellip1", "width": 100},
    #     "test_num": {"type": "ellip2", "width": 50}
    # }
    list_columns = ['test_name', 'test_num', 'des']    # 具体展示信息

    # edit_columns = add_columns
    # add_form_extra_fields = {}
    # edit_form_extra_fields = add_form_extra_fields
    # import_data=True  # 导入数据
    # download_data=True  # 导出数据
    # def pre_add(self,item):
    #     if not item.owner:
    #         item.owner=g.user.username
    # def post_list(self,items):
    #     flash(Markup('可批量删除不使用的数据集,可批量上传自产数据集'),category='info')
    #     return items


class Lyctest_ModelView_Api(Lyctest_ModelView_base, MyappModelRestApi):
    datamodel = SQLAInterface(Lyctest)
    route_base = '/lyctest_modelview/api'

appbuilder.add_api(Lyctest_ModelView_Api)




# 数据表视图
# class TestView(BaseView):
#     # 相对路径的url
#     route_base = '/'

#     @expose('/data_annotation/_info')
#     def hello(self):
#         # return redirect(url_for('Myapp.welcome'))
#         # return self.render_template('annotation.html', username='lyc')
#         # return redirect('/pipeline_modelview/web/%s' % username)
#         return 'hello'
#         # return redirect('https://www.baidu.com')
#         # return redirect('http://10.10.20.234:8088')

# appbuilder.add_view_no_menu(TestView()) 