# Chen et al., Applied Energy 2025 — Liên hệ với GSI

## Ý chính
- Đề xuất multi-modal fusion:
  partial voltage profile + histogram vận hành → SOH.
- Mục tiêu: bù nhược điểm của từng nguồn dữ liệu.
- Kết quả tốt nhất: RMSPE 0.74%, giảm lỗi tới ~42%, và cần ít training cells hơn histogram-only khoảng 60%.

## Gap liên quan đến GSI

1. **SOH–voltage mismatch**
   - Cùng SOH nhưng voltage/IC curve giữa các cell có thể khác nhau.
   - Chen xử lý bằng cách thêm histogram.
   - GSI hướng tới giảm mismatch ngay trong voltage representation bằng ΔGSI/BOL normalization.

2. **Phụ thuộc nhiều nguồn dữ liệu**
   - Chen cần partial profile + accumulated histogram history.
   - GSI chỉ cần partial-discharge trajectory + BOL reference.
   - → GSI có tiềm năng giảm data/history/storage burden.

3. **Window sensitivity**
   - Chen cho thấy vị trí và độ dài partial window ảnh hưởng mạnh đến accuracy.
   - GSI cần chứng minh Head/Tail region ổn định và transferable khi freeze sang unseen cells/dataset.

4. **Generalization**
   - Chen có unseen-cell testing trong từng dataset.
   - Chưa chứng minh frozen cross-dataset/cross-chemistry transfer.
   - GSI nên nhắm strict LOCO + frozen feature geometry + external transfer.

5. **Physical interpretation**
   - Chen chủ yếu giải thích ở mức phenomenological; final CNN/FNN vẫn khó diễn giải.
   - GSI có thể mạnh hơn nếu Head/Tail regions được support bằng ICA/DVA.

6. **Computational cost**
   - Chen đã benchmark trên Jetson Nano (~15.6 ms, ~1.97 MB).
   - GSI cần benchmark end-to-end để chứng minh lợi thế của one-scalar + linear regression.