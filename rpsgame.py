import random
t=['Rock','Paper','Sicssor']
c=random.choice(t)
upoint=0
cpoint=0
u=input("Rock,Paper,Sicssor :" )
if u=="Rock" or u=="Paper" or u=="Sicssor":
    if c==u:
        print("tie")
        print(c,u)
        print("Score")
        print("computer :",cpoint,"User :",upoint)
    elif c=="Rock":
        if u=="Paper":
            upoint=upoint+1
            print("you won")
            print(c,u)
            print("Score")
            print("computer :",cpoint,"User :",upoint)
        elif u=="Sicssor":
            cpoint=cpoint+1
            print("you lost")
            print(c,u)
            print("Score")
            print("computer :",cpoint,"User :",upoint)
    elif c=="Paper":
        if u=="Rock":
            cpoint=cpoint+1
            print("you lost")
            print(c,u)
            print("Score")
            print("computer :",cpoint,"User :",upoint)
        elif u=="Sicssor":
            upoint=upoint+1
            print("you win")
            print(c,u)
            print("Score")
            print("computer :",cpoint,"User :",upoint)
    elif c=="Sicssor":
        if u=="Rock":
            upoint=upoint+1
            print("you won")
            print(c,u)
            print("Score")
            print("computer :",cpoint,"User :",upoint)
        elif u=="Paper":
            cpoint=cpoint+1
            print("you lost")
            print(c,u)
            print("score")
            print("computer :",cpoint,"User :",upoint)
else:
    print("check your input it should be Rock or Paper or Sicssor ")