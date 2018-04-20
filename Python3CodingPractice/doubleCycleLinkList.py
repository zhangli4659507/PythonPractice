#coding  =  utf-8

class LinkNode(object):
    def __init__(self,data,nextNode = None,preNode = None):
        self.data = data
        self.nextNode = nextNode
        self.preNode = preNode
class DoubleCycleLinkList():
    def createLinkList(self,elem):
        self.head = LinkNode(elem)
        self.head.nextNode = self.head
        self.head.preNode = self.head
        print(self.head)
        pass
    def getElemP(self,index):
        head = self.head
        i = 0
        while i < index -1 and head.nextNode != self.head:
            i += 1
            head = head.nextNode
        if i != index - 1:
            return None
        return head

    def insertLinkList(self,index,elem):
        head = self.getElemP(index)
        if head == None:
            # 插入失败
            print("error")
            return  False
        newNode = LinkNode(elem,nextNode=head,preNode=head.preNode)
        print(elem,newNode,head)
        head.preNode.nextNode = newNode
        head.preNode = newNode
    def deleteElemOfIndex(self,index):
        pass
    def printDoubleCycleLinkList(self):
        head = self.head
        while True:
            if head == self.head:
                print("aaaaa",head.data,head, end=' ')
                break
            else:
                print(head.data,head,head.nextNode,end=' ')
                head = head.nextNode
        print()
linkList = DoubleCycleLinkList()
linkList.createLinkList(10)
linkList.insertLinkList(1,11)
linkList.insertLinkList(1,1111)

linkList.printDoubleCycleLinkList()