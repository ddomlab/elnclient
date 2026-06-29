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

ex.upload_image(image_path='Picture/testing.jpg', comment='Testing image')
ex.upload_image(image_path='Pictures/capture_20260625_100237.jpg', comment='Image number 2')
ex.add_step("Testing")

#TODO Lookup glob, pathlib