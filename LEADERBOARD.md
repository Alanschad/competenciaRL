# 🏆 Leaderboard — Campeonato RL (DQN)

Entorno base: `MountainCar-v0` · 5 circuitos · Ranking por **MEDIA** en cada circuito · Actualizado: 2026-10-30 13:31 UTC

Puntos por circuito: 25, 18, 15, 12, 10, 8, 6, 4, 2, 1 (del 1° al 10°). La misma policy corre en todos los circuitos. Detalle de cada uno en el README.

**Un auto titular por escudería** (cuenta de GitHub): es el único que suma puntos y ocupa posiciones. Es el auto de la escudería que más puntos suma contra los titulares de las demás. El resto son autos de reserva: aparecen abajo, pero no le sacan puestos a nadie.

## 🏁 Campeonato

| # | Auto | Escudería | **Pts** | Estándar | Largada libre | Lluvia | Motor débil | Otra pista |
|---|------|-----------|-----:|:---:|:---:|:---:|:---:|:---:|
| 🥇 | vanafa | VANAFA | **46** | 2° (18) | 2° (18) | 22° | 17° | 5° (10) |
| 🥈 | naoagent-greedy2 | naomicouriel | **45** | 1° (25) | 15° | 9° (2) | 22° | 2° (18) |
| 🥉 | DeCruz | BrunoDC-dev | **40** | 14° | 1° (25) | 14° | 3° (15) | 20° |
| 4 | fium-V3 | tomasbenavidez | **38** | 10° (1) | 16° | 4° (12) | 24° | 1° (25) |
| 5 | Alan-Schadan-v2 | Alanschad | **37** | 25° | 4° (12) | 15° | 1° (25) | 27° |
| 6 | tomas-castro-equilibrado | tommycass | **35** | 15° | 8° (4) | 1° (25) | 7° (6) | 11° |
| 7 | ivan-de-pineda-101 | RamaMusic | **33** | 6° (8) | 9° (2) | 3° (15) | 11° | 6° (8) |
| 8 | bravo-andres | Andresbravo9 | **32** | 17° | 5° (10) | 5° (10) | 4° (12) | 15° |
| 9 | leon-alderete | joaquinleondev | **31** | 3° (15) | 14° | 8° (4) | 23° | 4° (12) |
| 10 | gonzalezds | mariagonzalezdelsolar | **28** | 4° (12) | 10° (1) | 24° | 21° | 3° (15) |
| 11 | lein | matilein | **26** | 21° | 19° | 2° (18) | 6° (8) | 19° |
| 12 | salim | athinasalimm | **25** | 5° (10) | 3° (15) | 21° | 15° | 12° |
| 13 | valentino-pettazi | ValenPettaz1 | **24** | 22° | 11° | 7° (6) | 2° (18) | 23° |
| 14 | Franco-Colapinto | famatodlr | **16** | 20° | 7° (6) | 11° | 5° (10) | 14° |
| 15 | domabot2 | Sdomato | **12** | 19° | 17° | 6° (8) | 8° (4) | 16° |
| 16 | Meteoro | FacundoFirpo | **10** | 8° (4) | 23° | 27° | 25° | 7° (6) |
| 17 | sb3zoo | Gabo-Tor | **8** | 16° | 6° (8) | 25° | 27° | 24° |
| 18 | agusamblard | agusamblard | **6** | 7° (6) | 13° | 19° | 26° | 21° |
| 19 | mateofreire | mateofreire | **4** | 24° | 12° | 12° | 13° | 8° (4) |
| 20 | joaco-di-cola | joaco1212004 | **3** | 27° | 28° | 9° (2) | 10° (1) | 28° |
| 21 | viaggio | FelipeViaggioFL | **2** | 12° | 27° | 26° | 16° | 9° (2) |
| 22 | jazgeller | jazgeller | **2** | 9° (2) | 22° | 17° | 20° | 13° |
| 23 | maxi | maxividela2577 | **2** | 23° | 25° | 13° | 9° (2) | 18° |
| 24 | auto-cipre | CiprianoOss | **1** | 29° | 21° | 29° | 18° | 10° (1) |
| 25 | martin-bianchi | martinbianchi0 | **0** | 11° | 24° | 20° | 28° | 26° |
| 26 | zoffi | florzoffi | **0** | 26° | 29° | 16° | 12° | 25° |
| 27 | sgroba | Santi2065 | **0** | 13° | 20° | 18° | 14° | 17° |
| 28 | matbr | mateobramer | **0** | 18° | 18° | 28° | 29° | 29° |
| 29 | valeriano | Isivaleriano | **0** | 28° | 26° | 23° | 19° | 22° |
| 30 | ion_h_RL_TP2 | 72Ion | **0** | 30° | 30° | 30° | 30° | 30° |

## 🔧 Autos de reserva

No suman ni ocupan posiciones. Las posiciones son las que tendría cada auto si fuera el titular de su escudería (contra los titulares de las demás).

