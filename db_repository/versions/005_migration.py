from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
alimentacion = Table('alimentacion', pre_meta,
    Column('id_alimentacion', INTEGER, primary_key=True, nullable=False),
    Column('pautasalimentacion', VARCHAR(length=300)),
    Column('nombreblanda', VARCHAR(length=20)),
    Column('nombredura', VARCHAR(length=20)),
)

higiene = Table('higiene', pre_meta,
    Column('id_higiene', INTEGER, primary_key=True, nullable=False),
    Column('tipohigiene', VARCHAR(length=20)),
    Column('pautashigiene', VARCHAR(length=300)),
)

cuidados = Table('cuidados', post_meta,
    Column('id_cuidados', Integer, primary_key=True, nullable=False),
    Column('nombrecuidados', String(length=20)),
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
    pre_meta.tables['alimentacion'].drop()
    pre_meta.tables['higiene'].drop()
    post_meta.tables['cuidados'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['alimentacion'].create()
    pre_meta.tables['higiene'].create()
    post_meta.tables['cuidados'].drop()
