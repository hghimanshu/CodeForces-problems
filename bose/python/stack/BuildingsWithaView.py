import collections
def getBuldingsWithaView(buildingList):
    BuildingWithHeight = collections.namedtuple("BuildingWithHeight",("id","Height"))

    stack = []
    for idx,buildng_height in enumerate(buildingList):
        while stack and buildng_height >= stack[-1].Height:
            stack.pop()
        stack.append(BuildingWithHeight(idx,buildng_height))
    return stack


if __name__ == "__main__":
    # buildingList = [4,5,7,5,3,2,6]
    buildingList = [4,5,5,3,2,6]
    print(getBuldingsWithaView(buildingList))