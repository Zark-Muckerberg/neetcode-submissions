class LRUCache:

    def __init__(self, capacity: int):
        #create an ordered map cache and store the max capacity cap
        self.cache=OrderedDict()
        self.cap = capacity
    def get(self, key: int) -> int:
        #if key not in cache, return -1
        if key not in self.cache:
            return -1
        #if key is in cache we update the value and move the key to most recent position
        self.cache.move_to_end(key)
        return self.cache[key]
        
    def put(self, key: int, value: int) -> None:
        #if key is already in cache, we update its value and move it to most recent pos
        if key in self.cache:
            self.cache.move_to_end(key)
        self.cache[key]=value

        #if size of cache greater than cap.remove the least recently used key
        if len(self.cache) > self.cap:
            self.cache.popitem(last=False)

        
