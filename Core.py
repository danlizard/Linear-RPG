def Luck(ans,stg):
    x=0
    y=0
    if ans==2 or ans==3 or ans==4:
        x=randint(1,len(Traps[stg])-1)
        if Traps[stg][x][2]=='s':
            print("You see",*Traps[stg][x][0].split('_'),"!")
        else:
            print("It's a corridor, but it is strange.")
    elif ans==5 or ans==6 or ans==7 or ans==8 or ans==9:
        x=randint(1,len(Enemies[stg])-1)
        print("You encountered",*Enemies[stg][x][0].split('_'),"!")
    elif ans==10 or ans==11:
        x=randint(1,10)
        y=randint(1,2)*10
        print("You found an ancient idol!")
    elif ans==12:
        x=randint(1,len(Spells)-1)
        print("You found a magical book of ",Spells[x][0],"!",sep='')
    else:
        print("You see a simple corridor.")
    return x,y
def Staging():
    Lister=[]
    LSt=open('Base.txt','r')
    deca=LSt.readlines()
    for i in range(1,len(deca)):
        Lister.append(deca[i].split())
    return Lister
def Rivals(Stages):
    Lister=[[] for i in range(len(Stages))]
    ListEn=open("Enemies.txt",'r')
    deca=ListEn.readlines()
    for i in range(0,len(deca)):
        x=deca[i].split()
        Lister[int(x[4])-1].append(x)
    return Lister
def Looting(Stages):
    Treasure=[[] for i in range(len(Stages))]
    ListTr=open('Treasures.txt','r')
    deca=ListTr.readlines()
    for i in range(0,len(deca)):
        x=deca[i].split()
        Treasure[int(x[4])-1].append(x)
    return Treasure
def Failing(Stages):
    Trappy=[[] for i in range(len(Stages))]
    LT=open('Traps.txt','r')
    deca=LT.readlines()
    for i in range(0,len(deca)):
        x=deca[i].split()
        Trappy[int(x[4])-1].append(x)
    return Trappy
def Casting():
    Spelling=[]
    SC=open('Spells.txt','r')
    deca=SC.readlines()
    for i in range(0,len(deca)):
        x=deca[i].split()
        Spelling.append(x)
    return Spelling
from random import *
Stages=Staging()
Enemies=Rivals(Stages)
Goods=Looting(Stages)
Traps=Failing(Stages)
Spells=Casting()
print("Made by Dan_ku")
print("Version for now - Alpha 3.0, Stage Update!")
print("Ready?")
cssc=input()
Character=dict()
Character['Hp']=randint(20,30)
Character['Dead']=False
Character['Fight']=False
Character['Mp']=20
Character['Spells']=[0]*len(Spells)
Character['Weapon']='a_Shiv'
Character['Armor']='a_Coat'
Character['Arstat']=[0,2]
Character['Westat']=[2,0]
Character['Alt']=[1,0]
Character['HpReg']=0
Character['MpReg']=0
print("Do you want to be a Warrior or a Mage?")
cls=input()
if cls=="Warrior":
    Character['Hp']+=10
    Character['Dmg']=Character['Arstat'][0]+Character['Westat'][0]
    Character['Block']=Character['Arstat'][1]+Character['Westat'][1]
    for i in range(0,len(Spells)):
        if int(Spells[i][3])==1:
            Character['Spells'][i]=1
    Character['HpReg']=0.20
elif cls=="Mage":
    Character['Mp']+=10
    Character['Spells']=[1]*len(Spells)
    Character['Dmg']=Character['Arstat'][0]+Character['Westat'][0]
    Character['Block']=Character['Arstat'][1]+Character['Westat'][1]
    Character['MpReg']=0.10
