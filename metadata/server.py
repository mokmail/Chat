# math_server.py


from mcp.server.fastmcp import FastMCP
import os
import requests
from datetime import datetime
from pathlib import Path

import pikepdf
import sys

def extract_pdf_metadata(pdf_path):
    """
    Extract metadata from a PDF file.
    """
    metadata = {}
    try:
        with pikepdf.open(pdf_path) as pdf:
            metadata = pdf.docinfo
    except Exception as e:
        print(f"Error reading {pdf_path}: {e}", file=sys.stderr)
    return metadata 

mcp = FastMCP("Metadata")

@mcp.tool()
def get_file_properties(file_url):
    """
    Get the properties of a file from a URL.
    args: file_url (str): The URL of the file to retrieve properties for.
    returns: string containing the file properties, or None if an error occurred.

    """

    # Send a GET request to the URL

    response = requests.get(file_url)
    with open('metadata.pdf', 'wb') as f:
        f.write(response.content)

    metadata = extract_pdf_metadata('metadata.pdf')
    return metadata


if __name__ == "__main__":
    mcp.run(transport="stdio")