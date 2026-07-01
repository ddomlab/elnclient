from elnclient import ElnClient
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.environ.get("ELN_KEY")
if api_key is None:
    raise ValueError("Please provide an API key")

ex = ElnClient(
    api_key=api_key, 
    url="https://eln.ddomlab.org/api/v2",
    title="This better work", 
    desc="More api testing!!"
    )

ex.upload_file(image_path='./scialog_1.yaml', comment='Testing image')
ex.add_step("Testing")

#TODO Lookup glob, pathlib