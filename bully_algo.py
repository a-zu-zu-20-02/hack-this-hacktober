#initalizing the leader variable
leader = 1
#taking the number of input processes and their status, while choosing the leader which is the highest active input process
numberProcess = int(input("Enter the number of processes : "))
numberProcessList = list()
for i in range(1,numberProcess+1):
    numberProcessList.append(i)
statuslist = list()
for i in range(numberProcess):
    #A process can either be active-> 1 or inactive-> 0
    n = int(input(f"Enter the status of the process {numberProcessList[i]} - active/inactive(1/0) : "))
    statuslist.append(n)
    if(statuslist[i]):
        leader = i+1
#display function for all the processes and their status, and the leader of the election
def display(leader):
    print("\n")
    print("\n")
    print("Processes : \n")
    for i in numberProcessList:
        print(f'{i}',end="\t")
    print('\n')
    print("Alive  : \n")
    for i in statuslist:
        print(f'{i}',end="\t")
    print("\n")
    print(f"The leader is : {leader}\n")

#bully algorithm function
def bully(leader):
    print("Enter")
    print("1.Crash\n2.Activate\n3.Display\n4.Exit\n")
    bully = int(input())
    #Using a loop untill the user input the correct options out of 1, 2, 3, 4
    while(True):
        if bully == 1:
            crashID = int(input(f"Enter a process to crash : (1 to {numberProcessList[-1]}) : "))
            if(statuslist[crashID-1]):
                statuslist[crashID-1] = 0
                print(f"Process {crashID} is crashed.\n")
            elif(statuslist[crashID-1] ==0):
                print(f"Process {crashID} is already dead.\n")
            elecGenerator = int(input("Enter the process to generate the election leader : "))
            while(leader == elecGenerator):
                print("Enter a valid leader.")
                elecGenerator = int(input("Enter the process to generate the election leader : "))
            print('\n')
            if(leader == crashID):
                for i in range(elecGenerator+1,len(statuslist)):
                    print(f"Message is sent from {elecGenerator} to {numberProcessList[i-1]}")
                    if(statuslist[i-1]):
                        print(f"Response is sent from {numberProcessList[i-1]} to {elecGenerator}")
                        leader = numberProcessList[i-1]
                print('\n')
                print(f"The new leader is : {leader}\n")
            display(leader)
            break
        elif bully==2:
            activateID = int(input(f"Enter a process to activate : (1 to {numberProcessList[-1]}) : "))
            if(statuslist[activateID-1]==0):
                statuslist[activateID-1]=1
                leader = activateID
            elif(statuslist[activateID-1]):
                print("The process is already alive. ")
            for i in range(activateID+1,len(statuslist)):
                print(f"Message is sent from {activateID} to {numberProcessList[i-1]}")
                if(statuslist[numberProcessList[i-1]]):
                    print(f"Response is sent from {numberProcessList[i-1]} to {activateID}")
                    leader = numberProcessList[i-1]
            print('\n')
            print(f'The new leader is : {leader}\n')
            display(leader)
            break
        elif bully ==3:
            display(leader)
            break
        elif bully ==4:
            exit()
        else:
            print("Enter correct input : ")
            print("1.Crash\n2.Activate\n3.Display\n4.Exit\n")
            bully = int(input())

print('\n')
print("Enter : ")
print("1.Bully Algorithm\n2.Display\n3.Exit\n")
decision = int(input())
while(True):
    if decision ==1:
        bully(leader)
        break
    elif decision == 2:
        display(leader)
        break
    elif decision ==3:
        exit()
    else:
        print("Enter correct input : ")
        print("1.Bully Algorithm\n2.Display\n3.Exit\n")
        decision = int(input())