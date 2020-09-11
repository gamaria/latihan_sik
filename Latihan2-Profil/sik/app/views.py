from flask import render_template
from flask_appbuilder.models.sqla.interface import SQLAInterface
from flask_appbuilder import ModelView, ModelRestApi, BaseView, expose, has_access

from . import appbuilder, db
#3.tambahkan modul tabel 
from .models import Profil
"""
    Create your Model based REST API::

    class MyModelApi(ModelRestApi):
        datamodel = SQLAInterface(MyModel)

    appbuilder.add_api(MyModelApi)


    Create your Views::


    class MyModelView(ModelView):
        datamodel = SQLAInterface(MyModel)


    Next, register your Views::


    appbuilder.add_view(
        MyModelView,
        "My View",
        icon="fa-folder-open-o",
        category="My Category",
        category_icon='fa-envelope'
    )
"""

"""
    Application wide 404 error handler
"""


@appbuilder.app.errorhandler(404)
def page_not_found(e):
    return (
        render_template(
            "404.html", base_template=appbuilder.base_template, appbuilder=appbuilder
        ),
        404,
    )

#4.Tampilan admin untuk profil
class ProfilAdminView(ModelView):
    datamodel = SQLAInterface(Profil)


#6.Tampilan profil untuk user umum

class MyView(BaseView):
    
    default_view = "method1"

    @expose("/method1/")
    
    def method1(self):
        # do something with param1
        # and return to previous page or index
        return "Hello"

    @expose("/method2/<string:param1>")
    
    def method2(self, param1):
        # do something with param1
        # and render template with param
        param1 = "Goodbye %s" % (param1)
        return param1

    @expose("/method3/<string:param1>")
    
    def method3(self, param1):
        # do something with param1
        # and render template with param
        param1 = "Goodbye %s" % (param1)
        return self.render_template("profil.html", param1=param1)
    


db.create_all()
#5.register class admin profil
appbuilder.add_view(
    ProfilAdminView, "Data Profil", icon="fa fa-bandcamp", category="Data Desa"
)


appbuilder.add_view(MyView(), "Method1", category="My View")
# appbuilder.add_view(
#     MyView(), "Method2", href='/myview/method2/jonh', category='My View'
# )
# Use add link instead there is no need to create MyView twice.
appbuilder.add_link("Method2", href="/myview/method2/jonh", category="My View")
appbuilder.add_link("Method3", href="/myview/method3/jonh", category="My View")