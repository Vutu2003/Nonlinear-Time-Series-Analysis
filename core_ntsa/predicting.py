# import numpy as np
# from scipy.spatial import cKDTree
# from sklearn.linear_model import LinearRegression

# def predict_zeroth_order(signal, m, tau, horizon, train_ratio=0.8):
#     """
#     Dự báo bậc 0 (Nearest Neighbor) cho chuỗi thời gian dựa trên không gian pha.
#     """
#     n_points = len(signal)
#     max_idx = n_points - (m - 1) * tau - horizon
    
#     if max_idx <= 0:
#         raise ValueError("Chiều dài tín hiệu không đủ cho tham số đã chọn.")

#     # Tạo không gian pha bằng phương pháp tọa độ trễ.
#     x_embedded = np.array([
#         signal[i : i + m * tau : tau] for i in range(max_idx)
#     ])
    
#     # Xác định giá trị thực tế trong tương lai làm mục tiêu dự báo.
#     y_target = np.array([
#         signal[i + (m - 1) * tau + horizon] for i in range(max_idx)
#     ])
    
#     split_idx = int(len(x_embedded) * train_ratio)
    
#     # Chia dữ liệu thành tập lịch sử để tra cứu.
#     x_library = x_embedded[:split_idx]
#     y_library = y_target[:split_idx]
    
#     # Chia dữ liệu thành tập truy vấn để kiểm thử.
#     x_query = x_embedded[split_idx:]
#     y_true = y_target[split_idx:]
    
#     # Xây dựng cấu trúc cây KD-Tree từ tập dữ liệu lịch sử.
#     tree = cKDTree(x_library)
    
#     # Truy vấn láng giềng gần nhất cho tất cả các điểm kiểm thử.
#     _, neighbor_indices = tree.query(x_query, k=1)
    
#     # Lấy diễn biến tương lai của láng giềng làm kết quả dự báo.
#     y_pred = y_library[neighbor_indices]
    
#     # Tính toán sai số quân phương (RMSE) của tập kiểm thử.
#     rmse = np.sqrt(np.mean((y_true - y_pred) ** 2))
#     std_data = np.std(y_true)
    
#     # Trả về sai số chuẩn hóa và tránh lỗi chia cho không.
#     normalized_error = rmse / std_data if std_data > 0 else np.inf
        
#     return normalized_error, y_true, y_pred


# def predict_first_order(signal, m, tau, horizon, k, train_ratio=0.8):
#     """
#     Dự báo xấp xỉ tuyến tính cục bộ (Bậc 1) cho chuỗi thời gian hỗn loạn.
#     """
#     n_points = len(signal)
#     max_idx = n_points - (m - 1) * tau - horizon
    
#     if max_idx <= 0:
#         raise ValueError("Chiều dài tín hiệu không đủ cho tham số đã chọn.")
        
#     if k <= m:
#         raise ValueError("Số láng giềng k phải lớn hơn số chiều nhúng m để ổn định ma trận.")

#     # Tạo không gian pha bằng phương pháp tọa độ trễ.
#     x_embedded = np.array([
#         signal[i : i + m * tau : tau] for i in range(max_idx)
#     ])
    
#     # Xác định giá trị thực tế trong tương lai làm mục tiêu dự báo.
#     y_target = np.array([
#         signal[i + (m - 1) * tau + horizon] for i in range(max_idx)
#     ])
    
#     split_idx = int(len(x_embedded) * train_ratio)
    
#     # Chia dữ liệu thành tập lịch sử để tra cứu và huấn luyện mô hình cục bộ.
#     x_library = x_embedded[:split_idx]
#     y_library = y_target[:split_idx]
    
#     # Chia dữ liệu thành tập truy vấn để kiểm thử độ chính xác.
#     x_query = x_embedded[split_idx:]
#     y_true = y_target[split_idx:]
    
#     # Xây dựng cấu trúc cây KD-Tree từ tập dữ liệu lịch sử để tối ưu truy vấn.
#     tree = cKDTree(x_library)
    
#     y_pred = np.zeros(len(x_query))
#     model = LinearRegression()
    
#     # Lặp qua từng điểm truy vấn để xây dựng mô hình tuyến tính cục bộ.
#     for i, query_point in enumerate(x_query):
#         # Lấy ra k láng giềng gần nhất cho điểm hiện tại.
#         _, neighbor_indices = tree.query(query_point, k=k)
        
