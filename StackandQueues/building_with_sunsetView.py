from collections import namedtuple

def stackApproach(buildings):
    buildingWithHeight = namedtuple('buildingWithHeight', ('id', 'height'))
    c = []

    for idx, b in enumerate(buildings):
        while c and b >= c[-1].height:
            c.pop()
        c.append(buildingWithHeight(idx, b))
    
    return [i.id for i in reversed(c)]




buildings = [10, 4, 6, 12, 5]

result = stackApproach(buildings)
print(result)
