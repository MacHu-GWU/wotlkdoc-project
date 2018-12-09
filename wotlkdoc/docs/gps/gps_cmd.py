# -*- coding: utf-8 -*-

def parse_go_command(cmd):
    """
    """
    chunks = [s.strip() for s in cmd.strip().split(" ") if s.strip()]
    if len(chunks) == 5:
        if chunks[0] == ".go" and chunks[1] != "xyz":
            x, y, z, map_id = (
                float(chunks[1]), float(chunks[2]), float(chunks[3]),
                int(chunks[4]),
            )

    return x, y, z, map_id


def construct_go_command(x, y, z, map_id):
    return ".go %.1f %.1f %.2f %.f" % (x, y, z, map_id)


def is_valid_go_command(cmd):
    """
    Test if it is a valid go command: ``.go 1.23 4.56 7.89 0``
    """
    try:
        if cmd != cmd.strip():
            return False
        if not cmd.startswith(".go"):
            return False
        if cmd.count(" ") != 4:
            return False
        chunks = cmd.split(" ")
        if len(chunks) != 5:
            return False
        float(chunks[1])
        float(chunks[2])
        float(chunks[3])
        if str(int(chunks[4])) != chunks[4]:
            return False
        return True
    except:
        return False


if __name__ == "__main__":
    print(construct_go_command(*parse_go_command(".go 1 2 3 500")))
