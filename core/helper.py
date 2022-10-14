from datetime import datetime
from pathlib import Path


class Utility(object):
    """
    A helper class containing common functions.
    """

    @staticmethod
    def ensurePath(path):
        """Ensures the path is in place by creating it if not exist.

        Parameters
        ----------
        path : str
            The directory path used by the application
        """

        # make sure the path exists where the files will be created
        if not Path(path).exists():
            Path(path).mkdir(exist_ok=True)

    @staticmethod
    def today_in_numeric_format() -> str:
        return datetime.today().strftime("%Y%m%d")

    @staticmethod
    def isvalid_numeric_date(date):
        val = False
        try:
            date = datetime(
                year=int(date[0:4]), month=int(date[4:6]), day=int(date[6:8])
            )
            val = True
        except ValueError:
            val = False

        return val


class FileUtility(object):
    @staticmethod
    def readfile(path) -> str:
        with open(path, "r", encoding="UTF-8") as read_obj:
            return read_obj.read()

    @staticmethod
    def load_properties(filepath, sep="=", comment_char="#"):
        """
        Read the file passed as parameter as a properties file.
        """
        props = {}

        with open(filepath, "rt") as f:
            for line in f:
                stripped = line.strip()
                if stripped and not stripped.startswith(comment_char):
                    key_value = stripped.split(sep)
                    key = key_value[0].strip()
                    value = sep.join(key_value[1:]).strip().strip('"')
                    props[key] = value
        return props
