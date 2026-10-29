# 🏆 Leaderboard — Campeonato RL (DQN)

Entorno base: `MountainCar-v0` · 5 circuitos · Ranking por **MEDIA** en cada circuito · Actualizado: 2026-10-29 19:07 UTC

Puntos por circuito: 25, 18, 15, 12, 10, 8, 6, 4, 2, 1 (del 1° al 10°). La misma policy corre en todos los circuitos. Detalle de cada uno en el README.

**Un auto titular por escudería** (cuenta de GitHub): es el único que suma puntos y ocupa posiciones. Es el auto de la escudería que más puntos suma contra los titulares de las demás. El resto son autos de reserva: aparecen abajo, pero no le sacan puestos a nadie.

## 🏁 Campeonato

| # | Auto | Escudería | **Pts** | Estándar | Largada libre | Lluvia | Motor débil | Otra pista |
|---|------|-----------|-----:|:---:|:---:|:---:|:---:|:---:|
| 🥇 | vanafa | VANAFA | **60** | 1° (25) | 1° (25) | 20° | 15° | 5° (10) |
| 🥈 | naoagent | naomicouriel | **48** | 19° | 3° (15) | 3° (15) | 2° (18) | 19° |
| 🥉 | ivan-de-pineda-105 | RamaMusic | **43** | 14° | 8° (4) | 1° (25) | 5° (10) | 8° (4) |
| 4 | DeCruz_v2 | BrunoDC-dev | **38** | 10° (1) | 4° (12) | 15° | 24° | 1° (25) |
| 5 | valentino-pettazi | ValenPettaz1 | **34** | 22° | 10° (1) | 6° (8) | 1° (25) | 23° |
| 6 | leon-alderete | joaquinleondev | **33** | 3° (15) | 14° | 7° (6) | 21° | 4° (12) |
| 7 | fium-V3 | tomasbenavidez | **30** | 11° | 15° | 4° (12) | 22° | 2° (18) |
| 8 | lein | matilein | **30** | 21° | 18° | 2° (18) | 4° (12) | 20° |
| 9 | gonzalezds | mariagonzalezdelsolar | **29** | 4° (12) | 9° (2) | 22° | 20° | 3° (15) |
| 10 | salim | athinasalimm | **28** | 5° (10) | 2° (18) | 19° | 12° | 12° |
| 11 | Franco-Colapinto | famatodlr | **25** | 20° | 6° (8) | 9° (2) | 3° (15) | 14° |
| 12 | tomas-castro | tommycass | **18** | 2° (18) | 11° | 14° | 14° | 15° |
| 13 | domabot2 | Sdomato | **18** | 18° | 16° | 5° (10) | 6° (8) | 16° |
| 14 | Alan-Schadan | Alanschad | **16** | 6° (8) | 7° (6) | 23° | 17° | 9° (2) |
| 15 | Meteoro | FacundoFirpo | **12** | 8° (4) | 22° | 26° | 23° | 6° (8) |
| 16 | sb3zoo | Gabo-Tor | **10** | 16° | 5° (10) | 24° | 26° | 24° |
| 17 | mateofreire | mateofreire | **8** | 24° | 12° | 10° (1) | 10° (1) | 7° (6) |
| 18 | joaco-di-cola | joaco1212004 | **8** | 26° | 27° | 8° (4) | 8° (4) | 27° |
| 19 | maxi | maxividela2577 | **6** | 23° | 24° | 11° | 7° (6) | 18° |
| 20 | agusamblard | agusamblard | **6** | 7° (6) | 13° | 17° | 25° | 21° |
| 21 | zoffi | florzoffi | **2** | 25° | 28° | 12° | 9° (2) | 25° |
| 22 | jazgeller | jazgeller | **2** | 9° (2) | 21° | 13° | 19° | 13° |
| 23 | viaggio | FelipeViaggioFL | **1** | 13° | 26° | 25° | 13° | 10° (1) |
| 24 | sgroba | Santi2065 | **0** | 15° | 19° | 16° | 11° | 17° |
| 25 | auto-cipre | CiprianoOss | **0** | 28° | 20° | 28° | 16° | 11° |
| 26 | martin-bianchi | martinbianchi0 | **0** | 12° | 23° | 18° | 27° | 26° |
| 27 | matbr | mateobramer | **0** | 17° | 17° | 27° | 28° | 28° |
| 28 | valeriano | Isivaleriano | **0** | 27° | 25° | 21° | 18° | 22° |

## 🔧 Autos de reserva

No suman ni ocupan posiciones. Las posiciones son las que tendría cada auto si fuera el titular de su escudería (contra los titulares de las demás).

