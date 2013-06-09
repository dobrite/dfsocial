from dfsocial.tests import BaseTestCase


# class TestHistoricalFigureModel(BaseTestCase):
#     def test_historical_figure_has_df_id(self):
#         from dfsocial.models.models import HistoricalFigure
#         hf = HistoricalFigure()
#         assert(hasattr(hf, "df_id"))


# class TestSkillModel(BaseTestCase):
#     def test_skill_has_name(self):
#         from dfsocial.models.models import Skill
#         s = Skill()
#         assert(hasattr(s, "text"))

class TestRegionModel(BaseTestCase):
    def test_regions_region_types_relationship(self):
        from dfsocial.models.models import Region
        from dfsocial.models.models import RegionType

        rt = RegionType(id=1, text='Ocean')
        r = Region(id=0, name='gulf', region_type=ocean)

        self.session.add(rt)
        self.session.commit()

        assert r.region_type is rt
        assert gulf.region_type.text == ocean.text
        assert gulf.region_type.id == ocean.id
        assert gulf.region_type_id == ocean.id

        assert gulf.type == ocean.text

        assert ocean.all_regions[0].name == 'gulf'
        assert ocean.regions == ['gulf',]
        assert ocean.all_regions[0].id == gulf.id
        #assert ocean.ids == [0,]
        assert ocean.all_regions[0] is gulf

    def test_regions_region_types_relationship_delete(self):
        from dfsocial.models.models import Region
        from dfsocial.models.models import RegionType

        ocean = RegionType(id=1, text='Ocean')
        gulf = Region(id=0, name='gulf', region_type=ocean)

        self.session.add(gulf)
        self.session.commit()
        self.session.delete(gulf)
        self.session.commit()

        region = self.session.query(Region).all()
        assert region == []

        region_type = self.session.query(RegionType).all()
        #assert region_type == []
