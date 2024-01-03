
import json
from pathlib import Path

basedir = Path("../models")


out = {
    "rootDir": "models",
    "models": [
]}

scene_list = []
for scene in list((basedir).glob("*")):
    name = scene.stem
    out["models"].append(
        {
            "name": f"{name}",
            "file": f"{name}/mesh.glb",
            "thumbnail": f"{name}/cover.png"
        }
    )

with open("../config/models.json", "w") as f:
    json.dump(out, f, indent=2)