#ROOT_PATH = os.path.dirname(__file__)


def pytest_sessionstart():
    from py.test import config

    # Only run database setup on master (in case of xdist/multiproc mode)
    if not hasattr(config, 'slaveinput'):
        from sqlalchemy import engine_from_config
        from paste.deploy.loadwsgi import appconfig

        from dfsocial.models.models import Base

        settings = appconfig('config:test.ini', relative_to='./')
        engine = engine_from_config(settings, prefix='sqlalchemy.')

        print 'Creating the tables on the test database %s' % engine

        #config = Configurator(settings=settings)
        #initialize_sql(settings, config)

        Base.metadata.drop_all(engine)
        Base.metadata.create_all(engine)
