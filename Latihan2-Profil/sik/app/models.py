from flask_appbuilder import Model
from sqlalchemy import Column, Integer, String, ForeignKey, Text
from sqlalchemy.orm import relationship


"""

You can use the extra Flask-AppBuilder fields and Mixin's

AuditMixin will add automatic timestamp of created and modified by who


"""
#2.tabel profil kelurahan
class Profil(Model):
    id = Column(Integer, primary_key=True)
    sejarah = Column(Text, nullable=False)
    profil_wilayah = Column(Text, nullable=False)
    def __repr__(self):
        return self.sejarah