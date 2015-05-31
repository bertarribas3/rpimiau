from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
alimentacion = Table('alimentacion', pre_meta,
    Column('id_alimentacion', INTEGER, primary_key=True, nullable=False),
    Column('tipoalimentacion', VARCHAR(length=20)),
    Column('nombrealimentacion', VARCHAR(length=20)),
    Column('pautasalimentacion', VARCHAR(length=300)),
)

alimentacion = Table('alimentacion', post_meta,
    Column('id_alimentacion', Integer, primary_key=True, nullable=False),
    Column('nombredura', String(length=20)),
    Column('nombreblanda', String(length=20)),
    Column('pautasalimentacion', String(length=300)),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['alimentacion'].columns['nombrealimentacion'].drop()
    pre_meta.tables['alimentacion'].columns['tipoalimentacion'].drop()
    post_meta.tables['alimentacion'].columns['nombreblanda'].create()
    post_meta.tables['alimentacion'].columns['nombredura'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['alimentacion'].columns['nombrealimentacion'].create()
    pre_meta.tables['alimentacion'].columns['tipoalimentacion'].create()
    post_meta.tables['alimentacion'].columns['nombreblanda'].drop()
    post_meta.tables['alimentacion'].columns['nombredura'].drop()
