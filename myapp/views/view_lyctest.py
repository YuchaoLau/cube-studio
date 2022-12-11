
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
    
    
    base_permissions = ['can_add','can_show','can_edit','can_list','can_delete']
    # base_permissions = ['can_add', 'can_edit']   # 这边对应的是每一条数据的操作

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
    
    


class Lyctest_ModelView_Api(Lyctest_ModelView_base, MyappModelRestApi):
    datamodel = SQLAInterface(Lyctest)
    route_base = '/lyctest_modelview/api'
    
    # @expose(show_lyc)
    # def show_lyc():
        

appbuilder.add_api(Lyctest_ModelView_Api)