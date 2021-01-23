"""
FORMATS:-
point: (float x, float y)
line: [point a, point b]
quad: [line A, line B, line C, line D]
"""

def get_points_from_file(path):
    points = ()
    with open(path, 'r') as file:
        lines = file.readlines()
        num = 0
        x, y = 0, 0
        for line_index in range(len(lines)):
            if line_index == 0:
                num = int(lines[line_index])
            elif line_index > num * 2:
                break
            elif line_index % 2 != 0:
                x = int(lines[line_index])
            else:
                y = int(lines[line_index])
                points = (*points, (x, y))
        return points

points = ()
INFINITY = float('inf')
# Taking Points as input and adding it to points tuple

# comment out this line if not taking input from file
points = get_points_from_file('sample_input.txt')

# uncomment till FLAG to accept input from user
# n = int(input())
# while n > 0:
#     n -= 1
#     x = int(input())
#     y = int(input())
#     point = (x, y)
#     points = (*point, point)
# FLAG

def get_quads(i, j, k, l):
    """
    Arguments: i, j, k, l are four points

    Return value: List of all possible quads from points i, j, k, l
    """
    return [[[i, j], [j, k], [k, l], [l, i]],
            [[i, j], [j, l], [l, k], [k, i]]]

def slope(line):
    """
    Arguments: line

    Return Value: slope of line
    """
    if line[1][0] - line[0][0] == 0:
        return INFINITY
    return (line[1][1] - line[0][1]) / (line[1][0] - line[0][0])

def is_parallel(line1, line2):
    """
    Arguments: line1 and line 2 are each lines

    Return Value: True if line1 is parallel to line2
    False otherwise.
    """
    m1 = slope(line1)
    m2 = slope(line2)
    if m1 == INFINITY:
        return m2 == INFINITY
    if m2 == INFINITY:
        return m1 == INFINITY
    return m1 == m2

def is_perp(line1, line2):
    """
    Arguments: line1 and line 2 are each lines

    Return Value: True if line1 is perpendicular to line2
    False otherwise.
    """
    m1 = slope(line1)
    m2 = slope(line2)
    if m1 == INFINITY:
        return m2 == 0
    if m2 == INFINITY:
        return m1 == 0
    return m1 * m2 == -1

def sq_length(line):
    """
    Argument: line

    Return Value: square of length of line
    """
    (x1, y1), (x2, y2) = line
    return (y2 - y1) ** 2 + (x2 - x1) ** 2

def area_of_rect(quad):
    """
    Argument: quad

    Return Value: Returns square of area of quadrilateral.
    Assuming that it is a rectangle.
    """
    return sq_length(quad[0]) * sq_length(quad[1])

def is_rect(quad):
    """
    Argument: quad

    Return Value: Returns true if quad is a rectangle
    Returns false otherwise
    """
    lineA, lineB, lineC, lineD = quad
    if lineA[0] == lineD[1] and lineA[1] == lineB[0] and lineB[1] == lineC[0] and lineC[1] == lineD[0]:
        if is_parallel(lineA, lineC) and is_parallel(lineB, lineD) and is_perp(lineA, lineB) and is_perp(lineC, lineD):
            return True
    return False

def is_sq(quad):
    """
    Argument: quad

    Return Value: Returns true if quad is a square
    Returns false otherwise
    """
    if not is_rect(quad):
        return False
    lineA, lineB, lineC, lineD = quad
    if sq_length(lineA) == sq_length(lineB):
        return True
    return False

def format_and_print(rect):
    """
    Argument: quad

    Return Value: None

    Prints the quad in format expected by VPROPEL.
    """
    lineA, lineB, lineC, lineD = rect
    a = lineA[0]
    b = lineB[0]
    c = lineC[0]
    d = lineD[0]
    print([[a, b], [d, c], [a, d], [b, c]])

biggest_sq = []
biggest_sq_area = 0
biggest_rect = []
biggest_rect_area = 0

# Going through every possible combination of four points
# and checking if the combination forms a square or rectangle
# and if so then checking it's area is greater than the previous greatest
# area. If it is then it is stored accordingly.
for i in range(len(points)):
    for j in range(len(points)):
        for k in range(len(points)):
            for l in range(len(points)):
                quads = get_quads(points[i], points[j], points[k], points[l])
                for quad in quads:
                    if is_rect(quad):
                        area = area_of_rect(quad)
                        if is_sq(quad):
                            if area > biggest_sq_area:
                                biggest_sq = quad
                                biggest_sq_area = area
                            continue
                        if area > biggest_rect_area:
                            biggest_rect = quad
                            biggest_rect_area = area

format_and_print(biggest_rect)
format_and_print(biggest_sq)
