# coding = utf-8

#创建一个节点类
class ListNode(object):
    def __init__(self,nextNode = None,data = 0):
        self.nextNode = nextNode
        self.data = data

class LinkList(object):
    def __init__(self):
        #创建一个头结点
        self.head = ListNode()
    def createLinkList(self,item):
        self.head.nextNode = ListNode(data=item)
        self.head.data = 1
#插入方法
    def insertData(self,index,item):
        q = self.head
        i = 0
        while i < index-1 and q != None:
            i += 1
            q = q.nextNode
        if q == None or i > index-1:
            return  False
        newNode = ListNode(nextNode=q.nextNode,data=item)
        q.nextNode = newNode
        self.head.data += 1
        return True

    def appendData(self,item):
        q = self.head
        while q.nextNode != None:
            q = q.nextNode
        newNode = ListNode(data=item)
        q.nextNode = newNode

#删除一个值
    def deleteData(self,index):
        q = self.head
        i = 0
        while i < index - 1 and q.nextNode != None:
            i += 1
            q = q.nextNode
        if q.nextNode == None or i > index-1:
            return  False
        q.nextNode = q.nextNode.nextNode
        return True
#根据坐标获取值
    def objectOfIndex(self,index):
        q = self.head
        i = 0
        while q != None and i < index:
            i += 1
            q = q.nextNode
        if q == None or i > index:
            return  None
        return q.data
#将链表置空
    def clearList(self):
        self.head.nextNode = None
        self.head.data = 0
#打印列表
    def printLinkList(self):
        head = self.head.nextNode
        while head != None:
            print(head.data,end=' ')
            head = head.nextNode
        print()


num = int(input())
while num > 0:
    num -= 1
    listInit = list(map(int,input().split()))
    listInit.pop(0)
    linkList = LinkList()
    linkList.printLinkList()
    for item in listInit:
        linkList.appendData(item)
    handleNum = int(input())
    while handleNum > 0:
        handleNum -= 1
        handleList = input().split()
        #获取操作指令
        handleOrder = str(handleList.pop(0))
        if handleOrder in "insert":
            indexNum = int(handleList.pop(0))
            handleList.pop(0)
            if indexNum == 0:
                #清空列表
                linkList.clearList()
                for item in handleList:
                    linkList.appendData(int(item))
            else:
                for index , item in enumerate(handleList):
                    linkList.insertData(int(index+1),int(item))
        elif handleOrder in "delete":
            startIndex = int(handleList[0])
            endIndex = int(handleList[1])
            for deleteIndex in reversed(range(startIndex,endIndex+1)):
                linkList.deleteData(deleteIndex)

    linkList.printLinkList()






