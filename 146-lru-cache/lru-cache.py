class LRUCache:
    class Node:
        def __init__(self,key,val):
            self.key=key
            self.val=val
            self.next=None
            self.prev=None
        
    def __init__(self, capacity: int):
        self.capacity=capacity
        self.map={}
        self.head=self.Node(-1,-1)
        self.tail=self.Node(-1,-1)
        self.head.next=self.tail
        self.tail.prev=self.head
    def addNode(self,newnode):
        temp=self.head.next
        self.head.next=newnode
        newnode.prev=self.head
        newnode.next=temp
        temp.prev=newnode
    def deleteNode(self,delnode):
        delprev=delnode.prev
        delnext=delnode.next
        delprev.next=delnext
        delnext.prev=delprev

    def get(self, key: int) -> int:
        if key in self.map:
            mapnode=self.map[key]
            mapval=mapnode.val
            del self.map[key]
            self.deleteNode(mapnode)
            self.addNode(mapnode)
            self.map[key]=self.head.next
            return mapval
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.map:
            mapnode=self.map[key]
            del self.map[key]
            self.deleteNode(mapnode)
        if len(self.map)==self.capacity:
            del self.map[self.tail.prev.key]
            self.deleteNode(self.tail.prev)
        self.addNode(self.Node(key,value))
        self.map[key]=self.head.next


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)