# PhamAnhCuong_19020038_Nhom3_Crawler

# Introduction: 
  + Problem: Crawl data from a web (newspaper or/and e-commerce) using Scrapy (Thu thập dữ liệu từ 1 web (báo hoặc/và trang thương mại điện tử).
  + Code run in Python 3.7.8, using Pycharm Community 2020.1.3.

# Newspaper: 24h.com.vn
  + Information collected: Crawling_link, title, time (public date), content, keywords, summary, source (but I don't know how to separate its with the last information in content)
    (Thông tin thu thập: Link thu thập, Tiêu đề, Thời gian, Nội dung, Từ khoá, Tóm tắt, Nguồn trang (Nhưng nó nằm trong phần cuối của Nội dung nên em chỉ viết code lấy chứ không in)
  + Status: Completed (Hoàn thành)
  + Number of page crawled: 2523 (end by close the terminal)
  + Total crawl time: 137s
  + Crawl speed: 18.5 pages/second

# E-commerce: sendo.vn 
  + Information collected: Crawling_link, name, link_to_product, description, img_url, keywords, price_shop
    (Thông tin thu thập: Link thu thập, Tên sản phẩm, Danh mục dẫn tới sản phẩm (em ghi là link_to_product), mô tả, url của ảnh, từ khoá, giá + shop bán (có giá riêng nhưng em thấy có đoạn text lưu cả giá bán cũng như shop bán nên gộp)
  + Status: Failed - Can't open output file although code run successfully
            (Code chạy nhưng không có file output xuất ra, không đo được tốc độ)
