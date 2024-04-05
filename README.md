File frequency_field: vẽ phổ trong miền tần số của file wav

File fir_lpf : bộ lọc thông thấp, đầu ra là 1 file nhạc sau khi lọc

File fir_hpf : bộ lọc thông cao, đầu ra là 1 file nhạc sau khi lọc

File fir_bpf : bộ lọc thông dải, đầu ra là 1 file nhạc sau khi lọc

File read : đọc file nhạc, in ra file txt là 16 bit biên độ

File write : tạo file nhạc dựa vào file txt

File pi: File nhạc định dạng wav, lấy mấu 16KHz, mono.

Trong folder 8 band là những gì mà tôi mới update
Tôi đã đưa tất cả các hàm trên vào 1 package
Ở trong package tôi thêm 1 số hàm

Hàm add_amp dùng để cộng biên độ các file wav sau khi xử lý
Hàm amplify dùng để khuếch đại Db của file wav
Hàm frequency_field dùng để vẽ trong miền tần số
Hàm time_field dùng để vẽ trong miền thời gian

Trong file main tôi đã làm như 1 chiếc equalizer gồm tách sóng bằng các bộ lọc, khuếch đại từng phần và tổng hợp lại
