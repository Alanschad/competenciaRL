# 🏆 Leaderboard — Campeonato RL (DQN)

Entorno base: `MountainCar-v0` · 5 circuitos · Ranking por **MEDIA** en cada circuito · Actualizado: 2026-10-30 14:12 UTC

Puntos por circuito: 25, 18, 15, 12, 10, 8, 6, 4, 2, 1 (del 1° al 10°). La misma policy corre en todos los circuitos. Detalle de cada uno en el README.

**Un auto titular por escudería** (cuenta de GitHub): es el único que suma puntos y ocupa posiciones. Es el auto de la escudería que más puntos suma contra los titulares de las demás. El resto son autos de reserva: aparecen abajo, pero no le sacan puestos a nadie.

## 🏁 Campeonato

| # | Auto | Escudería | **Pts** | Estándar | Largada libre | Lluvia | Motor débil | Otra pista |
|---|------|-----------|-----:|:---:|:---:|:---:|:---:|:---:|
| 🥇 | naoagent-greedy2 | naomicouriel | **43** | 1° (25) | 17° | 7° (6) | 23° | 4° (12) |
| 🥈 | vanafa | VANAFA | **42** | 2° (18) | 2° (18) | 21° | 18° | 7° (6) |
| 🥉 | DeCruz | BrunoDC-dev | **40** | 15° | 1° (25) | 12° | 3° (15) | 21° |
| 4 | ivan-de-pineda-101 | RamaMusic | **40** | 6° (8) | 10° (1) | 1° (25) | 9° (2) | 8° (4) |
| 5 | Alan-Schadan-v2 | Alanschad | **35** | 25° | 5° (10) | 13° | 1° (25) | 28° |
| 6 | bravo-andres | Andresbravo9 | **35** | 17° | 6° (8) | 3° (15) | 4° (12) | 17° |
| 7 | fium-V3 | tomasbenavidez | **33** | 11° | 18° | 2° (18) | 25° | 3° (15) |
| 8 | leon-alderete | joaquinleondev | **31** | 3° (15) | 16° | 6° (8) | 24° | 6° (8) |
| 9 | tomas-castro | tommycass | **30** | 21° | 4° (12) | 22° | 12° | 2° (18) |
| 10 | valentino-pettazi | ValenPettaz1 | **28** | 22° | 13° | 5° (10) | 2° (18) | 24° |
| 11 | lein2 | matilein | **25** | 29° | 11° | 25° | 17° | 1° (25) |
| 12 | salim | athinasalimm | **25** | 5° (10) | 3° (15) | 19° | 15° | 14° |
| 13 | gonzalezds | mariagonzalezdelsolar | **22** | 4° (12) | 12° | 24° | 22° | 5° (10) |
| 14 | domabot2 | Sdomato | **20** | 19° | 19° | 4° (12) | 6° (8) | 18° |
| 15 | Franco-Colapinto | famatodlr | **14** | 20° | 9° (2) | 9° (2) | 5° (10) | 16° |
| 16 | frangiavarini-exp12 | frangiavarini | **12** | 8° (4) | 7° (6) | 20° | 14° | 9° (2) |
| 17 | joaco-di-cola | joaco1212004 | **10** | 27° | 29° | 7° (6) | 8° (4) | 29° |
| 18 | maxi | maxividela2577 | **6** | 23° | 26° | 11° | 7° (6) | 20° |
| 19 | agusamblard | agusamblard | **6** | 7° (6) | 15° | 17° | 27° | 22° |
| 20 | sb3zoo | Gabo-Tor | **4** | 16° | 8° (4) | 26° | 28° | 25° |
| 21 | Meteoro | FacundoFirpo | **3** | 9° (2) | 24° | 28° | 26° | 10° (1) |
| 22 | mateofreire | mateofreire | **1** | 24° | 14° | 10° (1) | 11° | 11° |
| 23 | zoffi | florzoffi | **1** | 26° | 30° | 14° | 10° (1) | 26° |
| 24 | jazgeller | jazgeller | **1** | 10° (1) | 23° | 15° | 21° | 15° |
| 25 | viaggio | FelipeViaggioFL | **0** | 13° | 28° | 27° | 16° | 12° |
| 26 | martin-bianchi | martinbianchi0 | **0** | 12° | 25° | 18° | 29° | 27° |
| 27 | sgroba | Santi2065 | **0** | 14° | 21° | 16° | 13° | 19° |
| 28 | auto-cipre | CiprianoOss | **0** | 30° | 22° | 30° | 19° | 13° |
| 29 | matbr | mateobramer | **0** | 18° | 20° | 29° | 30° | 30° |
| 30 | valeriano | Isivaleriano | **0** | 28° | 27° | 23° | 20° | 23° |
| 31 | ion_h_RL_TP2 | 72Ion | **0** | 31° | 31° | 31° | 31° | 31° |

## 🔧 Autos de reserva

No suman ni ocupan posiciones. Las posiciones son las que tendría cada auto si fuera el titular de su escudería (contra los titulares de las demás).

| Auto | Escudería | Pts como titular | Estándar | Largada libre | Lluvia | Motor débil | Otra pista |
|------|-----------|-----:|:---:|:---:|:---:|:---:|:---:|
| Alan-Schadan | Alanschad | 8 | 7° (6) | 9° (2) | 24° | 19° | 12° |
| bravo-andres-r1 | Andresbravo9 | 30 | 14° | 5° (10) | 5° (10) | 5° (10) | 13° |
| bravo-andres-r2 | Andresbravo9 | 24 | 17° | 4° (12) | 9° (2) | 5° (10) | 14° |
| DeCruz_v2 | BrunoDC-dev | 25 | 11° | 5° (10) | 15° | 26° | 3° (15) |
| lein | matilein | 33 | 22° | 20° | 1° (25) | 6° (8) | 20° |
| lein3 | matilein | 25 | 29° | 11° | 25° | 21° | 1° (25) |
| naoagent-greedy3 | naomicouriel | 43 | 1° (25) | 14° | 6° (8) | 20° | 5° (10) |
| naoagent | naomicouriel | 43 | 19° | 5° (10) | 2° (18) | 3° (15) | 20° |
| naoagent-greedy | naomicouriel | 38 | 2° (18) | 12° | 4° (12) | 25° | 6° (8) |
| naoagent-ensemble | naomicouriel | 34 | 2° (18) | 7° (6) | 6° (8) | 13° | 9° (2) |
| ivan-de-pineda-102 | RamaMusic | 37 | 7° (6) | 12° | 1° (25) | 12° | 7° (6) |
| ivan-de-pineda-105 | RamaMusic | 34 | 13° | 10° (1) | 1° (25) | 6° (8) | 11° |
| ivan-de-pineda-106 | RamaMusic | 34 | 13° | 10° (1) | 1° (25) | 6° (8) | 13° |
| ivan-de-pineda-104 | RamaMusic | 34 | 18° | 10° (1) | 1° (25) | 6° (8) | 16° |
| ivan-de-pineda-es-inocente-sin-cos | RamaMusic | 34 | 3° (15) | 10° (1) | 5° (10) | 21° | 6° (8) |
| ivan-de-pineda-103 | RamaMusic | 32 | 14° | 10° (1) | 1° (25) | 7° (6) | 13° |
| ivan-de-pineda-es-inocente-con-features | RamaMusic | 32 | 3° (15) | 10° (1) | 5° (10) | 19° | 7° (6) |
| ivan-de-pineda-es-inocente-sin-features | RamaMusic | 31 | 3° (15) | 12° | 5° (10) | 15° | 7° (6) |
| ivan-de-pineda-107 | RamaMusic | 21 | 19° | 10° (1) | 4° (12) | 6° (8) | 13° |
| domabot | Sdomato | 0 | 18° | 30° | 29° | 29° | 21° |
| fium-V2 | tomasbenavidez | 25 | 26° | 28° | 27° | 1° (25) | 29° |
| fium-V1 | tomasbenavidez | 18 | 21° | 14° | 23° | 30° | 2° (18) |
| fium-V4 | tomasbenavidez | 12 | 21° | 8° (4) | 16° | 6° (8) | 27° |
| tomasbenavidez | tomasbenavidez | 10 | 9° (2) | 18° | 16° | 28° | 6° (8) |
| tomas-castro-equilibrado | tommycass | 35 | 16° | 9° (2) | 1° (25) | 6° (8) | 13° |

