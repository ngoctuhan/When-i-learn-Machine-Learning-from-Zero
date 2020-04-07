import numpy as np
n = int(input("Kich thuoc ban co : "))
# Ban co co kich thuoc n *  n

a = [10000,7,1,2,3,4,5,6,8] # bang a dung luu trang thai
# Mỗi quân hậu được lưu sẵn trên các cột khi và di chuyển trên các hàng thôi

# B1 Khoi tao trang thai ban dau: 
#a.append(0)
#for i in range(1,n+1):
#    a.append(int(input("Nhap ptu :")))

#B2 Cac tham tac tim trạng thai 

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
        a[i] =  i + a[i] -  1
    return count

# print (countQueenThreatened())
def count_threatened(i):
    count  = 0
    #kiem tra cac hàng 
    t = a.count(a[i])
    t = t - 1
    t = t * (t+1) // 2 
    count =  count + t
    #kiem tra duong cheo chinh
    for j in range(1,n+1):
        a[j] = a[j] - j
    t = a.count(a[i])
    t = t - 1
    t = (t * (t+1) )// 2 
    count = count + t
    for j in range(1,n+1):
        a[j] = a[j] + j    
    # kiem tra tren duong cheo phu
    for j in range(1,n+1):
        a[j] = j +  a[j] 
    t = a.count(a[i])
    t = t - 1
    t = t * (t+1) // 2 
    count = count + t
    for j in range(1,n+1):
        a[j] = a[j] - j
    return count


def find_queen_threatened():
    MAX = -1
    index_queen = 0
    for i in range(1,n+1):
        count = count_threatened(i)
        if count > MAX:
            MAX = count
            index_queen = i
    return index_queen

stop = 0
while countQueenThreatened != 0:
    index = find_queen_threatened()
    values = count_threatened(index)
    stop = values
    print(index,values)
    # Tim ham chi phi tot nhat cho bước tiếp theo 
    MIN = values
    for i in range(1,n+1):
        a[index] = i
        t = count_threatened(index)
        if(t < MIN):
            MIN = t
            values = i
        else:
            a[index] = values
        print (a)
    if values == stop:
        break    
# Dua trang  thai tot nhat ma no co the tim dc
print (a)








   



