# Lithium Intercalation in Graphite (LiC6) from DFT: Quantum ESPRESSO

*Self-directed learning project, November 2026. Author: Rizwan Haider, BS Physics, Thal University Bhakkar, Pakistan.*

This project computes the intercalation energy of lithium in graphite (the stage-1 compound LiC6, the fully lithiated graphite anode of lithium-ion batteries) with plane-wave density functional theory (DFT), and tests how the result depends on the van der Waals correction. It is a learning project that follows published methods, not new research. All results are compared with published values, and the limitations are listed below.

## Key results

| Quantity | This work, D3(BJ) (primary) | This work, D3 zero damping | Published |
|---|---|---|---|
| Intercalation energy per Li | -0.062 eV | -0.078 eV | -0.217 eV (vdW-DF) [12]; -0.188 eV (DFT-D3) [13] |
| LiC6 lattice constant a | 4.314 Å | 4.319 Å | 4.318 to 4.320 Å [13] |
| LiC6 layer spacing c | 3.612 Å | 3.658 Å | 3.654 to 3.659 Å [13]; experiment 3.70 Å [12] |
| Li bcc lattice constant | 3.333 Å | 3.379 Å | D3(BJ) 3.329 Å, D3 3.374 Å; experiment 3.449 Å [14] |

The intercalation energy is E_I = E(LiC6) - 6 x E(graphite)/4 - E(Li), with AB-stacked graphite (4 atoms per cell) and bcc Li metal as references, all computed with the same method. Negative values mean the intercalated compound is stable. Energies are converted with 1 Ry = 13.605693 eV.

**The calculated intercalation energy is about three times smaller in magnitude than the published values.** See the discussion below.

## Scope

- Non-spin-polarised calculations, static lattice at 0 K, no zero-point or thermal contributions, no Hubbard corrections.
- Only AA-stacked stage-1 LiC6 was studied, with AB graphite and bcc Li as references.
- One semilocal functional (PBE) with two D3 dispersion variants, plus an initial DFT-D2 test on graphite.

## Method

- **Code:** Quantum ESPRESSO 7.4.1 [1-3], compiled from source on Ubuntu 24.04 (WSL2); the packaged Ubuntu build crashed at start-up on this system. Laptop with 8 GB RAM.
- **Functional:** PBE [4] with Grimme dispersion corrections: D3 with Becke-Johnson damping [5,6] (`vdw_corr = 'grimme-d3'`, `dftd3_version = 4`, primary) and D3 with zero damping [5] (`dftd3_version = 3`). The assignment of these version numbers to the damping schemes was confirmed by the lithium lattice constants, which agree with published D3(BJ) and D3 values [14]. An early test used DFT-D2 [7].
- **Pseudopotentials:** li_pbe_v1.4.uspp.F.UPF (GBRV ultrasoft [9]) and C.pbe-n-kjpaw_psl.1.0.0.UPF (PAW from pslibrary [11]). Both files appear in the SSSP efficiency library [10] (Li in version 1.3; C in versions 1.0 and 1.1; the current version for C was not checked). File MD5 fingerprints: Li e912e257baa3777c20ea3d68f190483c, C 5f16ad9a65e90284d1d834d4ab3b0f7d.
- **Settings, identical for all three systems:** wavefunction cutoff 45 Ry, charge-density cutoff 360 Ry (8 times the wavefunction cutoff; for C this is a convention, not an SSSP value), Marzari-Vanderbilt smearing [8] of 0.02 Ry, Γ-centred unshifted k-grids: Li 16x16x16, graphite 16x16x5, LiC6 12x12x12.
- **Convergence thresholds:** SCF conv_thr 1e-8 Ry in the tests and 1e-10 Ry in relaxations and final runs; relaxation thresholds 1e-6 Ry (energy), 1e-4 Ry/bohr (forces), 0.1 kbar (pressure); variable-cell BFGS.

## Structures

- **Li:** bcc, 1 atom per primitive cell, starting a = 3.51 Å.
- **Graphite:** AB stacking, 4 atoms per cell, starting a = 2.46 Å and c = 6.71 Å.
- **LiC6:** AA stacking with one Li layer between graphene layers, sqrt(3) x sqrt(3) in-plane, 7 atoms (1 Li, 6 C). Li at (0, 0, 0); C at z = 1/2 at (1/3,0), (1/3,1/3), (0,1/3), (2/3,0), (2/3,2/3), (0,2/3) in crystal coordinates. Starting a = 4.270 Å (sqrt(3) times the D3(BJ) graphite a), starting c = 3.70 Å. The relaxation kept the symmetric positions, with a C-C bond of about 1.44 Å.
- **Final pressures after relaxation (D3(BJ)):** Li -0.02 kbar, graphite 0.21 kbar, LiC6 0.11 kbar.

