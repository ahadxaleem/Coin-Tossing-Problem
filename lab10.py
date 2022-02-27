import random


def createchrome():

    temp = []
    for i in range(10):
        temp.append(random.randint(0, 1))
    return temp


def calfitness(a):
    tempfit = 0
    for i in range(10):
        if a[i] == 1:
            tempfit += 1
    return tempfit


def selection(a):
    ratio = []
    rolw = []
    select = []
    total = 0
    for i in range(6):
        total += a[i].fitness
    for i in range(6):
        ratio.append((a[i].fitness/total)*100)
    rolw.append(ratio[0])
    for i in range(1, 6):
        rolw.append(rolw[i-1]+ratio[i])
    for i in range(6):
        assig = 0
        temp = random.randrange(0, 99)
        while 1:
            if temp > rolw[assig]:
                assig += 1
            else:
                select.append(assig)
                break
    return select


def crossOver(list, a):
    for i in range(0, 6, 2):
        b = []
        c=[]
        temp = random.randrange(2, 8)
        for j in range(temp):
            b.append(list[a[i]].chrome[j])
            c.append(list[a[i+1]].chrome[j])
        for j in range(temp,10):
            b.append(list[a[i+1]].chrome[j])
            c.append(list[a[i]].chrome[j])
        list[i].chrome=b
        list[i+1].chrome=c


def mutate(list, a):
    for i in range(6):
        temp = random.randrange(0, 11)
        if temp>9:
            continue
        else:
            if list[a[i]].chrome[temp]==1:
                list[a[i]].chrome[temp]=0
            else:
                list[a[i]].chrome[temp]=1



class chromosome:
    def __init__(self) -> None:
        self.chrome = createchrome()
        self.fitness = calfitness(self.chrome)


list = []
totalfit=0
generation=1
for i in range(6):
    list.append(chromosome())
for i in range(6):
    totalfit+=list[i].fitness
print("Generation#"+str(generation))
for i in range(6):
    print("Chromosome "+str(i+1)+" "+str(list[i].chrome)+" Fitness = "+str(list[i].fitness))
generation+=1
print("Total Fitness = "+str(totalfit))
while totalfit<59:
    a=selection(list)
    crossOver(list, a)
    mutate(list,a)
    for i in range(6):
        list[i].fitness=calfitness(list[i].chrome)
    totalfit=0
    for i in range(6):
        totalfit+=list[i].fitness
    print("\nGeneration#"+str(generation))
    for i in range(6):
        print("Chromosome "+str(i+1)+" "+str(list[i].chrome)+" Fitness = "+str(list[i].fitness))
    generation+=1
    print("Total Fitness = "+str(totalfit))