| Auto | Escudería | Pts como titular | Estándar | Largada libre | Lluvia | Motor débil | Otra pista |
|------|-----------|-----:|:---:|:---:|:---:|:---:|:---:|
| Alan-Schadan | Alanschad | 12 | 7° (6) | 8° (4) | 24° | 18° | 9° (2) |
| bravo-andres-r1 | Andresbravo9 | 27 | 13° | 4° (12) | 7° (6) | 6° (8) | 10° (1) |
| bravo-andres-r2 | Andresbravo9 | 20 | 17° | 4° (12) | 11° | 6° (8) | 12° |
| DeCruz_v2 | BrunoDC-dev | 38 | 10° (1) | 4° (12) | 17° | 25° | 1° (25) |
| lein2 | matilein | 26 | 28° | 10° (1) | 24° | 16° | 1° (25) |
| lein3 | matilein | 26 | 28° | 10° (1) | 24° | 20° | 1° (25) |
| naoagent-greedy3 | naomicouriel | 44 | 1° (25) | 12° | 8° (4) | 19° | 3° (15) |
| naoagent-greedy | naomicouriel | 39 | 2° (18) | 10° (1) | 6° (8) | 24° | 4° (12) |
| naoagent | naomicouriel | 39 | 19° | 4° (12) | 4° (12) | 3° (15) | 18° |
| naoagent-ensemble | naomicouriel | 38 | 2° (18) | 6° (8) | 8° (4) | 14° | 6° (8) |
| ivan-de-pineda-102 | RamaMusic | 42 | 7° (6) | 10° (1) | 1° (25) | 13° | 5° (10) |
| ivan-de-pineda-105 | RamaMusic | 35 | 12° | 9° (2) | 1° (25) | 8° (4) | 8° (4) |
| ivan-de-pineda-es-inocente-sin-cos | RamaMusic | 35 | 3° (15) | 9° (2) | 7° (6) | 20° | 4° (12) |
| ivan-de-pineda-es-inocente-con-features | RamaMusic | 33 | 3° (15) | 9° (2) | 7° (6) | 18° | 5° (10) |
| ivan-de-pineda-106 | RamaMusic | 32 | 12° | 9° (2) | 1° (25) | 8° (4) | 10° (1) |
| ivan-de-pineda-es-inocente-sin-features | RamaMusic | 32 | 3° (15) | 10° (1) | 7° (6) | 15° | 5° (10) |
| ivan-de-pineda-103 | RamaMusic | 29 | 13° | 9° (2) | 1° (25) | 9° (2) | 11° |
| ivan-de-pineda-104 | RamaMusic | 21 | 18° | 9° (2) | 3° (15) | 8° (4) | 14° |
| domabot | Sdomato | 0 | 18° | 29° | 28° | 28° | 20° |
| fium-V1 | tomasbenavidez | 25 | 21° | 12° | 23° | 29° | 1° (25) |
| fium-V2 | tomasbenavidez | 25 | 26° | 27° | 26° | 1° (25) | 28° |
| tomasbenavidez | tomasbenavidez | 16 | 8° (4) | 16° | 18° | 27° | 4° (12) |
| fium-V4 | tomasbenavidez | 14 | 21° | 6° (8) | 18° | 7° (6) | 26° |
| tomas-castro | tommycass | 37 | 20° | 4° (12) | 22° | 13° | 1° (25) |

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
| R | tomasbenavidez | tomasbenavidez | — | -97.911 | -100.694 | 0.0% | -104.0 | -83.0 | 1000 | +0.483 |
| 8 | Meteoro | FacundoFirpo | 4 | -97.934 | -100.976 | 0.0% | -104.0 | -83.0 | 1000 | +0.506 |
| 9 | jazgeller | jazgeller | 2 | -97.958 | -100.822 | 0.0% | -108.0 | -83.0 | 1000 | +0.530 |
| R | DeCruz_v2 | BrunoDC-dev | — | -98.071 | -100.854 | 0.0% | -107.0 | -84.0 | 1000 | +0.643 |
| 10 | fium-V3 | tomasbenavidez | 1 | -98.177 | -100.828 | 0.0% | -105.0 | -83.0 | 1000 | +0.749 |
| 11 | martin-bianchi | martinbianchi0 | 0 | -98.282 | -100.826 | 0.0% | -106.0 | -83.0 | 1000 | +0.854 |
| 12 | viaggio | FelipeViaggioFL | 0 | -98.343 | -101.658 | 0.0% | -104.0 | -83.0 | 1000 | +0.915 |
| R | bravo-andres-r1 | Andresbravo9 | — | -98.423 | -101.828 | 0.0% | -104.0 | -83.0 | 1000 | +0.995 |
| R | ivan-de-pineda-105 | RamaMusic | — | -98.508 | -102.030 | 0.0% | -104.0 | -83.0 | 1000 | +1.080 |
| R | ivan-de-pineda-106 | RamaMusic | — | -98.579 | -102.020 | 0.0% | -105.0 | -83.0 | 1000 | +1.151 |
| 13 | sgroba | Santi2065 | 0 | -98.663 | -101.698 | 0.0% | -106.0 | -83.0 | 1000 | +1.235 |
| R | ivan-de-pineda-103 | RamaMusic | — | -98.782 | -102.210 | 0.0% | -105.0 | -83.0 | 1000 | +1.354 |
| 14 | DeCruz | BrunoDC-dev | 0 | -98.927 | -102.420 | 0.0% | -104.0 | -83.0 | 1000 | +1.499 |
| 15 | tomas-castro-equilibrado | tommycass | 0 | -99.025 | -102.460 | 0.0% | -106.0 | -83.0 | 1000 | +1.597 |
| 16 | sb3zoo | Gabo-Tor | 0 | -99.114 | -101.784 | 0.0% | -108.0 | -84.0 | 1000 | +1.686 |
| 17 | bravo-andres | Andresbravo9 | 0 | -99.174 | -102.912 | 0.0% | -104.0 | -83.0 | 1000 | +1.746 |
| R | bravo-andres-r2 | Andresbravo9 | — | -99.185 | -102.602 | 0.0% | -107.0 | -83.0 | 1000 | +1.757 |
| R | domabot | Sdomato | — | -99.252 | -101.780 | 0.0% | -106.0 | -84.0 | 1000 | +1.824 |
| 18 | matbr | mateobramer | 0 | -99.276 | -102.014 | 0.0% | -106.0 | -84.0 | 1000 | +1.848 |
| R | ivan-de-pineda-104 | RamaMusic | — | -99.307 | -103.018 | 0.0% | -106.0 | -83.0 | 1000 | +1.879 |
| 19 | domabot2 | Sdomato | 0 | -99.526 | -103.570 | 0.0% | -104.0 | -84.0 | 1000 | +2.098 |
| R | naoagent | naomicouriel | — | -99.560 | -103.346 | 0.0% | -105.0 | -83.0 | 1000 | +2.132 |
| 20 | Franco-Colapinto | famatodlr | 0 | -99.734 | -103.508 | 0.0% | -107.0 | -83.0 | 1000 | +2.306 |
| R | tomas-castro | tommycass | — | -100.025 | -100.934 | 0.0% | -147.0 | -83.0 | 1000 | +2.597 |
| 21 | lein | matilein | 0 | -100.036 | -103.614 | 0.0% | -105.0 | -84.0 | 1000 | +2.608 |
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
| R | lein2 | matilein | — | -104.545 | -101.626 | 0.3% | -200.0 | -83.0 | 1000 | +7.117 |
| 29 | auto-cipre | CiprianoOss | 0 | -109.595 | -108.150 | 0.0% | -156.0 | -83.0 | 1000 | +12.167 |
| 30 | ion_h_RL_TP2 | 72Ion | 0 | -144.008 | -136.444 | 0.4% | -200.0 | -126.0 | 1000 | +46.580 |