## Convergence tests

Li cutoff (PBE only, 12x12x12 grid):

| Cutoff (Ry) | Total energy (Ry) | Change (mRy) |
|---|---|---|
| 30 | -14.47077572 | - |
| 40 | -14.47159731 | 0.82 |
| 45 | -14.47160076 | 0.003 |
| 50 | -14.47160720 | 0.006 |
| 60 | -14.47161074 | 0.004 |

Li k-points (PBE only, 45 Ry):

| Grid | Total energy (Ry) | Change (mRy) |
|---|---|---|
| 8x8x8 | -14.47127913 | - |
| 12x12x12 | -14.47160076 | 0.32 |
| 16x16x16 | -14.47181524 | 0.21 |
| 20x20x20 | -14.47181627 | 0.001 |
| 24x24x24 | -14.47181433 | 0.002 |

Graphite k-points (4 atoms, 45 Ry, DFT-D2 at the starting geometry):

| Grid | Total energy (Ry) | Change (mRy) |
|---|---|---|
| 8x8x3 | -73.80639547 | - |
| 12x12x4 | -73.80582724 | 0.57 |
| 16x16x5 | -73.80619897 | 0.37 |
| 20x20x6 | -73.80620230 | 0.003 |

LiC6 k-points (7 atoms, 45 Ry, D3(BJ) at the starting geometry):

| Grid | Total energy (Ry) | Change (mRy) |
|---|---|---|
| 8x8x8 | -125.20459368 | - |
| 12x12x12 | -125.20529961 | 0.71 |
| 16x16x16 | -125.20521279 | 0.09 |

Criterion: total-energy change below 1 mRy between neighbouring settings.

Cutoff convergence of the intercalation energy itself (fixed D3(BJ) relaxed geometries):

| Cutoff (Ry) | E_I (eV) |
|---|---|
| 45 | -0.0615 |
| 60 | -0.0618 |
| 80 | -0.0622 |

The change between 60 and 80 Ry is 0.4 meV, well below the threshold of 5 meV fixed before the test.

## Relaxed structures

| System | PBE only | D3(BJ) | D3 zero damping | Published or experiment |
|---|---|---|---|---|
| Li bcc, a (Å) | 3.435 | 3.333 | 3.379 | PAW GGA 3.439; D3(BJ) 3.329; D3 3.374; experiment 3.449 [14] |
| Graphite, a (Å) | not run | 2.466 | 2.466 | experiment about 2.46 (starting value) |
| Graphite, layer spacing c/2 (Å) | not run | 3.389 | 3.484 | experiment 3.3538; D3(BJ) 3.37 [15] |
| LiC6, a (Å) | not run | 4.314 | 4.319 | 4.318 to 4.320 [13] |
| LiC6, c (Å) | not run | 3.612 | 3.658 | 3.654 to 3.659 [13]; experiment 3.70 [12] |

An early DFT-D2 relaxation of graphite alone gave a layer spacing of 3.218 Å (published D2: 3.21 Å [15]). DFT-D2 was then abandoned because a published comparison reports an adsorption energy of -0.829 eV with D2 against -0.188 eV with D3 [13].

## Energies of the three systems (final relaxed calculations, Ry)

| | D3(BJ) | D3 zero damping |
|---|---|---|
| Li (1 atom) | -14.48452343 | -14.47903820 |
| Graphite (4 atoms) | -73.81335333 | -73.79607085 |
| LiC6 (7 atoms) | -125.20907200 | -125.17888590 |
| E_I, consistent method | -0.062 eV | -0.078 eV |
| E_I, with plain-PBE Li reference (-14.47206850 Ry) | -0.231 eV | -0.173 eV |

## Discussion and limitations

