from pyramid.httpexceptions import HTTPFound

from pyramid.response import Response
from pyramid.view import view_config

from sqlalchemy.exc import DBAPIError

from ..models import (
    Departamento,
    Profesor,
)


# @view_config(route_name='home', renderer='../templates/mytemplate.jinja2')
# def my_view(request):
#     try:
#         query = request.dbsession.query(MyModel)
#         one = query.filter(MyModel.name == 'one').first()
#     except DBAPIError:
#         return Response(db_err_msg, content_type='text/plain', status=500)
#     return {'one': one, 'project': 'crud'}


# db_err_msg = """\
# Pyramid is having a problem using your SQL database.  The problem
# might be caused by one of the following things:

# 1.  You may need to run the "initialize_crud_db" script
#     to initialize your database tables.  Check your virtual
#     environment's "bin" directory for this script and try to run it.

# 2.  Your database server may not be running.  Check that the
#     database server referred to by the "sqlalchemy.url" setting in
#     your "development.ini" file is running.

# After you fix the problem, please restart the Pyramid application to
# try it again.
# """


@view_config(route_name='home', renderer='../templates/home.pt')
def home(request):
    return {}


@view_config(route_name='listar_profesores', renderer='../templates/listar_profesores.pt')
def listar_profesores(request):
    query = request.dbsession.query(Profesor).order_by(Profesor.codigo)
    profesores = query.all()
    return {'profesores': profesores}


@view_config(route_name='listar_departamentos', renderer='../templates/listar_departamentos.pt')
def listar_departamentos(request):
    query = request.dbsession.query(Departamento).order_by(Departamento.codigo)
    departamentos = query.all()
    return {'departamentos': departamentos}


@view_config(route_name='crear_departamento', renderer='../templates/crear_departamento.pt')
def crear_departamento(request):
    if 'btn_crear' in request.params:
        nombre = request.params['campo_nombre']
        departamento = Departamento(nombre)
        request.dbsession.add(departamento)
        return HTTPFound(request.route_url('listar_departamentos'))
    if 'btn_cancelar' in request.params:
        return HTTPFound(request.route_url('listar_departamentos'))
    return {}

        
@view_config(route_name='crear_profesor', renderer='../templates/crear_profesor.pt')
def crear_profesor(request):
    query = request.dbsession.query(Departamento)
    departamentos = query.all()
    if 'btn_crear' in request.params:
        nombre = request.params['campo_nombre']
        nacimiento = request.params['campo_nacimiento']
        correo = request.params['campo_correo']
        telefono = request.params['campo_telefono']
        departamento = request.params['select_dep']

        profesor = Profesor(nombre, nacimiento, correo, telefono, departamento)
        request.dbsession.add(profesor)
        return HTTPFound(request.route_url('listar_profesores'))
    if 'btn_cancelar' in request.params:
        return HTTPFound(request.route_url('listar_profesores'))
    return {'departamentos': departamentos}


@view_config(route_name='ver_departamento', renderer='../templates/ver_departamento.pt')
def ver_departamento(request):
    codigo = request.matchdict['codigo']
    query = request.dbsession.query(Departamento)
    departamento = query.filter_by(codigo=codigo).first()
    if departamento is None:
        return HTTPFound(request.route_url('listar_departamentos'))
    return {'departamento': departamento}


@view_config(route_name='ver_profesor', renderer='../templates/ver_profesor.pt')
def ver_profesor(request):
    codigo = request.matchdict['codigo']
    query = request.dbsession.query(Profesor)
    profesor = query.filter_by(codigo=codigo).first()
    if profesor is None:
        return HTTPFound(request.route_url('listar_profesores'))
    
    query = request.dbsession.query(Departamento)
    departamento = query.filter_by(codigo=profesor.departamento).first()
    return {'profesor': profesor, 'departamento': departamento}


@view_config(route_name='eliminar_profesor', renderer='../templates/eliminar_profesor.pt')
def eliminar_profesor(request):
    codigo = request.matchdict['codigo']
    query = request.dbsession.query(Profesor)
    profesor = query.filter_by(codigo=codigo).one()
    if profesor is None:
        return HTTPFound(request.route_url('listar_profesores'))
    if 'btn_borrar' in request.params:
        request.dbsession.delete(profesor)
        return HTTPFound(request.route_url('home'))
    if 'btn_cancelar' in request.params:
        return HTTPFound(request.route_url('listar_profesores'))
    return {'profesor': profesor}


@view_config(route_name='eliminar_departamento', renderer='../templates/eliminar_departamento.pt')
def eliminar_departamento(request):
    codigo = request.matchdict['codigo']
    query = request.dbsession.query(Departamento)
    departamento = query.filter_by(codigo=codigo).one()
    if departamento is None:
        return HTTPFound(request.route_url('listar_departamentos'))
    if 'btn_borrar' in request.params:
        request.dbsession.delete(departamento)
        return HTTPFound(request.route_url('home'))
    if 'btn_cancelar' in request.params:
        return HTTPFound(request.route_url('listar_departamentos'))
    return {'departamento': departamento}


@view_config(route_name='actualizar_departamento', renderer='../templates/actualizar_departamento.pt')
def actualizar_departamento(request):
    codigo = request.matchdict['codigo']
    query = request.dbsession.query(Departamento)
    departamento = query.filter_by(codigo=codigo).one()
    if departamento is None:
        return HTTPFound(request.route_url('listar_departamentos'))
    if 'btn_actualizar' in request.params:
        departamento.nombre = request.params['campo_nombre']
        request.dbsession.add(departamento)
        return HTTPFound(request.route_url('home'))
    if 'btn_cancelar' in request.params:
        return HTTPFound(request.route_url('listar_departamentos'))
    return {'departamento': departamento}


@view_config(route_name='actualizar_profesor', renderer='../templates/actualizar_profesor.pt')
def actualizar_profesor(request):
    codigo = request.matchdict['codigo']
    query = request.dbsession.query(Profesor)
    profesor = query.filter_by(codigo=codigo).one()
    if profesor is None:
        return HTTPFound(request.route_url('listar_profesores'))
    if 'btn_actualizar' in request.params:
        profesor.nombre = request.params['campo_nombre']
        profesor.fecha_nac = request.params['campo_nacimiento']
        profesor.correo = request.params['campo_correo']
        profesor.telefono = request.params['campo_telefono']
        profesor.departamento = request.params['select_dep']
        request.dbsession.add(profesor)
        return HTTPFound(request.route_url('home'))
    if 'btn_cancelar' in request.params:
        return HTTPFound(request.route_url('listar_profesores'))
    query = request.dbsession.query(Departamento)
    departamentos = query.filter_by(codigo=profesor.departamento).all()
    return {'profesor': profesor, 'departamentos': departamentos}
