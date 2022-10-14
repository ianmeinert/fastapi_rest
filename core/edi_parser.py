import json
import xmltodict
import os
import subprocess
import time
from typing import List
from fastapi import HTTPException, Response
from fastapi.responses import JSONResponse

from core.config import settings
from core.helper import Utility


class X12:

    temp_files: List[str] = []

    def __init__(self, return_format, uploaded_file):
        self.uploaded_file = uploaded_file
        self.return_format = return_format

        # make sure the path is in place
        Utility.ensurePath(settings.TEMP_UPLOAD_STORE)

    async def parse_file(self):
        response = ""
        match self.return_format:
            case "xml":
                response = Response(
                    content=await self.toXml(), media_type="application/xml"
                )
            case "json":
                response = JSONResponse(content=await self.toJson())
            case _:
                raise HTTPException(status_code=406,
                                    detail="Format not acceptable")

        # delete the files in the temp store that were being worked with
        for file in self.temp_files:
            if os.path.isfile(file):
                os.remove(file)

        return response

    async def toJson(self):
        xml_data = await self.toXml()
        data_dict = xmltodict.parse(xml_data)
        json_data = json.dumps(data_dict)
        return json_data

    async def toXml(self):
        response = ""

        # translate the X12 file to XML
        input_file = await self.save_file()
        self.temp_files.append(input_file)

        basename = os.path.splitext(os.path.basename(input_file))[0]
        # translate the X12 file to XML
        output_path = os.path.join(settings.TEMP_UPLOAD_STORE, basename)

        output_file = output_path + ".xml"
        self.temp_files.append(output_file)

        cmd = "x12xml --outputfile " + output_file + " " + input_file
        print(f"Excuting command: {cmd}")
        subprocess.call(cmd, shell=True)

        with open(output_file, "rb") as reader:
            response = reader.read()

        return response

    async def save_file(self):
        filename = (
            f"{settings.TEMP_UPLOAD_STORE}/{time.time()}-" +
            f"{self.uploaded_file.filename}"
        )

        # process Unicode text
        with open(filename, "wb") as writer:
            # async read chunk
            while content := await self.uploaded_file.read(1024):
                writer.write(content)

        return filename
