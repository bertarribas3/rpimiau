from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
cuidados = Table('cuidados', pre_meta,
    Column('id_cuidados', INTEGER, primary_key=True, nullable=False),
    Column('nombrecomidadura', VARCHAR(length=20)),
    Column('nombrecomidablanda', VARCHAR(length=20)),
    Column('pautasalimentacion', VARCHAR(length=300)),
    Column('tipohigiene', VARCHAR(length=20)),
    Column('pautashigiene', VARCHAR(length=300)),
    Column('fechafincuidado', DATETIME),
    Column('fechainiciocuidado', DATETIME),
    Column('nombrecuidador', VARCHAR(length=20)),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['cuidados'].columns['fechafincuidado'].drop()
    pre_meta.tables['cuidados'].columns['fechainiciocuidado'].drop()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['cuidados'].columns['fechafincuidado'].create()
    pre_meta.tables['cuidados'].columns['fechainiciocuidado'].create()
