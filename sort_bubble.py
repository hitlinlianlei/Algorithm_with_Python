import numpy as np

x = np.random.randint(0,100,size=10)

def bubble_sort(x,sort_way='bigger2small'):
    for i in range(len(x)):
        for j in range(i):
            if sort_way == 'bigger2small':
                if x[i]>x[j]:
                    x[i],x[j]=x[j],x[i]
            elif sort_way == 'small2bigger':
                if x[i]<x[j]:
                    x[i], x[j] = x[j], x[i]
    return x
print('before sorted %s:'%x)
print('sorting...')
bubble_sort(x,sort_way='small2bigger')
print('after sorted %s:'%x)
