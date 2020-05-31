from vector import Vector


def test():
    # v = Vector()
    # print(v)
    # v2 = Vector([42.0, 101])
    # print(v2)
    # v3 = Vector(range(13,15))
    # print(v3)
    # v4 = Vector(2)
    # print(v4)
    vp1, vp2 = Vector([1.0, 2.0]), Vector([3.0, 4.0])
    print(f"1 {vp1}, 2: {vp2}")
    print(vp1 / vp2)
    print(vp1 / -1)
