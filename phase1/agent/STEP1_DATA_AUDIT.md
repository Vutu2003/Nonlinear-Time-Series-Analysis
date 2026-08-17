Sau cell import, `data_audit.ipynb` nên gồm các cell sau:

1. **Cell 2 — Dataset path**

   * Trỏ tới `dataset/dhdata/`.
   * Lấy danh sách tất cả file CSV.

2. **Cell 3 — Load sessions**

   * Dùng `load_session()`.
   * Lưu DataFrame và metadata của từng session.

3. **Cell 4 — Dataset overview**

   * Số sessions.
   * Tổng samples.
   * Tổng recording hours.
   * Duration từng session.
   * Estimated sampling rate từng session.

4. **Cell 5 — Data quality audit**

   * Null/NaN.
   * Duplicate rows/timestamps.
   * Non-monotonic timestamps.
   * Time gaps.
   * Empty columns.
   * Invalid labels.

5. **Cell 6 — Sampling & duration plot**

   * Recording duration theo session.
   * Sampling frequency theo session.
   * Dùng để phát hiện acquisition outliers.

6. **Cell 7 — Label statistics**

   * Mapping: `0 = Awake`, `1 = Drowsy`.
   * Samples, duration và percentage của từng trạng thái.
   * Tổng dataset và từng session.

7. **Cell 8 — Awake/Drowsy composition plot**

   * Horizontal stacked bar theo session.
   * Awake vs Drowsy duration.

8. **Cell 9 — Continuous state segments**

   * Tách các đoạn Awake/Drowsy liên tục.
   * Số transitions.
   * Số segments.
   * Longest/median duration theo state.

9. **Cell 10 — Segment-duration plot**

   * Distribution của contiguous Awake vs Drowsy segment durations.

10. **Cell 11 — Window availability**

* Kiểm tra:

```text
60 / 120 / 180 / 240 / 300 s
```

* Với mỗi duration:

  * Awake eligible.
  * Drowsy eligible.
  * Paired eligible.

11. **Cell 12 — Window availability plot**

* `x = 60, 120, 180, 240, 300 s`
* `y = eligible sessions`
* Series: Awake / Drowsy / Paired.

12. **Cell 13 — Final dataset summary**

* Original sessions.
* Excluded sessions.
* Final usable sessions.
* Total recording hours.
* Awake/Drowsy durations.
* Sampling-rate distribution.
* Paired availability ở `60/120/180/240/300 s`.

Flow tổng thể:

```text
Load
→ Overview
→ Quality
→ Sampling
→ Labels
→ Continuous segments
→ 60/120/180/240/300-s availability
→ Final dataset summary
```
