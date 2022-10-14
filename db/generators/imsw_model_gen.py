import subprocess
import importlib
from core.config import settings


def build_tables(spec_name, schema):
    cmd = (
        "sqlacodegen "
        + settings.IMSW_URI
        + " --outfile "
        + spec_name
        + ".py --schema "
        + schema
    )
    print(f"Excuting command: {cmd}")
    subprocess.call(cmd, shell=True)


def check_spec(spec_name):
    # find the spec
    model_spec = importlib.util.find_spec(spec_name)
    # does the spec exist?
    found = model_spec is not None
    print(f'{spec_name} was {("not " if not found else "")}found')
    return found


def main():
    spec_name = "imsw_models"
    schema = "views"
    if not check_spec(spec_name):
        build_tables(spec_name, schema)
    else:
        print(f"Halting process: {spec_name} model already exists")


if __name__ == "__main__":
    main()
