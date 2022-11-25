from flask_appbuilder import Model
from sqlalchemy import (
    Boolean,
    Text,
)

from myapp.models.helpers import AuditMixinNullable
from myapp import app
from myapp.models.helpers import ImportMixin
from sqlalchemy import Column, Integer, String

from myapp.models.base import MyappModelBase
metadata = Model.metadata
conf = app.config


class Lyctest(Model,AuditMixinNullable,ImportMixin,MyappModelBase):
    __tablename__ = 'lyctest'
    id = Column(Integer, primary_key=True)
    test_name = Column(String(100), nullable=False)
    test_num = Column(Integer, default=0)
    des = Column(String(300), nullable=False)

    def __repr__(self):
        return self.test_name


    def clone(self):
        return Lyctest(
            test_name = self.test_name,
            test_num = self.test_num,
            des = self.des
        )
