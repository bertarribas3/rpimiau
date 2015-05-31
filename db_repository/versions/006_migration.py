from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
cuidados = Table('cuidados', post_meta,
    Column('id_cuidados', Integer, primary_key=True, nullable=False),
    Column('fechainiciocuidado', DateTime),
    Column('fechafincuidado', DateTime),
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
    post_meta.tables['cuidados'].columns['fechafincuidado'].create()
    post_meta.tables['cuidados'].columns['fechainiciocuidado'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['cuidados'].columns['fechafincuidado'].drop()
    post_meta.tables['cuidados'].columns['fechainiciocuidado'].drop()
