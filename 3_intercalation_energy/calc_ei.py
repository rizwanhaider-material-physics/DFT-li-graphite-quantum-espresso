import re
Ry = 13.605693
def E(n, ec):
    t = open('ei_%s_%d.out' % (n, ec)).read()
    return float(re.findall(r'^!\s+total energy\s+=\s+(-?\d+\.\d+)', t, re.M)[-1])
prev = None
for ec in [45, 60, 80]:
    li, gr, lc = E('li', ec), E('gr', ec), E('lic6', ec)
    ei = (lc - 1.5 * gr - li) * Ry
    d = '' if prev is None else '   change vs previous: %+.4f eV' % (ei - prev)
    print('cutoff %d Ry: E_I = %.4f eV%s' % (ec, ei, d))
    prev = ei
