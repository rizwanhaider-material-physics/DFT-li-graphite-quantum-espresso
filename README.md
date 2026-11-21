# Lithium Intercalation in Graphite (LiC6) from DFT: Quantum ESPRESSO

*Self-directed learning project, November 2026. Author: Rizwan Haider, BS Physics, Thal University Bhakkar, Pakistan.*

This project computes the intercalation energy of lithium in graphite (stage-1 compound LiC6, the anode of lithium-ion batteries) with plane-wave density functional theory, and tests how the result depends on the van der Waals correction. It is a learning project that follows published methods, not new research. All results are compared with published values, and its limitations are listed below.

## Key results

| Quantity | This work (D3(BJ), primary) | This work (D3 zero damping) | Published |
|---|---|---|---|
| Intercalation energy per Li | -0.062 eV | -0.078 eV | -0.217 eV (vdW-DF) [12]; -0.188 eV (DFT-D3) [13] |
| LiC6 lattice constant a | 4.314 Å | 4.319 Å | 4.318 to 4.320 Å [13] |
| LiC6 layer spacing c | 3.612 Å | 3.658 Å | 3.654 to 3.659 Å [13]; experiment 3.70 Å [12] |
| Li bcc lattice constant | 3.333 Å | 3.379 Å | 3.329 (D3(BJ)), 3.374 (D3); experiment 3.449 Å [14] |

The intercalation energy is E_I = E(LiC6) - 6 x E(graphite)/4 - E(Li), where graphite is AB-stacked (4 atoms per cell) and Li is bcc metal; all three use the same method. Negative values mean the intercalated compound is stable.

**The calculated intercalation energy is about three times smaller in magnitude than the published values.** See the discussion below.

## Method

- **Code:** Quantum ESPRESSO 7.4.1 [1-3], compiled from source on Ubuntu 24.04 (WSL2); the packaged Ubuntu build crashed at start-up on this system. Laptop with 8 GB RAM.
- **Functional:** PBE [4], with Grimme dispersion corrections: D3 with Becke-Johnson damping [5,6] (primary) and D3 with zero damping [5] (sensitivity check).
- **Pseudopotentials:** li_pbe_v1.4.uspp.F.UPF (GBRV ultrasoft [9]) and C.pbe-n-kjpaw_psl.1.0.0.UPF (PAW from pslibrary [11]); both are the files recommended by the SSSP efficiency library [10]. MD5 fingerprints checked: Li e912e257baa3777c20ea3d68f190483c, C 5f16ad9a65e90284d1d834d4ab3b0f7d.
- **Settings (identical for all three systems):** plane-wave cutoff 45 Ry, charge-density cutoff 360 Ry, Marzari-Vanderbilt smearing [8] of 0.02 Ry. k-point grids: Li 16x16x16, graphite 16x16x5, LiC6 12x12x12.
- **Structures:** Li bcc (1 atom), AB graphite (4 atoms), AA-stacked stage-1 LiC6 (7 atoms, sqrt(3) x sqrt(3) in-plane, Li above each hexagon centre). Every cell and all atomic positions were relaxed (variable-cell relaxation).

## Convergence tests

Lithium cutoff, PBE only, 12x12x12 grid:

| Cutoff (Ry) | Total energy (Ry) |
|---|---|
| 30 | -14.47077572 |
| 40 | -14.47159731 |
| 45 | -14.47160076 |
| 50 | -14.47160720 |
| 60 | -14.47161074 |

Lithium k-points, PBE only, 45 Ry:

| Grid | Total energy (Ry) |
|---|---|
| 8x8x8 | -14.47127913 |
| 12x12x12 | -14.47160076 |
| 16x16x16 | -14.47181524 |
| 20x20x20 | -14.47181627 |
| 24x24x24 | -14.47181433 |

Graphite k-points (4 atoms, 45 Ry, DFT-D2 at the starting geometry):

