import numpy as np

# 最適化するデータ
sc = np.array([
    [1,2,14],
    [1,3,20],
    [1,4,7],
    [2,3,14],
    [2,4,3],
    [3,5,3],
    [4,5,5],
    [4,6,14],
    [5,6,1],
    [5,7,5],
    [6,7,2],
    [7,8,2]
])

# 表作成
def table():
    data = np.zeros((sc[-1,1]+1 , sc[-1,1]+1))

    for i in range(len(sc)):
        for j in range(len(sc)):
            for k in range(len(sc)):
                if sc[i,0]==j and sc[i,1]==k:
                    data[j,k] = sc[i,2]
    return data

# 最早値計算
def ear(data):
    a1 = data
    b1 = np.zeros(sc[-1,1]+1)
    M = 0

    for i in range(len(data)):
        for j in range(len(data)):

            if a1[j,i] > M:
                M = a1[j,i]
            b1[i] = M

            if  a1[i,j] != 0:
                a1[i,j] = data[i,j] + b1[i]

        M = 0

    return a1 , b1


# 最遅値計算
def late(data):
    a2 = data
    b2 = np.zeros(sc[-1,1]+1)
    b2[-1] = b1[-1]
    M = b1[-1]

    for i in range(len(data)):
        for j in range(len(data)):

            if a2[-j,-i] != 0:
                a2[-j,-i] = b2[-i] - data[-j,-i]

            if  a2[-i,-j] < M and a2[-i,-j] != 0:
                M = a2[-i,-j]
                b2[-i] = M

        M = b2[-1]
    
    for i in range(len(b2)):
        if  np.sum(a2[0:len(b2) , i:i+1]) == 0 and i-1 > 0:
            b2[i-1] = 0
    
    return a2 , b2


# 演算処理
data1 = table()
data2 = table()

a1 , b1 = ear(data1)
a2 , b2 = late(data2)


# クリティカルパス算出
cp = b1 - b2

for i in range(len(cp)):
    if cp[i] == 0 :
        if i != 0:
            print(i)