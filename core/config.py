
from typing import Any, Dict, List, Optional, Union

from pydantic import AnyHttpUrl, BaseSettings, validator


class Settings(BaseSettings):
    TAGS_METADATA = [
        {
            "name": "orm",
            "description": "Operations with X12 files.",
        },
        {
            "name": "edi",
            "description": "Operations with test data.",
        },
        {
            "name": "test-first-of-all",
            "description": "Demonstrates querying all records in the data "
            + "model, returning first result.",
        },
        {
            "name": "test-first",
            "description": "Demonstrates querying only the first result in "
            + "the data model.",
        },
        {
            "name": "test-filtered",
            "description": "Demonstrates querying all records in the data "
            + "model, then returning a filtered record set.",
        },
        {
            "name": "parse-file",
            "description": "Operations with a fileupload. Demonstrates a "
            + "file in 5010 X12 format being translated into XML or Json",
        },
    ]

    PROJECT_DESCRIPTION = """
FastAPI Prototype API.

## X12

You can **translate X12** to XML or Json.

## Data Modeling

You will be able to:

* **Read data** from certain data stores
"""
    API_V1_STR: str = "/api/v1"
    PROJECT_NAME: str
    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = []

    @validator("BACKEND_CORS_ORIGINS", pre=True)
    def assemble_cors_origins(cls,
                              v: Union[str,
                                       List[str]]) -> Union[List[str], str]:
        if isinstance(v, str) and not v.startswith("["):
            return [i.strip() for i in v.split(",")]
        elif isinstance(v, (list, str)):
            return v
        raise ValueError(v)

    TEMP_UPLOAD_STORE: str

    IMSW_HOST: str
    IMSW_DATABASE: str
    ODBC_SQL_DRIVER: str

    IRIS_HOST: str
    IRIS_PORT: int
    IRIS_DATABASE: str

    CACHE_HOST: str
    CACHE_PORT: int
    CACHE_DATABASE: str

    ODBC_IRIS_DRIVER: str

    IMSW_URI: Optional[str] = None
    IRIS_URI: Optional[str] = None
    CACHE_URI: Optional[str] = None

    @validator("IMSW_URI", pre=True)
    def assemble_imsw_connection(cls,
                                 v: Optional[str],
                                 values: Dict[str, Any]) -> Any:
        if isinstance(v, str):
            return v
        return f"mssql+pyodbc://{values.get('IMSW_HOST')}/" \
            f"{values.get('IMSW_DATABASE')}" \
            f"?driver={values.get('ODBC_SQL_DRIVER')}"

    @validator("IRIS_URI", pre=True)
    def assemble_iris_connection(cls,
                                 v: Optional[str],
                                 values: Dict[str, Any]) -> Any:

        if isinstance(v, str):
            return v

        from credentialcrypto import Credentials

        crypto = Credentials()
        crypto.hostname = values.get('IRIS_HOST')
        credential = crypto.read_cred()

        params = f"DRIVER={values.get('ODBC_IRIS_DRIVER')};" \
                 f"SERVER={values.get('IRIS_HOST')};" \
                 f"PORT={values.get('IRIS_PORT')};" \
                 f"DATABASE={values.get('IRIS_DATABASE')};" \
                 f"UID={credential['username']};" \
                 f"PWD={credential['password']}"
        conn_str = f"mssql+pyodbc:///?odbc_connect={params}"

        return conn_str

    @validator("CACHE_URI", pre=True)
    def assemble_cache_connection(cls,
                                  v: Optional[str],
                                  values: Dict[str, Any]) -> Any:

        if isinstance(v, str):
            return v

        from credentialcrypto import Credentials

        crypto = Credentials()
        crypto.hostname = values.get('CACHE_HOST')
        credential = crypto.read_cred()

        params = f"DRIVER={values.get('ODBC_IRIS_DRIVER')};" \
                 f"SERVER={values.get('CACHE_HOST')};" \
                 f"PORT={values.get('CACHE_PORT')};" \
                 f"DATABASE={values.get('CACHE_DATABASE')};" \
                 f"UID={credential['username']};" \
                 f"PWD={credential['password']}"
        conn_str = f"mssql+pyodbc:///?odbc_connect={params}"

        return conn_str

    class Config:
        case_sensitive = True
        env_file = ".env"


settings = Settings()
