def are_points_collinear(points):
    if len(points) < 3:
        return True
    x0, y0 = points[0]
    x1, y1 = points[1]
    for x2, y2 in points[2:]:
        if (y1 - y0) * (x2 - x1) != (y2 - y1) * (x1 - x0):
            return False
    return True

coords = [(1, 2), (2, 3), (3, 4)]
print(are_points_collinear(coords))
