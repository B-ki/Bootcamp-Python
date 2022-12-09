import numpy as np
from importlib import metadata
np_data = metadata.metadata("numpy")
print("Metadata about numpy packge:")
print("Version - ", np_data['Version'])
print("Summary - ", np_data['Summary'])

print("-"*8)
print("Metadata dictionary - ")
print(dict(np_data))
