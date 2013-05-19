from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Table
from sqlalchemy import ForeignKey

from sqlalchemy.ext.declarative import declarative_base

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


class HistoricalFigure(Base):
    __tablename__ = 'historical_figures'
    id = Column(Integer, primary_key=True)
    df_id = Column(Integer, nullable=False)
    name = Column(String(length=50), nullable=False, unique=True)

    race = relationship('Race')
    caste = relationship('Caste')
    associated_type = relationship('AssociatedType')

    # 'appeared',
    # 'associated_type',
    # 'birth_seconds72',
    # 'birth_year',
    # 'caste',
    # 'death_seconds72',
    # 'death_year',
    # 'deity',
    # 'ent_pop_id',
    # 'entity_former_position_link',
    # 'entity_link',
    # 'entity_position_link',
    # 'hf_link',
    # 'hf_skill',
    # 'id',
    # 'interaction_knowledge',
    # 'name',
    # 'race',
    # 'site_link',
    # 'sphere' m-m

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

    def __init__(self, df_id, name, race, caste, skills, spheres):
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
