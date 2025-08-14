# math_server.py


from mcp.server.fastmcp import FastMCP
import os
import requests
from datetime import datetime
from pathlib import Path
import re

import sys
from io import BytesIO
import pikepdf

import datetime
import pdfx





mcp = FastMCP("Metadata")

@mcp.tool()
def get_file_properties(file_url):
    """
    Get the properties of a file from a URL.
    
    args: file_url (str): The URL of the file to retrieve properties for.
    returns: a dictionary containing the file properties, or None if an error occurred.
    the following key in the meta data is based on the content of the file:
    - categories
    - keywords
    - description

    """

    # Send a GET request to the URL

    response = requests.get(file_url)
    #print(BytesIO(response.content))
    pdf_data = BytesIO(response.content)
    with open("temp.pdf", "wb") as f:
        f.write(pdf_data.getbuffer())
    pdf = pdfx.PDFx("temp.pdf")
    result = pdf.get_metadata()
    print(result)
    #print(dir(result))
    metadata = {
        "ID": result['xapmm'].get("DocumentID", None),
        "Modified": result['xap'].get("ModifyDate", None) if 'xap' in result and 'ModifyDate' in result['xap'] else result.get("ModDate", None),
        "Title": result.get("Title", None),
        "Author": result.get("Author", None),
        "URL": file_url,
        "Format": result['dc'].get("format", None),
        'Maintainer':'Bundesamt für Eich- und Vermessungswesen',
        'Publisher': 'Bundesamt für Eich- und Vermessungswesen',
        'License': 'CC BY 4.0',
        'date': result['xap'].get("CreateDate", None) if 'xap' in result and 'CreateDate' in result['xap'] else result.get("CreationDate", None),

        'categories': pdf.get_references_as_dict(),
      

    }
    return metadata


# if __name__ == "__main__":
#     mcp.run(transport="stdio")

res = get_file_properties("https://www.bev.gv.at/dam/bevgvat/PDF-Dateien/Vermessungswesen/Leistungsbericht/LEISTUNGSBERICHT_2007.pdf")
print(res)