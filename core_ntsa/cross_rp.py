# =============================================================================
# CRP 2002 CORE
# Historical implementation of Marwan & Kurths (2002).
#
# Architecture:
#   1. Phase Space      -> embed_time_series()
#   2. Cross Geometry   -> cross-distance / CR matrix
#   3. Lag Scanning     -> diagonal structures P_t(l)
#   4. Quantification   -> RR(t), DET(t), L(t)
#   5. Wrappers         -> run_crp_analysis(), analyze_lagged_interrelations()
#
# Principle: separate cross-recurrence geometry from lag-dependent statistics.
# =============================================================================