situation=1
print("Your journey begins! You wandered throughout the land searching, and finally - you're standing before an ancient gateway! Go deeper than ever and see what lies beneath!")
print("By the way, you have",Character['Hp'],"health points")
print('*Commands must be written in English, all low-case*')
while not Character['Dead']:
    if Character['Alt'][0]>len(Stages):
        print("You have defeated all of the ancient beings - you won!")
        Character['Dead']=True
        Character['Alt'][1]=3
    if Character['Alt'][1]==0:
        print("You're now wandering in the",*Stages[Character['Alt'][0]-1][0].split('_'),"while trying to find a boss or a path down.")
        Character['Alt'][1]=1
    if Character['Alt'][1]==1:
        if Character['Dmg']+Character['Block']>=int(Stages[Character['Alt'][0]-1][1]) and Character['Alt'][1]==1:
            Character['Alt'][1]=2    
            print("You can hear strange sounds from the next segment of the corridor. You move forward.")
            print("You have encountered the",*Stages[Character['Alt'][0]-1][2].split('_'),"!")
            mhp=int(Stages[Character['Alt'][0]-1][3])
            mdmg=int(Stages[Character['Alt'][0]-1][4])-int(Character['Block'])
            if mdmg<0:
                mdmg=0
            mdin=int(Character['Dmg'])-int(Stages[Character['Alt'][0]-1][5])
            if mdin<0:
                mdin=0
            Character['Fight']=True
            situation=5
            moment=int(Stages[Character['Alt'][0]-1][6])            
    com=input()
    if com=='move':
        if situation==1 or situation==10:
            print("You went forward.")
            if not Character['Fight']:
                situation=randint(1,12)
                moment,useless=Luck(situation,Character['Alt'][0]-1)
                if situation==5 or situation==6 or situation==7 or situation==8 or situation==9:
                    mhp=int(Enemies[Character['Alt'][0]-1][moment][1])
                    mdmg=int(Enemies[Character['Alt'][0]-1][moment][2])-int(Character['Block'])
                    if mdmg<0:
                        mdmg=0
                    mdin=int(Character['Dmg'])-int(Enemies[Character['Alt'][0]-1][moment][3])
                    if mdin<0:
                        mdin=0
                    Character['Fight']=True                   
        elif situation==2 or situation==3 or situation==4:
            print("A trap damaged you for ",Traps[Character['Alt'][0]-1][moment][1]," health points!",sep='')
            Character['Hp']-=int(Traps[Character['Alt'][0]-1][moment][1])
            situation=1
        elif situation==5 or situation==6 or situation==7 or situation==8 or situation==9 and Character['Fight']:
            print("Your enemy stopped you.")
    elif com=='hit':
        if situation==1 or situation==10:
            print("You hit the air.")
        elif situation==2 or situation==3 or situation==4:
            if com==Traps[Character['Alt'][0]-1][moment][3]:
                print("You escaped the trap!")
                situation=1
            else:
                print("A trap damaged you for ",Traps[Character['Alt'][0]-1][moment][1]," health points!",sep='')
                Character['Hp']-=int(Traps[Character['Alt'][0]-1][moment][1])
                situation=1
        elif situation==5 or situation==6 or situation==7 or situation==8 or situation==9:
            mhp-=mdin
            if mhp>0:
                if Character['Alt'][1]==2:
                    print("The ",*Stages[Character['Alt'][0]-1][2].split('_')," is now on ",mhp," health points.")
                else:
                    print("Your enemy,",*Enemies[Character['Alt'][0]-1][moment][0].split('_'),", is now on ",mhp," health points.")
            else:
                if Character['Alt'][1]==2:
                    print("Congratiulations! You have defeated the",*Stages[Character['Alt'][0]-1][2].split('_'),"!")
                    Character['Alt'][1]=0
                    Character['Alt'][0]+=1                    
                    situation=1
                    Character['Fight']=False
                else:
                    print("You killed",*Enemies[Character['Alt'][0]-1][moment][0].split('_'))
                    Character['Fight']=False
                    loot=randint(0,len(Goods[Character['Alt'][0]-1])-1)
                    print("You found",*Goods[Character['Alt'][0]-1][loot][0].split('_')," with stats ",Goods[Character['Alt'][0]-1][loot][1],"/",Goods[Character['Alt'][0]-1][loot][2],"!")
                    print("Want to equip?")
                    if input()=='yes':
                        if Goods[Character['Alt'][0]-1][loot][3]=='w':
                            Character['Weapon']=Goods[Character['Alt'][0]-1][loot][0]
                            Character['Westat']=[int(Goods[Character['Alt'][0]-1][loot][1]),int(Goods[Character['Alt'][0]-1][loot][2])]
                        elif Goods[Character['Alt'][0]-1][loot][3]=='a':
                            Character['Armor']=Goods[Character['Alt'][0]-1][loot][0]
                            Character['Arstat']=[int(Goods[Character['Alt'][0]-1][loot][1]),int(Goods[Character['Alt'][0]-1][loot][2])]                        
                    Character['Dmg']=Character['Arstat'][0]+Character['Westat'][0]
                    Character['Block']=Character['Arstat'][1]+Character['Westat'][1]
                    situation=1
    elif com=='take':
        if situation==10 or situation==11:
            print("You healed for",moment,"health points!")
            Character['Hp']+=moment
            print("You gathered",useless,"mana points!")
            Character['Mp']+=useless
            situation=1
        elif situation==12:
            if Character['Spells'][moment]==0:
                Character['Spells'][moment]=1
                print("You have learned the mighty spell of ",Spells[moment][0],"!",sep='')
                situation=1
            else:
                sac=randint(1,5)
                Character['Hp']+=sac
                print("You already know it, so you sacrifice it for",sac,"health points.")
                situation=1
        else:
            print("Nothing happened.")
    elif com=='2468':
        print("Overrunning session emerged.")
        while com!="play":
            com=input()
            if com=="situate":
                print(situation,moment)
            if com=="reroll":
                situation=randint(1,10)
                moment=Luck(situation)
            if com=="peace":
                Character["Fight"]=False
            if com=="cheat":
                Character['Dmg']=1000
    elif com=='cast':
        if Character['Fight']:
            print("You can cast ",end='')
            con=0
            Book=dict()
            for i in range(0,len(Spells)):
                if (Spells[i][2]=='dm' or Spells[i][2]=='ar' or Spells[i][2]=='in') and Character['Spells'][i]>0 and Character['Mp']>=int(Spells[i][4]):
                    print(Spells[i][0],', ',end='',sep='')
                    con+=1
                    Book[Spells[i][0]]=[Spells[i][1],Spells[i][4],Spells[i][2]]
            if con==0:
                print("nothing.")
            else:
                print("and that's all.")
                spl=input()
                try:
                    Character['Mp']-=int(Book[spl][1])
                    print("You casted ",spl,"!",sep='')
                    if Book[spl][2]=='dm':
                        mhp-=int(Book[spl][0])
                        if mhp>0:
                            if Character['Alt'][1]==2:
                                print("The ",*Stages[Character['Alt'][0]-1][2].split('_')," is now on ",mhp," health points.")
                            else:
                                print("Your enemy,",*Enemies[Character['Alt'][0]-1][moment][0].split('_')[1:],", is now on ",mhp," health points.")
                        else:
                            if Character['Alt'][1]==2:
                                print("Congratiulations! You have defeated the",*Stages[Character['Alt'][0]-1][2].split('_'),"!")
                                Character['Alt'][1]=0
                                Character['Alt'][0]+=1                    
                                situation=1
                                Character['Fight']=False
                            else:
                                print("You killed",*Enemies[Character['Alt'][0]-1][moment][0].split('_')[1:])
                                Character['Fight']=False
                                loot=randint(0,len(Goods[Character['Alt'][0]-1])-1)
                                print("You found",*Goods[Character['Alt'][0]-1][loot][0].split('_')," with stats ",Goods[Character['Alt'][0]-1][loot][1],"/",Goods[Character['Alt'][0]-1][loot][2],"!")
                                print("Want to equip?")
                                if input()=='yes':
                                    if Goods[Character['Alt'][0]-1][loot][3]=='w':
                                        Character['Weapon']=Goods[Character['Alt'][0]-1][loot][0]
                                        Character['Westat']=[int(Goods[Character['Alt'][0]-1][loot][1]),int(Goods[Character['Alt'][0]-1][loot][2])]
                                    elif Goods[Character['Alt'][0]-1][loot][3]=='a':
                                        Character['Armor']=Goods[Character['Alt'][0]-1][loot][0]
                                        Character['Arstat']=[int(Goods[Character['Alt'][0]-1][loot][1]),int(Goods[Character['Alt'][0]-1][loot][2])]                        
                                    Character['Dmg']=Character['Arstat'][0]+Character['Westat'][0]
                                    Character['Block']=Character['Arstat'][1]+Character['Westat'][1]
                                situation=1
                    elif Book[spl][2]=='ar':
                        mdin+=int(Book[spl][0])
                        if mdin>int(Character['Dmg']):
                            mdin=int(Character['Dmg'])
                        mar=int(Enemies[Character['Alt'][0]-1][moment][3])
                        mar-=int(Book[spl][0])
                        if mar<0:
                            mar=0
                        if Character['Alt'][1]==2:
                            print("The ",*Stages[Character['Alt'][0]-1][2].split('_')," is now on ",mhp," health points.")
                        else:
                            print("The ",Enemies[Character['Alt'][0]-1][moment][0]," is now on ",mhp," health points.",sep='')
                    elif Book[spl][2]=='in':
                        mdmg-=int(Book[spl][0])
                        if mdmg<0:
                            mdmg=0
                        if Character['Alt'][1]==2:
                            print("The ",*Stages[Character['Alt'][0]-1][2].split('_')," is now on ",mhp," health points.")
                        else:
                            print("The ",Enemies[Character['Alt'][0]-1][moment][0]," is now on ",mhp," health points.")
                except:
                    pass
        elif situation==2 or situation==3 or situation==4:
            print("You can cast ",end='')
            con=0
            Book=dict()
            for i in range(0,len(Spells)):
                if Spells[i][2]=='tr'and Character['Spells'][i]>0 and Character['Mp']>=int(Spells[i][4]):
                    print(Spells[i][0],', ',end='',sep='')
                    con+=1
                    Book[Spells[i][0]]=[Spells[i][1],i,Spells[i][4]]
            if con==0:
                print("nothing.")
            else:
                print("and that's all.")
                spl=input()
                try:
                    Character['Mp']-=int(Book[spl][2])
                    print("You casted ",spl,"!",sep='')                
                    tdm=int(Traps[Character['Alt'][0]-1][moment][1])
                    tdm-=int(Book[spl][0])
                    if tdm<0:
                        tdm=0
                    Character['Hp']-=tdm
                    print("A trap damaged you for ",tdm," health points!",sep='')
                    situation=1
                except:
                    pass
        else:
            print("You can cast ",end='')
            con=0
            Book=dict()
            for i in range(0,len(Spells)):
                if (Spells[i][2]=='hp' or Spells[i][2]=='bt') and Character['Spells'][i]>0 and Character['Mp']>=int(Spells[i][4]):
                    print(Spells[i][0],', ',end='',sep='')
                    con+=1
                    Book[Spells[i][0]]=[Spells[i][1],i,Spells[i][2],Spells[i][4]]
            if con==0:
                print("nothing.")
            else:
                print("and that's all.")
                spl=input()
                try:
                    Character['Mp']-=int(Book[spl][3])
                    print("You casted ",spl,"!",sep='')                
                    if Book[spl][2]=='hp':
                        Character['Hp']+=int(Book[spl][0])
                        print("You healed for",Book[spl][0],"health points!")
                    elif Book[spl][2]=='bt':
                        print("Do you want to enhance your weapon or your armor?")
                        uans=input()
                        if uans=='weapon':
                            Character['Westat'][0]+=int(Book[spl][0])
                            print("You imbued your weapon for",Book[spl][0],"points!")
                        elif uans=='armor':
                            Character['Arstat'][1]+=int(Book[spl][0])
                            print("You imbued your armor for",Book[spl][0],"points!")
                        Character['Dmg']=Character['Arstat'][0]+Character['Westat'][0]
                        Character['Block']=Character['Arstat'][1]+Character['Westat'][1]
                except:
                    pass
    elif com=='stats':
        print("You have",Character['Hp'],"health points,",Character['Mp'],"mana points,",Character['Dmg'],"attack points and",Character['Block'],"armor points.")
        print("You're equipped with",*Character['Weapon'].split('_'),"and wear",*Character['Armor'].split('_'))
    elif com=='help':
        print('To go forward, print "move". To attack an enemy, print "hit".')
        print('To use a spell, print "cast" and then the name of the spell from the list (with high-case).')
        print('To acknowledge your current stats, print "stats".')
        print('To escape a trap, print the command (one word, all low-case) that describes the best and only way to escape that trap.')
        print('To use an idol, print "take"')
    elif situation==2 or situation==3 or situation==4:
        if com==Traps[Character['Alt'][0]-1][moment][3]:
            print("You escaped the trap!")
            situation=1
        else:
            print("A trap damaged you for ",Traps[Character['Alt'][0]-1][moment][1]," health points!",sep='')
            Character['Hp']-=int(Traps[Character['Alt'][0]-1][moment][1])
            situation=1
    else:
        print("Nothing happened.")      
    if Character['Fight']:
        Character['Hp']-=mdmg
        if Character['Hp']>0:
            print("Your enemy damaged you for",mdmg,"health points!")
        else:
            print("You got killed by",*Enemies[Character['Alt'][0]-1][moment][0].split('_'))
            Character['Dead']=True
    else:
        Character['Hp']+=Character['HpReg']
    if Character['Hp']<=0:
        Character['Dead']=True
    else:
        Character['Mp']+=Character['MpReg']
if Character['Alt'][0]>len(Stages):
    print("|\*MAN OVER GAME*/|")
else:
    print("_<^GAME OVER MAN^>_")
print("Did you like it?")
x=input()