| Auto | Escudería | Pts como titular | Estándar | Largada libre | Lluvia | Motor débil | Otra pista |
|------|-----------|-----:|:---:|:---:|:---:|:---:|:---:|
| DeCruz | BrunoDC-dev | 36 | 2° (18) | 26° | 5° (10) | 26° | 6° (8) |
| lein2 | matilein | 27 | 27° | 9° (2) | 23° | 14° | 1° (25) |
| lein3 | matilein | 27 | 27° | 9° (2) | 22° | 19° | 1° (25) |
| naoagent-greedy2 | naomicouriel | 46 | 1° (25) | 14° | 7° (6) | 20° | 3° (15) |
| naoagent-greedy3 | naomicouriel | 45 | 1° (25) | 11° | 6° (8) | 17° | 4° (12) |
| naoagent-greedy | naomicouriel | 44 | 2° (18) | 8° (4) | 4° (12) | 22° | 5° (10) |
| naoagent-ensemble | naomicouriel | 44 | 3° (15) | 4° (12) | 6° (8) | 10° (1) | 6° (8) |
| ivan-de-pineda-102 | RamaMusic | 42 | 8° (4) | 9° (2) | 1° (25) | 10° (1) | 5° (10) |
| ivan-de-pineda-101 | RamaMusic | 42 | 6° (8) | 8° (4) | 2° (18) | 8° (4) | 6° (8) |
| ivan-de-pineda-es-inocente-con-features | RamaMusic | 40 | 2° (18) | 8° (4) | 6° (8) | 17° | 5° (10) |
| ivan-de-pineda-106 | RamaMusic | 39 | 14° | 8° (4) | 1° (25) | 5° (10) | 11° |
| ivan-de-pineda-es-inocente-sin-cos | RamaMusic | 39 | 3° (15) | 8° (4) | 6° (8) | 19° | 4° (12) |
| ivan-de-pineda-es-inocente-sin-features | RamaMusic | 38 | 2° (18) | 9° (2) | 6° (8) | 12° | 5° (10) |
| ivan-de-pineda-103 | RamaMusic | 37 | 15° | 8° (4) | 1° (25) | 6° (8) | 11° |
| ivan-de-pineda-104 | RamaMusic | 32 | 17° | 8° (4) | 2° (18) | 5° (10) | 15° |
| domabot | Sdomato | 0 | 17° | 28° | 27° | 27° | 20° |
| fium-V1 | tomasbenavidez | 25 | 21° | 12° | 21° | 28° | 1° (25) |
| fium-V2 | tomasbenavidez | 25 | 25° | 26° | 25° | 1° (25) | 27° |
| fium-V4 | tomasbenavidez | 20 | 21° | 5° (10) | 16° | 5° (10) | 26° |
| tomasbenavidez | tomasbenavidez | 16 | 8° (4) | 15° | 16° | 26° | 4° (12) |

## GP Estándar

_MountainCar-v0 tal cual._

| # | Auto | Escudería | Pts | Media | IQM | Sin llegar | Min | Max | Episodios | Dif. al 1° |
|---|------|-----------|----:|-------|-----|-----------:|-----|-----|-----------|-----------|
| R | naoagent-greedy3 | naomicouriel | — | -97.423 | -100.268 | 0.0% | -104.0 | -83.0 | 1000 | −0.007 |
| R | naoagent-greedy2 | naomicouriel | — | -97.428 | -100.276 | 0.0% | -104.0 | -83.0 | 1000 | −0.002 |
| 1 | vanafa | VANAFA | 25 | -97.430 | -100.282 | 0.0% | -104.0 | -83.0 | 1000 | — |
| R | ivan-de-pineda-es-inocente-con-features | RamaMusic | — | -97.434 | -100.282 | 0.0% | -104.0 | -83.0 | 1000 | +0.004 |
| R | naoagent-greedy | naomicouriel | — | -97.440 | -100.302 | 0.0% | -104.0 | -83.0 | 1000 | +0.010 |
| R | DeCruz | BrunoDC-dev | — | -97.460 | -100.344 | 0.0% | -104.0 | -83.0 | 1000 | +0.030 |
| R | ivan-de-pineda-es-inocente-sin-features | RamaMusic | — | -97.480 | -100.314 | 0.0% | -104.0 | -83.0 | 1000 | +0.050 |
| 2 | tomas-castro | tommycass | 18 | -97.526 | -100.316 | 0.0% | -104.0 | -83.0 | 1000 | +0.096 |
| R | ivan-de-pineda-es-inocente-sin-cos | RamaMusic | — | -97.544 | -100.458 | 0.0% | -104.0 | -83.0 | 1000 | +0.114 |
| R | naoagent-ensemble | naomicouriel | — | -97.548 | -100.312 | 0.0% | -104.0 | -83.0 | 1000 | +0.118 |
| 3 | leon-alderete | joaquinleondev | 15 | -97.549 | -100.408 | 0.0% | -104.0 | -83.0 | 1000 | +0.119 |
| 4 | gonzalezds | mariagonzalezdelsolar | 12 | -97.590 | -100.334 | 0.0% | -105.0 | -83.0 | 1000 | +0.160 |
| 5 | salim | athinasalimm | 10 | -97.613 | -100.276 | 0.0% | -104.0 | -83.0 | 1000 | +0.183 |
| R | ivan-de-pineda-101 | RamaMusic | — | -97.736 | -100.750 | 0.0% | -104.0 | -83.0 | 1000 | +0.306 |
| 6 | Alan-Schadan | Alanschad | 8 | -97.754 | -100.498 | 0.0% | -104.0 | -83.0 | 1000 | +0.324 |
| 7 | agusamblard | agusamblard | 6 | -97.756 | -100.484 | 0.0% | -105.0 | -83.0 | 1000 | +0.326 |
| R | ivan-de-pineda-102 | RamaMusic | — | -97.776 | -100.806 | 0.0% | -104.0 | -83.0 | 1000 | +0.346 |
| R | tomasbenavidez | tomasbenavidez | — | -97.911 | -100.694 | 0.0% | -104.0 | -83.0 | 1000 | +0.481 |
| 8 | Meteoro | FacundoFirpo | 4 | -97.934 | -100.976 | 0.0% | -104.0 | -83.0 | 1000 | +0.504 |
| 9 | jazgeller | jazgeller | 2 | -97.958 | -100.822 | 0.0% | -108.0 | -83.0 | 1000 | +0.528 |
| 10 | DeCruz_v2 | BrunoDC-dev | 1 | -98.071 | -100.854 | 0.0% | -107.0 | -84.0 | 1000 | +0.641 |
| 11 | fium-V3 | tomasbenavidez | 0 | -98.177 | -100.828 | 0.0% | -105.0 | -83.0 | 1000 | +0.747 |
| 12 | martin-bianchi | martinbianchi0 | 0 | -98.282 | -100.826 | 0.0% | -106.0 | -83.0 | 1000 | +0.852 |
| 13 | viaggio | FelipeViaggioFL | 0 | -98.343 | -101.658 | 0.0% | -104.0 | -83.0 | 1000 | +0.913 |
| 14 | ivan-de-pineda-105 | RamaMusic | 0 | -98.508 | -102.030 | 0.0% | -104.0 | -83.0 | 1000 | +1.078 |
| R | ivan-de-pineda-106 | RamaMusic | — | -98.579 | -102.020 | 0.0% | -105.0 | -83.0 | 1000 | +1.149 |
| 15 | sgroba | Santi2065 | 0 | -98.663 | -101.698 | 0.0% | -106.0 | -83.0 | 1000 | +1.233 |
| R | ivan-de-pineda-103 | RamaMusic | — | -98.782 | -102.210 | 0.0% | -105.0 | -83.0 | 1000 | +1.352 |
| 16 | sb3zoo | Gabo-Tor | 0 | -99.114 | -101.784 | 0.0% | -108.0 | -84.0 | 1000 | +1.684 |
| R | domabot | Sdomato | — | -99.252 | -101.780 | 0.0% | -106.0 | -84.0 | 1000 | +1.822 |
| 17 | matbr | mateobramer | 0 | -99.276 | -102.014 | 0.0% | -106.0 | -84.0 | 1000 | +1.846 |
| R | ivan-de-pineda-104 | RamaMusic | — | -99.307 | -103.018 | 0.0% | -106.0 | -83.0 | 1000 | +1.877 |
| 18 | domabot2 | Sdomato | 0 | -99.526 | -103.570 | 0.0% | -104.0 | -84.0 | 1000 | +2.096 |
| 19 | naoagent | naomicouriel | 0 | -99.560 | -103.346 | 0.0% | -105.0 | -83.0 | 1000 | +2.130 |
| 20 | Franco-Colapinto | famatodlr | 0 | -99.734 | -103.508 | 0.0% | -107.0 | -83.0 | 1000 | +2.304 |
| 21 | lein | matilein | 0 | -100.036 | -103.614 | 0.0% | -105.0 | -84.0 | 1000 | +2.606 |
| R | fium-V1 | tomasbenavidez | — | -100.090 | -102.276 | 0.0% | -127.0 | -84.0 | 1000 | +2.660 |
| R | fium-V4 | tomasbenavidez | — | -100.277 | -103.484 | 0.0% | -105.0 | -83.0 | 1000 | +2.847 |
| 22 | valentino-pettazi | ValenPettaz1 | 0 | -100.304 | -103.054 | 0.0% | -105.0 | -83.0 | 1000 | +2.874 |
| 23 | maxi | maxividela2577 | 0 | -100.353 | -104.166 | 0.0% | -107.0 | -84.0 | 1000 | +2.923 |
| 24 | mateofreire | mateofreire | 0 | -100.362 | -103.408 | 0.0% | -110.0 | -85.0 | 1000 | +2.932 |
| 25 | zoffi | florzoffi | 0 | -101.328 | -103.064 | 0.0% | -111.0 | -83.0 | 1000 | +3.898 |
| R | fium-V2 | tomasbenavidez | — | -102.789 | -104.438 | 0.0% | -106.0 | -84.0 | 1000 | +5.359 |
| 26 | joaco-di-cola | joaco1212004 | 0 | -102.982 | -107.744 | 0.0% | -109.0 | -83.0 | 1000 | +5.552 |
| 27 | valeriano | Isivaleriano | 0 | -104.107 | -106.666 | 0.0% | -113.0 | -84.0 | 1000 | +6.677 |
| R | lein3 | matilein | — | -104.276 | -101.390 | 0.0% | -171.0 | -83.0 | 1000 | +6.846 |
| R | lein2 | matilein | — | -104.545 | -101.626 | 0.3% | -200.0 | -83.0 | 1000 | +7.115 |
| 28 | auto-cipre | CiprianoOss | 0 | -109.595 | -108.150 | 0.0% | -156.0 | -83.0 | 1000 | +12.165 |