## GP Estándar

_MountainCar-v0 tal cual._

| # | Auto | Escudería | Pts | Media | IQM | Sin llegar | Min | Max | Episodios | Dif. al 1° |
|---|------|-----------|----:|-------|-----|-----------:|-----|-----|-----------|-----------|
| R | naoagent-greedy3 | naomicouriel | — | -97.423 | -100.268 | 0.0% | -104.0 | -83.0 | 1000 | −0.005 |
| 1 | naoagent-greedy2 | naomicouriel | 25 | -97.428 | -100.276 | 0.0% | -104.0 | -83.0 | 1000 | — |
| 2 | vanafa | VANAFA | 18 | -97.430 | -100.282 | 0.0% | -104.0 | -83.0 | 1000 | +0.002 |
| R | ivan-de-pineda-es-inocente-con-features | RamaMusic | — | -97.434 | -100.282 | 0.0% | -104.0 | -83.0 | 1000 | +0.006 |
| R | naoagent-greedy | naomicouriel | — | -97.440 | -100.302 | 0.0% | -104.0 | -83.0 | 1000 | +0.012 |
| R | ivan-de-pineda-es-inocente-sin-features | RamaMusic | — | -97.480 | -100.314 | 0.0% | -104.0 | -83.0 | 1000 | +0.052 |
| R | ivan-de-pineda-es-inocente-sin-cos | RamaMusic | — | -97.544 | -100.458 | 0.0% | -104.0 | -83.0 | 1000 | +0.116 |
| R | naoagent-ensemble | naomicouriel | — | -97.548 | -100.312 | 0.0% | -104.0 | -83.0 | 1000 | +0.120 |
| 3 | leon-alderete | joaquinleondev | 15 | -97.549 | -100.408 | 0.0% | -104.0 | -83.0 | 1000 | +0.121 |
| 4 | gonzalezds | mariagonzalezdelsolar | 12 | -97.590 | -100.334 | 0.0% | -105.0 | -83.0 | 1000 | +0.162 |
| 5 | salim | athinasalimm | 10 | -97.613 | -100.276 | 0.0% | -104.0 | -83.0 | 1000 | +0.185 |
| 6 | ivan-de-pineda-101 | RamaMusic | 8 | -97.736 | -100.750 | 0.0% | -104.0 | -83.0 | 1000 | +0.308 |
| R | Alan-Schadan | Alanschad | — | -97.754 | -100.498 | 0.0% | -104.0 | -83.0 | 1000 | +0.326 |
| 7 | agusamblard | agusamblard | 6 | -97.756 | -100.484 | 0.0% | -105.0 | -83.0 | 1000 | +0.328 |
| R | ivan-de-pineda-102 | RamaMusic | — | -97.776 | -100.806 | 0.0% | -104.0 | -83.0 | 1000 | +0.348 |
| 8 | frangiavarini-exp12 | frangiavarini | 4 | -97.904 | -100.918 | 0.0% | -104.0 | -83.0 | 1000 | +0.476 |
| R | tomasbenavidez | tomasbenavidez | — | -97.911 | -100.694 | 0.0% | -104.0 | -83.0 | 1000 | +0.483 |
| 9 | Meteoro | FacundoFirpo | 2 | -97.934 | -100.976 | 0.0% | -104.0 | -83.0 | 1000 | +0.506 |
| 10 | jazgeller | jazgeller | 1 | -97.958 | -100.822 | 0.0% | -108.0 | -83.0 | 1000 | +0.530 |
| R | DeCruz_v2 | BrunoDC-dev | — | -98.071 | -100.854 | 0.0% | -107.0 | -84.0 | 1000 | +0.643 |
| 11 | fium-V3 | tomasbenavidez | 0 | -98.177 | -100.828 | 0.0% | -105.0 | -83.0 | 1000 | +0.749 |
| 12 | martin-bianchi | martinbianchi0 | 0 | -98.282 | -100.826 | 0.0% | -106.0 | -83.0 | 1000 | +0.854 |
| 13 | viaggio | FelipeViaggioFL | 0 | -98.343 | -101.658 | 0.0% | -104.0 | -83.0 | 1000 | +0.915 |
| R | bravo-andres-r1 | Andresbravo9 | — | -98.423 | -101.828 | 0.0% | -104.0 | -83.0 | 1000 | +0.995 |
| R | ivan-de-pineda-105 | RamaMusic | — | -98.508 | -102.030 | 0.0% | -104.0 | -83.0 | 1000 | +1.080 |
| R | ivan-de-pineda-106 | RamaMusic | — | -98.579 | -102.020 | 0.0% | -105.0 | -83.0 | 1000 | +1.151 |
| 14 | sgroba | Santi2065 | 0 | -98.663 | -101.698 | 0.0% | -106.0 | -83.0 | 1000 | +1.235 |
| R | ivan-de-pineda-103 | RamaMusic | — | -98.782 | -102.210 | 0.0% | -105.0 | -83.0 | 1000 | +1.354 |
| 15 | DeCruz | BrunoDC-dev | 0 | -98.927 | -102.420 | 0.0% | -104.0 | -83.0 | 1000 | +1.499 |
| R | tomas-castro-equilibrado | tommycass | — | -99.025 | -102.460 | 0.0% | -106.0 | -83.0 | 1000 | +1.597 |
| 16 | sb3zoo | Gabo-Tor | 0 | -99.114 | -101.784 | 0.0% | -108.0 | -84.0 | 1000 | +1.686 |
| 17 | bravo-andres | Andresbravo9 | 0 | -99.174 | -102.912 | 0.0% | -104.0 | -83.0 | 1000 | +1.746 |
| R | bravo-andres-r2 | Andresbravo9 | — | -99.185 | -102.602 | 0.0% | -107.0 | -83.0 | 1000 | +1.757 |
| R | domabot | Sdomato | — | -99.252 | -101.780 | 0.0% | -106.0 | -84.0 | 1000 | +1.824 |
| 18 | matbr | mateobramer | 0 | -99.276 | -102.014 | 0.0% | -106.0 | -84.0 | 1000 | +1.848 |
| R | ivan-de-pineda-104 | RamaMusic | — | -99.307 | -103.018 | 0.0% | -106.0 | -83.0 | 1000 | +1.879 |
| 19 | domabot2 | Sdomato | 0 | -99.526 | -103.570 | 0.0% | -104.0 | -84.0 | 1000 | +2.098 |
| R | naoagent | naomicouriel | — | -99.560 | -103.346 | 0.0% | -105.0 | -83.0 | 1000 | +2.132 |
| R | ivan-de-pineda-107 | RamaMusic | — | -99.620 | -103.046 | 0.0% | -107.0 | -83.0 | 1000 | +2.192 |
| 20 | Franco-Colapinto | famatodlr | 0 | -99.734 | -103.508 | 0.0% | -107.0 | -83.0 | 1000 | +2.306 |
| 21 | tomas-castro | tommycass | 0 | -100.025 | -100.934 | 0.0% | -147.0 | -83.0 | 1000 | +2.597 |
| R | lein | matilein | — | -100.036 | -103.614 | 0.0% | -105.0 | -84.0 | 1000 | +2.608 |
| R | fium-V1 | tomasbenavidez | — | -100.090 | -102.276 | 0.0% | -127.0 | -84.0 | 1000 | +2.662 |
| R | fium-V4 | tomasbenavidez | — | -100.277 | -103.484 | 0.0% | -105.0 | -83.0 | 1000 | +2.849 |
| 22 | valentino-pettazi | ValenPettaz1 | 0 | -100.304 | -103.054 | 0.0% | -105.0 | -83.0 | 1000 | +2.876 |
| 23 | maxi | maxividela2577 | 0 | -100.353 | -104.166 | 0.0% | -107.0 | -84.0 | 1000 | +2.925 |
| 24 | mateofreire | mateofreire | 0 | -100.362 | -103.408 | 0.0% | -110.0 | -85.0 | 1000 | +2.934 |
| 25 | Alan-Schadan-v2 | Alanschad | 0 | -100.745 | -103.642 | 0.0% | -105.0 | -83.0 | 1000 | +3.317 |
| 26 | zoffi | florzoffi | 0 | -101.328 | -103.064 | 0.0% | -111.0 | -83.0 | 1000 | +3.900 |
| R | fium-V2 | tomasbenavidez | — | -102.789 | -104.438 | 0.0% | -106.0 | -84.0 | 1000 | +5.361 |
| 27 | joaco-di-cola | joaco1212004 | 0 | -102.982 | -107.744 | 0.0% | -109.0 | -83.0 | 1000 | +5.554 |
| 28 | valeriano | Isivaleriano | 0 | -104.107 | -106.666 | 0.0% | -113.0 | -84.0 | 1000 | +6.679 |
| R | lein3 | matilein | — | -104.276 | -101.390 | 0.0% | -171.0 | -83.0 | 1000 | +6.848 |
| 29 | lein2 | matilein | 0 | -104.545 | -101.626 | 0.3% | -200.0 | -83.0 | 1000 | +7.117 |
| 30 | auto-cipre | CiprianoOss | 0 | -109.595 | -108.150 | 0.0% | -156.0 | -83.0 | 1000 | +12.167 |
| 31 | ion_h_RL_TP2 | 72Ion | 0 | -144.008 | -136.444 | 0.4% | -200.0 | -126.0 | 1000 | +46.580 |

