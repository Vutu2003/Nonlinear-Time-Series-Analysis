| Component | Closest prior art | Similarity | Remaining distinction | Verdict |
|---|---|---|---|---|
| Raw GSI primitive | Naha 2020; Chen 2024 | High | Single capacity-defined Head–Tail ΔV using window averages | **Chỉ mang tính cải tiến; primitive ΔV không còn mới** |
| Partial-discharge regional descriptor | Wen 2022; Li 2024 | High | Vertical voltage separation rather than ΔSoC or dV/dt statistics | **Chỉ mang tính cải tiến; ý tưởng regional partial-discharge feature đã có** |
| Capacity normalization | Naha 2020 | Medium-High | Exact Head/Tail normalized-capacity formulation differs | **Có khác biệt về cách triển khai, nhưng khó xem là novelty độc lập** |
| Correlation-based window selection | Wen 2022 | High | Pairwise Head/Tail exhaustive search differs in implementation | **Không mới; chỉ khác ở chiến lược tìm kiếm window cụ thể** |
| Simple/linear SOH estimation | Wen 2022; Jenu 2022 | High | One-scalar GSI/ΔGSI + LR may be more parsimonious | **Không mới nếu đứng riêng; chỉ có giá trị nếu chứng minh được tính tối giản và hiệu quả** |
| ΔGSI BOL subtraction | No direct match in five papers | Low-Medium | Within-cell reference-normalized scalar intended to suppress cell offset | **Có tiềm năng là điểm khác biệt chính, nhưng chưa đủ bằng chứng để kết luận novel** |
| Cross-cell & external validation | Naha 2020; Wen 2022; Li 2024 | High | Strict LOCO + fixed feature/no target tuning may be stronger | **Là bằng chứng validation mạnh, không nên xem là novelty của phương pháp** |
| Physical mechanism | Jenu 2022; Wen 2022 | Partial | GSI still lacks direct electrochemical linkage | **Hiện chỉ có thể xem là physically motivated; chưa đủ cơ sở để claim cơ chế vật lý trực tiếp** |