import sys
sys.dont_write_bytecode = True

from harbor3d import Dock, Shipwright
import os

sys.path.append(os.sep.join(os.path.dirname(os.path.abspath(__file__)).split(os.sep)[:-1]))
from path_info import Const as PathInfo
from spec_model import Const

def main():
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)))
    fname = ''

    sw = Shipwright(Dock())

    for key, item in Const.tree_flattened.items():
        mirror_info = item.bone.info.mirror_info
        if mirror_info == None:
            continue
        target = sw.search_and_load_stl(PathInfo.dirs_parts_modeling, mirror_info.original + ".stl")
        if target == None:
            continue
        else:
            target.name = key
            sw.deformation(target, lambda x,y,z: (-x if mirror_info.x else x, -y if mirror_info.y else y, -z if mirror_info.z else z))
            if mirror_info.mirror_count()%2 != 0:
                for triangle in target.monocoque_shell.triangles:
                    triangle.inverse()

    sw.generate_stl_binary(path, fname, concatinated=False, divided=True)

if __name__ == "__main__":
    main()