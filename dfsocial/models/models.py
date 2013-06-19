from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import Table
from sqlalchemy import ForeignKey
from sqlalchemy import Unicode
from sqlalchemy import Boolean

from sqlalchemy.dialects import postgresql
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.associationproxy import association_proxy

from sqlalchemy.orm import relationship
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker

from zope.sqlalchemy import ZopeTransactionExtension

DBSession = scoped_session(sessionmaker(extension=ZopeTransactionExtension()))
Base = declarative_base()


historical_figures_skills = Table(
    'historical_figures_skills', Base.metadata,
    Column(
        'historical_figure_id',
        Integer,
        ForeignKey('historical_figures.id')
    ),
    Column(
        'skill_id',
        Integer,
        ForeignKey('skills.id')
    )
)


historical_figures_spheres = Table(
    'historical_figures_spheres', Base.metadata,
    Column(
        'historical_figure_id',
        Integer,
        ForeignKey('historical_figures.id')
    ),
    Column(
        'sphere_id',
        Integer,
        ForeignKey('spheres.id')
    )
)


class ReprMixin(object):
    def __repr__(self):
        def reprs():
            for col in self.__table__.c:
                yield col.name, repr(getattr(self, col.name))

        def format(seq):
            for key, value in seq:
                yield '%s=%s' % (key, value)

        args = '(%s)' % ', '.join(format(reprs()))
        classy = type(self).__name__
        return classy + args


class Artifact(ReprMixin, Base):
    __tablename__ = 'artifacts'
    id = Column(Integer, primary_key=True)
    name = Column(Unicode(length=100), nullable=True, unique=True)
    item = Column(Unicode(length=100), nullable=False, unique=True)


class Site(ReprMixin, Base):
    __tablename__ = 'sites'
    id = Column(Integer, primary_key=True)
    name = Column(Unicode(length=100), nullable=False, unique=True)
    site_type = relationship('SiteType', backref="all_sites")
    coords = Column(postgresql.ARRAY(Integer), nullable=False)
    structures = Column(Boolean, nullable=True)
    type = association_proxy('site_type', 'text')


class SiteType(ReprMixin, Base):
    __tablename__ = 'site_types'
    id = Column(Integer, primary_key=True)
    text = Column(Unicode(length=50), nullable=False, unique=True)


class HistoricalEra(ReprMixin, Base):
    __tablename__ = 'historical_eras'
    id = Column(Integer, primary_key=True)
    name = Column(Unicode(length=50), nullable=False, unique=True)
    start_year = Column(Integer, nullable=False)


class Entity(ReprMixin, Base):
    __tablename__ = 'entities'
    id = Column(Integer, primary_key=True)
    name = Column(Unicode(100), nullable=True, unique=True)


class EntityPopulation:
    __tablename__ = 'entity_populations'
    id = Column(Integer, primary_key=True)


class HistoricalEvent(ReprMixin, Base):
    __tablename__ = 'historical_events'


class Region(ReprMixin, Base):
    __tablename__ = 'regions'
    id = Column(Integer, primary_key=True)
    name = Column(Unicode(length=100), nullable=False)
    region_type = relationship("RegionType", backref="all_regions")
    region_type_id = Column(Integer, ForeignKey('region_types.id'))

    type = association_proxy('region_type', 'text')


class RegionType(ReprMixin, Base):
    __tablename__ = 'region_types'
    id = Column(Integer, primary_key=True)
    text = Column(Unicode(length=50), nullable=False, unique=True)

    regions = association_proxy('all_regions', 'name')


class UndergroundRegion(ReprMixin, Base):
    __tablename__ = 'underground_regions'
    id = Column(Integer, primary_key=True)
    name = Column(Unicode(length=50), nullable=False)
    depth = Column(Integer, nullable=False)

    underground_region_type = relationship(
        "UndergroundRegionType",
        backref="all_underground_regions",
    )
    underground_region_type_id = Column(
        Integer,
        ForeignKey('underground_region_types.id'),
    )

    type = association_proxy('underground_region_type', 'text')


