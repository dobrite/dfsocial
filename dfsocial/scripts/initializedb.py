import os
import sys


from sqlalchemy import engine_from_config

from pyramid.paster import setup_logging
from pyramid.paster import get_appsettings

from ..models.models import DBSession
from ..models.models import Base

#s = codecs.open('/share/region6-legends.xml', errors='ignore', encoding='utf-8').read()


def load_legends_xml(filename):
    """Takes a filename, assumed in the data directory.

    Returns the contents of the file as a string.
    """

    #TODO not rely on hardcoded dfsocial or cwd
    filepath = os.path.join(os.getcwd(), "dfsocial", "data", filename)

    try:
        with open(filepath) as f:
            xml_ = f.read().strip()
    except IOError:
        raise IOError('Invalid Legends File or Filename')

    return xml_


def usage(argv):
    cmd = os.path.basename(argv[0])
    print('usage: %s <config_uri>\n'
          '(example: "%s development.ini")' % (cmd, cmd))
    sys.exit(1)


def main(argv=sys.argv):
    if len(argv) != 2:
        usage(argv)
    config_uri = argv[1]
    setup_logging(config_uri)
    settings = get_appsettings(config_uri)
    engine = engine_from_config(settings, 'sqlalchemy.')
    DBSession.configure(bind=engine)
    Base.metadata.create_all(engine)
    #xml_ = load_legends_xml('region1-legends.xml')
    #with transaction.manager:
    #    model = MyModel(name='one', value=1)
    #    DBSession.add(model)
