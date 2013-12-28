
def sinSnell(cos_i, n_i, n_t):
    return (n_i / n_t) * ( 1 - cos_i ** 2 ) ** 0.5

def cosSnell(cos_i, n_i, n_t):
    c = n_t ** 2 / n_i ** 2
    return(1 - c + c * cos_i ** 2) ** 0.5

def fresnel(cos_i, n_i, n_t):
    cos_t = cosSnell(cos_i, n_i, n_t)
    ii = n_i * cos_i
    it = n_i * cos_t
    ti = n_t * cos_i
    tt = n_t * cos_t
    rs = ((ii - tt)/(ii + tt)) ** 2
    rp = ((it - ti)/(it + ti)) ** 2
    return (rs + rp) / 2
