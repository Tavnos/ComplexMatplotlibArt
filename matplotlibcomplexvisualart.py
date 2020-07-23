import numpy as np
import matplotlib.pyplot as plt


def generate_8_complex(t_range=0,
                        t_spread=0,
                        scale_exists=0,
                        abc_bump=0,
                        enable_t0=1,enable_t1=0,
                        enable_t2=0,enable_t3=0,
                        enable_t4=0,enable_t5=0,
                        enable_t_abc_denum=0, enable_t_abc_scale=0, 
                        t_a_inc=0,t_a_dec=0,
                        t_b_inc=0,t_b_dec=0,
                        t_c_inc=0,t_c_dec=0,
                        t_abc_denum=1,t_abc_scale=0):
    f_tr_x_ls = []
    f_ti_y_ls = []
    for i in range(t_range): 
        (f_tr_a_inc,f_tr_a_dec,
         f_tr_b_inc,f_tr_b_dec,
         f_tr_c_inc,f_tr_c_dec,
         f_tr_abc_scale,f_tr_abc_denum)=((np.real(np.e**(1j*2*np.pi*(i/t_spread)*t_a_inc))*enable_t0),
         (np.real(np.e**(1j*2*np.pi*(i/t_spread)*t_a_dec))*enable_t1),
         (np.real(np.e**(1j*2*np.pi*(i/t_spread)*t_b_inc))*enable_t2),
         (np.real(np.e**(1j*2*np.pi*(i/t_spread)*t_b_dec))*enable_t3),
         (np.real(np.e**(1j*2*np.pi*(i/t_spread)*t_c_inc))*enable_t4),
         (np.real(np.e**(1j*2*np.pi*(i/t_spread)*t_c_dec))*enable_t5),
         (np.real(np.e**(1j*2*np.pi*(i/t_spread)*t_abc_scale))*enable_t_abc_scale),
         (np.real(np.e**(1j*2*np.pi*(i/t_spread)*t_abc_denum))*enable_t_abc_denum))
        f_tr_x_ls +=  [(((f_tr_a_inc-f_tr_a_dec)+(f_tr_b_inc-f_tr_b_dec)+(f_tr_c_inc-f_tr_c_dec))/
                           (f_tr_abc_denum+abc_bump))                                              *(f_tr_abc_scale**scale_exists)]
        (f_ti_a_inc,f_ti_a_dec,
         f_ti_b_inc,f_ti_b_dec,
         f_ti_c_inc,f_ti_c_dec,
         f_ti_abc_scale,f_ti_abc_denum)=((np.imag(np.e**(1j*2*np.pi*(i/t_spread)*t_a_inc))*enable_t0),
         (np.imag(np.e**(1j*2*np.pi*(i/t_spread)*t_a_dec))*enable_t1),
         (np.imag(np.e**(1j*2*np.pi*(i/t_spread)*t_b_inc))*enable_t2),
         (np.imag(np.e**(1j*2*np.pi*(i/t_spread)*t_b_dec))*enable_t3),
         (np.imag(np.e**(1j*2*np.pi*(i/t_spread)*t_c_inc))*enable_t4),
         (np.imag(np.e**(1j*2*np.pi*(i/t_spread)*t_c_dec))*enable_t5),
         (np.imag(np.e**(1j*2*np.pi*(i/t_spread)*t_abc_scale))*enable_t_abc_scale),
         (np.imag(np.e**(1j*2*np.pi*(i/t_spread)*t_abc_denum))*enable_t_abc_denum))
        f_ti_y_ls +=  [(((f_ti_a_inc-f_ti_a_dec)+(f_ti_b_inc-f_ti_b_dec)+(f_ti_c_inc-f_ti_c_dec))/
                        (f_ti_abc_denum+abc_bump))                                                *(f_ti_abc_scale**scale_exists)]

    plt.scatter(f_tr_x_ls,f_ti_y_ls)
    plt.show()
    
generate_8_complex(1000,# Total ammount of jumps, lags if ~> 10 000        ##      1000 decent standard      ##
                   100,# t int loop spread, conclusive jumps ~ > 10     ##        pref around 100 - 1000    ##
                   2,   # 0 no mult, 1 enables, >1 uplifts, 1>pow>0 roots, ##  need to be 0 if not activated ##
                   100,  #  abc denum not to be 0, preferably not 1>denum>0  ##   slightly similar to spread  ##                    
                   ############################################################################################
                   ##   Mostly booleans for choice diversification: (not reccomended to use them as scale)   ##
                   ############################################################################################
                   1,1, #    # a1-a2                           ,     +a1     , or     -a2                    ##
                   1,1, #    # b1-b2                           ,     +b1     , or     -b2                    ##
                   1,1, #    # c1-c2                           ,     +c1     , or     -c2                    ##
                   1,1, #    # ((abc)/denum)*scale             , (abc)/denum , or   (abc)*scale              ##
                   ############################################################################################
                   ##   The lair of t itself, based on pi rationals and prime factors are encouraged         ##
                   ############################################################################################
                   ##              a1                         -                    a2                        ##
                   ((np.pi** 1 )/(np.pi* 1 ))* 1009              ,         ((np.pi** 1 )/(np.pi* 1 ))* 997,
                   ##              b1                         -                    b2                        ##
                   ((np.pi* 1 )/(np.pi* 1 ))* 991               ,          ((np.pi* 1 )/(np.pi* 1 ))* 983,  
                   ##              c1                         -                    c2                        ##
                   ((np.pi* 1 )/(np.pi* 1 ))* 977               ,          ((np.pi* 1 )/(np.pi* 1 ))* 971,  
                   ##        (abc)/denum                     and               (abc)*scale                   ##
                   ((np.pi** 1 )/(np.pi* 1 ))* 967         ,          ((np.pi* 1 )/(np.pi* 1 ))* 953      )  
                   ############################################################################################
                   #                             Keep in mind the current equation:                          ##
                   ############################################################################################
                   #               (a1-a2)+(b1-b2)+(c1-c2)               _^*scale_bool_ish                   ##
                   #               ------------------------ * abc_scale*^                                    ##
                   #               (abc_denum+no_div_0_airbag)                                               ##
                   ############################################################################################