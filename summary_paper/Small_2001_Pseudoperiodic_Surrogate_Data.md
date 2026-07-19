## BẢN PHÁC THẢO CÔ ĐỌNG THUẬT TOÁN PSEUDOPERIODIC SURROGATES (PPS)

### 1. Mục đích và Giả thuyết Null
* **Mục đích:** Khắc phục điểm yếu của các phương pháp tuyến tính (như IAAFT) khi xử lý dữ liệu có tính tuần hoàn giả (pseudoperiodic) mạnh như nhịp tim (ECG/PPG).
* **Giả thuyết Null:** Kiểm định xem chuỗi thời gian quan sát được có phải là một quỹ đạo tuần hoàn bị chi phối bởi nhiễu không tương quan (uncorrelated noise) hay không.

### 2. Quy trình 5 Bước Lập trình (Toán học Cốt lõi)

**Bước 1: Tái cấu trúc Không gian pha (Takens' Embedding)**
Chuyển chuỗi vô hướng $\{x_t\}_{t=1}^{N}$ thành các vector quỹ đạo đa chiều dựa trên độ trễ $\tau$ và số chiều nhúng $d_e$:
$$z_t = (x_t, x_{t-\tau}, \dots, x_{t-(d_e-1)\tau})$$
* Tập hợp quỹ đạo hợp lệ: $\{z_t\}_{t=1}^{\tilde{N}}$, với $\tilde{N} = N - (d_e - 1)\tau$.

**Bước 2: Khởi tạo Quỹ đạo Surrogate**
* Bắt đầu tạo quỹ đạo nhiễu $\{s_i\}$ bằng cách chọn ngẫu nhiên một điểm khởi đầu $s_1$ từ tập $\{z_t\}$.
* Đặt biến lặp $i = 1$.

**Bước 3: Hàm Xác suất Chuyển trạng thái (Trái tim của PPS)**
Tại trạng thái $s_i$, không đi theo quỹ đạo tất định mà "nhảy" sang một láng giềng $z_t$ (gọi điểm được chọn là $s_j$) với xác suất phân phối mũ dựa trên khoảng cách Euclide:
$$Prob(s_j = z_t) \sim \exp\left(\frac{-||z_t - s_i||}{\rho}\right)$$

> **Mẹo tối ưu code:** Sử dụng K-D Tree để tìm láng giềng gần thay vì tính toán trên toàn bộ không gian để giảm độ phức tạp xuống $O(N \log N)$.

**Bước 4: Bước nhảy Động lực học**
Sau khi chọn được láng giềng $s_j = z_t$, quỹ đạo surrogate mượn "bước tiến thời gian" của láng giềng đó để đi tiếp:
$$s_{i+1} = z_{t+1}$$
* Tăng $i$ và lặp lại Bước 3 cho đến khi đạt đủ độ dài $N$.

**Bước 5: Trích xuất Dữ liệu Vô hướng**
Chuỗi surrogate vô hướng 1D cuối cùng $\{x_t^{(s)}\}_{t=1}^N$ chính là thành phần đầu tiên của các vector quỹ đạo $\{s_t\}$:
$$x_t^{(s)} = s_t[0]$$

---

### 3. Cách chọn Bán kính nhiễu $\rho$ (Noise Radius)
Việc chọn $\rho$ quyết định hoàn toàn sự thành bại của thuật toán. Tác giả đề xuất một phương pháp không cần tham số (parameter-free) để tìm $\rho$ tự động:
* **Công thức:** Chọn $\rho$ sao cho số lượng các phân đoạn ngắn (có độ dài bằng 2 điểm dữ liệu liên tiếp) giống nhau giữa dữ liệu gốc và surrogate đạt giá trị cực đại.
* **Thực thi:** Quét (grid search) các giá trị $\rho$, sinh surrogate tương ứng, đếm số đoạn lặp lại và chọn đỉnh cực đại trên biểu đồ.

### 4. Ý nghĩa Động lực học của tham số $\rho$
* **Nếu $\rho \to \infty$:** Thuật toán chọn láng giềng ngẫu nhiên hoàn toàn trên không gian, quỹ đạo biến thành nhiễu IID thông thường.
* **Nếu $\rho \to 0$:** Xác suất chỉ tập trung vào láng giềng gần nhất, surrogate sinh ra sẽ giống hệt 100% dữ liệu gốc.
* **Trạng thái tối ưu:** Ở giá trị $\rho$ cực đại hóa sự trùng lặp ngắn hạn, PPS đạt được sự cân bằng hoàn hảo: Nó bảo tồn cấu trúc vĩ mô của chu kỳ (intracycle dynamics) nhưng lại xóa sổ (obliterate) hoàn toàn các cấu trúc vi mô tinh vi (fine structure) ẩn chứa giữa các chu kỳ.

**Kết luận:** Nếu tín hiệu siêu ngắn của bạn bác bỏ được bầy nhiễu này, bạn chính thức khẳng định sai lệch giữa các nhịp tim là Động lực học phi tuyến, không phải nhiễu!


# MÃ GIẢ CHUẨN MỰC (PYTHONIC PSEUDOCODE)

```python
def count_matching_segments(surrogate_indices, min_length=2):
    """
    Đếm số lượng các đoạn (segments) có chỉ số liên tiếp dài >= min_length.
    """
    count = 0
    current_len = 1
    
    for i in range(1, len(surrogate_indices)):
        if surrogate_indices[i] == surrogate_indices[i - 1] + 1:
            current_len += 1
        else:
            if current_len >= min_length:
                count += 1
            current_len = 1  # Reset khi chuỗi bị đứt gãy
            
    # Xử lý đoạn liên tục nằm ở cuối mảng
    if current_len >= min_length:
        count += 1
        
    return count


def optimize_rho(original_z, num_trials=10):
    """
    Quét (Grid Search) để tìm bán kính nhiễu tối ưu theo tỷ lệ logarit.
    """
    # 1. Tạo không gian quét logarit (VD: 50 điểm từ 10^-10 đến 10^0)
    rho_candidates = log_space(
        start=10**-10,
        stop=10**0,
        steps=50
    )
    
    best_rho = None
    max_expected_segments = -1
    
    # 2. Quét để tìm đỉnh (Peak)
    for rho in rho_candidates:
        total_segments = 0
        
        # Chạy nhiều lần để triệt tiêu nhiễu ngẫu nhiên
        for _ in range(num_trials):
            indices = generate_pps_indices(original_z, rho)
            total_segments += count_matching_segments(
                indices,
                min_length=2
            )
            
        expected_segments = total_segments / num_trials
        
        # 3. Cập nhật giá trị cực đại
        if expected_segments > max_expected_segments:
            max_expected_segments = expected_segments
            best_rho = rho
            
    return best_rho
```

# KỸ THUẬT SAI PHÂN TIỀN LÀM TRẮNG (PRE-WHITENING) TRONG PPS

## 1. Vấn đề (Cạm bẫy Nhiễu màu)
Thuật toán PPS sẽ bác bỏ Giả thuyết Null ($H_0$) khi hệ thống là "Chu kỳ + Nhiễu màu" do quá trình xáo trộn láng giềng đã phá hủy bộ nhớ (tự tương quan) của nhiễu màu, biến nó thành nhiễu trắng. Điều này dễ dẫn đến **False Positive**: Nhầm tưởng hệ thống có nhiễu trôi dạt chậm (như hô hấp đè lên nhịp tim) là hệ thống Hỗn độn (Chaos).

## 2. Giải pháp: Phép Sai phân (Differencing)
Thực hiện phép sai phân trên tín hiệu gốc trước khi tái cấu trúc không gian pha:
$$\Delta x_t = x_t - x_{t-\tau}$$
*(Lưu ý: Dùng trễ nhúng $\tau$ thay vì $1$ để giảm bớt độ gai góc).*

**Cơ chế toán học:** Phép sai phân đóng vai trò như một bộ lọc thông cao (high-pass filter), san phẳng phổ $1/f^2$ của nhiễu màu thành phổ phẳng (nhiễu trắng). Nếu tín hiệu chỉ là Limit Cycle + Nhiễu màu, sau khi sai phân, nó trở thành Limit Cycle + Nhiễu trắng -> **PPS sẽ không bác bỏ $H_0$ nữa.**

## 3. Rủi ro (Con dao hai lưỡi)
* **Khuếch đại nhiễu (Noise Amplification):** Phép trừ sẽ khuếch đại các nhiễu đo lường tần số cao (nhiễu trắng thành nhiễu xanh răng cưa).
* **Biến dạng Đa tạp:** Làm quỹ đạo vĩ mô trở nên gai góc, khiến quá trình Grid Search tìm tham số $\rho$ tối ưu của PPS trở nên khó hội tụ (đồ thị mất đỉnh Peak).

## 4. Best Practice (Quy trình Kiểm tra chéo)
Không dùng sai phân thay thế hoàn toàn, mà dùng làm lưới lọc xác nhận:
1. **Luồng 1 (Tín hiệu gốc):** Chạy PPS. Nếu **Không bác bỏ** $H_0$ -> Dừng. Nếu **Bác bỏ** -> Chuyển bước 2.
2. **Luồng 2 (Tín hiệu sai phân):** Chạy lại PPS trên tín hiệu $\Delta x_t$.
   * *Kết quả A:* Không bác bỏ được -> Phi tuyến ở Luồng 1 khả năng cao chỉ là nhiễu màu cơ học/sinh lý.
   * *Kết quả B:* **Vẫn Bác bỏ** $H_0$ -> Bằng chứng "vàng" khẳng định hệ thống có động lực học phi tuyến/hỗn độn nội tại cực mạnh, bất chấp phép lọc thông cao.

# PIPELINE THỰC NGHIỆM KÉP: KIỂM ĐỊNH ĐỘNG LỰC HỌC PHI TUYẾN TRÊN TÍN HIỆU PPG SIÊU NGẮN

**Mục tiêu:** Chứng minh sự tồn tại của động lực học phi tuyến tất định (Deterministic Nonlinear Dynamics) trong cấu trúc vi mô của tín hiệu PPG siêu ngắn, đồng thời loại trừ triệt để khả năng dương tính giả (false positive) do nhiễu màu sinh lý.

**Đại lượng phân định (Discriminating Statistic):** Sai số dự báo phi tuyến tất định (Deterministic Nonlinear Prediction Error - DNP).

---

## BƯỚC 1: TÁI TẠO BENCHMARK (Small, 2001)
* **Thực thi:** Khởi chạy thuật toán Pseudoperiodic Surrogates (PPS) kết hợp với DNP trên tập tín hiệu PPG gốc siêu ngắn. 
* **Mục đích:** Đánh giá khả năng dự báo của quỹ đạo gốc so với bầy surrogate (quỹ đạo tuần hoàn bị xáo trộn nhiễu không tương quan).
* **Kết quả kỳ vọng:** Sai số DNP của PPG gốc thấp hơn đáng kể so với bầy PPS.
* **Luận điểm:** Tương tự như kết quả trên dữ liệu ECG trong nghiên cứu của Small (2001), ta thành công bác bỏ giả thuyết $H_0$ (rằng tín hiệu chỉ là một Limit Cycle nhiễu trắng).

## BƯỚC 2: NHẬN DIỆN GIỚI HẠN THỐNG KÊ (Critical Acknowledgment)
* **Thực thi:** Trích dẫn trực tiếp hệ quả giới hạn từ bài báo của Small (2001).
* **Luận điểm:** Thừa nhận một cách khách quan rằng việc bác bỏ $H_0$ ở Bước 1 **chưa đủ điều kiện** để kết luận hệ thống có tính hỗn độn. Sự "phi tuyến" hoặc "tất định" vừa quan sát được hoàn toàn có thể là một ảo ảnh thống kê sinh ra bởi nhiễu màu sinh lý (ví dụ: dao động hô hấp tần số thấp hoặc trôi dạt thần kinh thực vật tác động lên cảm biến).

## BƯỚC 3: ĐỘT PHÁ PHƯƠNG PHÁP LUẬN (Pre-whitening Cross-validation)
* **Thực thi:** Áp dụng "Lưới lọc chéo" bằng kỹ thuật tiền làm trắng (pre-whitening). Thực hiện phép sai phân theo độ trễ nhúng trên toàn bộ chuỗi PPG:
  $$\Delta x_t = x_t - x_{t-\tau}$$
* **Mục đích:** Bộ lọc thông cao toán học này sẽ triệt tiêu hoàn toàn sự trôi dạt của nhiễu màu sinh lý (nếu có), biến nó thành nhiễu trắng. 
* **Kiểm định lại:** Chạy lại toàn bộ pipeline PPS + DNP trên chuỗi tín hiệu sai phân $\Delta x_t$.

## BƯỚC 4: KẾT LUẬN VÀNG RÒNG (The Golden Conclusion)
* **Điều kiện:** Đo lường lại DNP trên không gian pha của tín hiệu sai phân.
* **Luận điểm:** Nếu DNP vẫn cho thấy sai số dự báo của PPG sai phân thấp hơn mức ý nghĩa thống kê so với bầy nhiễu PPS sai phân, ta có cơ sở vững chắc để đưa ra tuyên bố học thuật: 
  > *"Khác với giới hạn của phương pháp PPS nguyên bản, quy trình kiểm định kép của chúng tôi chứng minh tín hiệu PPG siêu ngắn thực sự chứa Động lực học phi tuyến tất định, bảo toàn trọn vẹn đặc tính sinh lý và sống sót qua cả bộ lọc thông cao nhằm triệt tiêu nhiễu tương quan."*


  