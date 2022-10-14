from sqlalchemy import (
    Boolean,
    Column,
    DateTime,
    Identity,
    Integer,
    MetaData,
    Numeric,
    String,
    Table,
)
from sqlalchemy.dialects.mssql import DATETIME2, TINYINT

metadata = MetaData()


t_ViewRestricted = Table(
    "ViewRestricted",
    metadata,
    Column("RowId", Integer, Identity(), nullable=False),
    Column("SomeInt", Integer),
    Column("SomeBit", Boolean),
    Column("SomeVarchar", String(10, "SQL_Latin1_General_CP1_CI_AS")),
    Column("SomeDateTime", DateTime),
    Column("SomeNumeric", Numeric(16, 2)),
    schema="views",
)
