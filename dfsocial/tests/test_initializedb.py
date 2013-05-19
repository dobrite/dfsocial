import pytest

from dfsocial.tests import BaseTestCase


class TestInitializeDB(BaseTestCase):
    def test_usage(self):
        from dfsocial.scripts.initializedb import usage
        with pytest.raises(SystemExit):
            usage(["", ""])

    def test_main_calls_usage(self):
        from dfsocial.scripts.initializedb import main
        with pytest.raises(SystemExit):
            main(argv=["", "", ""])

    def test_main_creates_tables(self):
        from dfsocial.scripts.initializedb import main
        main(argv=["", "test.ini"])

    def test_load_legends_xml_for_invalid_filename(self):
        from dfsocial.scripts.initializedb import load_legends_xml
        with pytest.raises(IOError) as e:
            load_legends_xml('invalid.xml')

    def test_load_legends_xml_returns_string(self):
        from ..scripts.initializedb import load_legends_xml
        xml_ = load_legends_xml('region1-legends.xml')
        print "YARRR"

        assert isinstance(xml_, str)