#         x_neighbors = x_library[neighbor_indices]
#         y_neighbors = y_library[neighbor_indices]
        
#         # Khớp một siêu mặt phẳng đi qua k láng giềng này bằng bình phương tối thiểu.
#         model.fit(x_neighbors, y_neighbors)
        
#         # Nội suy giá trị dự báo bằng cách ánh xạ điểm truy vấn lên mặt phẳng vừa tạo.
#         y_pred[i] = model.predict(query_point.reshape(1, -1))[0]
        
#     # Tính toán sai số quân phương (RMSE) của tập kiểm thử so với giá trị thực tế.
#     rmse = np.sqrt(np.mean((y_true - y_pred) ** 2))
#     std_data = np.std(y_true)
    
#     # Trả về sai số chuẩn hóa nhằm đánh giá mức độ hội tụ của hệ thống.
#     normalized_error = rmse / std_data if std_data > 0 else np.inf
        
#     return normalized_error, y_true, y_pred

import numpy as np
from scipy.spatial import cKDTree
from scipy.stats import pearsonr

def predict_zeroth_order(signal, m, tau, horizon, train_ratio=0.8):
    """
    Dự báo bậc 0 (Nearest Neighbor) cho chuỗi thời gian dựa trên không gian pha.
    Theo Lorenz (1969) - Phương pháp trạng thái tương tự (Analogues).
    """
    n_points = len(signal)
    max_idx = n_points - (m - 1) * tau - horizon
    
    if max_idx <= 0:
        raise ValueError("Chiều dài tín hiệu không đủ cho tham số đã chọn.")

    # 1. Tái tạo không gian pha
    x_embedded = np.array([
        signal[i : i + m * tau : tau] for i in range(max_idx)
    ])
    y_target = np.array([
        signal[i + (m - 1) * tau + horizon] for i in range(max_idx)
    ])
    
    # 2. Chia tập Library (Huấn luyện) và Query (Kiểm thử)
    split_idx = int(len(x_embedded) * train_ratio)
    
    x_library = x_embedded[:split_idx]
    y_library = y_target[:split_idx]
    
    x_query = x_embedded[split_idx:]
    y_true = y_target[split_idx:]
    
    # 3. Tìm láng giềng bằng KD-Tree
    tree = cKDTree(x_library)
    _, neighbor_indices = tree.query(x_query, k=1)
    
    # 4. Dự báo và tính sai số
    y_pred = y_library[neighbor_indices]
    
    rmse = np.sqrt(np.mean((y_true - y_pred) ** 2))
    std_data = np.std(y_true)
    normalized_error = rmse / std_data if std_data > 0 else np.inf
        
    return normalized_error, y_true, y_pred


