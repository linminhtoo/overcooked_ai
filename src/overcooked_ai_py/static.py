import os
import random
import string
from pathlib import Path


random_string = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(20))
print(f"RANDOM STRING: {random_string}")

_current_dir = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(_current_dir, "data")
HUMAN_DATA_DIR = os.path.join(DATA_DIR, "human_data")
PLANNERS_DIR = os.path.join(DATA_DIR, f"planners_{random_string}")
Path(PLANNERS_DIR).mkdir(parents=True, exist_ok=True)
LAYOUTS_DIR = os.path.join(DATA_DIR, "layouts")
GRAPHICS_DIR = os.path.join(DATA_DIR, "graphics")
FONTS_DIR = os.path.join(DATA_DIR, "fonts")
TESTING_DATA_DIR = os.path.join(DATA_DIR, "testing")