## GP Largada libre

_Largan desde cualquier punto de la pista y con velocidad inicial._

| # | Auto | Escudería | Pts | Media | IQM | Sin llegar | Min | Max | Episodios | Dif. al 1° |
|---|------|-----------|----:|-------|-----|-----------:|-----|-----|-----------|-----------|
| 1 | DeCruz | BrunoDC-dev | 25 | -57.175 | -58.862 | 0.0% | -119.0 | -3.0 | 1000 | — |
| 2 | vanafa | VANAFA | 18 | -57.351 | -59.018 | 0.0% | -141.0 | -3.0 | 1000 | +0.176 |
| 3 | salim | athinasalimm | 15 | -57.393 | -58.892 | 0.0% | -142.0 | -3.0 | 1000 | +0.218 |
| R | bravo-andres-r2 | Andresbravo9 | — | -57.418 | -58.916 | 0.0% | -136.0 | -3.0 | 1000 | +0.243 |
| 4 | tomas-castro | tommycass | 12 | -57.466 | -58.982 | 0.0% | -143.0 | -3.0 | 1000 | +0.291 |
| R | bravo-andres-r1 | Andresbravo9 | — | -57.496 | -59.020 | 0.0% | -152.0 | -3.0 | 1000 | +0.321 |
| R | naoagent | naomicouriel | — | -57.585 | -58.898 | 0.0% | -163.0 | -3.0 | 1000 | +0.410 |
| 5 | Alan-Schadan-v2 | Alanschad | 10 | -57.654 | -59.382 | 0.0% | -119.0 | -3.0 | 1000 | +0.479 |
| R | DeCruz_v2 | BrunoDC-dev | — | -57.695 | -59.052 | 0.0% | -147.0 | -3.0 | 1000 | +0.520 |
| 6 | bravo-andres | Andresbravo9 | 8 | -57.696 | -59.090 | 0.0% | -154.0 | -3.0 | 1000 | +0.521 |
| R | naoagent-ensemble | naomicouriel | — | -57.720 | -58.972 | 0.0% | -149.0 | -3.0 | 1000 | +0.545 |
| 7 | frangiavarini-exp12 | frangiavarini | 6 | -57.728 | -59.366 | 0.0% | -115.0 | -3.0 | 1000 | +0.553 |
| R | fium-V4 | tomasbenavidez | — | -57.747 | -59.064 | 0.0% | -132.0 | -3.0 | 1000 | +0.572 |
| 8 | sb3zoo | Gabo-Tor | 4 | -57.810 | -59.354 | 0.0% | -129.0 | -3.0 | 1000 | +0.635 |
| 9 | Franco-Colapinto | famatodlr | 2 | -57.829 | -59.186 | 0.0% | -142.0 | -3.0 | 1000 | +0.654 |
| R | ivan-de-pineda-107 | RamaMusic | — | -57.837 | -59.074 | 0.0% | -152.0 | -3.0 | 1000 | +0.662 |
| R | tomas-castro-equilibrado | tommycass | — | -57.837 | -59.008 | 0.0% | -154.0 | -3.0 | 1000 | +0.662 |
| R | Alan-Schadan | Alanschad | — | -57.841 | -59.452 | 0.0% | -186.0 | -3.0 | 1000 | +0.666 |
| R | ivan-de-pineda-es-inocente-con-features | RamaMusic | — | -57.895 | -59.186 | 0.0% | -176.0 | -3.0 | 1000 | +0.720 |
| R | ivan-de-pineda-105 | RamaMusic | — | -57.929 | -58.962 | 0.0% | -160.0 | -3.0 | 1000 | +0.754 |
| R | ivan-de-pineda-104 | RamaMusic | — | -58.006 | -58.950 | 0.0% | -167.0 | -3.0 | 1000 | +0.831 |
| R | ivan-de-pineda-es-inocente-sin-cos | RamaMusic | — | -58.014 | -59.360 | 0.0% | -151.0 | -3.0 | 1000 | +0.839 |
| R | ivan-de-pineda-103 | RamaMusic | — | -58.019 | -58.990 | 0.0% | -169.0 | -3.0 | 1000 | +0.844 |
| R | ivan-de-pineda-106 | RamaMusic | — | -58.023 | -59.138 | 0.0% | -155.0 | -3.0 | 1000 | +0.848 |
| 10 | ivan-de-pineda-101 | RamaMusic | 1 | -58.043 | -59.416 | 0.0% | -155.0 | -3.0 | 1000 | +0.868 |
| R | lein3 | matilein | — | -58.114 | -59.438 | 0.0% | -149.0 | -3.0 | 1000 | +0.939 |
| 11 | lein2 | matilein | 0 | -58.148 | -59.228 | 0.0% | -187.0 | -3.0 | 1000 | +0.973 |
| R | naoagent-greedy | naomicouriel | — | -58.228 | -59.064 | 0.0% | -182.0 | -3.0 | 1000 | +1.053 |
| 12 | gonzalezds | mariagonzalezdelsolar | 0 | -58.248 | -60.034 | 0.0% | -152.0 | -3.0 | 1000 | +1.073 |
| R | ivan-de-pineda-es-inocente-sin-features | RamaMusic | — | -58.294 | -59.248 | 0.0% | -186.0 | -3.0 | 1000 | +1.119 |
| R | ivan-de-pineda-102 | RamaMusic | — | -58.301 | -59.080 | 0.0% | -181.0 | -3.0 | 1000 | +1.126 |
| 13 | valentino-pettazi | ValenPettaz1 | 0 | -58.336 | -59.816 | 0.0% | -149.0 | -3.0 | 1000 | +1.161 |
| R | fium-V1 | tomasbenavidez | — | -58.741 | -59.766 | 0.0% | -161.0 | -3.0 | 1000 | +1.566 |
| R | naoagent-greedy3 | naomicouriel | — | -58.917 | -60.364 | 0.0% | -152.0 | -3.0 | 1000 | +1.742 |
| 14 | mateofreire | mateofreire | 0 | -58.970 | -59.452 | 0.0% | -196.0 | -3.0 | 1000 | +1.795 |
| 15 | agusamblard | agusamblard | 0 | -59.257 | -60.216 | 0.0% | -165.0 | -3.0 | 1000 | +2.082 |
| 16 | leon-alderete | joaquinleondev | 0 | -59.310 | -60.590 | 0.0% | -179.0 | -3.0 | 1000 | +2.135 |
| 17 | naoagent-greedy2 | naomicouriel | 0 | -59.333 | -60.468 | 0.0% | -161.0 | -3.0 | 1000 | +2.158 |
| R | tomasbenavidez | tomasbenavidez | — | -59.372 | -59.928 | 0.0% | -157.0 | -3.0 | 1000 | +2.197 |
| 18 | fium-V3 | tomasbenavidez | 0 | -59.419 | -60.222 | 0.0% | -160.0 | -3.0 | 1000 | +2.244 |
| 19 | domabot2 | Sdomato | 0 | -59.642 | -61.210 | 0.0% | -160.0 | -3.0 | 1000 | +2.467 |
| 20 | matbr | mateobramer | 0 | -59.704 | -61.216 | 0.0% | -129.0 | -3.0 | 1000 | +2.529 |
| R | lein | matilein | — | -59.877 | -60.294 | 0.0% | -180.0 | -3.0 | 1000 | +2.702 |
| 21 | sgroba | Santi2065 | 0 | -60.074 | -59.796 | 0.0% | -161.0 | -3.0 | 1000 | +2.899 |
| 22 | auto-cipre | CiprianoOss | 0 | -60.302 | -61.328 | 0.0% | -148.0 | -3.0 | 1000 | +3.127 |
| 23 | jazgeller | jazgeller | 0 | -60.339 | -61.520 | 0.0% | -162.0 | -3.0 | 1000 | +3.164 |
| 24 | Meteoro | FacundoFirpo | 0 | -60.682 | -62.440 | 0.0% | -171.0 | -3.0 | 1000 | +3.507 |
| 25 | martin-bianchi | martinbianchi0 | 0 | -61.128 | -62.554 | 0.0% | -145.0 | -3.0 | 1000 | +3.953 |
| 26 | maxi | maxividela2577 | 0 | -61.359 | -63.004 | 0.0% | -172.0 | -3.0 | 1000 | +4.184 |
| 27 | valeriano | Isivaleriano | 0 | -61.487 | -61.228 | 0.0% | -188.0 | -3.0 | 1000 | +4.312 |
| 28 | viaggio | FelipeViaggioFL | 0 | -63.259 | -65.332 | 0.0% | -170.0 | -3.0 | 1000 | +6.084 |
| R | fium-V2 | tomasbenavidez | — | -63.521 | -65.594 | 0.0% | -167.0 | -3.0 | 1000 | +6.346 |
| 29 | joaco-di-cola | joaco1212004 | 0 | -65.656 | -67.556 | 0.0% | -199.0 | -3.0 | 1000 | +8.481 |
| 30 | zoffi | florzoffi | 0 | -65.818 | -66.818 | 0.1% | -200.0 | -3.0 | 1000 | +8.643 |
| R | domabot | Sdomato | — | -67.175 | -69.610 | 0.0% | -167.0 | -3.0 | 1000 | +10.000 |
| 31 | ion_h_RL_TP2 | 72Ion | 0 | -80.179 | -78.134 | 0.0% | -199.0 | -3.0 | 1000 | +23.004 |

