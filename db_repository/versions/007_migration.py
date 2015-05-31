from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
cuidados = Table('cuidados', pre_meta,
    Column('id_cuidados', INTEGER, primary_key=True, nullable=False),
    Column('nombrecuidados', VARCHAR(length=20)),
    Column('nombrecomidadura', VARCHAR(length=20)),
    Column('nombrecomidablanda', VARCHAR(length=20)),
    Column('pautasalimentacion', VARCHAR(length=300)),
    Column('tipohigiene', VARCHAR(length=20)),
    Column('pautashigiene', VARCHAR(length=300)),
    Column('fechafincuidado', DATETIME),
    Column('fechainiciocuidado', DATETIME),
)

cuidados = Table('cuidados', post_meta,
    Column('id_cuidados', Integer, primary_key=True, nullable=False),
    Column('fechainiciocuidado', DateTime),
    Column('fechafincuidado', DateTime),
    Column('nombrecuidador', String(length=20)),
    Column('nombrecomidadura', String(length=20)),
    Column('nombrecomidablanda', String(length=20)),
    Column('pautasalimentacion', String(length=300)),
    Column('tipohigiene', String(length=20)),
    Column('pautashigiene', String(length=300)),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['cuidados'].columns['nombrecuidados'].drop()
    post_meta.tables['cuidados'].columns['nombrecuidador'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['cuidados'].columns['nombrecuidados'].create()
    post_meta.tables['cuidados'].columns['nombrecuidador'].drop()
