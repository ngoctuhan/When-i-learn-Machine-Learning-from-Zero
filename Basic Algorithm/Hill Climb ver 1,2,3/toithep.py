import random

#n = random.randint(1,1000)
n = int(input("Kich thuoc ban co : "))
a = [10000,7,1,2,3,4,5,6,8]

def countQueenThreatened():

    count  = 0
    #kiem tra cac hàng 
    for i in range(1,n+1):
        t = a.count(i)
        t = t - 1
        t = t * (t+1) // 2 # sô uy hiep trên mỗi hàng
        if(t > 0):
        # xem hang i co bao nhieu con
            count = count + t
    #kiem tra trên đường chéo chính

    for i in range(1,n+1):
        a[i] = i - a[i] + n 
    for i in range(0, 2*n -1):
        t = a.count(i)
        t = t - 1
        t = (t * (t+1) )// 2 # sô uy hiep trên mỗi hàng
        if(t > 0):
        # xem hang i co bao nhieu con
            count = count + t
    for i in range(1,n+1):
        a[i] = - a[i] + n + i
    print (a)
    #kiểm tra trên đường chéo phụ
    for i in range(1,n+1):
        a[i] = i +  a[i] -  1
    for i in range (1, 2 * n):
        t = a.count(i)
        t = t - 1
        t = t * (t+1) // 2 # sô uy hiep trên mỗi hàng
        if(t > 0):
        # xem hang i co bao nhieu con
            count = count + t
    for i in range(1,n+1):
        a[i] =  - i + a[i] +  1
    return count

def swap(i,j):
    t = a[i]
    a[i] = a[j]
    a[j] = t

conflicts = countQueenThreatened()

def find_state_next():
    cur_conflicts = countQueenThreatened()
    print ("So uy hiep hien tai :", cur_conflicts)
    if cur_conflicts == 0:
        return False
    for i in range(0,n):
        i = random.randint(1, n)
        j = random.randint(1, n)    
        print (i, j)
        swap (i,j)
        print ("SAU HOAN DOI : ", a)
        temp_conflicts = float(countQueenThreatened()/cur_conflicts) 
        if (temp_conflicts < 1.25):
            cur_conflicts = temp_conflicts
            return True
        swap(i, j)
    return False

print ("Trang thai ban dau cac quan hau : ")
print(a)

while(True):

    if(conflicts == 0): 
        break
    if find_state_next() == False:
        break

print ("Trang thai tim dc la : ")
print (a)





    