## GP Largada libre

_Largan desde cualquier punto de la pista y con velocidad inicial._

| # | Auto | Escudería | Pts | Media | IQM | Sin llegar | Min | Max | Episodios | Dif. al 1° |
|---|------|-----------|----:|-------|-----|-----------:|-----|-----|-----------|-----------|
| 1 | vanafa | VANAFA | 25 | -57.351 | -59.018 | 0.0% | -141.0 | -3.0 | 1000 | — |
| 2 | salim | athinasalimm | 18 | -57.393 | -58.892 | 0.0% | -142.0 | -3.0 | 1000 | +0.042 |
| 3 | naoagent | naomicouriel | 15 | -57.585 | -58.898 | 0.0% | -163.0 | -3.0 | 1000 | +0.234 |
| 4 | DeCruz_v2 | BrunoDC-dev | 12 | -57.695 | -59.052 | 0.0% | -147.0 | -3.0 | 1000 | +0.344 |
| R | naoagent-ensemble | naomicouriel | — | -57.720 | -58.972 | 0.0% | -149.0 | -3.0 | 1000 | +0.369 |
| R | fium-V4 | tomasbenavidez | — | -57.747 | -59.064 | 0.0% | -132.0 | -3.0 | 1000 | +0.396 |
| 5 | sb3zoo | Gabo-Tor | 10 | -57.810 | -59.354 | 0.0% | -129.0 | -3.0 | 1000 | +0.459 |
| 6 | Franco-Colapinto | famatodlr | 8 | -57.829 | -59.186 | 0.0% | -142.0 | -3.0 | 1000 | +0.478 |
| 7 | Alan-Schadan | Alanschad | 6 | -57.841 | -59.452 | 0.0% | -186.0 | -3.0 | 1000 | +0.490 |
| R | ivan-de-pineda-es-inocente-con-features | RamaMusic | — | -57.895 | -59.186 | 0.0% | -176.0 | -3.0 | 1000 | +0.544 |
| 8 | ivan-de-pineda-105 | RamaMusic | 4 | -57.929 | -58.962 | 0.0% | -160.0 | -3.0 | 1000 | +0.578 |
| R | ivan-de-pineda-104 | RamaMusic | — | -58.006 | -58.950 | 0.0% | -167.0 | -3.0 | 1000 | +0.655 |
| R | ivan-de-pineda-es-inocente-sin-cos | RamaMusic | — | -58.014 | -59.360 | 0.0% | -151.0 | -3.0 | 1000 | +0.663 |
| R | ivan-de-pineda-103 | RamaMusic | — | -58.019 | -58.990 | 0.0% | -169.0 | -3.0 | 1000 | +0.668 |
| R | ivan-de-pineda-106 | RamaMusic | — | -58.023 | -59.138 | 0.0% | -155.0 | -3.0 | 1000 | +0.672 |
| R | ivan-de-pineda-101 | RamaMusic | — | -58.043 | -59.416 | 0.0% | -155.0 | -3.0 | 1000 | +0.692 |
| R | lein3 | matilein | — | -58.114 | -59.438 | 0.0% | -149.0 | -3.0 | 1000 | +0.763 |
| R | lein2 | matilein | — | -58.148 | -59.228 | 0.0% | -187.0 | -3.0 | 1000 | +0.797 |
| R | naoagent-greedy | naomicouriel | — | -58.228 | -59.064 | 0.0% | -182.0 | -3.0 | 1000 | +0.877 |
| 9 | gonzalezds | mariagonzalezdelsolar | 2 | -58.248 | -60.034 | 0.0% | -152.0 | -3.0 | 1000 | +0.897 |
| R | ivan-de-pineda-es-inocente-sin-features | RamaMusic | — | -58.294 | -59.248 | 0.0% | -186.0 | -3.0 | 1000 | +0.943 |
| R | ivan-de-pineda-102 | RamaMusic | — | -58.301 | -59.080 | 0.0% | -181.0 | -3.0 | 1000 | +0.950 |
| 10 | valentino-pettazi | ValenPettaz1 | 1 | -58.336 | -59.816 | 0.0% | -149.0 | -3.0 | 1000 | +0.985 |
| 11 | tomas-castro | tommycass | 0 | -58.499 | -60.186 | 0.0% | -154.0 | -3.0 | 1000 | +1.148 |
| R | fium-V1 | tomasbenavidez | — | -58.741 | -59.766 | 0.0% | -161.0 | -3.0 | 1000 | +1.390 |
| R | naoagent-greedy3 | naomicouriel | — | -58.917 | -60.364 | 0.0% | -152.0 | -3.0 | 1000 | +1.566 |
| 12 | mateofreire | mateofreire | 0 | -58.970 | -59.452 | 0.0% | -196.0 | -3.0 | 1000 | +1.619 |
| 13 | agusamblard | agusamblard | 0 | -59.257 | -60.216 | 0.0% | -165.0 | -3.0 | 1000 | +1.906 |
| 14 | leon-alderete | joaquinleondev | 0 | -59.310 | -60.590 | 0.0% | -179.0 | -3.0 | 1000 | +1.959 |
| R | naoagent-greedy2 | naomicouriel | — | -59.333 | -60.468 | 0.0% | -161.0 | -3.0 | 1000 | +1.982 |
| R | tomasbenavidez | tomasbenavidez | — | -59.372 | -59.928 | 0.0% | -157.0 | -3.0 | 1000 | +2.021 |
| 15 | fium-V3 | tomasbenavidez | 0 | -59.419 | -60.222 | 0.0% | -160.0 | -3.0 | 1000 | +2.068 |
| 16 | domabot2 | Sdomato | 0 | -59.642 | -61.210 | 0.0% | -160.0 | -3.0 | 1000 | +2.291 |
| 17 | matbr | mateobramer | 0 | -59.704 | -61.216 | 0.0% | -129.0 | -3.0 | 1000 | +2.353 |
| 18 | lein | matilein | 0 | -59.877 | -60.294 | 0.0% | -180.0 | -3.0 | 1000 | +2.526 |
| 19 | sgroba | Santi2065 | 0 | -60.074 | -59.796 | 0.0% | -161.0 | -3.0 | 1000 | +2.723 |
| 20 | auto-cipre | CiprianoOss | 0 | -60.302 | -61.328 | 0.0% | -148.0 | -3.0 | 1000 | +2.951 |
| 21 | jazgeller | jazgeller | 0 | -60.339 | -61.520 | 0.0% | -162.0 | -3.0 | 1000 | +2.988 |
| 22 | Meteoro | FacundoFirpo | 0 | -60.682 | -62.440 | 0.0% | -171.0 | -3.0 | 1000 | +3.331 |
| 23 | martin-bianchi | martinbianchi0 | 0 | -61.128 | -62.554 | 0.0% | -145.0 | -3.0 | 1000 | +3.777 |
| 24 | maxi | maxividela2577 | 0 | -61.359 | -63.004 | 0.0% | -172.0 | -3.0 | 1000 | +4.008 |
| 25 | valeriano | Isivaleriano | 0 | -61.487 | -61.228 | 0.0% | -188.0 | -3.0 | 1000 | +4.136 |
| 26 | viaggio | FelipeViaggioFL | 0 | -63.259 | -65.332 | 0.0% | -170.0 | -3.0 | 1000 | +5.908 |
| R | fium-V2 | tomasbenavidez | — | -63.521 | -65.594 | 0.0% | -167.0 | -3.0 | 1000 | +6.170 |
| R | DeCruz | BrunoDC-dev | — | -64.719 | -66.624 | 0.0% | -197.0 | -3.0 | 1000 | +7.368 |
| 27 | joaco-di-cola | joaco1212004 | 0 | -65.656 | -67.556 | 0.0% | -199.0 | -3.0 | 1000 | +8.305 |
| 28 | zoffi | florzoffi | 0 | -65.818 | -66.818 | 0.1% | -200.0 | -3.0 | 1000 | +8.467 |
| R | domabot | Sdomato | — | -67.175 | -69.610 | 0.0% | -167.0 | -3.0 | 1000 | +9.824 |

