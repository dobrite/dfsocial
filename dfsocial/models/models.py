from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Table
from sqlalchemy import ForeignKey

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
    Column('historical_figure_id', Integer, ForeignKey('historical_figures.id')),
    Column('skill_id', Integer, ForeignKey('skills.id'))
)


historical_figures_spheres = Table(
    'historical_figures_spheres', Base.metadata,
    Column('historical_figure_id', Integer, ForeignKey('historical_figures.id')),
    Column('sphere_id', Integer, ForeignKey('spheres.id'))
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


class Region(ReprMixin, Base):
    __tablename__ = 'regions'
    id = Column(Integer, primary_key=True)
    name = Column(String(length=50), nullable=False)
    region_type = relationship("RegionType", backref="all_regions")
    region_type_id = Column(Integer, ForeignKey('region_types.id'))

    type = association_proxy('region_type', 'text')


class RegionType(Base):
    __tablename__ = 'region_types'
    id = Column(Integer, primary_key=True)
    text = Column(String(length=50), nullable=False)

    regions = association_proxy('all_regions', 'name')


class UndergroundRegion(ReprMixin, Base):
    __tablename__ = 'underground_regions'
    id = Column(Integer, primary_key=True)
    name = Column(String(length=50), nullable=False)
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
    text = Column(String(length=50), nullable=False)

    underground_regions = association_proxy(
        'all_undergournd_regions',
        'name',
    )


class HistoricalFigure(Base):
    __tablename__ = 'historical_figures'
    id = Column(Integer, primary_key=True)
    hf_id = Column(Integer, nullable=False)
    name = Column(String(length=50), nullable=False, unique=True)

    race = relationship('Race')
    caste = relationship('Caste')
    associated_type = relationship('AssociatedType')


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

    def __init__(self, hf_id, name, race, caste, skills, spheres):
        pass


class Race(Base):
    __tablename__ = "races"
    id = Column(Integer, primary_key=True)
    historical_figure_id = Column(Integer, ForeignKey('historical_figures.id'))
    text = Column(String(length=50), nullable=False, unique=True)


class Caste(Base):
    __tablename__ = "castes"
    id = Column(Integer, primary_key=True)
    historical_figure_id = Column(Integer, ForeignKey('historical_figures.id'))
    text = Column(String(length=50), nullable=False, unique=True)


class AssociatedType(Base):
    __tablename__ = "associated_types"
    id = Column(Integer, primary_key=True)
    historical_figure_id = Column(Integer, ForeignKey('historical_figures.id'))
    text = Column(String(length=50), nullable=False, unique=True)


class Skill(Base):
    __tablename__ = "skills"
    id = Column(Integer, primary_key=True)
    text = Column(String(length=50), nullable=False, unique=True)


class Sphere(Base):
    __tablename__ = "spheres"
    id = Column(Integer, primary_key=True)
    text = Column(String(length=50), nullable=False, unique=True)
