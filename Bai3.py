# Khởi tạo danh sách sản phẩm ban đầu của hệ thống cửa hàng Yody
product_list = [
    {
        "product_id": "SP001",
        "product_name": "Áo polo nam",
        "price": 299000,
        "quantity": 20
    },
    {
        "product_id": "SP002",
        "product_name": "Quần kaki nam",
        "price": 399000,
        "quantity": 15
    },
    {
        "product_id": "SP003",
        "product_name": "Váy công sở nữ",
        "price": 459000,
        "quantity": 10
    }
]


def display_menu():
    """Hiển thị menu điều khiển hệ thống quản lý sản phẩm"""
    print("\n===== HỆ THỐNG QUẢN LÝ SẢN PHẨM YODY =====")
    print("1. Hiển thị danh sách sản phẩm")
    print("2. Thêm sản phẩm mới")
    print("3. Cập nhật thông tin sản phẩm")
    print("4. Xóa sản phẩm theo mã")
    print("5. Thoát chương trình")
    print("=" * 42)


# Vòng lặp điều khiển chính của chương trình
while True:
    display_menu()
    choice_input = input("Vui lòng nhập lựa chọn (1-5): ").strip()

    # Bẫy 5 — Người dùng nhập sai lựa chọn menu (Nhập chữ, ký tự đặc biệt, số thực)
    try:
        choice = int(choice_input)
    except ValueError:
        print('Lựa chọn không hợp lệ, vui lòng nhập lại!')
        continue

    if choice < 1 or choice > 5:
        print('Lựa chọn không hợp lệ, vui lòng nhập lại!')
        continue

    # Xử lý các chức năng nghiệp vụ tương ứng
    if choice == 1:
        print("\n--- 1. DANH SÁCH SẢN PHẨM HIỆN TẠI ---")
        if len(product_list) == 0:
            print("Danh sách sản phẩm hiện đang trống.")
        else:
            print("Danh sách sản phẩm hiện tại:")
            for index, product in enumerate(product_list, start=1):
                print(
                    f"{index}. Mã SP: {product['product_id']} | "
                    f"Tên: {product['product_name']} | "
                    f"Giá: {product['price']} | "
                    f"Số lượng: {product['quantity']}"
                )

    elif choice == 2:
        print("\n--- 2. THÊM SẢN PHẨM MỚI ---")
        raw_id = input("- Nhập mã sản phẩm: ")
        product_name = input("- Nhập tên sản phẩm: ").strip()
        raw_price = input("- Nhập giá sản phẩm: ").strip()
        raw_quantity = input("- Nhập số lượng sản phẩm: ").strip()

        # Bẫy 1 — Khử khoảng trắng và chuyển chữ thường thành chữ hoa đối với mã sản phẩm
        clean_id = raw_id.strip().upper()

        # Bẫy 2 — Kiểm tra trùng lặp mã sản phẩm trong bộ cơ sở dữ liệu hiện hành
        is_duplicate = False
        for product in product_list:
            if product["product_id"] == clean_id:
                is_duplicate = True
                break

        if is_duplicate:
            print("[LỖI] Mã sản phẩm bị trùng")
            continue

        # Bẫy 4 — Xác thực giá bán và số lượng nhập vào phải là số nguyên dương (> 0)
        try:
            price = int(raw_price)
            quantity = int(raw_quantity)
            if price <= 0 or quantity <= 0:
                print("[LỖI] Giá/Số lượng không hợp lệ")
                continue
        except ValueError:
            print("[LỖI] Giá/Số lượng không hợp lệ")
            continue

        # Sau khi mọi dữ liệu vượt qua vòng kiểm tra hợp lệ, tiến hành thêm sản phẩm
        new_product = {
            "product_id": clean_id,
            "product_name": product_name,
            "price": price,
            "quantity": quantity
        }
        product_list.append(new_product)
        print("Thêm sản phẩm thành công")

    elif choice == 3:
        print("\n--- 3. CẬP NHẬT THÔNG TIN SẢN PHẨM ---")
        raw_id = input("Nhập mã sản phẩm cần cập nhật: ")
        
        # Bẫy 1 — Chuẩn hóa mã sản phẩm
        clean_id = raw_id.strip().upper()

        # Bẫy 3 — Tìm kiếm xem mã sản phẩm có tồn tại hay không
        found_product = None
        for product in product_list:
            if product["product_id"] == clean_id:
                found_product = product
                break

        if found_product is None:
            print("Không tìm thấy mã sản phẩm cần cập nhật!")
            continue

        # Nếu tìm thấy sản phẩm, tiến hành lấy thông tin cập nhật mới
        print(f"-> Đang sửa sản phẩm: {found_product['product_name']} ({found_product['product_id']})")
        new_name = input("Nhập tên sản phẩm mới: ").strip()
        raw_price = input("Nhập giá sản phẩm mới: ").strip()
        raw_quantity = input("Nhập số lượng tồn kho mới: ").strip()

        # Bẫy 4 — Kiểm định tính hợp lý của giá và số lượng cập nhật mới
        try:
            price = int(raw_price)
            quantity = int(raw_quantity)
            if price <= 0 or quantity <= 0:
                print("[LỖI] Giá/Số lượng không hợp lệ")
                continue
        except ValueError:
            print("[LỖI] Giá/Số lượng không hợp lệ")
            continue

        # Ghi đè cập nhật dữ liệu mới vào từ điển của sản phẩm được chọn
        found_product["product_name"] = new_name
        found_product["price"] = price
        found_product["quantity"] = quantity
        print("[THÀNH CÔNG] Đã cập nhật thông tin sản phẩm!")

    elif choice == 4:
        print("\n--- 4. XÓA SẢN PHẨM THEO MÃ ---")
        raw_id = input("Nhập mã sản phẩm cần xóa: ")
        
        # Bẫy 1 — Chuẩn hóa mã sản phẩm
        clean_id = raw_id.strip().upper()

        # Bẫy 3 — Kiểm tra sự tồn tại của sản phẩm trước khi tiến hành xóa
        remove_index = -1
        for index, product in enumerate(product_list):
            if product["product_id"] == clean_id:
                remove_index = index
                break

        if remove_index == -1:
            print("Không tìm thấy mã sản phẩm cần xoá!")
        else:
            # Rút trích và xóa Dictionary của sản phẩm khỏi List bằng phương thức .pop()
            deleted_product = product_list.pop(remove_index)
            print(f"[THÀNH CÔNG] Đã xóa sản phẩm: {deleted_product['product_name']} ({deleted_product['product_id']})")

    elif choice == 5:
        print("\nThoát chương trình.")
        break