## GP Lluvia

_Sensores con ruido gaussiano en posición y velocidad._

| # | Auto | Escudería | Pts | Media | IQM | Sin llegar | Min | Max | Episodios | Dif. al 1° |
|---|------|-----------|----:|-------|-----|-----------:|-----|-----|-----------|-----------|
| R | ivan-de-pineda-106 | RamaMusic | — | -99.960 | -102.236 | 0.0% | -169.0 | -83.0 | 1000 | −0.192 |
| 1 | ivan-de-pineda-105 | RamaMusic | 25 | -100.152 | -102.388 | 0.0% | -176.0 | -83.0 | 1000 | — |
| R | ivan-de-pineda-102 | RamaMusic | — | -100.277 | -101.974 | 0.0% | -176.0 | -83.0 | 1000 | +0.125 |
| R | ivan-de-pineda-103 | RamaMusic | — | -100.382 | -102.450 | 0.0% | -172.0 | -83.0 | 1000 | +0.230 |
| 2 | lein | matilein | 18 | -100.563 | -103.400 | 0.0% | -186.0 | -83.0 | 1000 | +0.411 |
| R | ivan-de-pineda-101 | RamaMusic | — | -100.571 | -101.786 | 0.0% | -173.0 | -83.0 | 1000 | +0.419 |
| R | ivan-de-pineda-104 | RamaMusic | — | -100.616 | -102.922 | 0.0% | -173.0 | -83.0 | 1000 | +0.464 |
| 3 | naoagent | naomicouriel | 15 | -101.021 | -103.266 | 0.0% | -174.0 | -83.0 | 1000 | +0.869 |
| 4 | fium-V3 | tomasbenavidez | 12 | -101.088 | -102.022 | 0.0% | -186.0 | -83.0 | 1000 | +0.936 |
| R | naoagent-greedy | naomicouriel | — | -101.103 | -101.656 | 0.0% | -179.0 | -83.0 | 1000 | +0.951 |
| R | DeCruz | BrunoDC-dev | — | -101.112 | -101.764 | 0.3% | -200.0 | -83.0 | 1000 | +0.960 |
| 5 | domabot2 | Sdomato | 10 | -101.321 | -103.686 | 0.0% | -178.0 | -83.0 | 1000 | +1.169 |
| 6 | valentino-pettazi | ValenPettaz1 | 8 | -101.441 | -103.492 | 0.0% | -160.0 | -83.0 | 1000 | +1.289 |
| R | naoagent-ensemble | naomicouriel | — | -101.768 | -101.994 | 0.0% | -189.0 | -83.0 | 1000 | +1.616 |
| R | ivan-de-pineda-es-inocente-sin-cos | RamaMusic | — | -101.808 | -102.138 | 0.0% | -189.0 | -83.0 | 1000 | +1.656 |
| R | ivan-de-pineda-es-inocente-sin-features | RamaMusic | — | -101.885 | -101.772 | 0.0% | -186.0 | -83.0 | 1000 | +1.733 |
| R | naoagent-greedy3 | naomicouriel | — | -102.200 | -101.928 | 0.0% | -174.0 | -83.0 | 1000 | +2.048 |
| R | ivan-de-pineda-es-inocente-con-features | RamaMusic | — | -102.255 | -101.862 | 0.0% | -183.0 | -83.0 | 1000 | +2.103 |
| 7 | leon-alderete | joaquinleondev | 6 | -102.486 | -102.160 | 0.0% | -183.0 | -83.0 | 1000 | +2.334 |
| 8 | joaco-di-cola | joaco1212004 | 4 | -103.230 | -105.882 | 0.0% | -192.0 | -83.0 | 1000 | +3.078 |
| R | naoagent-greedy2 | naomicouriel | — | -103.230 | -102.098 | 0.0% | -177.0 | -83.0 | 1000 | +3.078 |
| 9 | Franco-Colapinto | famatodlr | 2 | -103.258 | -103.960 | 0.0% | -167.0 | -83.0 | 1000 | +3.106 |
| 10 | mateofreire | mateofreire | 1 | -103.743 | -104.048 | 0.0% | -167.0 | -84.0 | 1000 | +3.591 |
| 11 | maxi | maxividela2577 | 0 | -103.774 | -104.896 | 0.0% | -194.0 | -84.0 | 1000 | +3.622 |
| 12 | zoffi | florzoffi | 0 | -104.280 | -105.628 | 0.0% | -182.0 | -83.0 | 1000 | +4.128 |
| 13 | jazgeller | jazgeller | 0 | -104.373 | -104.084 | 0.0% | -182.0 | -83.0 | 1000 | +4.221 |
| 14 | tomas-castro | tommycass | 0 | -104.455 | -102.680 | 0.0% | -174.0 | -83.0 | 1000 | +4.303 |
| 15 | DeCruz_v2 | BrunoDC-dev | 0 | -104.736 | -102.696 | 0.0% | -180.0 | -83.0 | 1000 | +4.584 |
| 16 | sgroba | Santi2065 | 0 | -104.912 | -103.818 | 0.2% | -200.0 | -83.0 | 1000 | +4.760 |
| R | fium-V4 | tomasbenavidez | — | -105.019 | -104.376 | 0.0% | -176.0 | -83.0 | 1000 | +4.867 |
| R | tomasbenavidez | tomasbenavidez | — | -105.572 | -102.982 | 0.0% | -199.0 | -83.0 | 1000 | +5.420 |
| 17 | agusamblard | agusamblard | 0 | -105.586 | -103.796 | 0.0% | -197.0 | -83.0 | 1000 | +5.434 |
| 18 | martin-bianchi | martinbianchi0 | 0 | -106.083 | -104.532 | 0.1% | -200.0 | -83.0 | 1000 | +5.931 |
| 19 | salim | athinasalimm | 0 | -106.224 | -102.868 | 0.0% | -183.0 | -83.0 | 1000 | +6.072 |
| 20 | vanafa | VANAFA | 0 | -106.377 | -102.934 | 0.0% | -172.0 | -83.0 | 1000 | +6.225 |
| 21 | valeriano | Isivaleriano | 0 | -106.790 | -107.256 | 0.7% | -200.0 | -84.0 | 1000 | +6.638 |
| R | fium-V1 | tomasbenavidez | — | -107.063 | -103.426 | 0.0% | -196.0 | -84.0 | 1000 | +6.911 |
| 22 | gonzalezds | mariagonzalezdelsolar | 0 | -107.371 | -102.788 | 0.0% | -170.0 | -83.0 | 1000 | +7.219 |
| R | lein3 | matilein | — | -107.460 | -102.700 | 0.0% | -173.0 | -83.0 | 1000 | +7.308 |
| 23 | Alan-Schadan | Alanschad | 0 | -107.569 | -103.778 | 0.0% | -176.0 | -83.0 | 1000 | +7.417 |
| R | lein2 | matilein | — | -107.947 | -103.168 | 0.0% | -160.0 | -83.0 | 1000 | +7.795 |
| 24 | sb3zoo | Gabo-Tor | 0 | -108.171 | -105.530 | 0.2% | -200.0 | -83.0 | 1000 | +8.019 |
| 25 | viaggio | FelipeViaggioFL | 0 | -108.386 | -103.134 | 0.0% | -188.0 | -83.0 | 1000 | +8.234 |
| R | fium-V2 | tomasbenavidez | — | -109.136 | -105.960 | 0.1% | -200.0 | -84.0 | 1000 | +8.984 |
| 26 | Meteoro | FacundoFirpo | 0 | -110.196 | -104.878 | 0.1% | -200.0 | -83.0 | 1000 | +10.044 |
| 27 | matbr | mateobramer | 0 | -110.346 | -106.632 | 0.0% | -183.0 | -83.0 | 1000 | +10.194 |
| R | domabot | Sdomato | — | -111.638 | -105.518 | 0.3% | -200.0 | -83.0 | 1000 | +11.486 |
| 28 | auto-cipre | CiprianoOss | 0 | -116.572 | -112.482 | 0.0% | -174.0 | -83.0 | 1000 | +16.420 |