class UndergroundRegionType(Base):
    __tablename__ = 'underground_region_types'
    id = Column(Integer, primary_key=True)
    text = Column(Unicode(length=50), nullable=False, unique=True)

    underground_regions = association_proxy(
        'all_underground_regions',
        'name',
    )


class HistoricalFigureLinkType(ReprMixin, Base):
    __tablename__ = 'historical_figure_link_types'
    id = Column(Integer, primary_key=True)
    historical_figure_link_type = relationship(
        'HistoricalFigureLinkType',
        backref="all_historical_figure_types"
    )


class HistoricalFigureLink(ReprMixin, Base):
    __tablename__ = 'historical_figure_links'

    id = Column(Integer, primary_key=True)
    hf_id = Column(Integer, ForeignKey('historical_figures.id'))
    link_strength = Column(Integer, nullable=True)
    #link_type = Column(


class HistoricalFigure(Base):
    __tablename__ = 'historical_figures'
    id = Column(Integer, primary_key=True)
    name = Column(Unicode(length=50), nullable=False, unique=True)

    race = relationship('Race')
    caste = relationship('Caste')

    appeared = Column(Integer, nullable=False)
    birth_year = Column(Integer, nullable=False)
    birth_seconds = Column(Integer, nullable=False)
    death_year = Column(Integer, nullable=False)
    death_seconds = Column(Integer, nullable=False)

    associated_type = relationship('AssociatedType')
    #hf_link 0-10
    #  hfid 1
    #  link_strength 0 or 1
    #  link_type 1
    #entity_reputation 0-10
    # first_ageless_season_count 0 or 1
    # entity_id 1
    # unsolved_murders 0 or 1
    # first_ageless_years 0 or 1
    #entity_link 0-10
    #  entity_id 1
    #  link_strength 0 or 1
    #  link_type 1
    #hf_skill 0-10
    # skill 1
    # total_ip 1
    #ent_pop_id 0 or 1
    #diety 0 or 1
    #goal 0 or 1
    #holds_artifact 0 or 1
    #active_interaction 0 or 1
    #entity_position_link 0 or 1
    #  entity_id 1
    #  start_year 1
    #  position_profile_id 1
    #current_identity_id 0 or 1
    #used_identity_id 0 or 1
    #entity_former_position_link 0-3
    #  end_year 1
    #  entity_id 1
    #  start_year 1
    #  position_profile_id 1
    #animated 0 or 1
    #animated_string 0 or 1
    #journey_pet 0-10
    #interaction_knowledge 0 or 1
    #site_link 0 or 1
    #  sub_id 0 or 1
    #  entity_id 0 or 1
    #  site_id 1
    #  link_type 1
    #force 0 or 1
    skills = relationship(
        'Skill',
        secondary=historical_figures_skills,
        backref='historical_figures',
    )

    spheres = relationship(
        'Sphere',
        secondary=historical_figures_spheres,
        backref='historical_figures',
    )


class Race(Base):
    __tablename__ = "races"
    id = Column(Integer, primary_key=True)
    historical_figure_id = Column(Integer, ForeignKey('historical_figures.id'))
    text = Column(Unicode(length=50), nullable=False, unique=True)


class Caste(Base):
    __tablename__ = "castes"
    id = Column(Integer, primary_key=True)
    historical_figure_id = Column(Integer, ForeignKey('historical_figures.id'))
    text = Column(Unicode(length=50), nullable=False, unique=True)


class AssociatedType(Base):
    __tablename__ = "associated_types"
    id = Column(Integer, primary_key=True)
    historical_figure_id = Column(Integer, ForeignKey('historical_figures.id'))
    text = Column(Unicode(length=50), nullable=False, unique=True)


class Skill(Base):
    __tablename__ = "skills"
    id = Column(Integer, primary_key=True)
    text = Column(Unicode(length=50), nullable=False, unique=True)


class Sphere(Base):
    __tablename__ = "spheres"
    id = Column(Integer, primary_key=True)
    text = Column(Unicode(length=50), nullable=False, unique=True)
