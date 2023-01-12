from random import randrange
class Pagination():
    p1=0
    def __init__(self,items_p=[],pageSize=10):
        self.items_p=items_p
        self.pageSize=pageSize
        n=len(items_p)%pageSize
        if n==0:
            self.totalPages=int((len(items_p)/pageSize))
            self.currentPage=0
        else:
            self.totalPages=int((len(items_p)/pageSize)+1)
            self.currentPage=0

    def getVisibleItems(self):
        if (len(self.items_p)-self.p1) >= self.pageSize :
            liste=self.items_p[self.p1:self.p1+self.pageSize]
            print(liste)
        else:
            liste=self.items_p[self.p1:len(self.items_p)]
            print(liste)

    def next_page(self):
        if self.p1+self.pageSize > len(self.items_p):
            self.p1=0
        else:
            self.p1+=self.pageSize
    
    def prevPage(self):
        if self.p1-self.pageSize > 0:
            self.p1=0
        else:
            self.p1-=self.pageSize

    def last_page(self):
        long=len(self.items_p)
        n=long%self.pageSize
        if n == 0:
            self.p1=long-self.pageSize
        else:
            self.p1=long-n
    
    def gotopage(self,page):
        self.p1=self.pageSize
        if page in range(1,self.totalPages+1):
            self.p1=self.p1*page-self.p1
        elif page > self.totalPages:
            self.p1=self.p1*self.totalPages-self.p1
        else:
            self.p1=0
        self.getVisibleItems()

    


alphabetList = ("a b c d e f g h i j k l m n o p q r s t u v w x y z").split(" ")
p = Pagination(alphabetList, 5)
p.getVisibleItems()
p.next_page()
p.getVisibleItems()
p.prevPage()
p.getVisibleItems()
p.last_page()
p.getVisibleItems()
p.gotopage(3)