## GP Largada libre

_Largan desde cualquier punto de la pista y con velocidad inicial._

| # | Auto | Escudería | Pts | Media | IQM | Sin llegar | Min | Max | Episodios | Dif. al 1° |
|---|------|-----------|----:|-------|-----|-----------:|-----|-----|-----------|-----------|
| 1 | DeCruz | BrunoDC-dev | 25 | -57.175 | -58.862 | 0.0% | -119.0 | -3.0 | 1000 | — |
| 2 | vanafa | VANAFA | 18 | -57.351 | -59.018 | 0.0% | -141.0 | -3.0 | 1000 | +0.176 |
| 3 | salim | athinasalimm | 15 | -57.393 | -58.892 | 0.0% | -142.0 | -3.0 | 1000 | +0.218 |
| R | bravo-andres-r2 | Andresbravo9 | — | -57.418 | -58.916 | 0.0% | -136.0 | -3.0 | 1000 | +0.243 |
| R | tomas-castro | tommycass | — | -57.466 | -58.982 | 0.0% | -143.0 | -3.0 | 1000 | +0.291 |
| R | bravo-andres-r1 | Andresbravo9 | — | -57.496 | -59.020 | 0.0% | -152.0 | -3.0 | 1000 | +0.321 |
| R | naoagent | naomicouriel | — | -57.585 | -58.898 | 0.0% | -163.0 | -3.0 | 1000 | +0.410 |
| 4 | Alan-Schadan-v2 | Alanschad | 12 | -57.654 | -59.382 | 0.0% | -119.0 | -3.0 | 1000 | +0.479 |
| R | DeCruz_v2 | BrunoDC-dev | — | -57.695 | -59.052 | 0.0% | -147.0 | -3.0 | 1000 | +0.520 |
| 5 | bravo-andres | Andresbravo9 | 10 | -57.696 | -59.090 | 0.0% | -154.0 | -3.0 | 1000 | +0.521 |
| R | naoagent-ensemble | naomicouriel | — | -57.720 | -58.972 | 0.0% | -149.0 | -3.0 | 1000 | +0.545 |
| R | fium-V4 | tomasbenavidez | — | -57.747 | -59.064 | 0.0% | -132.0 | -3.0 | 1000 | +0.572 |
| 6 | sb3zoo | Gabo-Tor | 8 | -57.810 | -59.354 | 0.0% | -129.0 | -3.0 | 1000 | +0.635 |
| 7 | Franco-Colapinto | famatodlr | 6 | -57.829 | -59.186 | 0.0% | -142.0 | -3.0 | 1000 | +0.654 |
| 8 | tomas-castro-equilibrado | tommycass | 4 | -57.837 | -59.008 | 0.0% | -154.0 | -3.0 | 1000 | +0.662 |
| R | Alan-Schadan | Alanschad | — | -57.841 | -59.452 | 0.0% | -186.0 | -3.0 | 1000 | +0.666 |
| R | ivan-de-pineda-es-inocente-con-features | RamaMusic | — | -57.895 | -59.186 | 0.0% | -176.0 | -3.0 | 1000 | +0.720 |
| R | ivan-de-pineda-105 | RamaMusic | — | -57.929 | -58.962 | 0.0% | -160.0 | -3.0 | 1000 | +0.754 |
| R | ivan-de-pineda-104 | RamaMusic | — | -58.006 | -58.950 | 0.0% | -167.0 | -3.0 | 1000 | +0.831 |
| R | ivan-de-pineda-es-inocente-sin-cos | RamaMusic | — | -58.014 | -59.360 | 0.0% | -151.0 | -3.0 | 1000 | +0.839 |
| R | ivan-de-pineda-103 | RamaMusic | — | -58.019 | -58.990 | 0.0% | -169.0 | -3.0 | 1000 | +0.844 |
| R | ivan-de-pineda-106 | RamaMusic | — | -58.023 | -59.138 | 0.0% | -155.0 | -3.0 | 1000 | +0.848 |
| 9 | ivan-de-pineda-101 | RamaMusic | 2 | -58.043 | -59.416 | 0.0% | -155.0 | -3.0 | 1000 | +0.868 |
| R | lein3 | matilein | — | -58.114 | -59.438 | 0.0% | -149.0 | -3.0 | 1000 | +0.939 |
| R | lein2 | matilein | — | -58.148 | -59.228 | 0.0% | -187.0 | -3.0 | 1000 | +0.973 |
| R | naoagent-greedy | naomicouriel | — | -58.228 | -59.064 | 0.0% | -182.0 | -3.0 | 1000 | +1.053 |
| 10 | gonzalezds | mariagonzalezdelsolar | 1 | -58.248 | -60.034 | 0.0% | -152.0 | -3.0 | 1000 | +1.073 |
| R | ivan-de-pineda-es-inocente-sin-features | RamaMusic | — | -58.294 | -59.248 | 0.0% | -186.0 | -3.0 | 1000 | +1.119 |
| R | ivan-de-pineda-102 | RamaMusic | — | -58.301 | -59.080 | 0.0% | -181.0 | -3.0 | 1000 | +1.126 |
| 11 | valentino-pettazi | ValenPettaz1 | 0 | -58.336 | -59.816 | 0.0% | -149.0 | -3.0 | 1000 | +1.161 |
| R | fium-V1 | tomasbenavidez | — | -58.741 | -59.766 | 0.0% | -161.0 | -3.0 | 1000 | +1.566 |
| R | naoagent-greedy3 | naomicouriel | — | -58.917 | -60.364 | 0.0% | -152.0 | -3.0 | 1000 | +1.742 |
| 12 | mateofreire | mateofreire | 0 | -58.970 | -59.452 | 0.0% | -196.0 | -3.0 | 1000 | +1.795 |
| 13 | agusamblard | agusamblard | 0 | -59.257 | -60.216 | 0.0% | -165.0 | -3.0 | 1000 | +2.082 |
| 14 | leon-alderete | joaquinleondev | 0 | -59.310 | -60.590 | 0.0% | -179.0 | -3.0 | 1000 | +2.135 |
| 15 | naoagent-greedy2 | naomicouriel | 0 | -59.333 | -60.468 | 0.0% | -161.0 | -3.0 | 1000 | +2.158 |
| R | tomasbenavidez | tomasbenavidez | — | -59.372 | -59.928 | 0.0% | -157.0 | -3.0 | 1000 | +2.197 |
| 16 | fium-V3 | tomasbenavidez | 0 | -59.419 | -60.222 | 0.0% | -160.0 | -3.0 | 1000 | +2.244 |
| 17 | domabot2 | Sdomato | 0 | -59.642 | -61.210 | 0.0% | -160.0 | -3.0 | 1000 | +2.467 |
| 18 | matbr | mateobramer | 0 | -59.704 | -61.216 | 0.0% | -129.0 | -3.0 | 1000 | +2.529 |
| 19 | lein | matilein | 0 | -59.877 | -60.294 | 0.0% | -180.0 | -3.0 | 1000 | +2.702 |
| 20 | sgroba | Santi2065 | 0 | -60.074 | -59.796 | 0.0% | -161.0 | -3.0 | 1000 | +2.899 |
| 21 | auto-cipre | CiprianoOss | 0 | -60.302 | -61.328 | 0.0% | -148.0 | -3.0 | 1000 | +3.127 |
| 22 | jazgeller | jazgeller | 0 | -60.339 | -61.520 | 0.0% | -162.0 | -3.0 | 1000 | +3.164 |
| 23 | Meteoro | FacundoFirpo | 0 | -60.682 | -62.440 | 0.0% | -171.0 | -3.0 | 1000 | +3.507 |
| 24 | martin-bianchi | martinbianchi0 | 0 | -61.128 | -62.554 | 0.0% | -145.0 | -3.0 | 1000 | +3.953 |
| 25 | maxi | maxividela2577 | 0 | -61.359 | -63.004 | 0.0% | -172.0 | -3.0 | 1000 | +4.184 |
| 26 | valeriano | Isivaleriano | 0 | -61.487 | -61.228 | 0.0% | -188.0 | -3.0 | 1000 | +4.312 |
| 27 | viaggio | FelipeViaggioFL | 0 | -63.259 | -65.332 | 0.0% | -170.0 | -3.0 | 1000 | +6.084 |
| R | fium-V2 | tomasbenavidez | — | -63.521 | -65.594 | 0.0% | -167.0 | -3.0 | 1000 | +6.346 |
| 28 | joaco-di-cola | joaco1212004 | 0 | -65.656 | -67.556 | 0.0% | -199.0 | -3.0 | 1000 | +8.481 |
| 29 | zoffi | florzoffi | 0 | -65.818 | -66.818 | 0.1% | -200.0 | -3.0 | 1000 | +8.643 |
| R | domabot | Sdomato | — | -67.175 | -69.610 | 0.0% | -167.0 | -3.0 | 1000 | +10.000 |
| 30 | ion_h_RL_TP2 | 72Ion | 0 | -80.179 | -78.134 | 0.0% | -199.0 | -3.0 | 1000 | +23.004 |

