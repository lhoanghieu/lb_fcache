import orjson
import json
import os 
dir_path = os.path.dirname(os.path.realpath(__file__))
import timeit


print('dir_path: ', dir_path)

data = [{"f_p_code":1,"p_p_code":125,"name_en":"Ho Chi Minh","name_vi":"TP Hồ Chí Minh"},{"f_p_code":2,"p_p_code":93,"name_en":"Ha Noi","name_vi":"Thành phố Hà Nội"},{"f_p_code":3,"p_p_code":75,"name_en":"An Giang","name_vi":"Tỉnh An Giang"},{"f_p_code":4,"p_p_code":76,"name_en":"Ba Ria - Vung Tau","name_vi":"Tỉnh Bà Rịa - Vũng Tàu"},{"f_p_code":5,"p_p_code":82,"name_en":"Bac Giang","name_vi":"Tỉnh Bắc Giang"},{"f_p_code":6,"p_p_code":83,"name_en":"Bac Kan","name_vi":"Tỉnh Bắc Kạn"},{"f_p_code":7,"p_p_code":81,"name_en":"Bac Lieu","name_vi":"Tỉnh Bạc Liêu"},{"f_p_code":8,"p_p_code":84,"name_en":"Bac Ninh","name_vi":"Tỉnh Bắc Ninh"},{"f_p_code":9,"p_p_code":85,"name_en":"Ben Tre","name_vi":"Tỉnh Bến Tre"},{"f_p_code":10,"p_p_code":80,"name_en":"Binh Dinh","name_vi":"Tỉnh Bình Định"},{"f_p_code":11,"p_p_code":77,"name_en":"Binh Duong","name_vi":"Tỉnh Bình Dương"},{"f_p_code":12,"p_p_code":78,"name_en":"Binh Phuoc","name_vi":"Tỉnh Bình Phước"},{"f_p_code":13,"p_p_code":79,"name_en":"Binh Thuan","name_vi":"Tỉnh Bình Thuận"},{"f_p_code":14,"p_p_code":87,"name_en":"Ca Mau","name_vi":"Tỉnh Cà Mau"},{"f_p_code":15,"p_p_code":88,"name_en":"Can Tho","name_vi":"Thành phố Cần Thơ"},{"f_p_code":16,"p_p_code":86,"name_en":"Cao Bang","name_vi":"Tỉnh Cao Bằng"},{"f_p_code":17,"p_p_code":133,"name_en":"Da Nang","name_vi":"Thành phố Đà Nẵng"},{"f_p_code":18,"p_p_code":134,"name_en":"Dak Lak","name_vi":"Tỉnh Đắk Lắk"},{"f_p_code":19,"p_p_code":1,"name_en":"Dak Nong","name_vi":"Tỉnh Đắk Nông"},{"f_p_code":20,"p_p_code":132,"name_en":"Dien Bien","name_vi":"Tỉnh Điện Biên"},{"f_p_code":21,"p_p_code":2,"name_en":"Dong Nai","name_vi":"Tỉnh Đồng Nai"},{"f_p_code":22,"p_p_code":7,"name_en":"Dong Thap","name_vi":"Tỉnh Đồng Tháp"},{"f_p_code":23,"p_p_code":89,"name_en":"Gia Lai","name_vi":"Tỉnh Gia Lai"},{"f_p_code":24,"p_p_code":91,"name_en":"Ha Giang","name_vi":"Tỉnh Hà Giang"},{"f_p_code":25,"p_p_code":92,"name_en":"Ha Nam","name_vi":"Tỉnh Hà Nam"},{"f_p_code":26,"p_p_code":94,"name_en":"Ha Tinh","name_vi":"Tỉnh Hà Tĩnh"},{"f_p_code":27,"p_p_code":96,"name_en":"Hai Duong","name_vi":"Tỉnh Hải Dương"},{"f_p_code":28,"p_p_code":97,"name_en":"Hai Phong","name_vi":"Thành phố Hải Phòng"},{"f_p_code":29,"p_p_code":98,"name_en":"Hau Giang","name_vi":"Tỉnh Hậu Giang"},{"f_p_code":30,"p_p_code":90,"name_en":"Hoa Binh","name_vi":"Tỉnh Hòa Bình"},{"f_p_code":31,"p_p_code":95,"name_en":"Hung Yen","name_vi":"Tỉnh Hưng Yên"},{"f_p_code":32,"p_p_code":99,"name_en":"Khanh Hoa","name_vi":"Tỉnh Khánh Hòa"},{"f_p_code":33,"p_p_code":100,"name_en":"Kien Giang","name_vi":"Tỉnh Kiên Giang"},{"f_p_code":34,"p_p_code":101,"name_en":"Kon Tum","name_vi":"Tỉnh Kon Tum"},{"f_p_code":35,"p_p_code":102,"name_en":"Lai Chau","name_vi":"Tỉnh Lai Châu"},{"f_p_code":36,"p_p_code":105,"name_en":"Lam Dong","name_vi":"Tỉnh Lâm Đồng"},{"f_p_code":37,"p_p_code":106,"name_en":"Lang Son","name_vi":"Tỉnh Lạng Sơn"},{"f_p_code":38,"p_p_code":104,"name_en":"Lao Cai","name_vi":"Tỉnh Lào Cai"},{"f_p_code":39,"p_p_code":103,"name_en":"Long An","name_vi":"Tỉnh Long An"},{"f_p_code":40,"p_p_code":107,"name_en":"Nam Dinh","name_vi":"Tỉnh Nam Định"},{"f_p_code":41,"p_p_code":108,"name_en":"Nghe An","name_vi":"Tỉnh Nghệ An"},{"f_p_code":42,"p_p_code":109,"name_en":"Ninh Binh","name_vi":"Tỉnh Ninh Bình"},{"f_p_code":43,"p_p_code":110,"name_en":"Ninh Thuan","name_vi":"Tỉnh Ninh Thuận"},{"f_p_code":44,"p_p_code":111,"name_en":"Phu Tho","name_vi":"Tỉnh Phú Thọ"},{"f_p_code":45,"p_p_code":112,"name_en":"Phu Yen","name_vi":"Tỉnh Phú Yên"},{"f_p_code":46,"p_p_code":113,"name_en":"Quang Binh","name_vi":"Tỉnh Quảng Bình"},{"f_p_code":47,"p_p_code":114,"name_en":"Quang Nam","name_vi":"Tỉnh Quảng Nam"},{"f_p_code":48,"p_p_code":115,"name_en":"Quang Ngai","name_vi":"Tỉnh Quảng Ngãi"},{"f_p_code":49,"p_p_code":116,"name_en":"Quang Ninh","name_vi":"Tỉnh Quảng Ninh"},{"f_p_code":50,"p_p_code":117,"name_en":"Quang Tri","name_vi":"Tỉnh Quảng Trị"},{"f_p_code":51,"p_p_code":118,"name_en":"Soc Trang","name_vi":"Tỉnh Sóc Trăng"},{"f_p_code":52,"p_p_code":119,"name_en":"Son La","name_vi":"Tỉnh Sơn La"},{"f_p_code":53,"p_p_code":128,"name_en":"Tay Ninh","name_vi":"Tỉnh Tây Ninh"},{"f_p_code":54,"p_p_code":121,"name_en":"Thai Binh","name_vi":"Tỉnh Thái Bình"},{"f_p_code":55,"p_p_code":122,"name_en":"Thai Nguyen","name_vi":"Tỉnh Thái Nguyên"},{"f_p_code":56,"p_p_code":120,"name_en":"Thanh Hoa","name_vi":"Tỉnh Thanh Hóa"},{"f_p_code":57,"p_p_code":123,"name_en":"Thua Thien Hue","name_vi":"Tỉnh Thừa Thiên - Huế"},{"f_p_code":58,"p_p_code":124,"name_en":"Tien Giang","name_vi":"Tỉnh Tiền Giang"},{"f_p_code":59,"p_p_code":126,"name_en":"Tra Vinh","name_vi":"Tỉnh Trà Vinh"},{"f_p_code":60,"p_p_code":127,"name_en":"Tuyen Quang","name_vi":"Tỉnh Tuyên Quang"},{"f_p_code":61,"p_p_code":129,"name_en":"Vinh Long","name_vi":"Tỉnh Vĩnh Long"},{"f_p_code":62,"p_p_code":130,"name_en":"Vinh Phuc","name_vi":"Tỉnh Vĩnh Phúc"},{"f_p_code":63,"p_p_code":131,"name_en":"Yen Bai","name_vi":"Tỉnh Yên Bái"},{"f_p_code":64,"p_p_code":135,"name_en":"DKQL Cu Tru va DLQG Ve Dan Cu","name_vi":"ĐKQL Cư Trú và DLQG Về Dân Cư"},{"f_p_code":65,"p_p_code":902,"name_en":"Quan Ly Hanh Chinh Ve Trat Tu Xa Hoi","name_vi":"Quản Lý Hành Chính Về Trật Tự Xã Hội"}]

def write_cache():
    start = timeit.default_timer()
    with open(f'{dir_path}/province.json', 'w') as f:
        json.dump(data, f)
    
    stop = timeit.default_timer()
    print('Time write_cache: ', stop - start)

def read_cache():
    start = timeit.default_timer()
    with open(f'{dir_path}/province.json', 'r') as f:
        d = json.load(f)
        print(d[1])
    stop = timeit.default_timer()
    print('Time read_cache: ', stop - start)
    
    
    
def write_cache_orjson():
    start = timeit.default_timer()
    with open(f'{dir_path}/province2.json', 'wb') as f:
        f.write(orjson.dumps(data))
    
    stop = timeit.default_timer()
    print('Time write_cache_orjson: ', stop - start)    
    
def read_cache_orjson():
    start = timeit.default_timer()
    with open(f'{dir_path}/province2.json', 'r') as f:
        d = orjson.loads(f.read())
        print(d[1])
    stop = timeit.default_timer()
    print('Time read_cache_orjson: ', stop - start)



write_cache_orjson()
read_cache_orjson()

write_cache()
read_cache()
