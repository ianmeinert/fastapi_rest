
# FastAPI Prototype
This is a prototype Application Programming Interface (API) which is intended to showcase several Python3 packages.

  1. InterSystems IRIS for Health connections,
  2. Microsoft SQL Server connections,
  3. Reverse engineering a database schema, and
  4. Parsing an EDI X12 5010 file into XML and JSon formats

## Security
With any database connection, security is paramount. Two approaches are introduced here:

  1. Integrated trust and
  2. Locally stored credentials

The latter will be encrypted and decrypted as needed from flatfiles using a custom cryptology package.

## Installation
### Install packages with *pip: -r requirements.txt*
The following command will install the packages according to the configuration file requirements.txt.

`$ pip install -r requirements.txt`

This document isn't yet fully organized ;)

### Credential Cryptography
The `credentialcrypto` package is only available in my Github and not available in pypi. Clone the repository and build per the projects instructions.

### InterSystems IRIS for Health
This uses a connection to IRIS for Health via irisnative python package. Download the [irisnative Python3 wheel](https://github.com/intersystems/Samples-python-helloworld/tree/master/wheel) and follow the instructions below. A server administrator will need to verify IRIS for Health Server has an ODBC driver installed.

  1. Check the supported tags for wheel version for your system(platform).
     - run the following command: `pip debug --verbose > pip_whl_tags.txt`
  2. When you run the command, you will get many lists, along with supported tags. Find the one that matches your environment
  3. Create a copy of the nearest match and rename it appropriately.
     - example pip_whl_tags.txt:
	  
			  cp34-abi3-win_amd64
			  cp33-abi3-win_amd64
			  cp32-abi3-win_amd64
			  py310-none-win_amd64 <-- matches my requirements
			  py3-none-win_amd64
			  py39-none-win_amd64
			  py38-none-win_amd64
			  py37-none-win_amd64

     - run the command: `c:\>copy irisnative-1.0.0-py37-none-win_amd64.whl irisnative-1.0.0-py310-none-win_amd64.whl`
		
  4. Install the package
  `c:\>pip install irisnative-1.0.0-py310-none-win_amd64.whl`

## Notes on SQLAlchemy Model Generation
When ORM is autogenerating models, the MetaData class may not be added to the SqlAlchemy import list. If this is the case, you'll need to manually import it.