def predict_first_order(signal, m, tau, horizon, k, train_ratio=0.8, theiler_window=50):
    """
    Dự báo Xấp xỉ Tuyến tính Cục bộ (Bậc 1) - Tối ưu hóa hiệu năng.
    Theo Farmer & Sidorowich (1987).
    
    Args:
        signal: Mảng 1D tín hiệu.
        m: Số chiều nhúng.
        tau: Độ trễ thời gian.
        horizon: Tầm nhìn dự báo (T bước tương lai).
        k: Số lượng láng giềng gần nhất (thường chọn k = m + 1 hoặc k = 2m).
        train_ratio: Tỷ lệ chia tập library/query.
        theiler_window: Cửa sổ Theiler để loại bỏ láng giềng quá gần về mặt thời gian (Khuyến nghị: = fs).
    """
    n_points = len(signal)
    max_idx = n_points - (m - 1) * tau - horizon
    
    if max_idx <= 0:
        raise ValueError("Chiều dài tín hiệu không đủ cho tham số đã chọn.")
    if k <= m:
        raise ValueError("Số láng giềng k phải lớn hơn số chiều nhúng m (k >= m + 1).")

    # 1. Tái tạo không gian pha
    x_embedded = np.array([
        signal[i : i + m * tau : tau] for i in range(max_idx)
    ])
    y_target = np.array([
        signal[i + (m - 1) * tau + horizon] for i in range(max_idx)
    ])
    
    # 2. Chia tập Library và Query
    split_idx = int(len(x_embedded) * train_ratio)
    
    x_library = x_embedded[:split_idx]
    y_library = y_target[:split_idx]
    
    x_query = x_embedded[split_idx:]
    y_true = y_target[split_idx:]
    
    # 3. Tìm láng giềng bằng KD-Tree
    tree = cKDTree(x_library)
    y_pred = np.zeros(len(x_query))
    
    # Truy vấn dư ra một số lượng láng giềng để trừ hao khi lọc bằng Theiler Window
    safe_k = k + theiler_window * 2 if theiler_window > 0 else k

    # 4. Vòng lặp dự báo tuyến tính cục bộ bằng Đại số tuyến tính Numpy
    for i in range(len(x_query)):
        query_point = x_query[i]
        actual_query_idx = split_idx + i # Vị trí thực tế trên chuỗi thời gian
        
        # Tìm các ứng viên láng giềng
        distances, raw_indices = tree.query(query_point, k=safe_k)
        
        # --- BỘ LỌC THEILER WINDOW ---
        # Chỉ giữ lại láng giềng có khoảng cách thời gian > theiler_window
        valid_indices = []
        # Xử lý trường hợp KDTree trả về số nguyên (khi k=1) hoặc mảng (k>1)
        raw_indices = np.atleast_1d(raw_indices) 
        
        for idx in raw_indices:
            if abs(idx - actual_query_idx) > theiler_window:
                valid_indices.append(idx)
            if len(valid_indices) == k:
                break
                
        # Fallback: Nếu không tìm đủ điểm ngoài cửa sổ Theiler, đành lấy các điểm gần nhất
        if len(valid_indices) < k:
            valid_indices = raw_indices[:k]
            
        idx_neighbors = np.array(valid_indices, dtype=int)
        
        # Lấy tọa độ và giá trị mục tiêu của k láng giềng hợp lệ
        X_mat = x_library[idx_neighbors]
        Y_mat = y_library[idx_neighbors]
        
        # --- HỒI QUY TUYẾN TÍNH SIÊU TỐC (NUMPY LSTSQ) ---
        # Thêm cột giá trị 1 vào ma trận X để tính hệ số tự do (Bias/Intercept)
        X_mat_bias = np.c_[X_mat, np.ones(k)]
        
        # Giải hệ phương trình X * beta = Y để tìm vector trọng số beta
        # beta chứa: [w1, w2, ..., wm, bias]
        beta, _, _, _ = np.linalg.lstsq(X_mat_bias, Y_mat, rcond=None)
        
        # Nội suy điểm dự báo: Y_pred = X_query * W + bias
        query_point_bias = np.append(query_point, 1.0)
        y_pred[i] = np.dot(query_point_bias, beta)
        
    # 5. Tính sai số chuẩn hóa
    rmse = np.sqrt(np.mean((y_true - y_pred) ** 2))
    std_data = np.std(y_true)
    
    normalized_error = rmse / std_data if std_data > 0 else np.inf
        
    return normalized_error, y_true, y_pred

