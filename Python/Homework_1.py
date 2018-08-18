
# coding: utf-8

# In[1]:


import datetime                             #truy cập Module datetime
now = datetime.datetime.now()               #khởi tạo biến now
                                            #datetime.datetime cho giá trị ngày và giờ các thuộc tính: năm ,tháng ,ngày,giờ,phút,giây,..
                                            #.now() trả về ngày giờ địa phương hiện tại
print ("Current date and time : ")
print (now.strftime("%Y-%m-%d %H:%M:%S"))   #strtime: chuyển đổi tuple thành chuỗi xđ bởi tham số : 
                                                     # %Y: Năm bao gồm cả thế kỷ
                                                     # %m: Tháng (01 tới 12)
                                                     # %d: Ngày trong tháng (01 đến 31)
                                                     # %H: Giờ (00 đến 23)
                                                     # %M: Phút
                                                     # %S: Giây                  


# Chương trình trên trả về thời gian hiện tại.

# In[2]:


def sum(x, y):                  #hàm tính toán
    sum = x + y                 #cộng hai số
    if sum in range(15, 20):    # nếu sum nằm trong khoảng từ 15 đến 20 thì in ra 20
        return 20
    else:
        return sum              #nếu không nằm trong khaongr 15 đến 20 thì in ra sum

print(sum(10, 6))               # sum=16 nằm trong khoảng [15,20] nên kết quả là 20
print(sum(10, 2))               # sum=12 không nằm trong khoảng [15,20] nên kết quả là 12    
print(sum(10, 12))


# Chương trình tính tổng của 2 số, nếu tổng của hai số không nằm trong khoảng [15,20] thì in ra tổng của 2 số nếu không in ra 20.
