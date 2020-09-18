import random
a=int(input("starting "))
b=int(input("ending "))
n=[]
for i in range(a,b+1):
    n.append(i)
g=random.choice(n)
#g
s=100
if g%2==0:
    print("Hint: g is a even")
else:
    print("Hint:g is odd")

d=int(input("guess the number"))
if d==g:
    print("correct")
    print("Score ",s)
    print("Wow")

else:
    print("wrong")
    print("1.require hint")
    print("2.give up")
    
    c=int(input())
    if c==1:
        s=s-25
        q=g-g//2
        w=g+g//2
        if q<a:
            q=a
        if w>b:
            w=b
        
        print("number lies between ",q," and ",w)
        d=int(input())
        if d==g:
            print("correct")
            print("score ",s)
    
        else:
            print("wrong")
            print("1. for another hint")
            print("2. for give up")
            p=list(str(g))
            add=0
            prod=1
            for i in range(len(p)):
                add=add+int(p[i])
                prod=prod*int(p[i])
                
            c=int(input())
            if c==1:
                s=s-25
                print("addition of digits ",add)
                d=int(input())
                if d==g:
                    print("correct")
                    print("Score ",s)
                else:
                    print("wrong")
                    print("1. for another hint")
                    print("2. for give up")    
                    c=int(input())
                    if c==1:
                        s=s-25
                        print("product of digits ",prod)        

                        d=int(input())
                        if d==g:
                            print("correct")
                            print("Score ",s)
                        else:
                            print("wrong")
                            print(g)
                            print("better luck next time")