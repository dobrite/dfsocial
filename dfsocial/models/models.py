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


# association table
historical_figures_skills = Table(
    'historical_figures_skills', Base.metadata,
    Column('historical_figure_id', Integer, ForeignKey('historical_figures.id')),
    Column('skill_id', Integer, ForeignKey('skills.id'))
)


#http://docs.sqlalchemy.org/en/latest/orm/mapper_config.html
#mapping-a-class-against-multiple-tables
class HistoricalFigure(Base):
    __tablename__ = 'historical_figures'
    id = Column(Integer, primary_key=True)
    df_id = Column(Integer, nullable=False)
    name = Column(String(length=50), nullable=False)
    race = Column(String(length=50), nullable=False)
    caste = Column(String(length=50), nullable=False)

    skills = relationship(
        'Skill',
        secondary=historical_figures_skills,
        backref='posts'
    )


class Skill(Base):
    __tablename__ = "skills"
    id = Column(Integer, primary_key=True)
    text = Column(String(length=50), nullable=False, unique=True)


class Sphere(Base):
    __tablename__ = "spheres"
    id = Column(Integer, primary_key=True)
    text = Column(String(length=50), nullable=False, unique=True)