- The calculated intercalation energy is much less negative than the published values. The probable cause is the lithium reference. Published work shows that D3-type corrections can overcorrect alkali metals [14], and this calculation reproduces that: the Li lattice constant shrinks from 3.435 Å (PBE) to 3.333 Å (D3(BJ)) against 3.449 Å in experiment, and bulk Li becomes about 0.17 eV more stable. The sensitivity values (last row above) are close to the published numbers, but they combine two methods, so they are not the headline result. It is not known which Li energy was used in the published work [12,13].
- With D3(BJ), the LiC6 layer spacing is 2.4 % below experiment, a known deficiency [13].
- Graphite k-point convergence was tested with DFT-D2 and assumed to hold for D3; this was not tested. Cutoff convergence was tested for Li and, through E_I, for the combined result; it was not tested separately for graphite and LiC6.
- The smearing width (0.02 Ry) was not varied.
- Cells were relaxed at a fixed 45 Ry cutoff; the effect of Pulay stress on the lattice constants was not tested.
- D3 as implemented in Quantum ESPRESSO prints three-body terms; whether the published calculations include them was not checked.
- Possible extensions, not done: other LiCx stages, AB-stacked LiC6, Li diffusion barriers.

## Files

- `1_convergence/`: cutoff and k-point convergence tests (inputs and outputs)
- `2_relaxation/`: variable-cell relaxations of Li, graphite and LiC6
- `3_intercalation_energy/`: fixed-geometry runs at 45, 60 and 80 Ry, and the scripts `make_ei.py` and `calc_ei.py`

File names: `li` = lithium, `gr` = graphite, `lic6` = LiC6. In `2_relaxation/`, the plain `li.vc` is PBE only and `gr.vc` is DFT-D2; the suffix `3` marks D3(BJ) (`li3`, `gr3`) and `3z` marks D3 zero damping (`li3z`, `gr3z`, `lic6z`); `lic6.vc` is D3(BJ). Files beginning `ei_` are the fixed-geometry runs. Pseudopotential files are not included; download them from the SSSP library [10] or the Quantum ESPRESSO pseudopotential site.

## How to reproduce

```
pw.x < lic6.vc.in > lic6.vc.out        # relaxation, D3(BJ); likewise li3 and gr3
python3 make_ei.py                       # builds the ei_*.in files from the relaxed cells
pw.x < ei_lic6_45.in > ei_lic6_45.out    # likewise li and gr, cutoffs 45, 60, 80
python3 calc_ei.py                       # computes E_I at each cutoff
```

`make_ei.py` reads `li3.vc.out`, `gr3.vc.out` and `lic6.vc.out` from the same folder.

## Acknowledgements

The workflow was planned and checked with the help of an AI assistant (Claude, Anthropic). All calculations were run by the author.

## References

[1] P. Giannozzi et al., J. Phys.: Condens. Matter 21, 395502 (2009).

[2] P. Giannozzi et al., J. Phys.: Condens. Matter 29, 465901 (2017).

[3] P. Giannozzi et al., J. Chem. Phys. 152, 154105 (2020).

[4] J. P. Perdew, K. Burke, and M. Ernzerhof, Phys. Rev. Lett. 77, 3865 (1996).

[5] S. Grimme, J. Antony, S. Ehrlich, and H. Krieg, J. Chem. Phys. 132, 154104 (2010).

[6] S. Grimme, S. Ehrlich, and L. Goerigk, J. Comput. Chem. 32, 1456 (2011).

[7] S. Grimme, J. Comput. Chem. 27, 1787 (2006).

[8] N. Marzari, D. Vanderbilt, A. De Vita, and M. C. Payne, Phys. Rev. Lett. 82, 3296 (1999).

[9] K. F. Garrity, J. W. Bennett, K. M. Rabe, and D. Vanderbilt, Comput. Mater. Sci. 81, 446 (2014).

[10] G. Prandini, A. Marrazzo, I. E. Castelli, N. Mounet, and N. Marzari, npj Comput. Mater. 4, 72 (2018).

[11] A. Dal Corso, Comput. Mater. Sci. 95, 337 (2014).

[12] Li intercalation in graphite: a van der Waals density-functional study, arXiv:1410.5632.

[13] Supplementary information of DOI:10.1039/D1NR01946E (Li on graphite, comparison of dispersion corrections).

[14] Van der Waals density-functional theory study for bulk solids with BCC, FCC, and diamond structures, arXiv:1504.01219.

[15] Interatomic force constants including the DFT-D dispersion contribution, arXiv:1801.08741.
