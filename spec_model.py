import sys
sys.dont_write_bytecode = True

import numpy as np
import os


from harbor3d.util.bone_util import Bone, Info, Restriction, DefaultAngle, DefaultLocation, ModelMirrorInfo, LocationMirrorInfo, AngleMirrorInfo
from harbor3d.util.bone_json_util import PostureWrapper, BoneKeys
from harbor3d.util.json_util import JsonLoader

from path_info import Const as PathInfo

class Const:

    default_len = 0.5
    short_len = 0.05
    scale_for_avator_limit = 0.8

    tree_hand_l = Bone(name="wrist_l", info=Info(alias_of="wrist"), child=[
        Bone(name="palm_l", child=[
            Bone(name="thumb_proximal_phalanx_l", info=Info(alias_of="thumb_proximal_phalanx", length=short_len), child=[
                Bone(name="thumb_distal_phalanx_l", info=Info(alias_of="thumb_distal_phalanx", length=short_len))
            ]),
            Bone(name="index_f_proximal_phalanx_l", info=Info(alias_of="f_proximal_phalanx", length=short_len), child=[
                Bone(name="index_f_middle_phalanx_l", info=Info(alias_of="f_middle_phalanx", length=short_len), child=[
                    Bone(name="index_f_distal_phalanx_l", info=Info(alias_of="f_distal_phalanx", length=short_len))
                ])
            ]),
            Bone(name="middle_f_proximal_phalanx_l", info=Info(alias_of="f_proximal_phalanx", length=short_len), child=[
                Bone(name="middle_f_middle_phalanx_l", info=Info(alias_of="f_middle_phalanx", length=short_len), child=[
                    Bone(name="middle_f_distal_phalanx_l", info=Info(alias_of="f_distal_phalanx", length=short_len))
                ])
            ]),
            Bone(name="ring_f_proximal_phalanx_l", info=Info(alias_of="f_proximal_phalanx", length=short_len), child=[
                Bone(name="ring_f_middle_phalanx_l", info=Info(alias_of="f_middle_phalanx", length=short_len), child=[
                    Bone(name="ring_f_distal_phalanx_l", info=Info(alias_of="f_distal_phalanx", length=short_len))
                ])
            ]),
            Bone(name="little_f_proximal_phalanx_l", info=Info(alias_of="f_proximal_phalanx", length=short_len), child=[
                Bone(name="little_f_middle_phalanx_l", info=Info(alias_of="f_middle_phalanx", length=short_len), child=[
                    Bone(name="little_f_distal_phalanx_l", info=Info(alias_of="f_distal_phalanx", length=short_len))
                ])
            ]),
            Bone(name="weapon_l"),
        ])
    ])

    tree_hand_l_pose_info = {
        "palm_l": {"angle": DefaultAngle(y=-np.pi/2), "location": DefaultLocation(y=0.5)},

        "thumb_proximal_phalanx_l": {"angle": DefaultAngle(y=np.pi, x=-np.pi/6), "location": DefaultLocation(x=-0.7 ,y=0.7, z=0.5)},
        "thumb_distal_phalanx_l": {"location": DefaultLocation(y=0.9)},

        "index_f_proximal_phalanx_l": {"location": DefaultLocation(x=-0.6 ,y=2.2, z=-0.45)},
        "middle_f_proximal_phalanx_l": {"location": DefaultLocation(x=-0.2 ,y=2.3, z=-0.45), "angle": DefaultAngle(x=np.pi/3)},
        "ring_f_proximal_phalanx_l": {"location": DefaultLocation(x=0.2 ,y=2.3, z=-0.45), "angle": DefaultAngle(x=np.pi/3)},
        "little_f_proximal_phalanx_l": {"location": DefaultLocation(x=0.6 ,y=2.2, z=-0.45), "angle": DefaultAngle(x=np.pi/3)},

        "index_f_middle_phalanx_l": {"location": DefaultLocation(y=0.7)},
        "middle_f_middle_phalanx_l": {"location": DefaultLocation(y=0.7), "angle": DefaultAngle(x=np.pi/3)},
        "ring_f_middle_phalanx_l": {"location": DefaultLocation(y=0.7), "angle": DefaultAngle(x=np.pi/3)},
        "little_f_middle_phalanx_l": {"location": DefaultLocation(y=0.7), "angle": DefaultAngle(x=np.pi/3)},

        "index_f_distal_phalanx_l": {"location": DefaultLocation(y=0.6)},
        "middle_f_distal_phalanx_l": {"location": DefaultLocation(y=0.6), "angle": DefaultAngle(x=np.pi/4)},
        "ring_f_distal_phalanx_l": {"location": DefaultLocation(y=0.6), "angle": DefaultAngle(x=np.pi/4)},
        "little_f_distal_phalanx_l": {"location": DefaultLocation(y=0.6), "angle": DefaultAngle(x=np.pi/4)},

        "weapon_l": {"location": DefaultLocation(y=1.8, z=0.3)}
    }

    tree_hand_l_flattened = tree_hand_l.flatten(None, {})
    for k,v in tree_hand_l_pose_info.items():
        tree_hand_l_flattened[k].bone.info.set_pose(**v)
    
    location_mirror_x = LocationMirrorInfo(x=True)
    tree_hand_r_mirror_info = {
        "palm_r": {
            "model": ModelMirrorInfo(original="palm_l", x=True),
            "angle": AngleMirrorInfo(y=True),
        }, 
        
        "thumb_proximal_phalanx_r": {"location": location_mirror_x},

        "index_f_proximal_phalanx_r": {"location": location_mirror_x},
        "middle_f_proximal_phalanx_r": {"location": location_mirror_x},
        "ring_f_proximal_phalanx_r": {"location": location_mirror_x},
        "little_f_proximal_phalanx_r": {"location": location_mirror_x},
    }
    
    tree_arm_l = Bone(name="shoulder_base_l", child=[
        Bone(name="shoulder_bellows_1_l", info=Info(alias_of="shoulder_bellows"), child=[
            Bone(name="shoulder_bellows_2_l", info=Info(alias_of="shoulder_bellows"), child=[
                Bone(name="shoulder_bellows_3_l", info=Info(alias_of="shoulder_bellows"), child=[
                    Bone(name="upper_arm_base_l", child=[
                        Bone(name="upper_arm_l", child=[
                            Bone(name="elbow_l", child=[
                                Bone(name="forearm_adapter_l", child=[
                                    Bone(name="forearm_root_l", child=[
                                        Bone(name="forearm_attachment_l"),
                                        Bone(name="forearm_end_l", child=[
                                            tree_hand_l
                                        ])
                                    ])
                                ])
                            ])
                        ])
                    ])
                ])
            ])
        ])
    ])

    tree_arm_l_pose_info = {
        "shoulder_base_l": {"angle": DefaultAngle(z=-np.pi/2), "location": DefaultLocation(x=3.8 ,y=5.4, z=-1.2)},
        "shoulder_bellows_1_l": {"angle": DefaultAngle(z=-np.pi/6), "location": DefaultLocation(y=0.8)},
        "shoulder_bellows_2_l": {"angle": DefaultAngle(z=-np.pi/6), "location": DefaultLocation(y=1.2)},
        "shoulder_bellows_3_l": {"angle": DefaultAngle(z=-np.pi/6), "location": DefaultLocation(y=1.2)},
        "upper_arm_base_l": {"angle": DefaultAngle(y=np.pi/2), "location": DefaultLocation(y=1.)},
        "upper_arm_l": {"location": DefaultLocation(y=0.5)},
        "elbow_l": {"angle": DefaultAngle(z=-np.pi/2+np.pi/12), "location": DefaultLocation(y=2.5, x=-0.65)},
        "forearm_adapter_l": {"angle": DefaultAngle(z=np.pi/2), "location": DefaultLocation(y=1.2)},
        "forearm_root_l": {"angle": DefaultAngle(y=np.pi/3), "location": DefaultLocation(x=0.6, y=1.2)},
        "forearm_attachment_l": {"angle": DefaultAngle(z=-np.pi/2), "location": DefaultLocation(x=0.7, y=2.)},
        "forearm_end_l": {"location": DefaultLocation(y=0.5)},
        "wrist_l": {"location": DefaultLocation(y=3.5)},
    }
    tree_arm_l_flattened = tree_arm_l.flatten(None, {})
    for k,v in tree_arm_l_pose_info.items():
        tree_arm_l_flattened[k].bone.info.set_pose(**v)

    tree_arm_r = tree_arm_l.left_to_right()
    tree_arm_r_mirror_info = {
        "shoulder_base_r": {
            "model": ModelMirrorInfo(original="shoulder_base_l", x=True),
            "angle": AngleMirrorInfo(z=True),
            "location": LocationMirrorInfo(x=True),
        },"shoulder_bellows_1_r": {
            "angle": AngleMirrorInfo(z=True),
        },"shoulder_bellows_2_r": {
            "angle": AngleMirrorInfo(z=True),
        },"shoulder_bellows_3_r": {
            "angle": AngleMirrorInfo(z=True),
        },"upper_arm_base_r": {
            "model": ModelMirrorInfo(original="upper_arm_base_l", x=True),
            "angle": AngleMirrorInfo(y=True),
        },"upper_arm_r": {
            "model": ModelMirrorInfo(original="upper_arm_l", x=True),
        },"elbow_r": {
            "model": ModelMirrorInfo(original="elbow_l", x=True),
            "angle": AngleMirrorInfo(z=True),
            "location": LocationMirrorInfo(x=True),
        },"forearm_adapter_r": {
            "model": ModelMirrorInfo(original="forearm_adapter_l",x=True, y=True),
            "angle": AngleMirrorInfo(z=True),
        },"forearm_root_r": {
            "model": ModelMirrorInfo(original="forearm_root_l",x=True, y=True),
            "angle": AngleMirrorInfo(y=True),
            "location": LocationMirrorInfo(x=True),
        },"forearm_attachment_r": {
            "angle": AngleMirrorInfo(z=True),
            "location": LocationMirrorInfo(x=True),
        },"forearm_end_r": {
            "model": ModelMirrorInfo(original="forearm_end_l", x=True),
        },
    }

    tree_arm_r_flattened = tree_arm_r.flatten(None, {})
    for k,v in tree_arm_r_mirror_info.items():
        tree_arm_r_flattened[k].bone.info.set_mirror_info(**v)

    for k,v in tree_hand_r_mirror_info.items():
        tree_arm_r_flattened[k].bone.info.set_mirror_info(**v)

    tree_body_upper = Bone(name="spine", child=[
        Bone(name="body_upper", child=[
            tree_arm_l,
            tree_arm_r,
            Bone(name="neck_joint", child=[
                Bone(name="neck", child=[
                    Bone(name="head_adapter", child=[
                        Bone(name="head_base", child=[
                            Bone(name="head", child=[
                                Bone(name="head_armor_adapter_l", child=[
                                    Bone(name="head_armor_l")
                                ]),
                                Bone(name="head_armor_adapter_r", child=[
                                    Bone(name="head_armor_r")
                                ]),
                                Bone(name="eye_adapter", child=[
                                    Bone(name="eye_base", child=[
                                        Bone(name="eye")
                                    ])
                                ])
                            ])
                        ])
                    ])
                ])
            ])
        ])
    ])

    tree_body_upper_pose_info = {
        "spine": {"location": DefaultLocation(y=1.)},
        "body_upper": {"location": DefaultLocation(y=2.)},
        "neck_joint": {"location": DefaultLocation(y=4.2, z=1.5)},
        "neck": {"angle": DefaultAngle(x=-np.pi/2)},
        "head_adapter": {"angle": DefaultAngle(x=np.pi/2), "location": DefaultLocation(y=1.6)},
        "head_base": {"location": DefaultLocation(y=0.5)},
        "head": {"angle": DefaultAngle(x=np.pi/2)},
        "head_armor_adapter_l": {"angle": DefaultAngle(z=-np.pi/4), "location": DefaultLocation(y=0.6, z=-0.6)},
        "head_armor_l": {"angle": DefaultAngle(z=-np.pi/4), "location": DefaultLocation(y=1.4)},
        "head_armor_adapter_r": {"angle": DefaultAngle(z=-np.pi/4), "location": DefaultLocation(y=0.6, z=-0.6)},
        "head_armor_r": {"angle": DefaultAngle(z=-np.pi/4), "location": DefaultLocation(y=1.4)},
        "eye_adapter": {"angle": DefaultAngle(x=np.pi/2), "location": DefaultLocation(y=2.7, z=0.5)},
        "eye_base": {"location": DefaultLocation(y=0.3)},
        "eye": {"angle": DefaultAngle(x=-np.pi/2), "location": DefaultLocation(y=0.6)},
    }

    tree_body_upper_mirror_info = {
        "head_armor_adapter_r": {
            "model": ModelMirrorInfo(original="head_armor_adapter_l", x=True),
            "angle": AngleMirrorInfo(z=True),
        },
        "head_armor_r": {
            "model": ModelMirrorInfo(original="head_armor_l", x=True),
            "angle": AngleMirrorInfo(z=True),
        },
    }

    tree_body_upper_flattened = tree_body_upper.flatten(None, {})
    for k,v in tree_body_upper_pose_info.items():
        tree_body_upper_flattened[k].bone.info.set_pose(**v)
    for k,v in tree_body_upper_mirror_info.items():
        tree_body_upper_flattened[k].bone.info.set_mirror_info(**v)

    tree_leg_l = Bone(name="leg_rotation_base_l", info=Info(alias_of="leg_rotation_base"), child=[
        Bone(name="leg_extension_base_l", info=Info(alias_of="leg_extension_base"), child=[
            Bone(name="femur_root_l", info=Info(alias_of="femur_root") ,child=[
                Bone(name="femur_end_l", info=Info(alias_of="femur_end"), child=[
                    Bone(name="shin_l", child=[
                        Bone(name="metatarsal_l", child=[
                            Bone(name="foot_adapter_l", child=[
                                Bone(name="foot_l", child=[
                                    Bone(name="foot_front_l"),
                                    Bone(name="foot_back_l"),
                                ])
                            ])
                        ])
                    ])
                ])
            ])
        ])
    ])
    tree_leg_l_pose_info = {
        "leg_rotation_base_l": {"location": DefaultLocation(x=1.6 ,z=-0.2)},
        "leg_extension_base_l": {"location": DefaultLocation(y=0.8, z=0.5)},
        "femur_root_l": {"angle": DefaultAngle(x=-np.pi/2), "location": DefaultLocation(y=1.1)},
        "femur_end_l": {"location": DefaultLocation(y=2.)},
        "shin_l": {"angle": DefaultAngle(x=np.pi*2/3), "location": DefaultLocation(y=1.2)},
        "metatarsal_l": {"angle": DefaultAngle(x=-np.pi/4), "location": DefaultLocation(y=5.5)},
        "foot_adapter_l": {"angle": DefaultAngle(x=np.pi/12), "location": DefaultLocation(y=4.5)},
        "foot_l": {"location": DefaultLocation(y=1.)},
        "foot_front_l": {"angle": DefaultAngle(x=-np.pi/2), "location": DefaultLocation(y=0.8, z=-1.4)},
        "foot_back_l": {"angle": DefaultAngle(x=np.pi/2), "location": DefaultLocation(y=0.8, z=1.4)},
    }
    tree_leg_l_mirror_info = {
        "foot_back_l": {
            "model": ModelMirrorInfo(original="foot_front_l", y=True),
        }
    }

    tree_leg_l_flattened = tree_leg_l.flatten(None, {})
    for k,v in tree_leg_l_pose_info.items():
        tree_leg_l_flattened[k].bone.info.set_pose(**v)
    for k,v in tree_leg_l_mirror_info.items():
        tree_leg_l_flattened[k].bone.info.set_mirror_info(**v)

    tree_leg_r = tree_leg_l.left_to_right()
    tree_leg_r_mirror_info = {
        "leg_rotation_base_r": {
            "location": LocationMirrorInfo(x=True),
        },"shin_r": {
            "model": ModelMirrorInfo(original="shin_l", x=True),
        },"metatarsal_r": {
            "model": ModelMirrorInfo(original="metatarsal_l", x=True),
        },"foot_adapter_r": {
            "model": ModelMirrorInfo(original="foot_adapter_l", x=True),
        },"foot_r": {
            "model": ModelMirrorInfo(original="foot_l", x=True),
        },"foot_front_r": {
            "model": ModelMirrorInfo(original="foot_front_l", x=True),
        },"foot_back_r": {
            "model": ModelMirrorInfo(original="foot_front_l", x=True, y=True),
        },
    }

    tree_leg_r_flattened = tree_leg_r.flatten(None, {})
    for k,v in tree_leg_r_mirror_info.items():
        tree_leg_r_flattened[k].bone.info.set_mirror_info(**v)

    tree_dummy = Bone(name="dummy_hip", child=[
        Bone(name="dummy_spine", child=[
            Bone(name="dummy_chest", child=[
                Bone(name="dummy_neck", child=[
                    Bone(name="dummy_head"),
                ]),
                Bone(name="dummy_shoulder_l", child=[
                    Bone(name="dummy_upper_arm_l", child=[
                        Bone(name="dummy_lower_arm_l", child=[
                            Bone(name="dummy_hand_l")
                        ])
                    ])
                ]),
                Bone(name="dummy_shoulder_r", child=[
                    Bone(name="dummy_upper_arm_r", child=[
                        Bone(name="dummy_lower_arm_r", child=[
                            Bone(name="dummy_hand_r")
                        ])
                    ])
                ]),
            ])
        ]),
        Bone(name="dummy_upper_leg_l", child=[
            Bone(name="dummy_lower_leg_l", child=[
                Bone(name="dummy_foot_l"),
            ]),
        ]),
        Bone(name="dummy_upper_leg_r", child=[
            Bone(name="dummy_lower_leg_r", child=[
                Bone(name="dummy_foot_r"),
            ]),
        ]),
    ])

    tree_dummy_info = {
        "dummy_hip": {"location": DefaultLocation(y=12., z=-1.)},
        "dummy_spine": {"location": DefaultLocation(y=1.)},
        "dummy_chest": {"location": DefaultLocation(y=2.)},
        "dummy_neck": {"location": DefaultLocation(y=1.)},
        "dummy_head": {"location": DefaultLocation(y=1.)},
        "dummy_shoulder_l": {"location": DefaultLocation(x=-1.,y=1.)},
        "dummy_upper_arm_l": {"location": DefaultLocation(y=1.)},
        "dummy_lower_arm_l": {"location": DefaultLocation(y=1.)},
        "dummy_hand_l": {"location": DefaultLocation(y=1.)},
        "dummy_shoulder_r": {"location": DefaultLocation(x=1.,y=1.)},
        "dummy_upper_arm_r": {"location": DefaultLocation(y=1.)},
        "dummy_lower_arm_r": {"location": DefaultLocation(y=1.)},
        "dummy_hand_r": {"location": DefaultLocation(y=1.)},
        "dummy_upper_leg_l": {"location": DefaultLocation(x=-1.,y=1.)},
        "dummy_lower_leg_l": {"location": DefaultLocation(y=1.)},
        "dummy_foot_l": {"location": DefaultLocation(y=1.)},
        "dummy_upper_leg_r": {"location": DefaultLocation(x=1.,y=1.)},
        "dummy_lower_leg_r": {"location": DefaultLocation(y=1.)},
        "dummy_foot_r": {"location": DefaultLocation(y=1.)},
    }

    tree_dummy_flattened = tree_dummy.flatten(None, {})
    for k,v in tree_dummy_info.items():
        tree_dummy_flattened[k].bone.info.set_pose(**v)

    tree = Bone(name="base", child=[
        Bone(name="body_lower", child=[
            Bone(name="back_panel"),
            tree_body_upper,
            Bone(name="leg_base", child=[
                tree_leg_l,
                tree_leg_r,
            ])
        ]),
        tree_dummy
    ])

    tree_pose_info = {
        "body_lower": {"location": DefaultLocation(y=13.2)},
        "back_panel": {"angle": DefaultAngle(x=-np.pi*8/9), "location": DefaultLocation(y=1.,z=-3.)},
        "leg_base": {"angle": DefaultAngle(y=np.pi, z=np.pi), "location": DefaultLocation(z=-1.3)},
    }

    tree_flattened = tree.flatten(None, {})

    for k,v in tree_pose_info.items():
        tree_flattened[k].bone.info.set_pose(**v)

    bones_relationship = {k:v.key_parent for k,v in tree_flattened.items()}

    bones_alias = {k:v.bone.info.alias_of for k,v in tree_flattened.items() if v.bone.info.alias_of != None}

    bones = bones_relationship.keys()