## GP Motor débil

_El motor rinde entre 8% y 12% menos._

| # | Auto | Escudería | Pts | Media | IQM | Sin llegar | Min | Max | Episodios | Dif. al 1° |
|---|------|-----------|----:|-------|-----|-----------:|-----|-----|-----------|-----------|
| R | fium-V2 | tomasbenavidez | — | -110.867 | -111.010 | 0.0% | -125.0 | -92.0 | 1000 | −1.682 |
| 1 | valentino-pettazi | ValenPettaz1 | 25 | -112.549 | -110.862 | 0.0% | -171.0 | -92.0 | 1000 | — |
| 2 | naoagent | naomicouriel | 18 | -114.634 | -110.542 | 0.4% | -200.0 | -92.0 | 1000 | +2.085 |
| 3 | Franco-Colapinto | famatodlr | 15 | -116.096 | -111.902 | 0.0% | -182.0 | -92.0 | 1000 | +3.547 |
| 4 | lein | matilein | 12 | -116.266 | -110.862 | 0.2% | -200.0 | -92.0 | 1000 | +3.717 |
| R | fium-V4 | tomasbenavidez | — | -116.694 | -112.252 | 0.4% | -200.0 | -93.0 | 1000 | +4.145 |
| R | ivan-de-pineda-106 | RamaMusic | — | -118.243 | -110.816 | 0.2% | -200.0 | -92.0 | 1000 | +5.694 |
| R | ivan-de-pineda-104 | RamaMusic | — | -118.274 | -110.740 | 0.3% | -200.0 | -92.0 | 1000 | +5.725 |
| 5 | ivan-de-pineda-105 | RamaMusic | 10 | -118.723 | -111.188 | 0.3% | -200.0 | -92.0 | 1000 | +6.174 |
| 6 | domabot2 | Sdomato | 8 | -118.738 | -111.758 | 0.2% | -200.0 | -92.0 | 1000 | +6.189 |
| R | ivan-de-pineda-103 | RamaMusic | — | -118.976 | -110.844 | 0.3% | -200.0 | -92.0 | 1000 | +6.427 |
| 7 | maxi | maxividela2577 | 6 | -119.282 | -112.610 | 0.4% | -200.0 | -93.0 | 1000 | +6.733 |
| 8 | joaco-di-cola | joaco1212004 | 4 | -119.523 | -113.392 | 2.2% | -200.0 | -92.0 | 1000 | +6.974 |
| R | ivan-de-pineda-101 | RamaMusic | — | -120.693 | -113.274 | 0.3% | -200.0 | -92.0 | 1000 | +8.144 |
| 9 | zoffi | florzoffi | 2 | -121.367 | -114.872 | 7.1% | -200.0 | -92.0 | 1000 | +8.818 |
| 10 | mateofreire | mateofreire | 1 | -122.323 | -112.370 | 1.0% | -200.0 | -92.0 | 1000 | +9.774 |
| R | naoagent-ensemble | naomicouriel | — | -123.640 | -117.036 | 0.2% | -200.0 | -92.0 | 1000 | +11.091 |
| R | ivan-de-pineda-102 | RamaMusic | — | -123.804 | -114.862 | 2.2% | -200.0 | -92.0 | 1000 | +11.255 |
| 11 | sgroba | Santi2065 | 0 | -124.057 | -113.460 | 1.6% | -200.0 | -93.0 | 1000 | +11.508 |
| 12 | salim | athinasalimm | 0 | -125.186 | -119.948 | 0.0% | -195.0 | -93.0 | 1000 | +12.637 |
| R | ivan-de-pineda-es-inocente-sin-features | RamaMusic | — | -125.251 | -117.268 | 2.9% | -200.0 | -92.0 | 1000 | +12.702 |
| 13 | viaggio | FelipeViaggioFL | 0 | -125.442 | -114.484 | 0.2% | -200.0 | -94.0 | 1000 | +12.893 |
| 14 | tomas-castro | tommycass | 0 | -126.047 | -118.862 | 0.5% | -200.0 | -92.0 | 1000 | +13.498 |
| R | lein2 | matilein | — | -126.332 | -123.906 | 0.0% | -193.0 | -92.0 | 1000 | +13.783 |
| 15 | vanafa | VANAFA | 0 | -126.354 | -120.288 | 0.5% | -200.0 | -93.0 | 1000 | +13.805 |
| 16 | auto-cipre | CiprianoOss | 0 | -126.476 | -122.788 | 0.0% | -154.0 | -99.0 | 1000 | +13.927 |
| 17 | Alan-Schadan | Alanschad | 0 | -126.532 | -119.804 | 0.7% | -200.0 | -93.0 | 1000 | +13.983 |
| R | ivan-de-pineda-es-inocente-con-features | RamaMusic | — | -126.765 | -119.776 | 1.5% | -200.0 | -92.0 | 1000 | +14.216 |
| R | naoagent-greedy3 | naomicouriel | — | -126.967 | -121.108 | 0.9% | -200.0 | -92.0 | 1000 | +14.418 |
| 18 | valeriano | Isivaleriano | 0 | -127.281 | -114.172 | 3.9% | -200.0 | -102.0 | 1000 | +14.732 |
| 19 | jazgeller | jazgeller | 0 | -127.327 | -120.268 | 0.1% | -200.0 | -93.0 | 1000 | +14.778 |
| R | ivan-de-pineda-es-inocente-sin-cos | RamaMusic | — | -127.381 | -120.494 | 0.8% | -200.0 | -92.0 | 1000 | +14.832 |
| R | lein3 | matilein | — | -127.464 | -126.000 | 0.0% | -192.0 | -92.0 | 1000 | +14.915 |
| 20 | gonzalezds | mariagonzalezdelsolar | 0 | -127.507 | -123.486 | 0.0% | -186.0 | -93.0 | 1000 | +14.958 |
| R | naoagent-greedy2 | naomicouriel | — | -128.727 | -122.904 | 0.9% | -200.0 | -92.0 | 1000 | +16.178 |
| 21 | leon-alderete | joaquinleondev | 0 | -129.705 | -122.852 | 2.3% | -200.0 | -93.0 | 1000 | +17.156 |
| 22 | fium-V3 | tomasbenavidez | 0 | -130.158 | -122.592 | 0.4% | -200.0 | -92.0 | 1000 | +17.609 |
| R | naoagent-greedy | naomicouriel | — | -130.435 | -123.528 | 1.9% | -200.0 | -93.0 | 1000 | +17.886 |
| 23 | Meteoro | FacundoFirpo | 0 | -130.904 | -120.308 | 6.0% | -200.0 | -93.0 | 1000 | +18.355 |
| 24 | DeCruz_v2 | BrunoDC-dev | 0 | -132.224 | -129.800 | 0.4% | -200.0 | -92.0 | 1000 | +19.675 |
| 25 | agusamblard | agusamblard | 0 | -133.343 | -125.230 | 4.9% | -200.0 | -93.0 | 1000 | +20.794 |
| 26 | sb3zoo | Gabo-Tor | 0 | -133.939 | -128.688 | 0.6% | -200.0 | -93.0 | 1000 | +21.390 |
| R | tomasbenavidez | tomasbenavidez | — | -134.285 | -128.850 | 1.6% | -200.0 | -93.0 | 1000 | +21.736 |
| R | DeCruz | BrunoDC-dev | — | -134.626 | -123.780 | 6.2% | -200.0 | -92.0 | 1000 | +22.077 |
| 27 | martin-bianchi | martinbianchi0 | 0 | -135.643 | -130.480 | 0.3% | -200.0 | -94.0 | 1000 | +23.094 |
| R | domabot | Sdomato | — | -138.948 | -133.360 | 0.6% | -200.0 | -111.0 | 1000 | +26.399 |
| 28 | matbr | mateobramer | 0 | -140.219 | -136.596 | 0.2% | -200.0 | -99.0 | 1000 | +27.670 |
| R | fium-V1 | tomasbenavidez | — | -140.761 | -142.958 | 0.7% | -200.0 | -92.0 | 1000 | +28.212 |

