from PIL import Image
from PIL import ImageColor
from path import find_path
from path import Node

im = Image.open("maze.png")
px = im.load()


maze = []
width = im.width
height = im.height

for x in range(width):
    maze.append([])
    for y in range(height):
        if px[x, y] == ImageColor.getrgb("Black"):
            maze[x].append('B')
        else:
            maze[x].append('W')

graph = []
for x in range(width):
    graph.append([])
    for y in range(height):
        n = Node(x, y, maze[x][y])
        graph[x].append(n)
        if n.type == 'B':
            continue

        if x != 0 and maze[x-1][y] == 'W':
            n.add_neighbor(graph[x - 1][y])
            graph[x-1][y].add_neighbor(n)
        if y != 0 and maze[x][y-1] == 'W':
            n.add_neighbor(graph[x][y - 1])
            graph[x][y-1].add_neighbor(n)


nodes = []

for i in graph:
    for j in i:
        if j.type == 'W':
            nodes.append(j)

target = find_path(nodes, graph[1][0], graph[width-2][height-1])

curr = target
while curr.xy != (1, 0):
    im.putpixel(curr.xy, ImageColor.getrgb('green'))
    curr = curr.prev

im.save("solved.png")