def main():
    generate_posture(os.path.join(PathInfo.dir_posture_json, PathInfo.file_posture_model_generated))
    fnames = [PathInfo.file_posture_model_default, PathInfo.file_posture_model_posed]
    for fname in fnames:
        apply_bone_relationship(os.path.join(PathInfo.dir_posture_json,fname))

def generate_posture(posture_file):
    pw = PostureWrapper({})
    for key in Const.bones:
        bone = Const.tree_flattened[key].bone
        length_info = bone.info.length
        length = length_info if length_info!=None else Const.default_len
        pw.add_bone(key, Const.bones_relationship[key], length)
        if bone.info.default_angle != None:
            pw.set_rotation(
                key,
                bone.info.default_angle.get_rotation(**(AngleMirrorInfo().info() if bone.info.angle_mirror == None else bone.info.angle_mirror.info())),
            )
        if bone.info.default_location != None:
            pw.set_offset_on_bone_axis(
                key=key,
                **bone.info.default_location.get_location(**(LocationMirrorInfo().info() if bone.info.location_mirror == None else bone.info.location_mirror.info())),
            )
    json_loader = JsonLoader(posture_file)
    json_loader.dictionary = pw.postures
    json_loader.dump()

def apply_bone_relationship(posture_file):
    json_loader = JsonLoader(posture_file)
    pw = PostureWrapper(json_loader.fetch())
    for key in Const.bones:       
        length_info = Const.tree_flattened[key].bone.info.length
        length = length_info if length_info!=None else Const.default_len
        
        if pw.has_key(key):
            pw.set_length(key, length)
            pw.set_parent(key, Const.bones_relationship[key])
        else:
            pw.add_bone(key, Const.bones_relationship[key], length)
    
    key_diff = pw.postures.keys() ^ Const.bones
    for key in key_diff:
        del pw.postures[key]

    json_loader.dictionary = pw.postures
    json_loader.dump()
    
if __name__ == "__main__":
    main()