## GP Otra pista

_La montaña cambia de forma: cos(f·x) con f entre 2.6 y 2.8 (en vez de 3)._

| # | Auto | Escudería | Pts | Media | IQM | Sin llegar | Min | Max | Episodios | Dif. al 1° |
|---|------|-----------|----:|-------|-----|-----------:|-----|-----|-----------|-----------|
| R | lein2 | matilein | — | -95.981 | -96.168 | 0.0% | -109.0 | -82.0 | 1000 | −1.670 |
| R | lein3 | matilein | — | -96.393 | -96.448 | 0.0% | -113.0 | -83.0 | 1000 | −1.258 |
| R | fium-V1 | tomasbenavidez | — | -97.121 | -97.652 | 0.0% | -111.0 | -83.0 | 1000 | −0.530 |
| 1 | DeCruz_v2 | BrunoDC-dev | 25 | -97.651 | -99.442 | 0.0% | -109.0 | -82.0 | 1000 | — |
| 2 | fium-V3 | tomasbenavidez | 18 | -98.192 | -100.480 | 0.0% | -110.0 | -82.0 | 1000 | +0.541 |
| R | naoagent-greedy2 | naomicouriel | — | -98.919 | -101.578 | 0.0% | -109.0 | -82.0 | 1000 | +1.268 |
| 3 | gonzalezds | mariagonzalezdelsolar | 15 | -98.962 | -100.764 | 0.0% | -112.0 | -83.0 | 1000 | +1.311 |
| R | ivan-de-pineda-es-inocente-sin-cos | RamaMusic | — | -99.134 | -102.084 | 0.0% | -109.0 | -82.0 | 1000 | +1.483 |
| R | naoagent-greedy3 | naomicouriel | — | -99.197 | -101.904 | 0.0% | -110.0 | -82.0 | 1000 | +1.546 |
| 4 | leon-alderete | joaquinleondev | 12 | -99.202 | -101.910 | 0.0% | -110.0 | -82.0 | 1000 | +1.551 |
| R | ivan-de-pineda-102 | RamaMusic | — | -99.342 | -102.606 | 0.0% | -110.0 | -82.0 | 1000 | +1.691 |
| R | naoagent-greedy | naomicouriel | — | -99.366 | -102.134 | 0.0% | -109.0 | -82.0 | 1000 | +1.715 |
| R | ivan-de-pineda-es-inocente-sin-features | RamaMusic | — | -99.473 | -102.166 | 0.0% | -111.0 | -82.0 | 1000 | +1.822 |
| R | ivan-de-pineda-es-inocente-con-features | RamaMusic | — | -99.569 | -102.144 | 0.0% | -111.0 | -83.0 | 1000 | +1.918 |
| R | tomasbenavidez | tomasbenavidez | — | -100.060 | -102.298 | 0.0% | -122.0 | -83.0 | 1000 | +2.409 |
| 5 | vanafa | VANAFA | 10 | -100.162 | -102.492 | 0.0% | -113.0 | -83.0 | 1000 | +2.511 |
| R | ivan-de-pineda-101 | RamaMusic | — | -100.175 | -103.304 | 0.0% | -111.0 | -82.0 | 1000 | +2.524 |
| R | naoagent-ensemble | naomicouriel | — | -100.460 | -103.536 | 0.0% | -111.0 | -82.0 | 1000 | +2.809 |
| 6 | Meteoro | FacundoFirpo | 8 | -100.551 | -103.898 | 0.0% | -111.0 | -83.0 | 1000 | +2.900 |
| R | DeCruz | BrunoDC-dev | — | -100.831 | -102.220 | 0.0% | -125.0 | -82.0 | 1000 | +3.180 |
| 7 | mateofreire | mateofreire | 6 | -101.106 | -104.210 | 0.0% | -114.0 | -82.0 | 1000 | +3.455 |
| 8 | ivan-de-pineda-105 | RamaMusic | 4 | -101.108 | -105.178 | 0.0% | -111.0 | -82.0 | 1000 | +3.457 |
| 9 | Alan-Schadan | Alanschad | 2 | -101.159 | -103.448 | 0.0% | -114.0 | -83.0 | 1000 | +3.508 |
| 10 | viaggio | FelipeViaggioFL | 1 | -101.387 | -105.796 | 0.0% | -112.0 | -82.0 | 1000 | +3.736 |
| 11 | auto-cipre | CiprianoOss | 0 | -101.474 | -103.940 | 0.0% | -117.0 | -82.0 | 1000 | +3.823 |
| R | ivan-de-pineda-106 | RamaMusic | — | -101.539 | -105.534 | 0.0% | -113.0 | -82.0 | 1000 | +3.888 |
| R | ivan-de-pineda-103 | RamaMusic | — | -101.690 | -105.754 | 0.0% | -113.0 | -82.0 | 1000 | +4.039 |
| 12 | salim | athinasalimm | 0 | -102.124 | -104.612 | 0.0% | -144.0 | -84.0 | 1000 | +4.473 |
| 13 | jazgeller | jazgeller | 0 | -102.260 | -104.368 | 0.0% | -119.0 | -83.0 | 1000 | +4.609 |
| 14 | Franco-Colapinto | famatodlr | 0 | -102.281 | -107.276 | 0.0% | -114.0 | -82.0 | 1000 | +4.630 |
| 15 | tomas-castro | tommycass | 0 | -102.323 | -103.908 | 0.0% | -119.0 | -83.0 | 1000 | +4.672 |
| R | ivan-de-pineda-104 | RamaMusic | — | -102.476 | -107.082 | 0.0% | -114.0 | -82.0 | 1000 | +4.825 |
| 16 | domabot2 | Sdomato | 0 | -102.947 | -107.528 | 0.0% | -115.0 | -83.0 | 1000 | +5.296 |
| 17 | sgroba | Santi2065 | 0 | -102.965 | -105.862 | 0.0% | -117.0 | -83.0 | 1000 | +5.314 |
| 18 | maxi | maxividela2577 | 0 | -103.585 | -107.732 | 0.0% | -118.0 | -83.0 | 1000 | +5.934 |
| 19 | naoagent | naomicouriel | 0 | -103.726 | -108.442 | 0.0% | -115.0 | -82.0 | 1000 | +6.075 |
| 20 | lein | matilein | 0 | -104.051 | -108.690 | 0.0% | -115.0 | -83.0 | 1000 | +6.400 |
| R | domabot | Sdomato | — | -104.832 | -108.060 | 0.0% | -121.0 | -83.0 | 1000 | +7.181 |
| 21 | agusamblard | agusamblard | 0 | -106.427 | -107.062 | 0.6% | -200.0 | -85.0 | 1000 | +8.776 |
| 22 | valeriano | Isivaleriano | 0 | -109.701 | -111.716 | 2.2% | -200.0 | -84.0 | 1000 | +12.050 |
| 23 | valentino-pettazi | ValenPettaz1 | 0 | -109.825 | -110.946 | 1.8% | -200.0 | -83.0 | 1000 | +12.174 |
| 24 | sb3zoo | Gabo-Tor | 0 | -111.205 | -112.318 | 0.7% | -200.0 | -83.0 | 1000 | +13.554 |
| 25 | zoffi | florzoffi | 0 | -111.519 | -109.972 | 4.8% | -200.0 | -83.0 | 1000 | +13.868 |
| 26 | martin-bianchi | martinbianchi0 | 0 | -112.161 | -110.708 | 0.1% | -200.0 | -86.0 | 1000 | +14.510 |
| R | fium-V4 | tomasbenavidez | — | -112.716 | -113.488 | 1.4% | -200.0 | -85.0 | 1000 | +15.065 |
| 27 | joaco-di-cola | joaco1212004 | 0 | -114.668 | -120.210 | 0.0% | -130.0 | -84.0 | 1000 | +17.017 |
| R | fium-V2 | tomasbenavidez | — | -128.591 | -113.772 | 19.5% | -200.0 | -83.0 | 1000 | +30.940 |
| 28 | matbr | mateobramer | 0 | -140.896 | -137.290 | 2.6% | -200.0 | -91.0 | 1000 | +43.245 |