| Grid | Total energy (Ry) |
|---|---|
| 8x8x3 | -73.80639547 |
| 12x12x4 | -73.80582724 |
| 16x16x5 | -73.80619897 |
| 20x20x6 | -73.80620230 |

LiC6 k-points (7 atoms, 45 Ry, D3(BJ) at the starting geometry):

| Grid | Total energy (Ry) |
|---|---|
| 8x8x8 | -125.20459368 |
| 12x12x12 | -125.20529961 |
| 16x16x16 | -125.20521279 |

Convergence criterion: total-energy change below 1 mRy between neighbouring settings.

**Cutoff convergence of the intercalation energy itself** (fixed D3(BJ) geometries):

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
| Graphite, a (Å) | not run | 2.466 | 2.466 | experiment 2.46 |
| Graphite, layer spacing (Å) | not run | 3.389 | 3.484 | experiment 3.3538; D3(BJ) 3.37 [15] |
| LiC6, a (Å) | not run | 4.314 | 4.319 | 4.318 to 4.320 [13] |
| LiC6, c (Å) | not run | 3.612 | 3.658 | 3.654 to 3.659 [13]; experiment 3.70 [12] |

An earlier attempt with DFT-D2 on graphite alone gave a layer spacing of 3.218 Å (published D2: 3.21 Å [15]). DFT-D2 was then abandoned because a published comparison reports an adsorption energy of -0.829 eV with D2, against -0.188 eV with D3 [13].

## Energies of the three systems (final relaxed calculations, Ry)

| | D3(BJ) | D3 zero damping |
|---|---|---|
| Li (1 atom) | -14.48452343 | -14.47903820 |
| Graphite (4 atoms) | -73.81335333 | -73.79607085 |
| LiC6 (7 atoms) | -125.20907200 | -125.17888590 |
| E_I, consistent method | -0.062 eV | -0.078 eV |
| E_I, with plain-PBE Li reference (-14.47206850 Ry) | -0.231 eV | -0.173 eV |

## Discussion and limitations

- The calculated intercalation energy is much less negative than the published values. The probable cause is the lithium reference. Published work shows that D3 and D3(BJ) corrections can overcorrect alkali metals [14], and this calculation reproduces that: the Li lattice constant shrinks from 3.435 Å (PBE) to 3.333 Å (D3(BJ)) against 3.449 Å in experiment, and bulk Li becomes about 0.17 eV more stable. The sensitivity values (last row above) are close to the published numbers, but they combine two methods, so they are not the headline result. It is not known which Li energy was used in the published work [12,13].
- With D3(BJ), the LiC6 layer spacing is 2.4 % below experiment, a known deficiency [13].
- Graphite k-point convergence was tested with DFT-D2 and assumed to hold for D3; this assumption was not tested.
- Only AA-stacked LiC6 was studied, with one family of dispersion corrections.
- Cells were relaxed at a fixed 45 Ry cutoff; the effect of Pulay stress on the lattice constants was not tested.
- D3 as implemented in Quantum ESPRESSO prints three-body terms; whether the published calculations include them was not checked.

## Files

- `1_convergence/`: cutoff and k-point convergence tests (inputs and outputs)
- `2_relaxation/`: variable-cell relaxations of Li, graphite and LiC6 with each dispersion scheme
- `3_intercalation_energy/`: fixed-geometry runs at 45, 60 and 80 Ry, and the scripts `make_ei.py` and `calc_ei.py`

Pseudopotential files are not included; download them from the SSSP library [10] or the Quantum ESPRESSO pseudopotential site.

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

[13] Supplementary information, DOI 10.1039/D1NR01946E (Li on graphite, comparison of dispersion corrections).

[14] Van der Waals density-functional theory study for bulk solids with BCC, FCC, and diamond structures, arXiv:1504.01219.

[15] Interatomic force constants including the DFT-D dispersion contribution, arXiv:1801.08741.