## GP Lluvia

_Sensores con ruido gaussiano en posición y velocidad._

| # | Auto | Escudería | Pts | Media | IQM | Sin llegar | Min | Max | Episodios | Dif. al 1° |
|---|------|-----------|----:|-------|-----|-----------:|-----|-----|-----------|-----------|
| R | ivan-de-pineda-106 | RamaMusic | — | -99.960 | -102.236 | 0.0% | -169.0 | -83.0 | 1000 | −0.611 |
| R | ivan-de-pineda-105 | RamaMusic | — | -100.152 | -102.388 | 0.0% | -176.0 | -83.0 | 1000 | −0.419 |
| R | ivan-de-pineda-102 | RamaMusic | — | -100.277 | -101.974 | 0.0% | -176.0 | -83.0 | 1000 | −0.294 |
| R | ivan-de-pineda-103 | RamaMusic | — | -100.382 | -102.450 | 0.0% | -172.0 | -83.0 | 1000 | −0.189 |
| R | tomas-castro-equilibrado | tommycass | — | -100.485 | -102.648 | 0.0% | -175.0 | -83.0 | 1000 | −0.086 |
| R | lein | matilein | — | -100.563 | -103.400 | 0.0% | -186.0 | -83.0 | 1000 | −0.008 |
| 1 | ivan-de-pineda-101 | RamaMusic | 25 | -100.571 | -101.786 | 0.0% | -173.0 | -83.0 | 1000 | — |
| R | ivan-de-pineda-104 | RamaMusic | — | -100.616 | -102.922 | 0.0% | -173.0 | -83.0 | 1000 | +0.045 |
| R | naoagent | naomicouriel | — | -101.021 | -103.266 | 0.0% | -174.0 | -83.0 | 1000 | +0.450 |
| 2 | fium-V3 | tomasbenavidez | 18 | -101.088 | -102.022 | 0.0% | -186.0 | -83.0 | 1000 | +0.517 |
| 3 | bravo-andres | Andresbravo9 | 15 | -101.102 | -102.880 | 0.0% | -162.0 | -83.0 | 1000 | +0.531 |
| R | naoagent-greedy | naomicouriel | — | -101.103 | -101.656 | 0.0% | -179.0 | -83.0 | 1000 | +0.532 |
| 4 | domabot2 | Sdomato | 12 | -101.321 | -103.686 | 0.0% | -178.0 | -83.0 | 1000 | +0.750 |
| R | ivan-de-pineda-107 | RamaMusic | — | -101.429 | -103.294 | 0.0% | -188.0 | -83.0 | 1000 | +0.858 |
| 5 | valentino-pettazi | ValenPettaz1 | 10 | -101.441 | -103.492 | 0.0% | -160.0 | -83.0 | 1000 | +0.870 |
| R | naoagent-ensemble | naomicouriel | — | -101.768 | -101.994 | 0.0% | -189.0 | -83.0 | 1000 | +1.197 |
| R | ivan-de-pineda-es-inocente-sin-cos | RamaMusic | — | -101.808 | -102.138 | 0.0% | -189.0 | -83.0 | 1000 | +1.237 |
| R | ivan-de-pineda-es-inocente-sin-features | RamaMusic | — | -101.885 | -101.772 | 0.0% | -186.0 | -83.0 | 1000 | +1.314 |
| R | bravo-andres-r1 | Andresbravo9 | — | -102.105 | -102.678 | 0.0% | -167.0 | -83.0 | 1000 | +1.534 |
| R | naoagent-greedy3 | naomicouriel | — | -102.200 | -101.928 | 0.0% | -174.0 | -83.0 | 1000 | +1.629 |
| R | ivan-de-pineda-es-inocente-con-features | RamaMusic | — | -102.255 | -101.862 | 0.0% | -183.0 | -83.0 | 1000 | +1.684 |
| 6 | leon-alderete | joaquinleondev | 8 | -102.486 | -102.160 | 0.0% | -183.0 | -83.0 | 1000 | +1.915 |
| 7 | joaco-di-cola | joaco1212004 | 6 | -103.230 | -105.882 | 0.0% | -192.0 | -83.0 | 1000 | +2.659 |
| 7 | naoagent-greedy2 | naomicouriel | 6 | -103.230 | -102.098 | 0.0% | -177.0 | -83.0 | 1000 | +2.659 |
| 9 | Franco-Colapinto | famatodlr | 2 | -103.258 | -103.960 | 0.0% | -167.0 | -83.0 | 1000 | +2.687 |
| R | bravo-andres-r2 | Andresbravo9 | — | -103.324 | -103.756 | 0.0% | -166.0 | -83.0 | 1000 | +2.753 |
| 10 | mateofreire | mateofreire | 1 | -103.743 | -104.048 | 0.0% | -167.0 | -84.0 | 1000 | +3.172 |
| 11 | maxi | maxividela2577 | 0 | -103.774 | -104.896 | 0.0% | -194.0 | -84.0 | 1000 | +3.203 |
| 12 | DeCruz | BrunoDC-dev | 0 | -103.804 | -103.392 | 0.0% | -176.0 | -83.0 | 1000 | +3.233 |
| 13 | Alan-Schadan-v2 | Alanschad | 0 | -104.049 | -103.880 | 0.0% | -171.0 | -83.0 | 1000 | +3.478 |
| 14 | zoffi | florzoffi | 0 | -104.280 | -105.628 | 0.0% | -182.0 | -83.0 | 1000 | +3.709 |
| 15 | jazgeller | jazgeller | 0 | -104.373 | -104.084 | 0.0% | -182.0 | -83.0 | 1000 | +3.802 |
| R | DeCruz_v2 | BrunoDC-dev | — | -104.736 | -102.696 | 0.0% | -180.0 | -83.0 | 1000 | +4.165 |
| 16 | sgroba | Santi2065 | 0 | -104.912 | -103.818 | 0.2% | -200.0 | -83.0 | 1000 | +4.341 |
| R | fium-V4 | tomasbenavidez | — | -105.019 | -104.376 | 0.0% | -176.0 | -83.0 | 1000 | +4.448 |
| R | tomasbenavidez | tomasbenavidez | — | -105.572 | -102.982 | 0.0% | -199.0 | -83.0 | 1000 | +5.001 |
| 17 | agusamblard | agusamblard | 0 | -105.586 | -103.796 | 0.0% | -197.0 | -83.0 | 1000 | +5.015 |
| 18 | martin-bianchi | martinbianchi0 | 0 | -106.083 | -104.532 | 0.1% | -200.0 | -83.0 | 1000 | +5.512 |
| 19 | salim | athinasalimm | 0 | -106.224 | -102.868 | 0.0% | -183.0 | -83.0 | 1000 | +5.653 |
| 20 | frangiavarini-exp12 | frangiavarini | 0 | -106.306 | -103.634 | 0.0% | -182.0 | -83.0 | 1000 | +5.735 |
| 21 | vanafa | VANAFA | 0 | -106.377 | -102.934 | 0.0% | -172.0 | -83.0 | 1000 | +5.806 |
| 22 | tomas-castro | tommycass | 0 | -106.729 | -102.804 | 0.0% | -171.0 | -83.0 | 1000 | +6.158 |
| 23 | valeriano | Isivaleriano | 0 | -106.790 | -107.256 | 0.7% | -200.0 | -84.0 | 1000 | +6.219 |
| R | fium-V1 | tomasbenavidez | — | -107.063 | -103.426 | 0.0% | -196.0 | -84.0 | 1000 | +6.492 |
| 24 | gonzalezds | mariagonzalezdelsolar | 0 | -107.371 | -102.788 | 0.0% | -170.0 | -83.0 | 1000 | +6.800 |
| R | lein3 | matilein | — | -107.460 | -102.700 | 0.0% | -173.0 | -83.0 | 1000 | +6.889 |
| R | Alan-Schadan | Alanschad | — | -107.569 | -103.778 | 0.0% | -176.0 | -83.0 | 1000 | +6.998 |
| 25 | lein2 | matilein | 0 | -107.947 | -103.168 | 0.0% | -160.0 | -83.0 | 1000 | +7.376 |
| 26 | sb3zoo | Gabo-Tor | 0 | -108.171 | -105.530 | 0.2% | -200.0 | -83.0 | 1000 | +7.600 |
| 27 | viaggio | FelipeViaggioFL | 0 | -108.386 | -103.134 | 0.0% | -188.0 | -83.0 | 1000 | +7.815 |
| R | fium-V2 | tomasbenavidez | — | -109.136 | -105.960 | 0.1% | -200.0 | -84.0 | 1000 | +8.565 |
| 28 | Meteoro | FacundoFirpo | 0 | -110.196 | -104.878 | 0.1% | -200.0 | -83.0 | 1000 | +9.625 |
| 29 | matbr | mateobramer | 0 | -110.346 | -106.632 | 0.0% | -183.0 | -83.0 | 1000 | +9.775 |
| R | domabot | Sdomato | — | -111.638 | -105.518 | 0.3% | -200.0 | -83.0 | 1000 | +11.067 |
| 30 | auto-cipre | CiprianoOss | 0 | -116.572 | -112.482 | 0.0% | -174.0 | -83.0 | 1000 | +16.001 |
| 31 | ion_h_RL_TP2 | 72Ion | 0 | -148.168 | -140.578 | 4.1% | -200.0 | -125.0 | 1000 | +47.597 |

