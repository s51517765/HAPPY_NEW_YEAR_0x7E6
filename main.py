import random
import string
import os
N = 300  # 世代あたりの個体数
Generation = 0  # 世代数
MUTATION_RATE = 0.05  # 突然変異率
TARGET = "HAPPY NEW YEAR 0x7E6"
LENGTH = len(TARGET)  # 遺伝子長
pool = []  # 現世代個体
ALFABETO = list(string.ascii_letters+string.digits+"x"+" ")  # 使える文字をリストで


def mutate(str):  # 突然変異、文字ごとに変異させる
    tmp = ""
    for i in str:
        if random.random() < MUTATION_RATE:
            tmp += random.choice(ALFABETO)
        else:
            tmp += i
    return tmp


def getFitness(pool):  # 適応度
    value = 0
    for i in range(LENGTH):
        if pool[i] == TARGET[i]:
            value += 1
    #print("value", value)
    return value


def init():   # 初期個体を生成
    global pool
    for i in range(N):
        tmp = ""
        for j in range(LENGTH):
            tmp += str(random.choice(ALFABETO))
        pool.append(tmp)
    # print(pool)
    return 0


def selection():  # 優良個体を選択
    value = []
    for i in range(N):
        value.append(getFitness(pool[i]))
    return value.index(max(value))


init()

while(True):
    Generation += 1
    idx = selection()
    for i in range(N):
        pool[i] = mutate(pool[idx])
    if Generation % 5 == 0 or getFitness(pool[0]) == LENGTH:
        os.system('cls')
        print("Iteration", Generation, pool[0])
    if getFitness(pool[0]) == LENGTH:
        break

'''
ランダムで初期個体を生成
トーナメント選択
#個体同士で交配
交配されたものから突然変異
→ 新世代
'''
