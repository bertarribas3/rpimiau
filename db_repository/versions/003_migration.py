from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
alimentacion = Table('alimentacion', post_meta,
    Column('id_alimentacion', Integer, primary_key=True, nullable=False),
    Column('tipoalimentacion', String(length=20)),
    Column('nombrealimentacion', String(length=20)),
    Column('pautasalimentacion', String(length=300)),
)

higiene = Table('higiene', post_meta,
    Column('id_higiene', Integer, primary_key=True, nullable=False),
    Column('tipohigiene', String(length=20)),
    Column('pautashigiene', String(length=300)),
)

tratamiento = Table('tratamiento', post_meta,
    Column('id_tratamiento', Integer, primary_key=True, nullable=False),
    Column('nombremedicamento', String(length=20)),
    Column('posologiamedicamento', String(length=100)),
)

veterinario = Table('veterinario', post_meta,
    Column('id_veterinario', Integer, primary_key=True, nullable=False),
    Column('nombreveterinario', String(length=10)),
    Column('apellveterinario', String(length=20)),
    Column('tlfnoveterinario', Integer),
    Column('tlfnourgencias', Integer),
    Column('direccionveterinario', String(length=100)),
    Column('emailveterinario', String(length=30)),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['alimentacion'].create()
    post_meta.tables['higiene'].create()
    post_meta.tables['tratamiento'].create()
    post_meta.tables['veterinario'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['alimentacion'].drop()
    post_meta.tables['higiene'].drop()
    post_meta.tables['tratamiento'].drop()
    post_meta.tables['veterinario'].drop()
