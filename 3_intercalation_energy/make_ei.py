import re
CU = "li_pbe_v1.4.uspp.F.UPF"
CC = "C.pbe-n-kjpaw_psl.1.0.0.UPF"
systems = {
    'li':   dict(out='li3.vc.out',  nat=1, sp=[('Li', 6.94, CU)],               k='16 16 16'),
    'gr':   dict(out='gr3.vc.out',  nat=4, sp=[('C', 12.011, CC)],              k='16 16 5'),
    'lic6': dict(out='lic6.vc.out', nat=7, sp=[('Li', 6.94, CU), ('C', 12.011, CC)], k='12 12 12'),
}
cutoffs = [45, 60, 80]
for name, s in systems.items():
    L = open(s['out']).read().split('\n')
    ic = max(i for i, l in enumerate(L) if l.startswith('CELL_PARAMETERS'))
    alat = re.search(r'alat=\s*([0-9.]+)', L[ic]).group(1)
    cell = '\n'.join(L[ic+1:ic+4])
    ia = max(i for i, l in enumerate(L) if l.startswith('ATOMIC_POSITIONS'))
    hdr = L[ia].strip()
    pos = '\n'.join(L[ia+1:ia+1+s['nat']])
    species = '\n'.join('  %s %s %s' % x for x in s['sp'])
    for ec in cutoffs:
        txt = f"""&CONTROL
  calculation = 'scf'
  prefix = 'ei_{name}_{ec}'
  outdir = './tmp'
  pseudo_dir = '../pseudo'
/
&SYSTEM
  ibrav = 0
  celldm(1) = {alat}
  nat = {s['nat']}
  ntyp = {len(s['sp'])}
  ecutwfc = {ec}.0
  ecutrho = {ec*8}.0
  occupations = 'smearing'
  smearing = 'marzari-vanderbilt'
  degauss = 0.02
  vdw_corr = 'grimme-d3'
  dftd3_version = 4
/
&ELECTRONS
  conv_thr = 1.0d-10
/
ATOMIC_SPECIES
{species}
CELL_PARAMETERS alat
{cell}
{hdr}
{pos}
K_POINTS automatic
  {s['k']} 0 0 0
"""
        open(f'ei_{name}_{ec}.in', 'w').write(txt)
print('made', len(systems)*len(cutoffs), 'input files')
