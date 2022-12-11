from myapp import app
from flask import render_template, request, redirect, url_for
from werkzeug.utils import secure_filename
from flask import send_from_directory, send_file
import os

config = app.config

@app.route("/health")
def health():
    return "OK"


@app.route("/healthcheck")
def healthcheck():
    return "OK"


@app.route("/ping")
def ping():
    return "OK"


# @app.route("/upload_page")
# def upload_page():
#     # basepath = os.path.dirname(__file__)  # /home/myapp/myapp/views
#     # pwd = os.getcwd()       # /home/myapp 
#     # return pwd
#     return render_template('upload.html')
# # pwd = os.getcwd()       # /home/myapp 


# # 上传
# @app.route('/upload_dataset/<id>', methods=['GET', 'POST'])
# def upload_dataset(id):
#     if request.method == 'POST':
#         f = request.files['file']
#         # app.logger.info(request.files)
#         if f.filename == '':
#             return '文件名为空'
        
#         UPLOAD_FOLDER = config.get("UPLOAD_FOLDER")
#         secure_f = secure_filename(f.filename)        # secure_filename 获取文件夹名的安全版本
#         file_type = os.path.splitext(secure_f)[-1]
#         file_path = os.path.join(UPLOAD_FOLDER, id) 
        
#         if os.path.exists(file_path):
#             app.logger.info(file_path + '该文件已存在')
#             return '该文件已存在'
#         f.save(file_path)
#         return 'success, 保存的文件名为:' + file_path
#     else:
#         return '上传失败'
    
    

# # 下载
# @app.route('/download_dataset/<filename>', methods=['GET', 'POST'])
# def download(filename):
#     if request.method == "POST":
#         #通过文件名下载文件
#         path = os.path.isfile(os.path.join(app.config['UPLOAD_FOLDER'], filename));
#         if path:
#             return send_from_directory(app.config['UPLOAD_FOLDER'], filename, as_attachment=True)
#         else:
#             return '数据集不存在'
#     else:
#         return '下载失败'
    
    