def simplex_projection(signal, tau, m, T, train_ratio=0.8, theiler_window=None):
    """
    Thực hiện dự báo phi tuyến Simplex Projection với cKDTree.
    
    Tham số:
        signal (1D array): Chuỗi tín hiệu đầu vào.
        tau (int): Độ trễ thời gian.
        m (int): Chiều nhúng.
        T (int): Tầm nhìn dự báo.
        train_ratio (float): Tỷ lệ dữ liệu dành cho tập Thư viện (Train).
        theiler_window (int, optional): Cửa sổ loại trừ láng giềng.
        
    Trả về:
        p (float): Hệ số tương quan Pearson.
        ypred (1D array): Chuỗi dự báo.
        yobsever (1D array): Chuỗi thực tế.
    """
    # Khử xu hướng tuyến tính bằng cách lấy sai phân bậc 1.
    y = np.diff(signal)
    n_points = len(y)
    
    # Đặt cửa sổ Theiler mặc định để tránh tự tương quan nếu không được cung cấp.
    if theiler_window is None:
        theiler_window = m * tau
        
    # Xác định ranh giới thời gian hợp lệ để không bị trượt quá giới hạn mảng.
    min_t = (m - 1) * tau
    max_t = n_points - T
    
    if min_t >= max_t:
        raise ValueError("Độ dài tín hiệu không đủ cho cấu hình hiện tại.")
        
    valid_t = np.arange(min_t, max_t)
    num_vecs = len(valid_t)
    
    # Khởi tạo ma trận chứa không gian pha và giá trị đích tương lai.
    X = np.zeros((num_vecs, m))
    Y_target = np.zeros(num_vecs)
    
    # Trích xuất các vector không gian pha theo định lý Takens.
    for i, t in enumerate(valid_t):
        X[i, :] = y[t - (m - 1) * tau : t + 1 : tau]
        Y_target[i] = y[t + T]
        
    # Xác định điểm cắt để chia tập dữ liệu.
    split_idx = int(num_vecs * train_ratio)
    if split_idx == 0 or split_idx == num_vecs:
        raise ValueError("train_ratio không hợp lệ.")
        
    # Phân chia tập dữ liệu thành Thư viện (Train) và tập Kiểm thử (Test).
    X_train = X[:split_idx]
    Y_train = Y_target[:split_idx]
    t_train = valid_t[:split_idx]
    
    X_test = X[split_idx:]
    Y_test = Y_target[split_idx:]
    t_test = valid_t[split_idx:]
    
    # Xây dựng cấu trúc cây KD để tăng tốc độ tìm kiếm láng giềng gần nhất.
    tree = cKDTree(X_train)
    
    # Khối Simplex cần m + 1 đỉnh để bao bọc điểm truy vấn.
    k_neighbors = m + 1
    ypred = np.zeros(len(X_test))
    
    # Dự trù số lượng láng giềng truy vấn dư ra để bù trừ cho cửa sổ Theiler.
    query_k = min(k_neighbors + theiler_window, len(X_train))
    
    # Lặp qua từng điểm truy vấn trong tập Kiểm thử để thực hiện dự báo.
    for q, x_q in enumerate(X_test):
        # Lấy các láng giềng gần nhất ban đầu từ cây KD.
        dists, indices = tree.query(x_q, k=query_k)
        
        # Xử lý định dạng mảng khi chỉ truy vấn 1 láng giềng.
        if query_k == 1:
            dists = np.array([dists])
            indices = np.array([indices])
            
        # Lọc bỏ các láng giềng quá gần về mặt thời gian so với điểm truy vấn.
        time_diffs = np.abs(t_test[q] - t_train[indices])
        valid_mask = time_diffs > theiler_window
        
        valid_dists = dists[valid_mask]
        valid_indices = indices[valid_mask]
        
        # Mở rộng tìm kiếm trên toàn bộ tập Train nếu thiếu láng giềng hợp lệ.
        if len(valid_dists) < k_neighbors:
            dists_all, indices_all = tree.query(x_q, k=len(X_train))
            time_diffs_all = np.abs(t_test[q] - t_train[indices_all])
            valid_mask_all = time_diffs_all > theiler_window
            valid_dists = dists_all[valid_mask_all]
            valid_indices = indices_all[valid_mask_all]
            
        # Chọn ra chính xác m + 1 láng giềng hợp lệ gần nhất để tạo khối Simplex.
        d_neighbors = valid_dists[:k_neighbors]
        idx_neighbors = valid_indices[:k_neighbors]
        y_neighbors = Y_train[idx_neighbors]
        
        # Xử lý trọng số dựa trên khoảng cách của láng giềng gần nhất.
        d1 = d_neighbors[0]
        if d1 == 0:
            # Gán toàn bộ trọng số cho láng giềng trùng khớp hoàn hảo.
            W = np.zeros(k_neighbors)
            W[0] = 1.0
        else:
            # Tính và chuẩn hóa trọng số suy giảm hàm mũ để tạo tổ hợp lồi.
            w = np.exp(-d_neighbors / d1)
            W = w / np.sum(w)
            
        # Phóng chiếu nội suy giá trị tương lai bằng trung bình có trọng số.
        ypred[q] = np.sum(W * y_neighbors)
        
    # Đánh giá hệ số tương quan Pearson, bỏ qua nếu chuỗi là hằng số.
    if np.std(ypred) == 0 or np.std(Y_test) == 0:
        p = 0.0
    else:
        p, _ = pearsonr(ypred, Y_test)
        
    return p, ypred, Y_test

