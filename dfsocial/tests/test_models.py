from dfsocial.tests import BaseTestCase


class TestHistoricalFigureModel(BaseTestCase):
    def test_historical_figure_has_df_id(self):
        from dfsocial.models.models import HistoricalFigure
        hf = HistoricalFigure()
        assert(hasattr(hf, "df_id"))


class TestSkillModel(BaseTestCase):
    def test_skill_has_name(self):
        from dfsocial.models.models import Skill
        s = Skill()
        assert(hasattr(s, "text"))