## GP Lluvia

_Sensores con ruido gaussiano en posición y velocidad._

| # | Auto | Escudería | Pts | Media | IQM | Sin llegar | Min | Max | Episodios | Dif. al 1° |
|---|------|-----------|----:|-------|-----|-----------:|-----|-----|-----------|-----------|
| R | ivan-de-pineda-106 | RamaMusic | — | -99.960 | -102.236 | 0.0% | -169.0 | -83.0 | 1000 | −0.525 |
| R | ivan-de-pineda-105 | RamaMusic | — | -100.152 | -102.388 | 0.0% | -176.0 | -83.0 | 1000 | −0.333 |
| R | ivan-de-pineda-102 | RamaMusic | — | -100.277 | -101.974 | 0.0% | -176.0 | -83.0 | 1000 | −0.208 |
| R | ivan-de-pineda-103 | RamaMusic | — | -100.382 | -102.450 | 0.0% | -172.0 | -83.0 | 1000 | −0.103 |
| 1 | tomas-castro-equilibrado | tommycass | 25 | -100.485 | -102.648 | 0.0% | -175.0 | -83.0 | 1000 | — |
| 2 | lein | matilein | 18 | -100.563 | -103.400 | 0.0% | -186.0 | -83.0 | 1000 | +0.078 |
| 3 | ivan-de-pineda-101 | RamaMusic | 15 | -100.571 | -101.786 | 0.0% | -173.0 | -83.0 | 1000 | +0.086 |
| R | ivan-de-pineda-104 | RamaMusic | — | -100.616 | -102.922 | 0.0% | -173.0 | -83.0 | 1000 | +0.131 |
| R | naoagent | naomicouriel | — | -101.021 | -103.266 | 0.0% | -174.0 | -83.0 | 1000 | +0.536 |
| 4 | fium-V3 | tomasbenavidez | 12 | -101.088 | -102.022 | 0.0% | -186.0 | -83.0 | 1000 | +0.603 |
| 5 | bravo-andres | Andresbravo9 | 10 | -101.102 | -102.880 | 0.0% | -162.0 | -83.0 | 1000 | +0.617 |
| R | naoagent-greedy | naomicouriel | — | -101.103 | -101.656 | 0.0% | -179.0 | -83.0 | 1000 | +0.618 |
| 6 | domabot2 | Sdomato | 8 | -101.321 | -103.686 | 0.0% | -178.0 | -83.0 | 1000 | +0.836 |
| 7 | valentino-pettazi | ValenPettaz1 | 6 | -101.441 | -103.492 | 0.0% | -160.0 | -83.0 | 1000 | +0.956 |
| R | naoagent-ensemble | naomicouriel | — | -101.768 | -101.994 | 0.0% | -189.0 | -83.0 | 1000 | +1.283 |
| R | ivan-de-pineda-es-inocente-sin-cos | RamaMusic | — | -101.808 | -102.138 | 0.0% | -189.0 | -83.0 | 1000 | +1.323 |
| R | ivan-de-pineda-es-inocente-sin-features | RamaMusic | — | -101.885 | -101.772 | 0.0% | -186.0 | -83.0 | 1000 | +1.400 |
| R | bravo-andres-r1 | Andresbravo9 | — | -102.105 | -102.678 | 0.0% | -167.0 | -83.0 | 1000 | +1.620 |
| R | naoagent-greedy3 | naomicouriel | — | -102.200 | -101.928 | 0.0% | -174.0 | -83.0 | 1000 | +1.715 |
| R | ivan-de-pineda-es-inocente-con-features | RamaMusic | — | -102.255 | -101.862 | 0.0% | -183.0 | -83.0 | 1000 | +1.770 |
| 8 | leon-alderete | joaquinleondev | 4 | -102.486 | -102.160 | 0.0% | -183.0 | -83.0 | 1000 | +2.001 |
| 9 | joaco-di-cola | joaco1212004 | 2 | -103.230 | -105.882 | 0.0% | -192.0 | -83.0 | 1000 | +2.745 |
| 9 | naoagent-greedy2 | naomicouriel | 2 | -103.230 | -102.098 | 0.0% | -177.0 | -83.0 | 1000 | +2.745 |
| 11 | Franco-Colapinto | famatodlr | 0 | -103.258 | -103.960 | 0.0% | -167.0 | -83.0 | 1000 | +2.773 |
| R | bravo-andres-r2 | Andresbravo9 | — | -103.324 | -103.756 | 0.0% | -166.0 | -83.0 | 1000 | +2.839 |
| 12 | mateofreire | mateofreire | 0 | -103.743 | -104.048 | 0.0% | -167.0 | -84.0 | 1000 | +3.258 |
| 13 | maxi | maxividela2577 | 0 | -103.774 | -104.896 | 0.0% | -194.0 | -84.0 | 1000 | +3.289 |
| 14 | DeCruz | BrunoDC-dev | 0 | -103.804 | -103.392 | 0.0% | -176.0 | -83.0 | 1000 | +3.319 |
| 15 | Alan-Schadan-v2 | Alanschad | 0 | -104.049 | -103.880 | 0.0% | -171.0 | -83.0 | 1000 | +3.564 |
| 16 | zoffi | florzoffi | 0 | -104.280 | -105.628 | 0.0% | -182.0 | -83.0 | 1000 | +3.795 |
| 17 | jazgeller | jazgeller | 0 | -104.373 | -104.084 | 0.0% | -182.0 | -83.0 | 1000 | +3.888 |
| R | DeCruz_v2 | BrunoDC-dev | — | -104.736 | -102.696 | 0.0% | -180.0 | -83.0 | 1000 | +4.251 |
| 18 | sgroba | Santi2065 | 0 | -104.912 | -103.818 | 0.2% | -200.0 | -83.0 | 1000 | +4.427 |
| R | fium-V4 | tomasbenavidez | — | -105.019 | -104.376 | 0.0% | -176.0 | -83.0 | 1000 | +4.534 |
| R | tomasbenavidez | tomasbenavidez | — | -105.572 | -102.982 | 0.0% | -199.0 | -83.0 | 1000 | +5.087 |
| 19 | agusamblard | agusamblard | 0 | -105.586 | -103.796 | 0.0% | -197.0 | -83.0 | 1000 | +5.101 |
| 20 | martin-bianchi | martinbianchi0 | 0 | -106.083 | -104.532 | 0.1% | -200.0 | -83.0 | 1000 | +5.598 |
| 21 | salim | athinasalimm | 0 | -106.224 | -102.868 | 0.0% | -183.0 | -83.0 | 1000 | +5.739 |
| 22 | vanafa | VANAFA | 0 | -106.377 | -102.934 | 0.0% | -172.0 | -83.0 | 1000 | +5.892 |
| R | tomas-castro | tommycass | — | -106.729 | -102.804 | 0.0% | -171.0 | -83.0 | 1000 | +6.244 |
| 23 | valeriano | Isivaleriano | 0 | -106.790 | -107.256 | 0.7% | -200.0 | -84.0 | 1000 | +6.305 |
| R | fium-V1 | tomasbenavidez | — | -107.063 | -103.426 | 0.0% | -196.0 | -84.0 | 1000 | +6.578 |
| 24 | gonzalezds | mariagonzalezdelsolar | 0 | -107.371 | -102.788 | 0.0% | -170.0 | -83.0 | 1000 | +6.886 |
| R | lein3 | matilein | — | -107.460 | -102.700 | 0.0% | -173.0 | -83.0 | 1000 | +6.975 |
| R | Alan-Schadan | Alanschad | — | -107.569 | -103.778 | 0.0% | -176.0 | -83.0 | 1000 | +7.084 |
| R | lein2 | matilein | — | -107.947 | -103.168 | 0.0% | -160.0 | -83.0 | 1000 | +7.462 |
| 25 | sb3zoo | Gabo-Tor | 0 | -108.171 | -105.530 | 0.2% | -200.0 | -83.0 | 1000 | +7.686 |
| 26 | viaggio | FelipeViaggioFL | 0 | -108.386 | -103.134 | 0.0% | -188.0 | -83.0 | 1000 | +7.901 |
| R | fium-V2 | tomasbenavidez | — | -109.136 | -105.960 | 0.1% | -200.0 | -84.0 | 1000 | +8.651 |
| 27 | Meteoro | FacundoFirpo | 0 | -110.196 | -104.878 | 0.1% | -200.0 | -83.0 | 1000 | +9.711 |
| 28 | matbr | mateobramer | 0 | -110.346 | -106.632 | 0.0% | -183.0 | -83.0 | 1000 | +9.861 |
| R | domabot | Sdomato | — | -111.638 | -105.518 | 0.3% | -200.0 | -83.0 | 1000 | +11.153 |
| 29 | auto-cipre | CiprianoOss | 0 | -116.572 | -112.482 | 0.0% | -174.0 | -83.0 | 1000 | +16.087 |
| 30 | ion_h_RL_TP2 | 72Ion | 0 | -148.168 | -140.578 | 4.1% | -200.0 | -125.0 | 1000 | +47.683 |

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
| 6 | lein | matilein | 8 | -116.266 | -110.862 | 0.2% | -200.0 | -92.0 | 1000 | +3.988 |
| R | fium-V4 | tomasbenavidez | — | -116.694 | -112.252 | 0.4% | -200.0 | -93.0 | 1000 | +4.416 |
| R | bravo-andres-r1 | Andresbravo9 | — | -116.829 | -111.446 | 0.0% | -193.0 | -92.0 | 1000 | +4.551 |
| R | bravo-andres-r2 | Andresbravo9 | — | -116.930 | -111.028 | 0.0% | -182.0 | -92.0 | 1000 | +4.652 |
| 7 | tomas-castro-equilibrado | tommycass | 6 | -117.999 | -110.830 | 0.1% | -200.0 | -92.0 | 1000 | +5.721 |
| R | ivan-de-pineda-106 | RamaMusic | — | -118.243 | -110.816 | 0.2% | -200.0 | -92.0 | 1000 | +5.965 |
| R | ivan-de-pineda-104 | RamaMusic | — | -118.274 | -110.740 | 0.3% | -200.0 | -92.0 | 1000 | +5.996 |
| R | ivan-de-pineda-105 | RamaMusic | — | -118.723 | -111.188 | 0.3% | -200.0 | -92.0 | 1000 | +6.445 |
| 8 | domabot2 | Sdomato | 4 | -118.738 | -111.758 | 0.2% | -200.0 | -92.0 | 1000 | +6.460 |
| R | ivan-de-pineda-103 | RamaMusic | — | -118.976 | -110.844 | 0.3% | -200.0 | -92.0 | 1000 | +6.698 |
| 9 | maxi | maxividela2577 | 2 | -119.282 | -112.610 | 0.4% | -200.0 | -93.0 | 1000 | +7.004 |
| 10 | joaco-di-cola | joaco1212004 | 1 | -119.523 | -113.392 | 2.2% | -200.0 | -92.0 | 1000 | +7.245 |
| 11 | ivan-de-pineda-101 | RamaMusic | 0 | -120.693 | -113.274 | 0.3% | -200.0 | -92.0 | 1000 | +8.415 |
| 12 | zoffi | florzoffi | 0 | -121.367 | -114.872 | 7.1% | -200.0 | -92.0 | 1000 | +9.089 |
| 13 | mateofreire | mateofreire | 0 | -122.323 | -112.370 | 1.0% | -200.0 | -92.0 | 1000 | +10.045 |
| R | tomas-castro | tommycass | — | -122.620 | -118.376 | 0.0% | -193.0 | -92.0 | 1000 | +10.342 |
| R | naoagent-ensemble | naomicouriel | — | -123.640 | -117.036 | 0.2% | -200.0 | -92.0 | 1000 | +11.362 |
| R | ivan-de-pineda-102 | RamaMusic | — | -123.804 | -114.862 | 2.2% | -200.0 | -92.0 | 1000 | +11.526 |
| 14 | sgroba | Santi2065 | 0 | -124.057 | -113.460 | 1.6% | -200.0 | -93.0 | 1000 | +11.779 |
| 15 | salim | athinasalimm | 0 | -125.186 | -119.948 | 0.0% | -195.0 | -93.0 | 1000 | +12.908 |
| R | ivan-de-pineda-es-inocente-sin-features | RamaMusic | — | -125.251 | -117.268 | 2.9% | -200.0 | -92.0 | 1000 | +12.973 |
| 16 | viaggio | FelipeViaggioFL | 0 | -125.442 | -114.484 | 0.2% | -200.0 | -94.0 | 1000 | +13.164 |
| R | lein2 | matilein | — | -126.332 | -123.906 | 0.0% | -193.0 | -92.0 | 1000 | +14.054 |
| 17 | vanafa | VANAFA | 0 | -126.354 | -120.288 | 0.5% | -200.0 | -93.0 | 1000 | +14.076 |
| 18 | auto-cipre | CiprianoOss | 0 | -126.476 | -122.788 | 0.0% | -154.0 | -99.0 | 1000 | +14.198 |
| R | Alan-Schadan | Alanschad | — | -126.532 | -119.804 | 0.7% | -200.0 | -93.0 | 1000 | +14.254 |
| R | ivan-de-pineda-es-inocente-con-features | RamaMusic | — | -126.765 | -119.776 | 1.5% | -200.0 | -92.0 | 1000 | +14.487 |
| R | naoagent-greedy3 | naomicouriel | — | -126.967 | -121.108 | 0.9% | -200.0 | -92.0 | 1000 | +14.689 |
| 19 | valeriano | Isivaleriano | 0 | -127.281 | -114.172 | 3.9% | -200.0 | -102.0 | 1000 | +15.003 |
| 20 | jazgeller | jazgeller | 0 | -127.327 | -120.268 | 0.1% | -200.0 | -93.0 | 1000 | +15.049 |
| R | ivan-de-pineda-es-inocente-sin-cos | RamaMusic | — | -127.381 | -120.494 | 0.8% | -200.0 | -92.0 | 1000 | +15.103 |
| R | lein3 | matilein | — | -127.464 | -126.000 | 0.0% | -192.0 | -92.0 | 1000 | +15.186 |
| 21 | gonzalezds | mariagonzalezdelsolar | 0 | -127.507 | -123.486 | 0.0% | -186.0 | -93.0 | 1000 | +15.229 |
| 22 | naoagent-greedy2 | naomicouriel | 0 | -128.727 | -122.904 | 0.9% | -200.0 | -92.0 | 1000 | +16.449 |
| 23 | leon-alderete | joaquinleondev | 0 | -129.705 | -122.852 | 2.3% | -200.0 | -93.0 | 1000 | +17.427 |
| 24 | fium-V3 | tomasbenavidez | 0 | -130.158 | -122.592 | 0.4% | -200.0 | -92.0 | 1000 | +17.880 |
| R | naoagent-greedy | naomicouriel | — | -130.435 | -123.528 | 1.9% | -200.0 | -93.0 | 1000 | +18.157 |
| 25 | Meteoro | FacundoFirpo | 0 | -130.904 | -120.308 | 6.0% | -200.0 | -93.0 | 1000 | +18.626 |
| R | DeCruz_v2 | BrunoDC-dev | — | -132.224 | -129.800 | 0.4% | -200.0 | -92.0 | 1000 | +19.946 |
| 26 | agusamblard | agusamblard | 0 | -133.343 | -125.230 | 4.9% | -200.0 | -93.0 | 1000 | +21.065 |
| 27 | sb3zoo | Gabo-Tor | 0 | -133.939 | -128.688 | 0.6% | -200.0 | -93.0 | 1000 | +21.661 |
| R | tomasbenavidez | tomasbenavidez | — | -134.285 | -128.850 | 1.6% | -200.0 | -93.0 | 1000 | +22.007 |
| 28 | martin-bianchi | martinbianchi0 | 0 | -135.643 | -130.480 | 0.3% | -200.0 | -94.0 | 1000 | +23.365 |
| R | domabot | Sdomato | — | -138.948 | -133.360 | 0.6% | -200.0 | -111.0 | 1000 | +26.670 |
| 29 | matbr | mateobramer | 0 | -140.219 | -136.596 | 0.2% | -200.0 | -99.0 | 1000 | +27.941 |
| R | fium-V1 | tomasbenavidez | — | -140.761 | -142.958 | 0.7% | -200.0 | -92.0 | 1000 | +28.483 |
| 30 | ion_h_RL_TP2 | 72Ion | 0 | -154.574 | -147.024 | 10.1% | -200.0 | -134.0 | 1000 | +42.296 |

