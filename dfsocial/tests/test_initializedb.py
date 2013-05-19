import unittest

import pytest

from pyramid import testing

from ..models.models import DBSession


hf = """
    <historical_figure>
        <id>8</id>
        <name>obi lieshaft the bad dungeons</name>
        <race>FORGOTTEN_BEAST_9</race>
        <caste>DEFAULT</caste>
        <appeared>1</appeared>
        <birth_year>-255</birth_year>
        <birth_seconds72>-1</birth_seconds72>
        <death_year>-1</death_year>
        <death_seconds72>-1</death_seconds72>
        <associated_type>STANDARD</associated_type>
        <sphere>caverns</sphere>
        <sphere>torture</sphere>
        <hf_skill>
            <skill>SITUATIONAL_AWARENESS</skill>
            <total_ip>4500</total_ip>
        </hf_skill>
        <hf_skill>
            <skill>DODGING</skill>
            <total_ip>4500</total_ip>
        </hf_skill>
        <hf_skill>
            <skill>MELEE_COMBAT</skill>
            <total_ip>4500</total_ip>
        </hf_skill>
        <hf_skill>
            <skill>STANCE_STRIKE</skill>
            <total_ip>4500</total_ip>
        </hf_skill>
        <hf_skill>
            <skill>GRASP_STRIKE</skill>
            <total_ip>4500</total_ip>
        </hf_skill>
        <hf_skill>
            <skill>BITE</skill>
            <total_ip>4500</total_ip>
        </hf_skill>
        <hf_skill>
            <skill>WRESTLING</skill>
            <total_ip>4500</total_ip>
        </hf_skill>
    </historical_figure>
"""


class TestInitializeDB(unittest.TestCase):
    def setUp(self):
        pass

    # def load_xml(self):
    #     from ..scripts.initializedb import load_legends_xml
    #     return load_legends_xml('region1-legends.xml')

    def test_usage(self):
        from ..scripts.initializedb import usage
        with pytest.raises(SystemExit):
            usage(["", ""])

    def test_main_calls_usage(self):
        from ..scripts.initializedb import main
        with pytest.raises(SystemExit):
            main(argv=["", "", ""])

    def test_main_creates_tables(self):
        from ..scripts.initializedb import main
        main(argv=["", "test.ini"])

    def test_load_legends_xml_for_invalid_filename(self):
        from ..scripts.initializedb import load_legends_xml
        with pytest.raises(IOError) as e:
            load_legends_xml('invalid.xml')

    def test_load_legends_xml_returns_string(self):
        from ..scripts.initializedb import load_legends_xml
        xml_ = load_legends_xml('region1-legends.xml')

        assert isinstance(xml_, str)
