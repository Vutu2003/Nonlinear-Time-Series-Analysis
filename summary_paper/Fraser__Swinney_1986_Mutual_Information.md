# 📘 GHI CHÚ NGHIÊN CỨU: THUẬT TOÁN $N \log N$ TÍNH THÔNG TIN TƯƠNG HỖ (MI)
**Tác giả:** Andrew M. Fraser & Harry L. Swinney (1986)
**Mục đích:** Biến đổi bài toán Tích phân Xác suất (Toán học Giải tích) thành bài toán Đếm nhánh Nhị phân / Quadtree (Khoa học Máy tính) để giải quyết nghịch lý kích thước lưới (grid size paradox) khi tính Thông tin tương hỗ $I(S,Q)$.

---

## BƯỚC 1: Tiền xử lý & Triệt tiêu Mẫu số (Đơn giản hóa Toán học)
**Mục tiêu:** Đơn giản hóa công thức Shannon Mutual Information (MI) bằng cách biến các xác suất biên (marginal probabilities) thành hằng số, từ đó giảm tải tính toán.

---

## 1. Bài toán gốc (Công thức 10)
Theo Shannon, Thông tin tương hỗ giữa hai biến $s = s(t)$ và $q = s(t+T)$ được tính bằng:
$$I(s,q) = \sum_{K} P_{sq}(R(K)) \log \left[ \frac{P_{sq}(R(K))}{P_s(R(K))P_q(R(K))} \right] \tag{10}$$
* **Khó khăn:** Phải liên tục tính và nội suy mẫu số $P_s$ và $P_q$ tại mọi mức phân hoạch $m$.

## 2. Phép biến đổi Hạng (Rank Transform)
Thuật toán sử dụng **QuickSort** để chuyển đổi toàn bộ giá trị thực của dữ liệu thành **Thứ hạng** (Rank) và chuẩn hóa về phân bố đều $U(0,1)$.

* **Sắp xếp & Gán hạng:** Biến $s_i$ được gán hạng $r_i \in \{1, \dots, N\}$. Biến $q_i$ được gán hạng $u_i \in \{1, \dots, N\}$.
* **Chuẩn hóa Uniform:** $$x_i = \frac{r_i - 0.5}{N}, \quad y_i = \frac{u_i - 0.5}{N}$$
* **Kết quả:** Ánh xạ tập điểm $(s,q) \longrightarrow (x,y)$ với $x,y \sim U(0,1)$.

## 3. Triệt tiêu Xác suất biên
Khi chia mỗi trục không gian $(x,y)$ thành $2^m$ đoạn bằng nhau ở độ sâu $m$:
* Vì dữ liệu phân bố đều, số điểm rơi vào mỗi đoạn trên 1 trục là hoàn toàn bằng nhau: $N/2^m$.
* **Xác suất biên trở thành hằng số:**
  $$P_s(i) = P_q(j) = \frac{N/2^m}{N} = \frac{1}{2^m}$$
* **Mẫu số bị triệt tiêu:**
  $$P_s(i) \times P_q(j) = \frac{1}{2^m} \times \frac{1}{2^m} = 4^{-m}$$

## 4. Rút gọn Phương trình (Công thức 11)
Thay $4^{-m}$ vào mẫu số của Công thức (10) và sử dụng tính chất logarit $\log(a \cdot b) = \log(a) + \log(b)$:

$$i_m = \sum P_{sq} \log \left( P_{sq} \cdot 4^m \right)$$
$$i_m = \sum P_{sq} \Big[ \log(P_{sq}) + \log(4^m) \Big]$$

Đưa hằng số ra ngoài tổng, và vì tổng các xác suất $\sum P_{sq} = 1$:
$$i_m = m \log(4) + \sum P_{sq} \log(P_{sq}) \tag{11}$$
*(Ghi chú: Cụm $\sum P_{sq} \log P_{sq}$ chính là $-H_{sq}$ hay Entropy kết hợp âm).*

---

## 5. Ý nghĩa Cốt lõi (Vật lý & Thống kê)
Phép biến đổi này (được biết đến như Empirical Copula trong thống kê) mang lại 3 giá trị vĩ đại:
1. **Lọc bỏ nhiễu phân bố:** Triệt tiêu hoàn toàn thông tin biên ($P_s, P_q$), ép hệ thống chỉ đo lường cấu trúc phụ thuộc (tính hỗn mang) giữa $s$ và $q$.
2. **Miễn nhiễm ngoại lai (Outliers):** Nhờ dùng "Thứ hạng", một điểm nhiễu văng cực xa cũng chỉ cách điểm liền kề $\frac{1}{N}$. Lưới toán học không bị bóp méo.
3. **Bất biến (Invariance):** Giá trị MI không thay đổi dù thiết bị đo đạc bị khuếch đại hay bị lệch phi tuyến (chỉ cần tính đơn điệu được giữ nguyên).

---

## BƯỚC 2: Động lực học Cắt lưới (Chi phí & Lợi ích)
Phân tích lượng thông tin thay đổi khi một ô mẹ (cấp $m$) bị chém làm 4 ô con (cấp $m+1$):

