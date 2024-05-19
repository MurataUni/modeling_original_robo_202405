import sys
sys.dont_write_bytecode = True

import os
import glob

class Const:
    project_path = os.path.dirname(os.path.abspath(__file__))
    dir_posture_json = os.sep.join([project_path, '_postures'])
    dir_anime_json = os.sep.join([project_path, '_postures', 'animation'])

    folder_divided = 'divided'

    dir_parts_version_1 = os.sep.join([project_path, '_parts_02_modeling'])
    dir_parts_draft = os.sep.join([project_path, '_parts_01_draft'])
    dirs_parts_modeling = [ #リストの先頭から一致を探す挙動になるので順番注意
        dir_parts_version_1,
        dir_parts_draft,
    ]
    
    dir_parts_reverse = os.sep.join([project_path, '_parts_reversed', folder_divided])
    dirs_parts_assembly = [dir_parts_reverse] + dirs_parts_modeling

    dir_parts_renamed = os.sep.join([project_path, '_parts_renamed', folder_divided])
    
    file_posture_model_generated = 'model_generated.json'
    file_posture_model_posed = 'model_pose_standing.json'

    dir_scaled_posture_json = os.sep.join([project_path, '_scaled', '_postures'])
    dir_scaled_anime_json = os.sep.join([project_path, '_scaled', '_postures', 'animation'])
    dir_scaled_parts = os.sep.join([project_path, '_scaled', folder_divided])

def output_list():
    output = {
        "model": {
            "parts": os.path.join(Const.project_path, Const.dir_parts_renamed),
            "posture_generated": os.path.join(Const.dir_posture_json, Const.file_posture_model_generated),
            "posture_posed": os.path.join(Const.dir_posture_json, Const.file_posture_model_posed),
        },
    }
    output_animation = []
    if os.path.exists(Const.dir_anime_json):
        output_animation = glob.glob(os.path.join(Const.dir_anime_json, "*.json"))

    file_full_name =  os.sep.join([Const.project_path, 'path_list.txt'])
    f = open(file_full_name, "w", encoding="ascii")
    for name, path_dict in output.items():
        f.write("[" + name + "]\n")
        max_path_name = len(max(path_dict.keys(), key=len))
        for path_name, path_value in path_dict.items():
            f.write(path_name.ljust(max_path_name, ' ') + ": " + path_value + "\n")
        f.write("\n")
    f.write("[animation]\n")
    for path in output_animation:
        f.write(path)
        f.write("\n")
    f.close()

if __name__ == "__main__":
    output_list()
