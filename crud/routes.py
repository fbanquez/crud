def includeme(config):
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('home', '/')
    ## Configuring teacher's routes
    config.add_route('listar_profesores', '/listar_profesores')
    config.add_route('crear_profesor', '/crear_profesor')
    config.add_route('ver_profesor', '/ver_profesor/{codigo}')
    config.add_route('eliminar_profesor', '/eliminar_profesor/{codigo}')
    config.add_route('actualizar_profesor', '/actualizar_profesor/{codigo}')
    ## Configuring Departament's routes
    config.add_route('listar_departamentos', '/listar_departamentos')
    config.add_route('crear_departamento', '/crear_departamento')
    config.add_route('ver_departamento', '/ver_departamento/{codigo}')
    config.add_route('eliminar_departamento', '/eliminar_departamento/{codigo}')
    config.add_route('actualizar_departamento', '/actualizar_departamento/{codigo}')
