laptop = 0
phone = 0
tablet = 0

while True:

    print("MENU QUẢN LÝ KHO")
    print("1. Xem báo cáo tồn kho")
    print("2. Nhập kho")
    print("3. Xuất kho")
    print("4. Cảnh báo hàng tồn kho thấp")
    print("5. Thoát chương trình")

    
    choice = input("Nhập lựa chọn (1-5): ").strip()

    if choice == "1":
        print(" BÁO CÁO TỒN KHO")
        print(f"Laptop:             {laptop}")
        print(f"Điện thoại:         {phone}")
        print(f"Máy tính bảng:       {tablet}")
        
        print("\n BIỂU ĐỒ TỒN KHO ")
        
        print("Laptop ", laptop, ":", end="")
        for i in range(laptop):
            print("*", end="")
        print()
        
        print("Điện thoại ", phone, ":", end="")
        for i in range(phone):
            print("*", end="")
        print()
        
        print("Máy tính bảng", tablet, ":", end="")
        for i in range(tablet):
            print("*", end="")
        print()

    elif choice == "2":
        print("\nNHẬP KHO")
        print("1. Laptop")
        print("2. Điện thoại")
        print("3. Máy tính bảng")
        
        item_choice = input("Chọn mặt hàng (1-3): ").strip()
        
        while True:
                quantity = int(input("Nhập số lượng: "))
                if quantity < 0:
                    print(" Số lượng không hợp lệ, vui lòng nhập lại!")
                    continue
                break


        if item_choice == "1":
            laptop += quantity
            print(f" Đã nhập {quantity} Laptop vào kho.")
        elif item_choice == "2":
            phone += quantity
            print(f" Đã nhập {quantity} Điện thoại vào kho.")
        elif item_choice == "3":
            tablet += quantity
            print(f" Đã nhập {quantity} Máy tính bảng vào kho.")
        else:
            print(" Mặt hàng không hợp lệ!")

    elif choice == "3":
        print("\n XUẤT KHO ")
        print("1. Laptop")
        print("2. Điện thoại")
        print("3. Máy tính bảng")
        
        item_choice = input("Chọn mặt hàng (1-3): ").strip()
        
        while True:
                quantity = int(input("Nhập số lượng: "))
                if quantity < 0:
                    print(" Số lượng không hợp lệ, vui lòng nhập lại!")
                    continue
                break

        if item_choice == "1":
            if quantity > laptop:
                print(" Không đủ hàng! Hiện chỉ còn", laptop, "Laptop.")
            else:
                laptop -= quantity
                print(f" Đã xuất {quantity} Laptop.")

        elif item_choice == "2":
            if quantity > phone:
                print(" Không đủ hàng! Hiện chỉ còn", phone, "Điện thoại.")
            else:
                phone -= quantity
                print(f" Đã xuất {quantity} Điện thoại.")

        elif item_choice == "3":
            if quantity > tablet:
                print(" Không đủ hàng! Hiện chỉ còn", tablet, "Máy tính bảng.")
            else:
                tablet -= quantity
                print(f" Đã xuất {quantity} Máy tính bảng.")
        else:
            print("Mặt hàng không hợp lệ!")

    elif choice == "4":

        print("CẢNH BÁO TỒN KHO THẤP")
        
        warning = False
        
        if laptop < 10:
            print(f" laptop sắp hết (Chỉ còn {laptop} sản phẩm)")
            warning = True
        if phone < 10:
            print(f" điện thoại sắp hết (Chỉ còn {phone} sản phẩm)")
            warning = True
        if tablet < 10:
            print(f" máy tính bảng sắp hết (Chỉ còn {tablet} sản phẩm)")
            warning = True
            
    elif choice == "5":
        print("\n thoát chương trình")
        break

    else:
        print(" Lựa chọn không hợp lệ vui lòng nhập lại .")
