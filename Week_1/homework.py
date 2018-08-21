def sum(x, y):                  #hàm tính toán
    sum = x + y                 #cộng hai số
    if sum in range(15, 20):    # nếu sum nằm trong khoảng từ 15 đến 20 thì in ra 20
        return 20
    else:
        return sum              #nếu không nằm trong khaongr 15 đến 20 thì in ra sum

print(sum(10, 6))               # sum=16 nằm trong khoảng [15,20] nên kết quả là 20
print(sum(10, 2))               # sum=12 không nằm trong khoảng [15,20] nên kết quả là 12    
print(sum(10, 12))
