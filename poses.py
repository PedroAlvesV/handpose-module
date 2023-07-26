poses = []

# 0 fingers pose
p = {"FIST": [False]*5}
poses.append(p)

# 1 finger poses
p = {
    "THUMB": [True, False, False, False, False],
    "POINT": [False, True, False, False, False],
    "MIDDLE": [False, False, True, False, False],
    "RING": [False, False, False, True, False],
    "PINKY": [False, False, False, False, True]
}
poses.append(p)

# 2 fingers poses
p = {
    "L": [True, True, False, False, False],
    "PEACE": [False, True, True, False, False],
    "ROCK": [False, True, False, False, True],
    "SHAKA": [True, False, False, False, True]
}
poses.append(p)

# 3 fingers poses
p = {
    "THUMB_THREE": [True, True, True, False, False],
    "THREE": [False, True, True, True, False],
    "PINKY_THREE": [False, False, True, True, True],
    "LOVE": [True, True, False, False, True]
}
poses.append(p)

# 4 fingers poses
p = {
    "FOUR": [False, True, True, True, True],
    "THUMB_FOUR": [True, True, True, True, False]
}
poses.append(p)

# 5 fingers poses
p = {"OPEN": [True]*5}
poses.append(p)

defined_poses = set()
for pose_class in poses:
    for pose in pose_class:
        defined_poses.add(pose)

def thumbs_orientation(lmList):
    # d1 = tip of thumb to ring finger knuckle
    # d2 = tip of thumb to thumb knuckle
    # 4,1 -> x ponta
    # 4,2 -> y ponta
    # 2,1 -> x base
    # 2,2 -> y base
    if(lmList[4][2] > lmList[2][2]):
        return "DOWN"
    return "UP"