## GP Motor débil

_El motor rinde entre 8% y 12% menos._

| # | Auto | Escudería | Pts | Media | IQM | Sin llegar | Min | Max | Episodios | Dif. al 1° |
|---|------|-----------|----:|-------|-----|-----------:|-----|-----|-----------|-----------|
| R | fium-V2 | tomasbenavidez | — | -110.867 | -111.010 | 0.0% | -125.0 | -92.0 | 1000 | −1.411 |
| 1 | Alan-Schadan-v2 | Alanschad | 25 | -112.278 | -111.942 | 0.1% | -200.0 | -92.0 | 1000 | — |
| 2 | valentino-pettazi | ValenPettaz1 | 18 | -112.549 | -110.862 | 0.0% | -171.0 | -92.0 | 1000 | +0.271 |
| R | naoagent | naomicouriel | — | -114.634 | -110.542 | 0.4% | -200.0 | -92.0 | 1000 | +2.356 |
| 3 | DeCruz | BrunoDC-dev | 15 | -115.643 | -111.288 | 0.2% | -200.0 | -92.0 | 1000 | +3.365 |
| 4 | bravo-andres | Andresbravo9 | 12 | -115.661 | -110.922 | 0.0% | -190.0 | -92.0 | 1000 | +3.383 |
| 5 | Franco-Colapinto | famatodlr | 10 | -116.096 | -111.902 | 0.0% | -182.0 | -92.0 | 1000 | +3.818 |
| R | lein | matilein | — | -116.266 | -110.862 | 0.2% | -200.0 | -92.0 | 1000 | +3.988 |
| R | fium-V4 | tomasbenavidez | — | -116.694 | -112.252 | 0.4% | -200.0 | -93.0 | 1000 | +4.416 |
| R | bravo-andres-r1 | Andresbravo9 | — | -116.829 | -111.446 | 0.0% | -193.0 | -92.0 | 1000 | +4.551 |
| R | bravo-andres-r2 | Andresbravo9 | — | -116.930 | -111.028 | 0.0% | -182.0 | -92.0 | 1000 | +4.652 |
| R | tomas-castro-equilibrado | tommycass | — | -117.999 | -110.830 | 0.1% | -200.0 | -92.0 | 1000 | +5.721 |
| R | ivan-de-pineda-107 | RamaMusic | — | -118.047 | -110.864 | 0.0% | -195.0 | -92.0 | 1000 | +5.769 |
| R | ivan-de-pineda-106 | RamaMusic | — | -118.243 | -110.816 | 0.2% | -200.0 | -92.0 | 1000 | +5.965 |
| R | ivan-de-pineda-104 | RamaMusic | — | -118.274 | -110.740 | 0.3% | -200.0 | -92.0 | 1000 | +5.996 |
| R | ivan-de-pineda-105 | RamaMusic | — | -118.723 | -111.188 | 0.3% | -200.0 | -92.0 | 1000 | +6.445 |
| 6 | domabot2 | Sdomato | 8 | -118.738 | -111.758 | 0.2% | -200.0 | -92.0 | 1000 | +6.460 |
| R | ivan-de-pineda-103 | RamaMusic | — | -118.976 | -110.844 | 0.3% | -200.0 | -92.0 | 1000 | +6.698 |
| 7 | maxi | maxividela2577 | 6 | -119.282 | -112.610 | 0.4% | -200.0 | -93.0 | 1000 | +7.004 |
| 8 | joaco-di-cola | joaco1212004 | 4 | -119.523 | -113.392 | 2.2% | -200.0 | -92.0 | 1000 | +7.245 |
| 9 | ivan-de-pineda-101 | RamaMusic | 2 | -120.693 | -113.274 | 0.3% | -200.0 | -92.0 | 1000 | +8.415 |
| 10 | zoffi | florzoffi | 1 | -121.367 | -114.872 | 7.1% | -200.0 | -92.0 | 1000 | +9.089 |
| 11 | mateofreire | mateofreire | 0 | -122.323 | -112.370 | 1.0% | -200.0 | -92.0 | 1000 | +10.045 |
| 12 | tomas-castro | tommycass | 0 | -122.620 | -118.376 | 0.0% | -193.0 | -92.0 | 1000 | +10.342 |
| R | naoagent-ensemble | naomicouriel | — | -123.640 | -117.036 | 0.2% | -200.0 | -92.0 | 1000 | +11.362 |
| R | ivan-de-pineda-102 | RamaMusic | — | -123.804 | -114.862 | 2.2% | -200.0 | -92.0 | 1000 | +11.526 |
| 13 | sgroba | Santi2065 | 0 | -124.057 | -113.460 | 1.6% | -200.0 | -93.0 | 1000 | +11.779 |
| 14 | frangiavarini-exp12 | frangiavarini | 0 | -124.562 | -115.994 | 1.4% | -200.0 | -93.0 | 1000 | +12.284 |
| 15 | salim | athinasalimm | 0 | -125.186 | -119.948 | 0.0% | -195.0 | -93.0 | 1000 | +12.908 |
| R | ivan-de-pineda-es-inocente-sin-features | RamaMusic | — | -125.251 | -117.268 | 2.9% | -200.0 | -92.0 | 1000 | +12.973 |
| 16 | viaggio | FelipeViaggioFL | 0 | -125.442 | -114.484 | 0.2% | -200.0 | -94.0 | 1000 | +13.164 |
| 17 | lein2 | matilein | 0 | -126.332 | -123.906 | 0.0% | -193.0 | -92.0 | 1000 | +14.054 |
| 18 | vanafa | VANAFA | 0 | -126.354 | -120.288 | 0.5% | -200.0 | -93.0 | 1000 | +14.076 |
| 19 | auto-cipre | CiprianoOss | 0 | -126.476 | -122.788 | 0.0% | -154.0 | -99.0 | 1000 | +14.198 |
| R | Alan-Schadan | Alanschad | — | -126.532 | -119.804 | 0.7% | -200.0 | -93.0 | 1000 | +14.254 |
| R | ivan-de-pineda-es-inocente-con-features | RamaMusic | — | -126.765 | -119.776 | 1.5% | -200.0 | -92.0 | 1000 | +14.487 |
| R | naoagent-greedy3 | naomicouriel | — | -126.967 | -121.108 | 0.9% | -200.0 | -92.0 | 1000 | +14.689 |
| 20 | valeriano | Isivaleriano | 0 | -127.281 | -114.172 | 3.9% | -200.0 | -102.0 | 1000 | +15.003 |
| 21 | jazgeller | jazgeller | 0 | -127.327 | -120.268 | 0.1% | -200.0 | -93.0 | 1000 | +15.049 |
| R | ivan-de-pineda-es-inocente-sin-cos | RamaMusic | — | -127.381 | -120.494 | 0.8% | -200.0 | -92.0 | 1000 | +15.103 |
| R | lein3 | matilein | — | -127.464 | -126.000 | 0.0% | -192.0 | -92.0 | 1000 | +15.186 |
| 22 | gonzalezds | mariagonzalezdelsolar | 0 | -127.507 | -123.486 | 0.0% | -186.0 | -93.0 | 1000 | +15.229 |
| 23 | naoagent-greedy2 | naomicouriel | 0 | -128.727 | -122.904 | 0.9% | -200.0 | -92.0 | 1000 | +16.449 |
| 24 | leon-alderete | joaquinleondev | 0 | -129.705 | -122.852 | 2.3% | -200.0 | -93.0 | 1000 | +17.427 |
| 25 | fium-V3 | tomasbenavidez | 0 | -130.158 | -122.592 | 0.4% | -200.0 | -92.0 | 1000 | +17.880 |
| R | naoagent-greedy | naomicouriel | — | -130.435 | -123.528 | 1.9% | -200.0 | -93.0 | 1000 | +18.157 |
| 26 | Meteoro | FacundoFirpo | 0 | -130.904 | -120.308 | 6.0% | -200.0 | -93.0 | 1000 | +18.626 |
| R | DeCruz_v2 | BrunoDC-dev | — | -132.224 | -129.800 | 0.4% | -200.0 | -92.0 | 1000 | +19.946 |
| 27 | agusamblard | agusamblard | 0 | -133.343 | -125.230 | 4.9% | -200.0 | -93.0 | 1000 | +21.065 |
| 28 | sb3zoo | Gabo-Tor | 0 | -133.939 | -128.688 | 0.6% | -200.0 | -93.0 | 1000 | +21.661 |
| R | tomasbenavidez | tomasbenavidez | — | -134.285 | -128.850 | 1.6% | -200.0 | -93.0 | 1000 | +22.007 |
| 29 | martin-bianchi | martinbianchi0 | 0 | -135.643 | -130.480 | 0.3% | -200.0 | -94.0 | 1000 | +23.365 |
| R | domabot | Sdomato | — | -138.948 | -133.360 | 0.6% | -200.0 | -111.0 | 1000 | +26.670 |
| 30 | matbr | mateobramer | 0 | -140.219 | -136.596 | 0.2% | -200.0 | -99.0 | 1000 | +27.941 |
| R | fium-V1 | tomasbenavidez | — | -140.761 | -142.958 | 0.7% | -200.0 | -92.0 | 1000 | +28.483 |
| 31 | ion_h_RL_TP2 | 72Ion | 0 | -154.574 | -147.024 | 10.1% | -200.0 | -134.0 | 1000 | +42.296 |