## GP Otra pista

_La montaña cambia de forma: cos(f·x) con f entre 2.6 y 2.8 (en vez de 3)._

| # | Auto | Escudería | Pts | Media | IQM | Sin llegar | Min | Max | Episodios | Dif. al 1° |
|---|------|-----------|----:|-------|-----|-----------:|-----|-----|-----------|-----------|
| R | lein2 | matilein | — | -95.981 | -96.168 | 0.0% | -109.0 | -82.0 | 1000 | −2.211 |
| R | lein3 | matilein | — | -96.393 | -96.448 | 0.0% | -113.0 | -83.0 | 1000 | −1.799 |
| R | fium-V1 | tomasbenavidez | — | -97.121 | -97.652 | 0.0% | -111.0 | -83.0 | 1000 | −1.071 |
| R | tomas-castro | tommycass | — | -97.286 | -98.346 | 0.0% | -110.0 | -82.0 | 1000 | −0.906 |
| R | DeCruz_v2 | BrunoDC-dev | — | -97.651 | -99.442 | 0.0% | -109.0 | -82.0 | 1000 | −0.541 |
| 1 | fium-V3 | tomasbenavidez | 25 | -98.192 | -100.480 | 0.0% | -110.0 | -82.0 | 1000 | — |
| 2 | naoagent-greedy2 | naomicouriel | 18 | -98.919 | -101.578 | 0.0% | -109.0 | -82.0 | 1000 | +0.727 |
| 3 | gonzalezds | mariagonzalezdelsolar | 15 | -98.962 | -100.764 | 0.0% | -112.0 | -83.0 | 1000 | +0.770 |
| R | ivan-de-pineda-es-inocente-sin-cos | RamaMusic | — | -99.134 | -102.084 | 0.0% | -109.0 | -82.0 | 1000 | +0.942 |
| R | naoagent-greedy3 | naomicouriel | — | -99.197 | -101.904 | 0.0% | -110.0 | -82.0 | 1000 | +1.005 |
| 4 | leon-alderete | joaquinleondev | 12 | -99.202 | -101.910 | 0.0% | -110.0 | -82.0 | 1000 | +1.010 |
| R | ivan-de-pineda-102 | RamaMusic | — | -99.342 | -102.606 | 0.0% | -110.0 | -82.0 | 1000 | +1.150 |
| R | naoagent-greedy | naomicouriel | — | -99.366 | -102.134 | 0.0% | -109.0 | -82.0 | 1000 | +1.174 |
| R | ivan-de-pineda-es-inocente-sin-features | RamaMusic | — | -99.473 | -102.166 | 0.0% | -111.0 | -82.0 | 1000 | +1.281 |
| R | ivan-de-pineda-es-inocente-con-features | RamaMusic | — | -99.569 | -102.144 | 0.0% | -111.0 | -83.0 | 1000 | +1.377 |
| R | tomasbenavidez | tomasbenavidez | — | -100.060 | -102.298 | 0.0% | -122.0 | -83.0 | 1000 | +1.868 |
| 5 | vanafa | VANAFA | 10 | -100.162 | -102.492 | 0.0% | -113.0 | -83.0 | 1000 | +1.970 |
| 6 | ivan-de-pineda-101 | RamaMusic | 8 | -100.175 | -103.304 | 0.0% | -111.0 | -82.0 | 1000 | +1.983 |
| R | naoagent-ensemble | naomicouriel | — | -100.460 | -103.536 | 0.0% | -111.0 | -82.0 | 1000 | +2.268 |
| 7 | Meteoro | FacundoFirpo | 6 | -100.551 | -103.898 | 0.0% | -111.0 | -83.0 | 1000 | +2.359 |
| 8 | mateofreire | mateofreire | 4 | -101.106 | -104.210 | 0.0% | -114.0 | -82.0 | 1000 | +2.914 |
| R | ivan-de-pineda-105 | RamaMusic | — | -101.108 | -105.178 | 0.0% | -111.0 | -82.0 | 1000 | +2.916 |
| R | Alan-Schadan | Alanschad | — | -101.159 | -103.448 | 0.0% | -114.0 | -83.0 | 1000 | +2.967 |
| 9 | viaggio | FelipeViaggioFL | 2 | -101.387 | -105.796 | 0.0% | -112.0 | -82.0 | 1000 | +3.195 |
| R | bravo-andres-r1 | Andresbravo9 | — | -101.458 | -105.860 | 0.0% | -112.0 | -82.0 | 1000 | +3.266 |
| 10 | auto-cipre | CiprianoOss | 1 | -101.474 | -103.940 | 0.0% | -117.0 | -82.0 | 1000 | +3.282 |
| R | ivan-de-pineda-106 | RamaMusic | — | -101.539 | -105.534 | 0.0% | -113.0 | -82.0 | 1000 | +3.347 |
| 11 | tomas-castro-equilibrado | tommycass | 0 | -101.662 | -105.994 | 0.0% | -113.0 | -82.0 | 1000 | +3.470 |
| R | ivan-de-pineda-103 | RamaMusic | — | -101.690 | -105.754 | 0.0% | -113.0 | -82.0 | 1000 | +3.498 |
| R | bravo-andres-r2 | Andresbravo9 | — | -101.889 | -106.284 | 0.0% | -112.0 | -82.0 | 1000 | +3.697 |
| 12 | salim | athinasalimm | 0 | -102.124 | -104.612 | 0.0% | -144.0 | -84.0 | 1000 | +3.932 |
| 13 | jazgeller | jazgeller | 0 | -102.260 | -104.368 | 0.0% | -119.0 | -83.0 | 1000 | +4.068 |
| 14 | Franco-Colapinto | famatodlr | 0 | -102.281 | -107.276 | 0.0% | -114.0 | -82.0 | 1000 | +4.089 |
| R | ivan-de-pineda-104 | RamaMusic | — | -102.476 | -107.082 | 0.0% | -114.0 | -82.0 | 1000 | +4.284 |
| 15 | bravo-andres | Andresbravo9 | 0 | -102.733 | -107.488 | 0.0% | -114.0 | -82.0 | 1000 | +4.541 |
| 16 | domabot2 | Sdomato | 0 | -102.947 | -107.528 | 0.0% | -115.0 | -83.0 | 1000 | +4.755 |
| 17 | sgroba | Santi2065 | 0 | -102.965 | -105.862 | 0.0% | -117.0 | -83.0 | 1000 | +4.773 |
| 18 | maxi | maxividela2577 | 0 | -103.585 | -107.732 | 0.0% | -118.0 | -83.0 | 1000 | +5.393 |
| R | naoagent | naomicouriel | — | -103.726 | -108.442 | 0.0% | -115.0 | -82.0 | 1000 | +5.534 |
| 19 | lein | matilein | 0 | -104.051 | -108.690 | 0.0% | -115.0 | -83.0 | 1000 | +5.859 |
| 20 | DeCruz | BrunoDC-dev | 0 | -104.448 | -108.368 | 0.0% | -121.0 | -83.0 | 1000 | +6.256 |
| R | domabot | Sdomato | — | -104.832 | -108.060 | 0.0% | -121.0 | -83.0 | 1000 | +6.640 |
| 21 | agusamblard | agusamblard | 0 | -106.427 | -107.062 | 0.6% | -200.0 | -85.0 | 1000 | +8.235 |
| 22 | valeriano | Isivaleriano | 0 | -109.701 | -111.716 | 2.2% | -200.0 | -84.0 | 1000 | +11.509 |
| 23 | valentino-pettazi | ValenPettaz1 | 0 | -109.825 | -110.946 | 1.8% | -200.0 | -83.0 | 1000 | +11.633 |
| 24 | sb3zoo | Gabo-Tor | 0 | -111.205 | -112.318 | 0.7% | -200.0 | -83.0 | 1000 | +13.013 |
| 25 | zoffi | florzoffi | 0 | -111.519 | -109.972 | 4.8% | -200.0 | -83.0 | 1000 | +13.327 |
| 26 | martin-bianchi | martinbianchi0 | 0 | -112.161 | -110.708 | 0.1% | -200.0 | -86.0 | 1000 | +13.969 |
| R | fium-V4 | tomasbenavidez | — | -112.716 | -113.488 | 1.4% | -200.0 | -85.0 | 1000 | +14.524 |
| 27 | Alan-Schadan-v2 | Alanschad | 0 | -112.926 | -111.050 | 4.7% | -200.0 | -84.0 | 1000 | +14.734 |
| 28 | joaco-di-cola | joaco1212004 | 0 | -114.668 | -120.210 | 0.0% | -130.0 | -84.0 | 1000 | +16.476 |
| R | fium-V2 | tomasbenavidez | — | -128.591 | -113.772 | 19.5% | -200.0 | -83.0 | 1000 | +30.399 |
| 29 | matbr | mateobramer | 0 | -140.896 | -137.290 | 2.6% | -200.0 | -91.0 | 1000 | +42.704 |
| 30 | ion_h_RL_TP2 | 72Ion | 0 | -145.736 | -141.406 | 0.0% | -179.0 | -129.0 | 1000 | +47.544 |
