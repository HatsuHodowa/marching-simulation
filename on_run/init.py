width = 85
length = 160
points = [Vector2(-length/2, -width/2), Vector2(-length/2, width/2), Vector2(length/2, width/2), Vector2(length/2, -width/2), Vector2(-length/2, -width/2)]

alt_bool = True
for i in range(8, length, 8):
    line_pos = i - length/2
    if alt_bool:
        points.append(Vector2(line_pos, -width/2))
        points.append(Vector2(line_pos, width/2))
    else:
        points.append(Vector2(line_pos, width/2))
        points.append(Vector2(line_pos, -width/2))

    alt_bool = not alt_bool

lines = Line(points, surface=screen, width=50)