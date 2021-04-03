class TimeMap:
    def __init__(self):
        self.time_map = {}

    def set(self, key,value,timestamp):
        if self.time_map.get(key):
            self.time_map[key].update({timestamp:value})
        else:
            self.time_map.update({key:{timestamp:value}})
        

    def get(self, key,timestamp):
        try:
            while timestamp>=0:
                if self.time_map[key].get(timestamp):
                    return self.time_map[key][timestamp]
                timestamp-=1
            return ""
        except KeyError:
            return ""




if __name__ == "__main__":
    obj = TimeMap()
    obj.set("love", "high", 10)
    obj.set("love", "low", 20)
    print(obj.get("love",5))
    print(obj.get("love",10))
    print(obj.get("love",15))
    print(obj.get("love",20))
    print(obj.get("love",25))