**Thông tin ô mẹ (12):**
$$C_r = P_r [m \log(4)] + P_r \log(P_r)$$

**Thông tin ô con thứ $j$ (13):**
$$C_j = P_j [(m+1) \log(4)] + P_j \log(P_j)$$

**Tổng thông tin 4 ô con (14):**
$$\sum_{j=0}^3 C_j = P_r [(m+1) \log(4)] + \sum_{j=0}^3 P_j \log(P_j)$$

> **📌 TỪ ĐIỂN KÝ HIỆU:**
> * $C_r$: Đóng góp thông tin của ô mẹ mang chỉ số $r$.
> * $C_j$: Đóng góp thông tin của ô con thứ $j$.
> * $j \in \{0, 1, 2, 3\}$: Chỉ số 4 góc phần tư của ô mẹ.
> * $P_r$: Xác suất điểm rơi vào ô mẹ ($\sum P_j = P_r$).
> * **Triết lý toán học:** Nếu ô mẹ có phân bố phẳng ($P_j = P_r/4$), tổng thông tin 4 ô con sẽ bằng đúng thông tin ô mẹ. Việc cắt nhỏ là vô ích.

---

## BƯỚC 3: Thiết lập Hàm Đệ quy (Khung xương Quadtree)
Xây dựng hàm đệ quy $F$ áp dụng cho bất kỳ ô lưới nào để tính cấu phần Entropy cục bộ:

**Trường hợp Dừng lại (16a) - Nếu ô phân bố phẳng:**
$$F(R(K)) = P_{sq}(R(K)) \log [P_{sq}(R(K))]$$

**Trường hợp Đào sâu (16b) - Nếu ô có cấu trúc phức tạp:**
$$F(R(K)) = P_{sq}(R(K)) \log(4) + \sum_{j=0}^3 F(R_{m+1}(K, j))$$

> **📌 TỪ ĐIỂN KÝ HIỆU:**
> * $F(...)$: Hàm đệ quy tính cấu phần thông tin.
> * $R_{m+1}(K, j)$: Lời gọi đệ quy (Recursive call) trỏ đến ô con thứ $j$ ở độ sâu $m+1$.

---

## BƯỚC 4: Tối ưu hóa Thực hành (Chuyển Xác suất thành Số nguyên)
Khử số thực ($P_{sq}$), quy đổi toàn bộ về số nguyên để tăng tốc độ tính toán của CPU lên mức tối đa:

**Dừng đệ quy (20a):**
$$F = N \log(N)$$

**Tiếp tục cắt (20b):**
$$F = N \log(4) + \sum F_{con}$$

**Tổng hợp MI cuối cùng (19):**
$$I(S,Q) = \frac{1}{N_p} F(R_0(K_0)) - \log(N_p)$$

> **📌 TỪ ĐIỂN KÝ HIỆU:**
> * $N_p$ (hoặc $N_{total}$): Tổng số lượng điểm dữ liệu toàn cục (Hằng số).
> * $N$: Số lượng điểm dữ liệu đếm được trong ô lưới hiện tại ($P_{sq} = N/N_p$).
> * $F_{con}$: Hàm $F$ tính cho 4 ô con.
> * $R_0(K_0)$: **Nút gốc (Root node)** bao trùm toàn bộ không gian pha. Phép chia cho $N_p$ chỉ diễn ra đúng 1 lần khi toàn bộ cây đã duyệt xong.

---

## BƯỚC 5: Khóa chốt Tự động (Kiểm định Thống kê $\chi^2$)
Đây là "trọng tài" quyết định khi nào thuật toán gọi phương trình (20a) và khi nào gọi (20b):

**Kiểm định mức 1 (21):**
$$\frac{1}{N} \sum_{i=1}^{4} (a_i - N/4)^2 \le 1.547$$

**Kiểm định mức 2 (22):**
$$\frac{1}{N} \sum_{i,j=1}^{4} (b_{ij} - N/16)^2 \le 1.287$$

> **📌 LÝ THUYẾT & LOGIC LẬP TRÌNH:**
> * $N$: Tổng số điểm trong ô mẹ.
> * $a_i$: Số điểm đếm được thực tế trong 4 ô con ($i \in \{1, 2, 3, 4\}$).
> * $N/4$: Số điểm kỳ vọng trong 1 ô con nếu phân bố đều.
> * $b_{ij}$: Số điểm đếm được thực tế nếu thử cắt tiếp thành 16 ô cháu.
> * $1.547$ & $1.287$: Ngưỡng tra bảng Chi-square ($\chi^2$) ở mức ý nghĩa ~20%.
> 
> **Mã giả (Pseudo-code):**
> ```python
> if (Phương_trình_21 <= 1.547) and (Phương_trình_22 <= 1.287):
>     # Dữ liệu phẳng / Chỉ là nhiễu ngẫu nhiên
>     return N * log(N)  # Gọi 20a (Đóng nhánh)
> else:
>     # Có cấu trúc phi tuyến ẩn giấu
>     return N * log(4) + sum(F_con)  # Gọi 20b (Chém làm 4 và đệ quy tiếp)
> ```