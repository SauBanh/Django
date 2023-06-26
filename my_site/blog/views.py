from datetime import date
from django.shortcuts import render

all_posts = [
    {
        "slug": "sinh-vien-hutech-dang-ky-hoc-phan-dong-hoc-phi-hoc-ky-1-nam-hoc-2023-2024",
        "image": "hoithao.jpg",
        "author": "Sáu Bảnh",
        "date": date(2023, 6, 23),
        "title": "Sinh viên HUTECH đóng học phí Học kỳ 1 năm học 2023 - 2024 từ 14/7",
        "excerpt": "Phòng Đào tạo Trường Đại học Công nghệ TP.HCM (HUTECH) thông báo đến sinh viên Đại học chính quy, Đại học liên thông, Đại học văn bằng...",
        "content": """ Sinh viên đăng ký học phần trực tuyến tại địa chỉ: http://daotao.hutech.edu.vn/ bằng cách đăng nhập tài khoản cá nhân như sau:

                        Tên tài khoản (account): mã số sinh viên
                        Mật khẩu mặc định (password): mã số sinh viên và ngày tháng năm sinh theo định dạng ddmmyyyy (dành cho những sinh viên truy cập vào tài khoản lần đầu tiên)

                        Ví dụ: Sinh viên Nguyễn Văn A có Mã số sinh viên là 1611145234 thì đây là tên tài khoản, ngày tháng năm sinh là 01/10/1993 thì nhập mật khẩu là 01101993.

                        Lưu ý: Đối với những sinh viên lần đầu đăng nhập vào tài khoản, sau khi đăng nhập thành công cần khai báo email (bắt buộc) và thay đổi mật khẩu cá nhân để bảo mật tài khoản.
                    """
    },
    {
        "slug": "sinh-vien-khoa-dieu-duong-va-xet-nghiem-tham-kham",
        "image": "anh.jpg",
        "author": "Sáu Bảnh",
        "date": date(2023, 6, 26),
        "title": "Chiến dịch Thanh niên tình nguyện hè 2023",
        "excerpt": "Vừa qua, Khoa Điều dưỡng và Xét nghiệm Trường Đại học Công nghệ TP.HCM (HUTECH) phối...",
        "content": """Vừa qua, Khoa Điều dưỡng và Xét nghiệm Trường Đại học Công nghệ TP.HCM (HUTECH) phối hợp cùng Đoàn Thanh niên, Hội Người cao tuổi và Trạm Y tế phường 27 đã tổ chức buổi khám bệnh hỗ trợ sức khỏe cho người dân tại nơi đây.
                        Được biết, chương trình nằm trong khuôn khổ Chiến dịch Thanh niên tình nguyện hè 2023 của Thành đoàn TP.HCM với các hoạt động thăm khám diễn ra trong 3 ngày từ 21 - 23/6. Chương trình hướng đến người già neo đơn, có hoàn cảnh khó khăn và trẻ em tại phường, qua đó đã tập trung thăm khám, xét nghiệm, cấp thuốc cho hơn 200 cá nhân trên địa bàn.
                        Tại chương trình, sinh viên Khoa Điều dưỡng và Xét nghiệm đã cùng tham gia vào các hoạt động khám sức khỏe tổng quát, đo các chỉ số cơ thể, đo huyết áp và tư vấn sức khỏe cho người dân địa phương. Ngoài ra, các bạn còn hỗ trợ các bác sĩ ghi nhận tình trạng bệnh nhân, lấy máu, mẫu xét nghiệm cũng như hỗ trợ siêu âm và đo điện tim. Đối với các em thiếu nhi, sinh viên cũng giúp khám răng và hướng dẫn các em cách chăm sóc răng miệng đúng cách.
                    """
    },
    {
        "slug": "hutech-football-cup-2023-clb-tan-tru-chinh-thuc-dang-quang-ngoi-vo-dich",
        "image": "avata.jpg",
        "author": "Sáu Bảnh",
        "date": date(2023, 6, 17),
        "title": "[HUTECH Football Cup 2023] CLB Tân Trụ chính thức đăng quang ngôi vô địch",
        "excerpt": "Khởi tranh từ 16/6/2023, quy tụ 07 đội bóng đến từ các Câu lạc bộ phong trào mạnh tại địa bàn TP.HCM, trải qua 16 lượt trận gay cấn, tối qua (23/6)...",
        "content": """Khởi tranh từ 16/6/2023, quy tụ 07 đội bóng đến từ các Câu lạc bộ phong trào mạnh tại địa bàn TP.HCM, trải qua 16 lượt trận gay cấn, tối qua (23/6) vòng Chung kết Giải Bóng đá HUTECH mở rộng “HUTECH Football Cup 2023” lần thứ 1 - năm 2023 đã khép lại đầy mãn nhãn với ngôi vô địch thuộc về Tân Trụ.
                        Được biết, lượt trận vòng Chung kết diễn ra tại sân Bóng đá cơ sở Hitech Park Campus của HUTECH giữa Tân Trụ - JinĐô (tranh Nhất, Nhì) và giữa Khánh Hạnh - N&N (tranh Hạng 3).
                        Trận tranh ngôi vô địch là cuộc chạm trán giữa đội đang thi đấu giải FI - Tân Trụ và đội đang thi đấu giải SPL - JinĐô. Với lối đá đôi công gây cấn, JinĐô vẫn có nhiều cơ hội ghi bàn nhưng lại dứt điểm không thành công, trong khi đó Tân Trụ lại tận dụng tối đa các cơ hội để ghi bàn. Suốt 40 phút thi đấu đầy hấp dẫn và kịch tính, kết quả chung cuộc đã được xác định thông qua tỉ số áp đảo (5-0) nghiêng về đội Tân Trụ. Với kết quả cách biệt này, Tân Trụ đã nâng cao cúp vô địch “HUTECH Football Cup 2023” và JinĐô là đội Á quân.
                        Trước đó lúc 17h30, trận tranh Hạng 3 giữa Khánh Hạnh và N&N diễn ra khá sôi nổi, đồng thời đây cũng là trận đấu có số bàn thắng được ghi nhiều nhất mùa giải với tổng số 15 bàn thắng, với tỉ số chung cuộc (9-6) nghiêng về N&N. Với kết quả này, N&N đã đánh bại Khánh Hạnh và về đích “HUTECH Football Cup 2023” ở vị trí Hạng 3.
                    """
    }
]

def get_date(post):
    return post['date']

# Create your views here.

def starting_page(request):
    sorted_posts = sorted(all_posts, key=get_date)
    latest_posts = sorted_posts[-3:]
    return render(request, "blog/index.html", {
        "posts": latest_posts
    })

def posts(request):
    return render(request, "blog/all-posts.html", {
        "all_posts": all_posts
    })

def post_detail(request, slug):
    indentified_post = next(post for post in all_posts if post['slug'] == slug)
    return render(request, "blog/post-detail.html", {
        "post": indentified_post
    })