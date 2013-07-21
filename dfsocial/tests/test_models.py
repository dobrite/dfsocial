from dfsocial.tests import BaseTestCase


class TestRegionModel(BaseTestCase):
    def test_regions_region_types_relationship(self):
        from dfsocial.models.models import Region
        from dfsocial.models.models import RegionType

        region_type = RegionType(text=u'RegionType')
        region = Region(name=u'region', region_type=region_type)

        self.session.add(region_type)
        self.session.commit()

        assert region.region_type is region_type
        assert region.region_type.text == region_type.text
        assert region.region_type.id == region_type.id
        assert region.region_type_id == region_type.id

        assert region.type == region_type.text

        assert region_type.regions == [u'region', ]
        assert region_type.all_regions[0].name == u'region'
        assert region_type.all_regions[0].id == region.id
        assert region_type.all_regions[0] is region

    def test_underground_region_underground_region_types_relationship(self):
        from dfsocial.models.models import UndergroundRegion
        from dfsocial.models.models import UndergroundRegionType

        underground_region_type = UndergroundRegionType(text=u"urt")
        underground_region = UndergroundRegion(
            name=u"ur",
            depth=100,
            underground_region_type=underground_region_type
        )

        self.session.add(underground_region)
        self.session.commit()

        assert underground_region.underground_region_type is underground_region_type
        assert underground_region.underground_region_type.text == underground_region_type.text
        assert underground_region.underground_region_type.id == underground_region_type.id
        assert underground_region.underground_region_type_id == underground_region_type.id

        assert underground_region.type == underground_region_type.text

        assert underground_region_type.underground_regions == [u"ur", ]
        assert underground_region_type.all_underground_regions[0].name == u"ur"
        assert underground_region_type.all_underground_regions[0].id == underground_region.id
        assert underground_region_type.all_underground_regions[0] is underground_region

    #def test_historical_figure_link_historical_figure_link_types_relationship(self):
    #    from dfsocial.models.models import HistoricalFigureLink
    #    from dfsocial.models.models import HistoricalFigureLinkTypes

    #    historical_figure_link = HistoricalFigureLink(

