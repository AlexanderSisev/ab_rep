def norm_cdf(x, mean=0, std=1):
    from math import erf, sqrt
    z = (x-mean)/std
    return (1.0 + erf(z / sqrt(2.0))) / 2.0

def advantage(m0,n0,m1,n1):
    if n0 == 0 or n1 == 0:
        print("Division by zero!")
        return
    p0 = 1.0*m0/n0
    p1 = 1.0*m1/n1
    if p1 != p0:
        return round(p1/p0-1,6)
    else:
        return 0

def sigma_pp(m0,n0,m1,n1):
    if n0 == 0 or n1 == 0:
        print("Division by zero!")
        return    
    p0 = 1.0*m0/n0
    p1 = 1.0*m1/n1
    return round(pow(p1*(1-p1)/n1+p0*(1-p0)/n0,0.5),6)

def z_stat(m0,n0,m1,n1):
    if n0 == 0 or n1 == 0:
        print("Division by zero!")
        return
    p0 = 1.0*m0/n0
    p1 = 1.0*m1/n1
    try:
        return round((p1-p0)/sigma_pp(m0,n0,m1,n1),6)
    except:
        return n1+n0

def power(m0,n0,m1,n1):
    if n0 == 0 or n1 == 0:
        print("Division by zero!")
        return
    p0 = 1.0*m0/n0
    p1 = 1.0*m1/n1
    if p1>p0:
        p_cr = 1.96 * sigma_pp(m0,n0,m1,n1)
        return round(1.0-norm_cdf(p_cr, mean=p1-p0, std=sigma_pp(m0,n0,m1,n1)),6)
    elif p1<p0:
        p_cr = -1.96 * sigma_pp(m0,n0,m1,n1)
        return round(norm_cdf(p_cr, mean=p1-p0, std=sigma_pp(m0,n0,m1,n1)),6)
    else:
        return 0.0

def n_left(m0,n0,m1,n1):
    if n0 == 0 or n1 == 0:
        print("Division by zero!")
        return
    p0 = 1.0*m0/n0
    p1 = 1.0*m1/n1
    if p1!=p0:
        return round(max(pow(2.8*sigma_pp(m0,n0,m1,n1)/(p1-p0),2)-1,0.0),6)
    else:
        return 10000

def n_left_smooth(m0,n0,m1,n1):
    if n0 == 0 or n1 == 0:
        print("Division by zero!")
        return
    p0 = 1.0*m0/n0
    dp = round(advantage(m0,n0,m1,n1)*3,2)/3*p0
    if dp !=0:
        return round(max(pow(2.8*sigma_pp(m0,n0,m1,n1)/dp,2)-1,0.0),6)
    else:
        return 10000

def get_all_stats(m0,n0,m1,n1):
    if n0 == 0 or n1 == 0:
        print("Division by zero!")
        return
    return (advantage(m0,n0,m1,n1), z_stat(m0,n0,m1,n1), power(m0,n0,m1,n1), n_left(m0,n0,m1,n1))

def pretty_all(m0,n0,m1,n1):
    if n0 == 0 or n1 == 0:
        print("Division by zero!")
        return
    print("Advantage: "+str(round(advantage(m0,n0,m1,n1)*100,2))+'%')
    print("Z: ", round(z_stat(m0,n0,m1,n1),2))
    print("Power: "+str(int(power(m0,n0,m1,n1)*100))+'%')
    print("Wait_Multiplier: ", round(n_left(m0,n0,m1,n1),2))