## GP Otra pista

_La montaña cambia de forma: cos(f·x) con f entre 2.6 y 2.8 (en vez de 3)._

| # | Auto | Escudería | Pts | Media | IQM | Sin llegar | Min | Max | Episodios | Dif. al 1° |
|---|------|-----------|----:|-------|-----|-----------:|-----|-----|-----------|-----------|
| 1 | lein2 | matilein | 25 | -95.981 | -96.168 | 0.0% | -109.0 | -82.0 | 1000 | — |
| R | lein3 | matilein | — | -96.393 | -96.448 | 0.0% | -113.0 | -83.0 | 1000 | +0.412 |
| R | fium-V1 | tomasbenavidez | — | -97.121 | -97.652 | 0.0% | -111.0 | -83.0 | 1000 | +1.140 |
| 2 | tomas-castro | tommycass | 18 | -97.286 | -98.346 | 0.0% | -110.0 | -82.0 | 1000 | +1.305 |
| R | DeCruz_v2 | BrunoDC-dev | — | -97.651 | -99.442 | 0.0% | -109.0 | -82.0 | 1000 | +1.670 |
| 3 | fium-V3 | tomasbenavidez | 15 | -98.192 | -100.480 | 0.0% | -110.0 | -82.0 | 1000 | +2.211 |
| 4 | naoagent-greedy2 | naomicouriel | 12 | -98.919 | -101.578 | 0.0% | -109.0 | -82.0 | 1000 | +2.938 |
| 5 | gonzalezds | mariagonzalezdelsolar | 10 | -98.962 | -100.764 | 0.0% | -112.0 | -83.0 | 1000 | +2.981 |
| R | ivan-de-pineda-es-inocente-sin-cos | RamaMusic | — | -99.134 | -102.084 | 0.0% | -109.0 | -82.0 | 1000 | +3.153 |
| R | naoagent-greedy3 | naomicouriel | — | -99.197 | -101.904 | 0.0% | -110.0 | -82.0 | 1000 | +3.216 |
| 6 | leon-alderete | joaquinleondev | 8 | -99.202 | -101.910 | 0.0% | -110.0 | -82.0 | 1000 | +3.221 |
| R | ivan-de-pineda-102 | RamaMusic | — | -99.342 | -102.606 | 0.0% | -110.0 | -82.0 | 1000 | +3.361 |
| R | naoagent-greedy | naomicouriel | — | -99.366 | -102.134 | 0.0% | -109.0 | -82.0 | 1000 | +3.385 |
| R | ivan-de-pineda-es-inocente-sin-features | RamaMusic | — | -99.473 | -102.166 | 0.0% | -111.0 | -82.0 | 1000 | +3.492 |
| R | ivan-de-pineda-es-inocente-con-features | RamaMusic | — | -99.569 | -102.144 | 0.0% | -111.0 | -83.0 | 1000 | +3.588 |
| R | tomasbenavidez | tomasbenavidez | — | -100.060 | -102.298 | 0.0% | -122.0 | -83.0 | 1000 | +4.079 |
| 7 | vanafa | VANAFA | 6 | -100.162 | -102.492 | 0.0% | -113.0 | -83.0 | 1000 | +4.181 |
| 8 | ivan-de-pineda-101 | RamaMusic | 4 | -100.175 | -103.304 | 0.0% | -111.0 | -82.0 | 1000 | +4.194 |
| 9 | frangiavarini-exp12 | frangiavarini | 2 | -100.200 | -103.320 | 0.0% | -111.0 | -83.0 | 1000 | +4.219 |
| R | naoagent-ensemble | naomicouriel | — | -100.460 | -103.536 | 0.0% | -111.0 | -82.0 | 1000 | +4.479 |
| 10 | Meteoro | FacundoFirpo | 1 | -100.551 | -103.898 | 0.0% | -111.0 | -83.0 | 1000 | +4.570 |
| 11 | mateofreire | mateofreire | 0 | -101.106 | -104.210 | 0.0% | -114.0 | -82.0 | 1000 | +5.125 |
| R | ivan-de-pineda-105 | RamaMusic | — | -101.108 | -105.178 | 0.0% | -111.0 | -82.0 | 1000 | +5.127 |
| R | Alan-Schadan | Alanschad | — | -101.159 | -103.448 | 0.0% | -114.0 | -83.0 | 1000 | +5.178 |
| 12 | viaggio | FelipeViaggioFL | 0 | -101.387 | -105.796 | 0.0% | -112.0 | -82.0 | 1000 | +5.406 |
| R | bravo-andres-r1 | Andresbravo9 | — | -101.458 | -105.860 | 0.0% | -112.0 | -82.0 | 1000 | +5.477 |
| 13 | auto-cipre | CiprianoOss | 0 | -101.474 | -103.940 | 0.0% | -117.0 | -82.0 | 1000 | +5.493 |
| R | ivan-de-pineda-106 | RamaMusic | — | -101.539 | -105.534 | 0.0% | -113.0 | -82.0 | 1000 | +5.558 |
| R | tomas-castro-equilibrado | tommycass | — | -101.662 | -105.994 | 0.0% | -113.0 | -82.0 | 1000 | +5.681 |
| R | ivan-de-pineda-103 | RamaMusic | — | -101.690 | -105.754 | 0.0% | -113.0 | -82.0 | 1000 | +5.709 |
| R | bravo-andres-r2 | Andresbravo9 | — | -101.889 | -106.284 | 0.0% | -112.0 | -82.0 | 1000 | +5.908 |
| R | ivan-de-pineda-107 | RamaMusic | — | -101.930 | -106.220 | 0.0% | -113.0 | -82.0 | 1000 | +5.949 |
| 14 | salim | athinasalimm | 0 | -102.124 | -104.612 | 0.0% | -144.0 | -84.0 | 1000 | +6.143 |
| 15 | jazgeller | jazgeller | 0 | -102.260 | -104.368 | 0.0% | -119.0 | -83.0 | 1000 | +6.279 |
| 16 | Franco-Colapinto | famatodlr | 0 | -102.281 | -107.276 | 0.0% | -114.0 | -82.0 | 1000 | +6.300 |
| R | ivan-de-pineda-104 | RamaMusic | — | -102.476 | -107.082 | 0.0% | -114.0 | -82.0 | 1000 | +6.495 |
| 17 | bravo-andres | Andresbravo9 | 0 | -102.733 | -107.488 | 0.0% | -114.0 | -82.0 | 1000 | +6.752 |
| 18 | domabot2 | Sdomato | 0 | -102.947 | -107.528 | 0.0% | -115.0 | -83.0 | 1000 | +6.966 |
| 19 | sgroba | Santi2065 | 0 | -102.965 | -105.862 | 0.0% | -117.0 | -83.0 | 1000 | +6.984 |
| 20 | maxi | maxividela2577 | 0 | -103.585 | -107.732 | 0.0% | -118.0 | -83.0 | 1000 | +7.604 |
| R | naoagent | naomicouriel | — | -103.726 | -108.442 | 0.0% | -115.0 | -82.0 | 1000 | +7.745 |
| R | lein | matilein | — | -104.051 | -108.690 | 0.0% | -115.0 | -83.0 | 1000 | +8.070 |
| 21 | DeCruz | BrunoDC-dev | 0 | -104.448 | -108.368 | 0.0% | -121.0 | -83.0 | 1000 | +8.467 |
| R | domabot | Sdomato | — | -104.832 | -108.060 | 0.0% | -121.0 | -83.0 | 1000 | +8.851 |
| 22 | agusamblard | agusamblard | 0 | -106.427 | -107.062 | 0.6% | -200.0 | -85.0 | 1000 | +10.446 |
| 23 | valeriano | Isivaleriano | 0 | -109.701 | -111.716 | 2.2% | -200.0 | -84.0 | 1000 | +13.720 |
| 24 | valentino-pettazi | ValenPettaz1 | 0 | -109.825 | -110.946 | 1.8% | -200.0 | -83.0 | 1000 | +13.844 |
| 25 | sb3zoo | Gabo-Tor | 0 | -111.205 | -112.318 | 0.7% | -200.0 | -83.0 | 1000 | +15.224 |
| 26 | zoffi | florzoffi | 0 | -111.519 | -109.972 | 4.8% | -200.0 | -83.0 | 1000 | +15.538 |
| 27 | martin-bianchi | martinbianchi0 | 0 | -112.161 | -110.708 | 0.1% | -200.0 | -86.0 | 1000 | +16.180 |
| R | fium-V4 | tomasbenavidez | — | -112.716 | -113.488 | 1.4% | -200.0 | -85.0 | 1000 | +16.735 |
| 28 | Alan-Schadan-v2 | Alanschad | 0 | -112.926 | -111.050 | 4.7% | -200.0 | -84.0 | 1000 | +16.945 |
| 29 | joaco-di-cola | joaco1212004 | 0 | -114.668 | -120.210 | 0.0% | -130.0 | -84.0 | 1000 | +18.687 |
| R | fium-V2 | tomasbenavidez | — | -128.591 | -113.772 | 19.5% | -200.0 | -83.0 | 1000 | +32.610 |
| 30 | matbr | mateobramer | 0 | -140.896 | -137.290 | 2.6% | -200.0 | -91.0 | 1000 | +44.915 |
| 31 | ion_h_RL_TP2 | 72Ion | 0 | -145.736 | -141.406 | 0.0% | -179.0 | -129.0 | 1000 | +49.755 |
