list(range(1,100))
print('''list(range(1,100)):this is the first reuse''' )
def testfunc(MyName):
    print('hello %s'% MyName)
testfunc('Mary')
def testfunc(FName,LName):
    print('hello %s %s'%(FName ,LName))
testfunc('Mary','Smith')
def saving(pocket_money,paper_route,spending):
    return pocket_money + paper_route -spending
print(saving(10,10,5))
import sys
def silly_age_joke1():
    print('How old are you ?')
    age = int(sys.stdin.readline())
    if age>= 10 and age<=13:
        print('what is 13 + 49 + 84? A headache')
    else:
        print('Huh?')
silly_age_joke1()
