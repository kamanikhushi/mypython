import random # GAME OF stone,paper and scissor
myhand1=["1","2","3"] # myhand2=["stone","paper","scissor"]
for i in range(0,20):
    computer=random.choice(myhand1)
    player=input("\n0.quit\n1.stone\n2.paper\n3.scissor\nenter your choice:")

    if(player=="0"):
        print("you are exit")
        break
    elif(player!="1" and player!="2" and player!="3"):
        raise ValueError("invaild input")
    else:
        print("computer choose : stone") if (computer=="1") else print("computer choose : paper") if (computer=="2") else print("computer choose : scissor")
        print("you choose : stone") if (player=="1") else print("you choose : paper") if (player=="2") else print("you choose : scissor")
        mych2=player+computer
        '''myhand=[
            ["11D","21W","31L"],
            ["12L","22D","32W"],
            ["13W","23L","33D"],
        ]'''
        if(mych2=="11" or mych2=="22" or mych2=="33"):
            print("\nDROW")
        elif(mych2=="21" or mych2=="32" or mych2=="13"):
            print("\nYOU ARE WIN!")
        else:
            print("\nYOU ARE LOSE!")