def simplex_projection_not_dif(signal,
                       tau,
                       m,
                       T,
                       train_ratio=0.8,
                       theiler_window=None):
    """
    Nonlinear forecasting using Simplex Projection.

    Parameters
    ----------
    signal : array-like
        Input time series.
    tau : int
        Time delay.
    m : int
        Embedding dimension.
    T : int
        Prediction horizon.
    train_ratio : float, optional
        Fraction of data used as library.
    theiler_window : int, optional
        Temporal exclusion window.

    Returns
    -------
    p : float
        Pearson correlation coefficient.
    ypred : ndarray
        Predicted values.
    yobs : ndarray
        Observed values.
    """

    # ==================================================
    # USE RAW SIGNAL (NO FIRST DIFFERENCE)
    # ==================================================
    y = np.asarray(signal, dtype=float)
    n_points = len(y)

    if theiler_window is None:
        theiler_window = m * tau

    min_t = (m - 1) * tau
    max_t = n_points - T

    if min_t >= max_t:
        raise ValueError(
            "Signal too short for current embedding configuration."
        )

    valid_t = np.arange(min_t, max_t)
    num_vecs = len(valid_t)

    # ==================================================
    # PHASE SPACE RECONSTRUCTION
    # ==================================================
    X = np.zeros((num_vecs, m))
    Y_target = np.zeros(num_vecs)

    for i, t in enumerate(valid_t):
        X[i, :] = y[t - (m - 1) * tau:t + 1:tau]
        Y_target[i] = y[t + T]

    # ==================================================
    # TRAIN / TEST SPLIT
    # ==================================================
    split_idx = int(num_vecs * train_ratio)

    if split_idx <= 0 or split_idx >= num_vecs:
        raise ValueError("Invalid train_ratio.")

    X_train = X[:split_idx]
    Y_train = Y_target[:split_idx]
    t_train = valid_t[:split_idx]

    X_test = X[split_idx:]
    Y_test = Y_target[split_idx:]
    t_test = valid_t[split_idx:]

    # ==================================================
    # KD-TREE
    # ==================================================
    tree = cKDTree(X_train)

    k_neighbors = m + 1

    query_k = min(
        max(5 * k_neighbors, k_neighbors + theiler_window),
        len(X_train)
    )

    ypred = np.zeros(len(X_test))

    # ==================================================
    # SIMPLEX FORECASTING
    # ==================================================
    for q, x_q in enumerate(X_test):

        dists, indices = tree.query(x_q, k=query_k)

        if np.isscalar(dists):
            dists = np.array([dists])
            indices = np.array([indices])

        # Apply Theiler window
        time_diffs = np.abs(t_test[q] - t_train[indices])

        valid_mask = time_diffs > theiler_window

        valid_dists = dists[valid_mask]
        valid_indices = indices[valid_mask]

        # Fallback search
        if len(valid_dists) < k_neighbors:

            dists_all, indices_all = tree.query(
                x_q,
                k=len(X_train)
            )

            time_diffs_all = np.abs(
                t_test[q] - t_train[indices_all]
            )

            valid_mask_all = (
                time_diffs_all > theiler_window
            )

            valid_dists = dists_all[valid_mask_all]
            valid_indices = indices_all[valid_mask_all]

        # Safety check
        if len(valid_dists) < k_neighbors:
            ypred[q] = np.nan
            continue

        d_neighbors = valid_dists[:k_neighbors]
        idx_neighbors = valid_indices[:k_neighbors]

        y_neighbors = Y_train[idx_neighbors]

        # ==================================================
        # EXPONENTIAL WEIGHTS
        # ==================================================
        d1 = d_neighbors[0]

        if d1 == 0:
            W = np.zeros(k_neighbors)
            W[0] = 1.0
        else:
            w = np.exp(-d_neighbors / d1)
            W = w / np.sum(w)

        ypred[q] = np.sum(W * y_neighbors)

    # ==================================================
    # REMOVE NAN
    # ==================================================
    valid = ~np.isnan(ypred)

    ypred = ypred[valid]
    yobs = Y_test[valid]

    if len(ypred) < 2:
        return 0.0, ypred, yobs

    if np.std(ypred) == 0 or np.std(yobs) == 0:
        p = 0.0
    else:
        p, _ = pearsonr(ypred, yobs)

    return p, ypred, yobs