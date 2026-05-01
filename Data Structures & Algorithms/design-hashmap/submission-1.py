class ListNode:
    def __init__(self,key,val):
        self.key = key
        self.val = val
        self.nxt = None

class MyHashMap:

    def __init__(self):
        self.size = 3313
        self.bucket = []

        for i in range(self.size):
            self.bucket.append(ListNode(-1,-1))

    def _insert(self,idx,key,val):
        head = self.bucket[idx]
        
        node = self._search(idx,key)

        if node:
            node.val = val
            return
        
        node = ListNode(key,val)
        
        ref = head.nxt
        head.nxt = node
        node.nxt = ref
    
    def put(self, key: int, value: int) -> None:
        idx = key%self.size
        self._insert(idx,key,value)

    def _search(self,idx,key):
        head = self.bucket[idx].nxt
        
        while head:
            if head.key==key:
                return head
            head = head.nxt

        return None

    def get(self, key: int) -> int:
        idx = key%self.size
        res = self._search(idx,key)
        return res.val if res else -1
    
    def _remove(self,idx,key):
        pre = self.bucket[idx]
        curr = pre.nxt

        while curr:
            if curr.key==key:
                break
            pre = curr
            curr = curr.nxt

        if curr:
            pre.nxt = curr.nxt
    
    def remove(self, key: int) -> None:
        idx = key%self.size
        self._remove(idx,key)


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)class ListNode: