import math

concentrations = [10, 15, 20, 25, 30]
dps_1_9 = [29.53528963,
45.82575695,
38.22302971,
35.17101079,
32.95957119]
dps_1_3 = [18.82374387,
36.01388621,
53.1130869,
23.64318084,
66.90540586]
dps_1_1 = [11.06044002,
14.14213562,
13.45362405,
10.11599394,
81]
dps_3_1 = [24.00694344,
10.06644591,
105.8158778,
30.61045573,
175.6710942]
dps_9_1 = [24.02776172,
2.516611478,
23.18045153,
14.17744688,
104.9190164]

p_1_9 = [536.33,
836.00,
1320.00,
1711.00,
2046.67]

p_1_3 = [506.33,
873.00,
1252.00,
1591.00,
2089.33]

p_1_1 = [420.33,
803,
1000,
1361.33,
1773]

p_3_1 = [454.33,
767.33,
1133,
1356,
1785.677]

p_9_1 = [488.67,
755.67,
1090.33,
1311,
1613]

mw30_t = [521.8333333,
801.6666667,
1086.5,
1399.5,
1729.833333]

mw_30_t_err = [0.6664320254,
0.6914230093,
1.647449665,
1.553848641,
3.240987737]

mw2000_t = [630,
1010.166667,
1422,
1841.333333,
2442.833333]

mw_2000_t_err = [0.8731232317249273,
1.4064887407220097,
1.526620668884931,
2.967169275776351,
1.239010106675668]

mw_differences = [108,
208.5000003,
335.5,
441.833333,
713]

def dp(mw30, mw2000):
    return 1/(mw2000 - mw30)

def dmw_30(p,mw30, mw2000):
    return (-1*(mw2000 - mw30) + (p - mw30))/(mw2000 - mw30)**2

def dmw_2000(p, mw30, mw2000):
    return -(p-mw30)(mw2000-mw30)**(-2)

def err_p(dp, dps):
    return (dp*dps)**2

def err_mw30(dmw30, dmws30):
    return (dmw30*dmws30)**2

def err_mw2000(dmw2000, dmws2000):
    return (dmw2000*dmws2000)**2

def err_total(err_p, err_mw30, err_mw2000):
    return math.sqrt(err_p + err_mw30 + err_mw2000)


for i in range(len(concentrations)):
    print(f"Concentration: {concentrations[i]}")
    dp_errs = [dps_1_9[i], dps_1_3[i], dps_1_1[i], dps_3_1[i], dps_9_1[i]]
    dmw30_abs = mw_30_t_err[i]
    dmw2000_abs = mw_2000_t_err[i]
    calculate_dp = dp(mw30_t[i], mw2000_t[i])
    dmw30 = [dmw_30(p_1_9[i], mw30_t[i], mw2000_t[i]), dmw_30(p_1_3[i], mw30_t[i], mw2000_t[i]), dmw_30(p_1_1[i], mw30_t[i], mw2000_t[i]), dmw_30(p_3_1[i], mw30_t[i], mw2000_t[i]), dmw_30(p_9_1[i], mw30_t[i], mw2000_t[i])]
    dmw2000 = [dmw_2000(p_1_9[i], mw30_t[i], mw2000_t[i]), dmw_2000(p_1_3[i], mw30_t[i], mw2000_t[i]), dmw_2000(p_1_1[i], mw30_t[i], mw2000_t[i]), dmw_2000(p_3_1[i], mw30_t[i], mw2000_t[i]), dmw_2000(p_9_1[i], mw30_t[i], mw2000_t[i])]
    total_errors = []
    for j in range(5):
        err_from_mw30 = err_mw30(dmw30[j], dmw30_abs)
        err_from_mw2000 = err_mw2000(dmw2000[j], dmw2000_abs)
        err_from_p = err_p(calculate_dp, dp_errs[j])
        error_totals = err_total(err_from_p, err_from_mw30, err_from_mw2000)
        print(error_totals)