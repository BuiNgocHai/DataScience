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
