
from flask_appbuilder.models.sqla.interface import SQLAInterface
from flask_babel import lazy_gettext as _
from wtforms.validators import DataRequired
from myapp import app, appbuilder, db
from wtforms import StringField, SelectField
from flask_appbuilder.fieldwidgets import BS3TextFieldWidget, Select2Widget
from myapp.forms import MyBS3TextAreaFieldWidget,MySelect2Widget
from flask_appbuilder.actions import action
from flask_babel import gettext as __
from flask_appbuilder import expose
from flask import Flask, redirect, request, send_from_directory, send_file, flash
from .baseApi import MyappModelRestApi
from .base import MyappModelView
from flask import g
from myapp.models.model_dataset import Dataset
import os
from flask import make_response

# from flask import render_template
# from flask_appbuilder.views import ModelView
from flask_appbuilder.upload import BS3FileUploadFieldWidget, FileUploadField
from flask_appbuilder.filemanager import FileManager
from werkzeug.utils import secure_filename
from flask_login import current_user

conf = app.config
logging = app.logger




class Dataset_ModelView_base():
    label_title='数据集'
    datamodel = SQLAInterface(Dataset)
    base_permissions = ['can_add','can_show','can_edit','can_list','can_delete']
    # base_permissions = []
    # can_show： 详情页
    base_order = ("id", "desc")
    order_columns=['id']

    add_columns = ['name','label','describe', 'source_type','source','industry','field','usage','research','storage_class','file_type','years','url','download_url','path','storage_size','entries_num','duration','price','status','icon','owner']
    show_columns = ['id','name','label','describe', 'dataset_file', 'download', 'source_type','source','industry','field','usage','research','storage_class','file_type','status','years','url','path','download_url','storage_size','entries_num','duration','price','status','icon','owner']
    search_columns=['name','label','describe', 'source_type', 'source','industry','field','usage','research','storage_class','file_type','status','years','url','path','download_url']
    spec_label_columns = {
        "source_type":"来源类型",
        "source":"数据来源",
        "usage":"数据用途",
        "research":"研究方向",
        "storage_class":"存储类型",
        "file_type":"文件类型",
        "years":"数据年份",
        "url":"相关网址",
        "url_html": "相关网址",
        "download_url":"下载地址",
        "download_url_html": "下载地址",
        # "path":"本地路径",
        "entries_num":"条目数量",
        "duration":"文件时长",
        "price": "价格",
        "icon": "示例图",
        "icon_html":"示例图",
        "download": "下载",
        "upload_dataset": "上传",
        "dataset_file": "文件名"
    }
    

    edit_columns = add_columns
    list_columns = ['id', 'icon_html','name','label', 'upload_dataset', 'download', 'describe', 'source_type','source','status','industry','field','url_html','download_url_html','usage','research','storage_class','file_type','years','path','storage_size','entries_num','duration','price','owner']
    cols_width = {
        "name": {"type": "ellip1", "width": 200},
        "label": {"type": "ellip2", "width": 250},
        "describe":{"type": "ellip2", "width": 300},
        "field":{"type": "ellip1", "width": 100},
        "source_type":{"type": "ellip1", "width": 100},
        "source": {"type": "ellip1", "width": 100},
        "industry": {"type": "ellip1", "width": 100},
        "url_html": {"type": "ellip1", "width": 200},
        "download_url_html": {"type": "ellip1", "width": 200},
        # "path":{"type": "ellip2", "width": 200},
        "storage_class": {"type": "ellip1", "width": 100},
        "storage_size":{"type": "ellip1", "width": 100},
        "file_type":{"type": "ellip1", "width": 100},
        "owner": {"type": "ellip1", "width": 200},
        "status": {"type": "ellip1", "width": 100},
        "entries_num": {"type": "ellip1", "width": 100},
        "duration": {"type": "ellip1", "width": 100},
        "price": {"type": "ellip1", "width": 100},
        "years": {"type": "ellip2", "width": 100},
        "usage": {"type": "ellip1", "width": 200},
        "research": {"type": "ellip2", "width": 100},
        "icon_html": {"type": "ellip1", "width": 100}
    }

    add_form_extra_fields = {
        "name": StringField(
            label=_(datamodel.obj.lab('name')),
            description='数据集英文名',
            default='',
            widget=BS3TextFieldWidget(),
            validators=[DataRequired()]
        ),
        "label": StringField(
            label=_(datamodel.obj.lab('label')),
            default='',
            description='数据集中文名',
            widget=BS3TextFieldWidget(),
            validators=[DataRequired()]
        ),
        "describe": StringField(
            label=_(datamodel.obj.lab('describe')),
            default='',
            description='数据集描述',
            widget=MyBS3TextAreaFieldWidget(),
            validators=[DataRequired()]
        ),
        # "dataset_file": FileUploadField(
        #     label= 'File',
        #     filemanager = FileManager,
        #     widget= BS3FileUploadFieldWidget()
        # ),
        "industry": SelectField(
            label=_(datamodel.obj.lab('industry')),
            description='行业分类',
            widget=MySelect2Widget(can_input=True),
            default='',
            choices=[[x,x] for x in ['农业','生物学','气候+天气','复杂网络','计算机网络','网络安全','数据挑战','地球科学','经济学','教育','能源','娱乐','金融','GIS','政府','医疗','图像处理','机器学习','博物馆','自然语言','神经科学','物理','前列腺癌','心理学+认知','公共领域','搜索引擎','社交网络','社会科学','软件','运动','时间序列','交通','电子竞技']],
            validators=[DataRequired()]
        ),
        "field":SelectField(
            label=_(datamodel.obj.lab('field')),
            description='领域',
            widget=MySelect2Widget(can_input=True),
            choices=[[x,x] for x in ['视觉',"音频","自然语言","风控","搜索",'推荐']],
            validators=[]
        ),
        "source_type": SelectField(
            label=_(datamodel.obj.lab('source_type')),
            description='来源分类',
            widget=Select2Widget(),
            default='开源',
            choices=[[x,x] for x in ["开源", "自产","购买"]],
            validators=[]
        ),
        "source": SelectField(
            label=_(datamodel.obj.lab('source')),
            description='数据来源',
            widget=MySelect2Widget(can_input=True),
            choices=[[x, x] for x in ['github',"kaggle", "天池",'UCI','AWS 公开数据集','Google 公开数据集',  "采购公司1", "标注团队1", "政府网站1"]],
            validators=[]
        ),
        "file_type": SelectField(
            label=_(datamodel.obj.lab('file_type')),
            description='文件类型',
            widget=MySelect2Widget(can_input=True),
            choices=[[x, x] for x in ["png", "jpg",'txt','csv','wav','mp3','mp4','nv4','zip','gz']],
        ),
        "storage_class": SelectField(
            label=_(datamodel.obj.lab('storage_class')),
            description='存储类型',
            widget=MySelect2Widget(can_input=True),
            choices=[[x, x] for x in ["压缩", "未压缩"]],
        ),
        "storage_size": StringField(
            label=_(datamodel.obj.lab('storage_size')),
            description='存储大小',
            widget=BS3TextFieldWidget(),
        ),
        "owner": StringField(
            label=_(datamodel.obj.lab('owner')),
            default='',
            description='责任人,逗号分隔的多个用户',
            widget=BS3TextFieldWidget(),
        ),
        "status": SelectField(
            label=_(datamodel.obj.lab('status')),
            description='数据集状态',
            widget=MySelect2Widget(can_input=True),
            choices=[[x, x] for x in ["损坏", "正常",'未购买','已购买','未标注','已标注','未校验','已校验']],
        ),
        "url": StringField(
            label=_(datamodel.obj.lab('url')),
            description='相关网址',
            widget=MyBS3TextAreaFieldWidget(rows=3),
            default=''
        ),
        "path": StringField(
            label=_(datamodel.obj.lab('path')),
            description='本地路径',
            widget=MyBS3TextAreaFieldWidget(rows=3),
            default=''
        ),
        "download_url": StringField(
            label=_(datamodel.obj.lab('download_url')),
            description='下载地址',
            widget=MyBS3TextAreaFieldWidget(rows=3),
            default=''
        )
    }
    edit_form_extra_fields = add_form_extra_fields


    import_data=True
    download_data=True

    def pre_add(self,item):
        if not item.owner:
            item.owner=g.user.username

    # def post_list(self,items):
    #     flash(Markup('可批量删除不使用的数据集,可批量上传自产数据集'),category='info')
    #     return items


    # 下载
    @expose('/download/<filename>', methods=['GET', 'POST'])
    def download(self, filename):
        if request.method == "GET":
            #通过文件名下载文件
            # filename = secure_filename(filename)        # secure_filename 获取文件夹名的安全版本
            download_path = os.path.join(app.config['UPLOAD_FOLDER'], str(g.user.get_id()))  
            # app.logger.info(download_path)
            if download_path:
                try:
                    # as_attachment=True的参数的话，那么就可以将文件作为一个待下载的文件发送给客户端
                    return send_from_directory(download_path, filename, as_attachment=True)
                except Exception as e:
                    print(e)
            else:
                return '文件不存在'
        else:
            return '下载失败'
    
    # 下载
    @expose('/download_from_script/<id>', methods=['GET', 'POST'])
    def download_from_script(self, id):
        if request.method == "GET":
            download_path = os.path.join(app.config['UPLOAD_FOLDER'], str(g.user.get_id())) 
            # 查询 id 是否存在
            dataset = db.session.query(Dataset).filter_by(id=id).first()
            if not dataset:
                return self.response(404)
            # 查询 文件名 是否存在
            if dataset.dataset_file:
                filename = dataset.dataset_file
            else:
                return self.response(404)
            try:
                return send_from_directory(download_path, filename, as_attachment=True)
            except Exception as e:
                print(e)
        else:
            return '下载失败'
    # flash('no task', 'warning')
    # return redirect('/pipeline_modelview/web/%s' % pipeline.id)
    
    
    # 跳转上传页面
    @expose('/upload_dataset_page/<id>/<name>', methods=['GET', 'POST']) 
    def upload_dataset_page(self, id, name):
        return self.render_template('upload.html', id=id, name=name)
    
    # 上传
    @expose('/upload_dataset/<id>', methods=['GET', 'POST'])
    def upload_dataset(self, id):
        if request.method == 'POST':
            f = request.files['file']
            # app.logger.info(request.files)
            if f.filename == '':
                return '文件名为空'
            # 查询 id 是否存在
            dataset = db.session.query(Dataset).filter_by(id=id).first()
            if not dataset:
                return '数据集id不存在'
            UPLOAD_FOLDER = app.config.get("UPLOAD_FOLDER")
            secure_f = secure_filename(f.filename)        # secure_filename 获取文件夹名的安全版本
            # file_type = os.path.splitext(secure_f)[-1]    # 获得文件后缀
            user_upload_path = os.path.join(UPLOAD_FOLDER, str(g.user.get_id()))    # 用户个人文件夹
            try:
                if not os.path.exists(user_upload_path):
                    os.makedirs(user_upload_path)
            except Exception as e:
                print(e)
            file_name = str(id) + '_' + secure_f
            file_path = os.path.join(user_upload_path, file_name) 
            # 上传，写到磁盘
            try:
                f.save(file_path)
            except Exception as e:
                print(e)
            # 修改文件名 
            dataset.dataset_file = file_name
            db.session.commit()
            return '上传成功'
        else:
            return '上传失败'
    
    
    # @expose('/label_studio/')  #这里指定了接收的username的类型,如果不符合会报错,
    # def label_studio(self):  
    #     url = 'http://10.10.20.233:8089/user/login/?next=/projects/'
    #     return redirect(url)
        
        
class Dataset_ModelView_Api(Dataset_ModelView_base, MyappModelRestApi):
    datamodel = SQLAInterface(Dataset)
    route_base = '/dataset_modelview/api'
appbuilder.add_api(Dataset_ModelView_Api)


class Dataset_ModelView(Dataset_ModelView_base, MyappModelView):
    datamodel = SQLAInterface(Dataset)
appbuilder.add_view_no_menu(Dataset_ModelView)


