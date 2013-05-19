import unittest

from pyramid import testing

from ..models.models import DBSession


class TestHistoricalFigureModel(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_historical_figure_has_df_id(self):
        from ..models.models import HistoricalFigure
        hf = HistoricalFigure()
        assert(hasattr(hf, "df_id"))


class TestSkillModel(unittest.TestCase):
    def test_skill_has_name(self):
        from ..models.models import Skill
        s = Skill()
        assert(hasattr(s, "text"))
