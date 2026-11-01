# 🏆 Leaderboard — Campeonato RL (DQN)

Entorno base: `MountainCar-v0` · 5 circuitos · Ranking por **MEDIA** en cada circuito · Actualizado: 2026-11-01 17:46 UTC

Puntos por circuito: 25, 18, 15, 12, 10, 8, 6, 4, 2, 1 (del 1° al 10°). La misma policy corre en todos los circuitos. Detalle de cada uno en el README.

**Un auto titular por escudería** (cuenta de GitHub): es el único que suma puntos y ocupa posiciones. Es el auto de la escudería que más puntos suma contra los titulares de las demás. El resto son autos de reserva: aparecen abajo, pero no le sacan puestos a nadie.

## 🏁 Campeonato

| # | Auto | Escudería | **Pts** | Estándar | Largada libre | Lluvia | Motor débil | Otra pista |
|---|------|-----------|-----:|:---:|:---:|:---:|:---:|:---:|
| 🥇 | sally-m | athinasalimm | **56** | 1° (25) | 1° (25) | 27° | 20° | 7° (6) |
| 🥈 | Larpest-v5 | ginerJuanUdesa | **42** | 25° | 3° (15) | 9° (2) | 1° (25) | 31° |
| 🥉 | bravo-andres | Andresbravo9 | **42** | 4° (12) | 4° (12) | 21° | 23° | 2° (18) |
| 4 | ivan-de-pineda-102 | RamaMusic | **39** | 7° (6) | 17° | 1° (25) | 16° | 6° (8) |
| 5 | naoagent-greedy | naomicouriel | **39** | 3° (15) | 14° | 4° (12) | 24° | 4° (12) |
| 6 | vanafa | VANAFA | **32** | 2° (18) | 5° (10) | 24° | 21° | 8° (4) |
| 7 | fium-V5 | tomasbenavidez | **31** | 31° | 7° (6) | 32° | 33° | 1° (25) |
| 8 | DeCruz | BrunoDC-dev | **26** | 14° | 2° (18) | 16° | 6° (8) | 22° |
| 9 | gonzalezds | mariagonzalezdelsolar | **23** | 6° (8) | 16° | 26° | 27° | 3° (15) |
| 10 | Alan-Schadan-v3 | Alanschad | **23** | 27° | 6° (8) | 17° | 3° (15) | 30° |
| 11 | leon-alderete | joaquinleondev | **21** | 5° (10) | 19° | 10° (1) | 28° | 5° (10) |
| 12 | valentino-pettazi-5 | ValenPettaz1 | **20** | 28° | 13° | 6° (8) | 4° (12) | 25° |
| 13 | tomas-castro-equilibrado | tommycass | **19** | 15° | 12° | 2° (18) | 10° (1) | 14° |
| 14 | lein | matilein | **19** | 21° | 22° | 3° (15) | 8° (4) | 21° |
| 15 | nixons | Anaholcman | **18** | 29° | 30° | 11° | 2° (18) | 32° |
| 16 | agusamblard-v4 | agusamblard | **16** | 22° | 11° | 7° (6) | 5° (10) | 23° |
| 17 | domabot2 | Sdomato | **10** | 19° | 20° | 5° (10) | 11° | 17° |
| 18 | frangiavarini-exp12 | frangiavarini | **10** | 8° (4) | 8° (4) | 23° | 18° | 9° (2) |
| 19 | Franco-Colapinto | famatodlr | **7** | 20° | 10° (1) | 13° | 7° (6) | 16° |
| 20 | espero-no-ser-ultimo | Tadeo-Casiraghi | **6** | 18° | 15° | 8° (4) | 9° (2) | 20° |
| 21 | Meteoro | FacundoFirpo | **3** | 9° (2) | 26° | 30° | 29° | 10° (1) |
| 22 | sb3zoo | Gabo-Tor | **2** | 16° | 9° (2) | 28° | 30° | 26° |
| 23 | jazgeller | jazgeller | **1** | 10° (1) | 25° | 19° | 26° | 15° |
| 24 | mateofreire | mateofreire | **0** | 24° | 18° | 14° | 15° | 11° |
| 25 | martin-bianchi | martinbianchi0 | **0** | 11° | 27° | 22° | 31° | 28° |
| 26 | viaggio | FelipeViaggioFL | **0** | 12° | 31° | 29° | 19° | 12° |
| 27 | joaco-di-cola | joaco1212004 | **0** | 30° | 32° | 12° | 13° | 29° |
| 28 | maxi | maxividela2577 | **0** | 23° | 28° | 15° | 12° | 19° |
| 29 | sgroba | Santi2065 | **0** | 13° | 23° | 20° | 17° | 18° |
| 30 | auto-cipre | CiprianoOss | **0** | 33° | 24° | 33° | 22° | 13° |
| 31 | zoffi | florzoffi | **0** | 26° | 33° | 18° | 14° | 27° |
| 32 | matbr | mateobramer | **0** | 17° | 21° | 31° | 32° | 33° |
| 33 | valeriano | Isivaleriano | **0** | 32° | 29° | 25° | 25° | 24° |
| 34 | ion_h_RL_TP2 | 72Ion | **0** | 34° | 34° | 34° | 34° | 34° |

## 🔧 Autos de reserva

No suman ni ocupan posiciones. Las posiciones son las que tendría cada auto si fuera el titular de su escudería (contra los titulares de las demás).

| Auto | Escudería | Pts como titular | Estándar | Largada libre | Lluvia | Motor débil | Otra pista |
|------|-----------|-----:|:---:|:---:|:---:|:---:|:---:|
| agusamblard-motor | agusamblard | 18 | 28° | 18° | 32° | 2° (18) | 31° |
| agusamblard | agusamblard | 6 | 7° (6) | 18° | 21° | 29° | 23° |
| Alan-Schadan-v4 | Alanschad | 23 | 28° | 6° (8) | 17° | 3° (15) | 31° |
| Alan-Schadan-v2 | Alanschad | 18 | 25° | 7° (6) | 17° | 4° (12) | 29° |
| Alan-Schadan | Alanschad | 6 | 7° (6) | 12° | 26° | 23° | 12° |
| bravo-andres-r4 | Andresbravo9 | 38 | 5° (10) | 5° (10) | 20° | 14° | 2° (18) |
| bravo-andres-r1 | Andresbravo9 | 26 | 18° | 6° (8) | 5° (10) | 6° (8) | 22° |
| bravo-andres-r5 | Andresbravo9 | 24 | 18° | 6° (8) | 6° (8) | 6° (8) | 22° |
| bravo-andres-r2 | Andresbravo9 | 22 | 22° | 4° (12) | 11° | 5° (10) | 23° |
| salim | athinasalimm | 18 | 6° (8) | 5° (10) | 23° | 19° | 14° |
| DeCruz_v2 | BrunoDC-dev | 24 | 11° | 7° (6) | 19° | 29° | 2° (18) |
| Larpest-v1 | ginerJuanUdesa | 40 | 25° | 3° (15) | 32° | 29° | 1° (25) |
| Larpest-v2 | ginerJuanUdesa | 40 | 29° | 3° (15) | 32° | 31° | 1° (25) |
| Larper-v1 | ginerJuanUdesa | 40 | 29° | 3° (15) | 33° | 31° | 1° (25) |
| Sloppeitors-v1 | ginerJuanUdesa | 36 | 21° | 2° (18) | 32° | 29° | 2° (18) |
| Wachinators-v4 | ginerJuanUdesa | 36 | 25° | 2° (18) | 32° | 30° | 2° (18) |
| Larpest-v4 | ginerJuanUdesa | 35 | 25° | 3° (15) | 9° (2) | 2° (18) | 30° |
| Wachinators-v3 | ginerJuanUdesa | 34 | 25° | 3° (15) | 10° (1) | 2° (18) | 31° |
| Larpest-v3 | ginerJuanUdesa | 27 | 7° (6) | 5° (10) | 10° (1) | 13° | 5° (10) |
| Wachinators-v2 | ginerJuanUdesa | 26 | 25° | 5° (10) | 10° (1) | 3° (15) | 31° |
| Wachinators-v1 | ginerJuanUdesa | 22 | 13° | 8° (4) | 25° | 29° | 2° (18) |
| Wachinator-v1 | ginerJuanUdesa | 18 | 29° | 15° | 33° | 33° | 2° (18) |
| lein2 | matilein | 18 | 32° | 15° | 27° | 20° | 2° (18) |
| lein3 | matilein | 18 | 32° | 15° | 26° | 26° | 2° (18) |
| naoagent-greedy2 | naomicouriel | 33 | 2° (18) | 19° | 11° | 27° | 3° (15) |
| naoagent-greedy3 | naomicouriel | 32 | 2° (18) | 17° | 9° (2) | 24° | 4° (12) |
| naoagent-ensemble | naomicouriel | 27 | 15° | 8° (4) | 3° (15) | 6° (8) | 18° |
| naoagent | naomicouriel | 26 | 19° | 7° (6) | 4° (12) | 6° (8) | 19° |
| ivan-de-pineda-105 | RamaMusic | 25 | 12° | 14° | 1° (25) | 11° | 11° |
| ivan-de-pineda-106 | RamaMusic | 25 | 12° | 14° | 1° (25) | 11° | 13° |
| ivan-de-pineda-103 | RamaMusic | 25 | 13° | 14° | 1° (25) | 12° | 14° |
| ivan-de-pineda-101 | RamaMusic | 25 | 7° (6) | 14° | 3° (15) | 14° | 8° (4) |
| ivan-de-pineda-es-inocente-sin-cos | RamaMusic | 24 | 5° (10) | 14° | 8° (4) | 26° | 5° (10) |
| ivan-de-pineda-es-inocente-con-features | RamaMusic | 23 | 3° (15) | 14° | 9° (2) | 23° | 7° (6) |
| ivan-de-pineda-es-inocente-sin-features | RamaMusic | 22 | 4° (12) | 17° | 8° (4) | 18° | 7° (6) |
| ivan-de-pineda-104 | RamaMusic | 15 | 17° | 14° | 3° (15) | 11° | 16° |
| ivan-de-pineda-107 | RamaMusic | 10 | 19° | 12° | 5° (10) | 11° | 14° |
| domabot4 | Sdomato | 6 | 20° | 25° | 28° | 7° (6) | 18° |
| domabot3 | Sdomato | 0 | 24° | 18° | 26° | 11° | 18° |
| domabot | Sdomato | 0 | 17° | 33° | 31° | 31° | 22° |
| fium-V3 | tomasbenavidez | 35 | 11° | 19° | 5° (10) | 29° | 1° (25) |
| fium-V1 | tomasbenavidez | 25 | 23° | 17° | 26° | 33° | 1° (25) |
| fium-V2 | tomasbenavidez | 15 | 30° | 31° | 30° | 3° (15) | 32° |
| tomasbenavidez | tomasbenavidez | 8 | 9° (2) | 19° | 22° | 31° | 7° (6) |
| fium-V4 | tomasbenavidez | 6 | 23° | 8° (4) | 21° | 9° (2) | 28° |
| tomas-castro | tommycass | 24 | 20° | 7° (6) | 24° | 15° | 2° (18) |
| valentino-pettazi | ValenPettaz1 | 20 | 23° | 17° | 6° (8) | 4° (12) | 25° |
| valentino-pettazi-3 | ValenPettaz1 | 18 | 13° | 14° | 2° (18) | 11° | 17° |
| valentino-pettazi-4 | ValenPettaz1 | 18 | 21° | 18° | 6° (8) | 5° (10) | 23° |
| valentino-pettazi-2 | ValenPettaz1 | 13 | 18° | 15° | 4° (12) | 10° (1) | 17° |
| SilverArrow | VANAFA | 18 | 13° | 5° (10) | 9° (2) | 7° (6) | 16° |

## GP Estándar

_MountainCar-v0 tal cual._

| # | Auto | Escudería | Pts | Media | IQM | Sin llegar | Min | Max | Episodios | Dif. al 1° |
|---|------|-----------|----:|-------|-----|-----------:|-----|-----|-----------|-----------|
| 1 | sally-m | athinasalimm | 25 | -97.409 | -100.244 | 0.0% | -104.0 | -83.0 | 1000 | — |
| R | naoagent-greedy3 | naomicouriel | — | -97.423 | -100.268 | 0.0% | -104.0 | -83.0 | 1000 | +0.014 |
| R | naoagent-greedy2 | naomicouriel | — | -97.428 | -100.276 | 0.0% | -104.0 | -83.0 | 1000 | +0.019 |
| 2 | vanafa | VANAFA | 18 | -97.430 | -100.282 | 0.0% | -104.0 | -83.0 | 1000 | +0.021 |
| R | ivan-de-pineda-es-inocente-con-features | RamaMusic | — | -97.434 | -100.282 | 0.0% | -104.0 | -83.0 | 1000 | +0.025 |
| 3 | naoagent-greedy | naomicouriel | 15 | -97.436 | -100.260 | 0.0% | -104.0 | -83.0 | 1000 | +0.027 |
| R | ivan-de-pineda-es-inocente-sin-features | RamaMusic | — | -97.480 | -100.314 | 0.0% | -104.0 | -83.0 | 1000 | +0.071 |
| 4 | bravo-andres | Andresbravo9 | 12 | -97.490 | -100.276 | 0.0% | -104.0 | -83.0 | 1000 | +0.081 |
| R | ivan-de-pineda-es-inocente-sin-cos | RamaMusic | — | -97.544 | -100.458 | 0.0% | -104.0 | -83.0 | 1000 | +0.135 |
| 5 | leon-alderete | joaquinleondev | 10 | -97.549 | -100.408 | 0.0% | -104.0 | -83.0 | 1000 | +0.140 |
| R | bravo-andres-r4 | Andresbravo9 | — | -97.564 | -100.356 | 0.0% | -104.0 | -83.0 | 1000 | +0.155 |
| 6 | gonzalezds | mariagonzalezdelsolar | 8 | -97.590 | -100.334 | 0.0% | -105.0 | -83.0 | 1000 | +0.181 |
| R | salim | athinasalimm | — | -97.613 | -100.276 | 0.0% | -104.0 | -83.0 | 1000 | +0.204 |
| R | Larpest-v3 | ginerJuanUdesa | — | -97.668 | -100.460 | 0.0% | -104.0 | -83.0 | 1000 | +0.259 |
| R | ivan-de-pineda-101 | RamaMusic | — | -97.736 | -100.750 | 0.0% | -104.0 | -83.0 | 1000 | +0.327 |
| R | Alan-Schadan | Alanschad | — | -97.754 | -100.498 | 0.0% | -104.0 | -83.0 | 1000 | +0.345 |
| R | agusamblard | agusamblard | — | -97.756 | -100.484 | 0.0% | -105.0 | -83.0 | 1000 | +0.347 |
| 7 | ivan-de-pineda-102 | RamaMusic | 6 | -97.776 | -100.806 | 0.0% | -104.0 | -83.0 | 1000 | +0.367 |
| 8 | frangiavarini-exp12 | frangiavarini | 4 | -97.904 | -100.918 | 0.0% | -104.0 | -83.0 | 1000 | +0.495 |
| R | tomasbenavidez | tomasbenavidez | — | -97.911 | -100.694 | 0.0% | -104.0 | -83.0 | 1000 | +0.502 |
| 9 | Meteoro | FacundoFirpo | 2 | -97.934 | -100.976 | 0.0% | -104.0 | -83.0 | 1000 | +0.525 |
| 10 | jazgeller | jazgeller | 1 | -97.958 | -100.822 | 0.0% | -108.0 | -83.0 | 1000 | +0.549 |
| R | DeCruz_v2 | BrunoDC-dev | — | -98.071 | -100.854 | 0.0% | -107.0 | -84.0 | 1000 | +0.662 |
| R | fium-V3 | tomasbenavidez | — | -98.177 | -100.828 | 0.0% | -105.0 | -83.0 | 1000 | +0.768 |
| 11 | martin-bianchi | martinbianchi0 | 0 | -98.282 | -100.826 | 0.0% | -106.0 | -83.0 | 1000 | +0.873 |
| 12 | viaggio | FelipeViaggioFL | 0 | -98.343 | -101.658 | 0.0% | -104.0 | -83.0 | 1000 | +0.934 |
| R | Wachinators-v1 | ginerJuanUdesa | — | -98.406 | -101.306 | 0.0% | -114.0 | -83.0 | 1000 | +0.997 |
| R | valentino-pettazi-3 | ValenPettaz1 | — | -98.406 | -101.806 | 0.0% | -104.0 | -83.0 | 1000 | +0.997 |
| R | ivan-de-pineda-105 | RamaMusic | — | -98.508 | -102.030 | 0.0% | -104.0 | -83.0 | 1000 | +1.099 |
| R | ivan-de-pineda-106 | RamaMusic | — | -98.579 | -102.020 | 0.0% | -105.0 | -83.0 | 1000 | +1.170 |
| 13 | sgroba | Santi2065 | 0 | -98.663 | -101.698 | 0.0% | -106.0 | -83.0 | 1000 | +1.254 |
| R | ivan-de-pineda-103 | RamaMusic | — | -98.782 | -102.210 | 0.0% | -105.0 | -83.0 | 1000 | +1.373 |
| R | SilverArrow | VANAFA | — | -98.865 | -102.346 | 0.0% | -106.0 | -83.0 | 1000 | +1.456 |
| 14 | DeCruz | BrunoDC-dev | 0 | -98.927 | -102.420 | 0.0% | -104.0 | -83.0 | 1000 | +1.518 |
| 15 | tomas-castro-equilibrado | tommycass | 0 | -99.025 | -102.460 | 0.0% | -106.0 | -83.0 | 1000 | +1.616 |
| R | naoagent-ensemble | naomicouriel | — | -99.111 | -102.670 | 0.0% | -104.0 | -83.0 | 1000 | +1.702 |
| 16 | sb3zoo | Gabo-Tor | 0 | -99.114 | -101.784 | 0.0% | -108.0 | -84.0 | 1000 | +1.705 |
| R | domabot | Sdomato | — | -99.252 | -101.780 | 0.0% | -106.0 | -84.0 | 1000 | +1.843 |
| 17 | matbr | mateobramer | 0 | -99.276 | -102.014 | 0.0% | -106.0 | -84.0 | 1000 | +1.867 |
| R | valentino-pettazi-2 | ValenPettaz1 | — | -99.294 | -103.312 | 0.0% | -105.0 | -84.0 | 1000 | +1.885 |
| R | ivan-de-pineda-104 | RamaMusic | — | -99.307 | -103.018 | 0.0% | -106.0 | -83.0 | 1000 | +1.898 |
| 18 | espero-no-ser-ultimo | Tadeo-Casiraghi | 0 | -99.315 | -103.292 | 0.0% | -104.0 | -83.0 | 1000 | +1.906 |
| R | bravo-andres-r1 | Andresbravo9 | — | -99.341 | -102.522 | 0.0% | -104.0 | -83.0 | 1000 | +1.932 |
| R | bravo-andres-r5 | Andresbravo9 | — | -99.494 | -103.084 | 0.0% | -105.0 | -83.0 | 1000 | +2.085 |
| 19 | domabot2 | Sdomato | 0 | -99.526 | -103.570 | 0.0% | -104.0 | -84.0 | 1000 | +2.117 |
| R | naoagent | naomicouriel | — | -99.560 | -103.346 | 0.0% | -105.0 | -83.0 | 1000 | +2.151 |
| R | ivan-de-pineda-107 | RamaMusic | — | -99.620 | -103.046 | 0.0% | -107.0 | -83.0 | 1000 | +2.211 |
| 20 | Franco-Colapinto | famatodlr | 0 | -99.734 | -103.508 | 0.0% | -107.0 | -83.0 | 1000 | +2.325 |
| R | valentino-pettazi-4 | ValenPettaz1 | — | -99.978 | -103.798 | 0.0% | -104.0 | -83.0 | 1000 | +2.569 |
| R | domabot4 | Sdomato | — | -100.003 | -103.400 | 0.0% | -106.0 | -84.0 | 1000 | +2.594 |
| R | Sloppeitors-v1 | ginerJuanUdesa | — | -100.011 | -101.438 | 0.0% | -141.0 | -83.0 | 1000 | +2.602 |
| R | tomas-castro | tommycass | — | -100.025 | -100.934 | 0.0% | -147.0 | -83.0 | 1000 | +2.616 |
| 21 | lein | matilein | 0 | -100.036 | -103.614 | 0.0% | -105.0 | -84.0 | 1000 | +2.627 |
| 22 | agusamblard-v4 | agusamblard | 0 | -100.043 | -103.068 | 0.0% | -104.0 | -83.0 | 1000 | +2.634 |
| R | fium-V1 | tomasbenavidez | — | -100.090 | -102.276 | 0.0% | -127.0 | -84.0 | 1000 | +2.681 |
| R | bravo-andres-r2 | Andresbravo9 | — | -100.113 | -102.910 | 0.0% | -104.0 | -83.0 | 1000 | +2.704 |
| R | fium-V4 | tomasbenavidez | — | -100.277 | -103.484 | 0.0% | -105.0 | -83.0 | 1000 | +2.868 |
| R | valentino-pettazi | ValenPettaz1 | — | -100.304 | -103.054 | 0.0% | -105.0 | -83.0 | 1000 | +2.895 |
| 23 | maxi | maxividela2577 | 0 | -100.353 | -104.166 | 0.0% | -107.0 | -84.0 | 1000 | +2.944 |
| 24 | mateofreire | mateofreire | 0 | -100.362 | -103.408 | 0.0% | -110.0 | -85.0 | 1000 | +2.953 |
| R | Wachinators-v4 | ginerJuanUdesa | — | -100.449 | -101.658 | 0.0% | -135.0 | -83.0 | 1000 | +3.040 |
| R | Wachinators-v2 | ginerJuanUdesa | — | -100.473 | -102.574 | 0.0% | -104.0 | -83.0 | 1000 | +3.064 |
| R | Larpest-v4 | ginerJuanUdesa | — | -100.541 | -102.672 | 0.0% | -104.0 | -83.0 | 1000 | +3.132 |
| R | domabot3 | Sdomato | — | -100.713 | -104.222 | 0.0% | -106.0 | -86.0 | 1000 | +3.304 |
| R | Wachinators-v3 | ginerJuanUdesa | — | -100.727 | -102.798 | 0.0% | -104.0 | -83.0 | 1000 | +3.318 |
| R | Alan-Schadan-v2 | Alanschad | — | -100.745 | -103.642 | 0.0% | -105.0 | -83.0 | 1000 | +3.336 |
| 25 | Larpest-v5 | ginerJuanUdesa | 0 | -101.291 | -103.582 | 0.0% | -105.0 | -83.0 | 1000 | +3.882 |
| R | Larpest-v1 | ginerJuanUdesa | — | -101.323 | -101.688 | 0.0% | -143.0 | -83.0 | 1000 | +3.914 |
| 26 | zoffi | florzoffi | 0 | -101.328 | -103.064 | 0.0% | -111.0 | -83.0 | 1000 | +3.919 |
| 27 | Alan-Schadan-v3 | Alanschad | 0 | -101.561 | -103.852 | 0.0% | -104.0 | -83.0 | 1000 | +4.152 |
| 28 | valentino-pettazi-5 | ValenPettaz1 | 0 | -101.615 | -104.252 | 0.0% | -105.0 | -84.0 | 1000 | +4.206 |
| R | Alan-Schadan-v4 | Alanschad | — | -101.753 | -103.976 | 0.0% | -104.0 | -83.0 | 1000 | +4.344 |
| R | agusamblard-motor | agusamblard | — | -101.893 | -103.652 | 0.0% | -105.0 | -83.0 | 1000 | +4.484 |
| 29 | nixons | Anaholcman | 0 | -102.409 | -104.028 | 0.0% | -105.0 | -83.0 | 1000 | +5.000 |
| R | Wachinator-v1 | ginerJuanUdesa | — | -102.682 | -103.352 | 0.0% | -158.0 | -83.0 | 1000 | +5.273 |
| R | fium-V2 | tomasbenavidez | — | -102.789 | -104.438 | 0.0% | -106.0 | -84.0 | 1000 | +5.380 |
| R | Larpest-v2 | ginerJuanUdesa | — | -102.891 | -102.984 | 0.0% | -160.0 | -84.0 | 1000 | +5.482 |
| R | Larper-v1 | ginerJuanUdesa | — | -102.947 | -102.994 | 0.0% | -150.0 | -84.0 | 1000 | +5.538 |
| 30 | joaco-di-cola | joaco1212004 | 0 | -102.982 | -107.744 | 0.0% | -109.0 | -83.0 | 1000 | +5.573 |
| 31 | fium-V5 | tomasbenavidez | 0 | -103.920 | -102.710 | 0.0% | -152.0 | -83.0 | 1000 | +6.511 |
| 32 | valeriano | Isivaleriano | 0 | -104.107 | -106.666 | 0.0% | -113.0 | -84.0 | 1000 | +6.698 |
| R | lein3 | matilein | — | -104.276 | -101.390 | 0.0% | -171.0 | -83.0 | 1000 | +6.867 |
| R | lein2 | matilein | — | -104.545 | -101.626 | 0.3% | -200.0 | -83.0 | 1000 | +7.136 |
| 33 | auto-cipre | CiprianoOss | 0 | -109.595 | -108.150 | 0.0% | -156.0 | -83.0 | 1000 | +12.186 |
| 34 | ion_h_RL_TP2 | 72Ion | 0 | -144.008 | -136.444 | 0.4% | -200.0 | -126.0 | 1000 | +46.599 |

## GP Largada libre

_Largan desde cualquier punto de la pista y con velocidad inicial._

| # | Auto | Escudería | Pts | Media | IQM | Sin llegar | Min | Max | Episodios | Dif. al 1° |
|---|------|-----------|----:|-------|-----|-----------:|-----|-----|-----------|-----------|
| 1 | sally-m | athinasalimm | 25 | -57.087 | -58.832 | 0.0% | -140.0 | -3.0 | 1000 | — |
| R | Sloppeitors-v1 | ginerJuanUdesa | — | -57.142 | -58.880 | 0.0% | -124.0 | -3.0 | 1000 | +0.055 |
| R | Wachinators-v4 | ginerJuanUdesa | — | -57.142 | -58.864 | 0.0% | -124.0 | -3.0 | 1000 | +0.055 |
| 2 | DeCruz | BrunoDC-dev | 18 | -57.175 | -58.862 | 0.0% | -119.0 | -3.0 | 1000 | +0.088 |
| R | Wachinators-v3 | ginerJuanUdesa | — | -57.227 | -58.850 | 0.0% | -133.0 | -3.0 | 1000 | +0.140 |
| R | Larpest-v2 | ginerJuanUdesa | — | -57.238 | -58.936 | 0.0% | -131.0 | -3.0 | 1000 | +0.151 |
| R | Larper-v1 | ginerJuanUdesa | — | -57.253 | -58.942 | 0.0% | -136.0 | -3.0 | 1000 | +0.166 |
| 3 | Larpest-v5 | ginerJuanUdesa | 15 | -57.261 | -58.874 | 0.0% | -137.0 | -3.0 | 1000 | +0.174 |
| R | Larpest-v1 | ginerJuanUdesa | — | -57.311 | -58.978 | 0.0% | -140.0 | -3.0 | 1000 | +0.224 |
| R | Larpest-v4 | ginerJuanUdesa | — | -57.319 | -58.868 | 0.0% | -148.0 | -3.0 | 1000 | +0.232 |
| R | bravo-andres-r2 | Andresbravo9 | — | -57.320 | -58.908 | 0.0% | -128.0 | -3.0 | 1000 | +0.233 |
| 4 | bravo-andres | Andresbravo9 | 12 | -57.341 | -58.936 | 0.0% | -149.0 | -3.0 | 1000 | +0.254 |
| 5 | vanafa | VANAFA | 10 | -57.351 | -59.018 | 0.0% | -141.0 | -3.0 | 1000 | +0.264 |
| R | Larpest-v3 | ginerJuanUdesa | — | -57.390 | -58.950 | 0.0% | -147.0 | -3.0 | 1000 | +0.303 |
| R | Alan-Schadan-v4 | Alanschad | — | -57.393 | -59.152 | 0.0% | -112.0 | -3.0 | 1000 | +0.306 |
| R | salim | athinasalimm | — | -57.393 | -58.892 | 0.0% | -142.0 | -3.0 | 1000 | +0.306 |
| R | SilverArrow | VANAFA | — | -57.394 | -58.948 | 0.0% | -143.0 | -3.0 | 1000 | +0.307 |
| R | bravo-andres-r4 | Andresbravo9 | — | -57.399 | -58.968 | 0.0% | -146.0 | -3.0 | 1000 | +0.312 |
| R | Wachinators-v2 | ginerJuanUdesa | — | -57.430 | -58.880 | 0.0% | -150.0 | -3.0 | 1000 | +0.343 |
| 6 | Alan-Schadan-v3 | Alanschad | 8 | -57.463 | -59.186 | 0.0% | -121.0 | -3.0 | 1000 | +0.376 |
| R | tomas-castro | tommycass | — | -57.466 | -58.982 | 0.0% | -143.0 | -3.0 | 1000 | +0.379 |
| R | bravo-andres-r1 | Andresbravo9 | — | -57.492 | -58.906 | 0.0% | -147.0 | -3.0 | 1000 | +0.405 |
| R | bravo-andres-r5 | Andresbravo9 | — | -57.524 | -58.934 | 0.0% | -159.0 | -3.0 | 1000 | +0.437 |
| R | naoagent | naomicouriel | — | -57.585 | -58.898 | 0.0% | -163.0 | -3.0 | 1000 | +0.498 |
| 7 | fium-V5 | tomasbenavidez | 6 | -57.606 | -59.036 | 0.0% | -158.0 | -3.0 | 1000 | +0.519 |
| R | Alan-Schadan-v2 | Alanschad | — | -57.654 | -59.382 | 0.0% | -119.0 | -3.0 | 1000 | +0.567 |
| R | DeCruz_v2 | BrunoDC-dev | — | -57.695 | -59.052 | 0.0% | -147.0 | -3.0 | 1000 | +0.608 |
| R | naoagent-ensemble | naomicouriel | — | -57.698 | -58.910 | 0.0% | -170.0 | -3.0 | 1000 | +0.611 |
| 8 | frangiavarini-exp12 | frangiavarini | 4 | -57.728 | -59.366 | 0.0% | -115.0 | -3.0 | 1000 | +0.641 |
| R | fium-V4 | tomasbenavidez | — | -57.747 | -59.064 | 0.0% | -132.0 | -3.0 | 1000 | +0.660 |
| R | Wachinators-v1 | ginerJuanUdesa | — | -57.785 | -59.024 | 0.0% | -171.0 | -3.0 | 1000 | +0.698 |
| 9 | sb3zoo | Gabo-Tor | 2 | -57.810 | -59.354 | 0.0% | -129.0 | -3.0 | 1000 | +0.723 |
| 10 | Franco-Colapinto | famatodlr | 1 | -57.829 | -59.186 | 0.0% | -142.0 | -3.0 | 1000 | +0.742 |
| 11 | agusamblard-v4 | agusamblard | 0 | -57.831 | -58.968 | 0.0% | -166.0 | -3.0 | 1000 | +0.744 |
| 12 | tomas-castro-equilibrado | tommycass | 0 | -57.837 | -59.008 | 0.0% | -154.0 | -3.0 | 1000 | +0.750 |
| R | ivan-de-pineda-107 | RamaMusic | — | -57.837 | -59.074 | 0.0% | -152.0 | -3.0 | 1000 | +0.750 |
| R | Alan-Schadan | Alanschad | — | -57.841 | -59.452 | 0.0% | -186.0 | -3.0 | 1000 | +0.754 |
| 13 | valentino-pettazi-5 | ValenPettaz1 | 0 | -57.866 | -58.962 | 0.0% | -151.0 | -3.0 | 1000 | +0.779 |
| R | ivan-de-pineda-es-inocente-con-features | RamaMusic | — | -57.895 | -59.186 | 0.0% | -176.0 | -3.0 | 1000 | +0.808 |
| R | ivan-de-pineda-105 | RamaMusic | — | -57.929 | -58.962 | 0.0% | -160.0 | -3.0 | 1000 | +0.842 |
| R | ivan-de-pineda-104 | RamaMusic | — | -58.006 | -58.950 | 0.0% | -167.0 | -3.0 | 1000 | +0.919 |
| R | ivan-de-pineda-es-inocente-sin-cos | RamaMusic | — | -58.014 | -59.360 | 0.0% | -151.0 | -3.0 | 1000 | +0.927 |
| R | ivan-de-pineda-103 | RamaMusic | — | -58.019 | -58.990 | 0.0% | -169.0 | -3.0 | 1000 | +0.932 |
| R | ivan-de-pineda-106 | RamaMusic | — | -58.023 | -59.138 | 0.0% | -155.0 | -3.0 | 1000 | +0.936 |
| R | ivan-de-pineda-101 | RamaMusic | — | -58.043 | -59.416 | 0.0% | -155.0 | -3.0 | 1000 | +0.956 |
| 14 | naoagent-greedy | naomicouriel | 0 | -58.056 | -58.982 | 0.0% | -166.0 | -3.0 | 1000 | +0.969 |
| R | valentino-pettazi-3 | ValenPettaz1 | — | -58.098 | -59.198 | 0.0% | -156.0 | -3.0 | 1000 | +1.011 |
| R | lein3 | matilein | — | -58.114 | -59.438 | 0.0% | -149.0 | -3.0 | 1000 | +1.027 |
| R | lein2 | matilein | — | -58.148 | -59.228 | 0.0% | -187.0 | -3.0 | 1000 | +1.061 |
| 15 | espero-no-ser-ultimo | Tadeo-Casiraghi | 0 | -58.185 | -59.512 | 0.0% | -152.0 | -3.0 | 1000 | +1.098 |
| R | valentino-pettazi-2 | ValenPettaz1 | — | -58.206 | -59.310 | 0.0% | -160.0 | -3.0 | 1000 | +1.119 |
| R | Wachinator-v1 | ginerJuanUdesa | — | -58.210 | -59.808 | 0.0% | -122.0 | -3.0 | 1000 | +1.123 |
| 16 | gonzalezds | mariagonzalezdelsolar | 0 | -58.248 | -60.034 | 0.0% | -152.0 | -3.0 | 1000 | +1.161 |
| R | ivan-de-pineda-es-inocente-sin-features | RamaMusic | — | -58.294 | -59.248 | 0.0% | -186.0 | -3.0 | 1000 | +1.207 |
| 17 | ivan-de-pineda-102 | RamaMusic | 0 | -58.301 | -59.080 | 0.0% | -181.0 | -3.0 | 1000 | +1.214 |
| R | valentino-pettazi | ValenPettaz1 | — | -58.336 | -59.816 | 0.0% | -149.0 | -3.0 | 1000 | +1.249 |
| R | domabot3 | Sdomato | — | -58.570 | -59.758 | 0.0% | -136.0 | -3.0 | 1000 | +1.483 |
| R | fium-V1 | tomasbenavidez | — | -58.741 | -59.766 | 0.0% | -161.0 | -3.0 | 1000 | +1.654 |
| R | naoagent-greedy3 | naomicouriel | — | -58.917 | -60.364 | 0.0% | -152.0 | -3.0 | 1000 | +1.830 |
| 18 | mateofreire | mateofreire | 0 | -58.970 | -59.452 | 0.0% | -196.0 | -3.0 | 1000 | +1.883 |
| R | valentino-pettazi-4 | ValenPettaz1 | — | -59.018 | -60.550 | 0.0% | -181.0 | -3.0 | 1000 | +1.931 |
| R | agusamblard-motor | agusamblard | — | -59.050 | -59.956 | 0.0% | -126.0 | -3.0 | 1000 | +1.963 |
| R | agusamblard | agusamblard | — | -59.257 | -60.216 | 0.0% | -165.0 | -3.0 | 1000 | +2.170 |
| 19 | leon-alderete | joaquinleondev | 0 | -59.310 | -60.590 | 0.0% | -179.0 | -3.0 | 1000 | +2.223 |
| R | naoagent-greedy2 | naomicouriel | — | -59.333 | -60.468 | 0.0% | -161.0 | -3.0 | 1000 | +2.246 |
| R | tomasbenavidez | tomasbenavidez | — | -59.372 | -59.928 | 0.0% | -157.0 | -3.0 | 1000 | +2.285 |
| R | fium-V3 | tomasbenavidez | — | -59.419 | -60.222 | 0.0% | -160.0 | -3.0 | 1000 | +2.332 |
| 20 | domabot2 | Sdomato | 0 | -59.642 | -61.210 | 0.0% | -160.0 | -3.0 | 1000 | +2.555 |
| 21 | matbr | mateobramer | 0 | -59.704 | -61.216 | 0.0% | -129.0 | -3.0 | 1000 | +2.617 |
| 22 | lein | matilein | 0 | -59.877 | -60.294 | 0.0% | -180.0 | -3.0 | 1000 | +2.790 |
| 23 | sgroba | Santi2065 | 0 | -60.074 | -59.796 | 0.0% | -161.0 | -3.0 | 1000 | +2.987 |
| 24 | auto-cipre | CiprianoOss | 0 | -60.302 | -61.328 | 0.0% | -148.0 | -3.0 | 1000 | +3.215 |
| 25 | jazgeller | jazgeller | 0 | -60.339 | -61.520 | 0.0% | -162.0 | -3.0 | 1000 | +3.252 |
| R | domabot4 | Sdomato | — | -60.370 | -61.782 | 0.0% | -145.0 | -3.0 | 1000 | +3.283 |
| 26 | Meteoro | FacundoFirpo | 0 | -60.682 | -62.440 | 0.0% | -171.0 | -3.0 | 1000 | +3.595 |
| 27 | martin-bianchi | martinbianchi0 | 0 | -61.128 | -62.554 | 0.0% | -145.0 | -3.0 | 1000 | +4.041 |
| 28 | maxi | maxividela2577 | 0 | -61.359 | -63.004 | 0.0% | -172.0 | -3.0 | 1000 | +4.272 |
| 29 | valeriano | Isivaleriano | 0 | -61.487 | -61.228 | 0.0% | -188.0 | -3.0 | 1000 | +4.400 |
| 30 | nixons | Anaholcman | 0 | -63.256 | -63.388 | 0.1% | -200.0 | -3.0 | 1000 | +6.169 |
| 31 | viaggio | FelipeViaggioFL | 0 | -63.259 | -65.332 | 0.0% | -170.0 | -3.0 | 1000 | +6.172 |
| R | fium-V2 | tomasbenavidez | — | -63.521 | -65.594 | 0.0% | -167.0 | -3.0 | 1000 | +6.434 |
| 32 | joaco-di-cola | joaco1212004 | 0 | -65.656 | -67.556 | 0.0% | -199.0 | -3.0 | 1000 | +8.569 |
| 33 | zoffi | florzoffi | 0 | -65.818 | -66.818 | 0.1% | -200.0 | -3.0 | 1000 | +8.731 |
| R | domabot | Sdomato | — | -67.175 | -69.610 | 0.0% | -167.0 | -3.0 | 1000 | +10.088 |
| 34 | ion_h_RL_TP2 | 72Ion | 0 | -80.179 | -78.134 | 0.0% | -199.0 | -3.0 | 1000 | +23.092 |

## GP Lluvia

_Sensores con ruido gaussiano en posición y velocidad._

| # | Auto | Escudería | Pts | Media | IQM | Sin llegar | Min | Max | Episodios | Dif. al 1° |
|---|------|-----------|----:|-------|-----|-----------:|-----|-----|-----------|-----------|
| R | ivan-de-pineda-106 | RamaMusic | — | -99.960 | -102.236 | 0.0% | -169.0 | -83.0 | 1000 | −0.317 |
| R | ivan-de-pineda-105 | RamaMusic | — | -100.152 | -102.388 | 0.0% | -176.0 | -83.0 | 1000 | −0.125 |
| 1 | ivan-de-pineda-102 | RamaMusic | 25 | -100.277 | -101.974 | 0.0% | -176.0 | -83.0 | 1000 | — |
| R | valentino-pettazi-3 | ValenPettaz1 | — | -100.288 | -102.146 | 0.0% | -188.0 | -83.0 | 1000 | +0.011 |
| R | ivan-de-pineda-103 | RamaMusic | — | -100.382 | -102.450 | 0.0% | -172.0 | -83.0 | 1000 | +0.105 |
| 2 | tomas-castro-equilibrado | tommycass | 18 | -100.485 | -102.648 | 0.0% | -175.0 | -83.0 | 1000 | +0.208 |
| R | naoagent-ensemble | naomicouriel | — | -100.542 | -102.904 | 0.0% | -181.0 | -83.0 | 1000 | +0.265 |
| 3 | lein | matilein | 15 | -100.563 | -103.400 | 0.0% | -186.0 | -83.0 | 1000 | +0.286 |
| R | ivan-de-pineda-101 | RamaMusic | — | -100.571 | -101.786 | 0.0% | -173.0 | -83.0 | 1000 | +0.294 |
| R | ivan-de-pineda-104 | RamaMusic | — | -100.616 | -102.922 | 0.0% | -173.0 | -83.0 | 1000 | +0.339 |
| R | valentino-pettazi-2 | ValenPettaz1 | — | -100.631 | -103.012 | 0.0% | -168.0 | -83.0 | 1000 | +0.354 |
| 4 | naoagent-greedy | naomicouriel | 12 | -100.999 | -101.660 | 0.0% | -188.0 | -83.0 | 1000 | +0.722 |
| R | naoagent | naomicouriel | — | -101.021 | -103.266 | 0.0% | -174.0 | -83.0 | 1000 | +0.744 |
| R | fium-V3 | tomasbenavidez | — | -101.088 | -102.022 | 0.0% | -186.0 | -83.0 | 1000 | +0.811 |
| R | bravo-andres-r1 | Andresbravo9 | — | -101.111 | -103.244 | 0.0% | -162.0 | -83.0 | 1000 | +0.834 |
| 5 | domabot2 | Sdomato | 10 | -101.321 | -103.686 | 0.0% | -178.0 | -83.0 | 1000 | +1.044 |
| R | bravo-andres-r5 | Andresbravo9 | — | -101.357 | -103.246 | 0.0% | -162.0 | -83.0 | 1000 | +1.080 |
| R | ivan-de-pineda-107 | RamaMusic | — | -101.429 | -103.294 | 0.0% | -188.0 | -83.0 | 1000 | +1.152 |
| R | valentino-pettazi | ValenPettaz1 | — | -101.441 | -103.492 | 0.0% | -160.0 | -83.0 | 1000 | +1.164 |
| R | valentino-pettazi-4 | ValenPettaz1 | — | -101.568 | -103.568 | 0.0% | -199.0 | -83.0 | 1000 | +1.291 |
| 6 | valentino-pettazi-5 | ValenPettaz1 | 8 | -101.620 | -104.428 | 0.0% | -166.0 | -83.0 | 1000 | +1.343 |
| 7 | agusamblard-v4 | agusamblard | 6 | -101.651 | -103.590 | 0.0% | -186.0 | -83.0 | 1000 | +1.374 |
| 8 | espero-no-ser-ultimo | Tadeo-Casiraghi | 4 | -101.677 | -103.312 | 0.0% | -168.0 | -83.0 | 1000 | +1.400 |
| R | SilverArrow | VANAFA | — | -101.696 | -103.060 | 0.0% | -177.0 | -83.0 | 1000 | +1.419 |
| R | ivan-de-pineda-es-inocente-sin-cos | RamaMusic | — | -101.808 | -102.138 | 0.0% | -189.0 | -83.0 | 1000 | +1.531 |
| R | Larpest-v4 | ginerJuanUdesa | — | -101.837 | -103.412 | 0.0% | -157.0 | -83.0 | 1000 | +1.560 |
| R | ivan-de-pineda-es-inocente-sin-features | RamaMusic | — | -101.885 | -101.772 | 0.0% | -186.0 | -83.0 | 1000 | +1.608 |
| 9 | Larpest-v5 | ginerJuanUdesa | 2 | -102.055 | -103.754 | 0.0% | -156.0 | -83.0 | 1000 | +1.778 |
| R | naoagent-greedy3 | naomicouriel | — | -102.200 | -101.928 | 0.0% | -174.0 | -83.0 | 1000 | +1.923 |
| R | ivan-de-pineda-es-inocente-con-features | RamaMusic | — | -102.255 | -101.862 | 0.0% | -183.0 | -83.0 | 1000 | +1.978 |
| 10 | leon-alderete | joaquinleondev | 1 | -102.486 | -102.160 | 0.0% | -183.0 | -83.0 | 1000 | +2.209 |
| R | bravo-andres-r2 | Andresbravo9 | — | -102.565 | -103.570 | 0.0% | -166.0 | -83.0 | 1000 | +2.288 |
| R | Larpest-v3 | ginerJuanUdesa | — | -102.578 | -102.460 | 0.0% | -189.0 | -83.0 | 1000 | +2.301 |
| R | Wachinators-v2 | ginerJuanUdesa | — | -102.731 | -103.472 | 0.0% | -163.0 | -83.0 | 1000 | +2.454 |
| R | Wachinators-v3 | ginerJuanUdesa | — | -102.857 | -103.572 | 0.0% | -175.0 | -83.0 | 1000 | +2.580 |
| 11 | nixons | Anaholcman | 0 | -102.882 | -104.266 | 0.1% | -200.0 | -83.0 | 1000 | +2.605 |
| 12 | joaco-di-cola | joaco1212004 | 0 | -103.230 | -105.882 | 0.0% | -192.0 | -83.0 | 1000 | +2.953 |
| R | naoagent-greedy2 | naomicouriel | — | -103.230 | -102.098 | 0.0% | -177.0 | -83.0 | 1000 | +2.953 |
| 13 | Franco-Colapinto | famatodlr | 0 | -103.258 | -103.960 | 0.0% | -167.0 | -83.0 | 1000 | +2.981 |
| 14 | mateofreire | mateofreire | 0 | -103.743 | -104.048 | 0.0% | -167.0 | -84.0 | 1000 | +3.466 |
| 15 | maxi | maxividela2577 | 0 | -103.774 | -104.896 | 0.0% | -194.0 | -84.0 | 1000 | +3.497 |
| 16 | DeCruz | BrunoDC-dev | 0 | -103.804 | -103.392 | 0.0% | -176.0 | -83.0 | 1000 | +3.527 |
| R | Alan-Schadan-v2 | Alanschad | — | -104.049 | -103.880 | 0.0% | -171.0 | -83.0 | 1000 | +3.772 |
| R | Alan-Schadan-v4 | Alanschad | — | -104.166 | -103.996 | 0.0% | -175.0 | -83.0 | 1000 | +3.889 |
| 17 | Alan-Schadan-v3 | Alanschad | 0 | -104.181 | -103.998 | 0.0% | -175.0 | -83.0 | 1000 | +3.904 |
| 18 | zoffi | florzoffi | 0 | -104.280 | -105.628 | 0.0% | -182.0 | -83.0 | 1000 | +4.003 |
| 19 | jazgeller | jazgeller | 0 | -104.373 | -104.084 | 0.0% | -182.0 | -83.0 | 1000 | +4.096 |
| R | bravo-andres-r4 | Andresbravo9 | — | -104.605 | -102.590 | 0.0% | -184.0 | -83.0 | 1000 | +4.328 |
| R | DeCruz_v2 | BrunoDC-dev | — | -104.736 | -102.696 | 0.0% | -180.0 | -83.0 | 1000 | +4.459 |
| 20 | sgroba | Santi2065 | 0 | -104.912 | -103.818 | 0.2% | -200.0 | -83.0 | 1000 | +4.635 |
| R | fium-V4 | tomasbenavidez | — | -105.019 | -104.376 | 0.0% | -176.0 | -83.0 | 1000 | +4.742 |
| 21 | bravo-andres | Andresbravo9 | 0 | -105.291 | -102.634 | 0.0% | -184.0 | -83.0 | 1000 | +5.014 |
| R | tomasbenavidez | tomasbenavidez | — | -105.572 | -102.982 | 0.0% | -199.0 | -83.0 | 1000 | +5.295 |
| R | agusamblard | agusamblard | — | -105.586 | -103.796 | 0.0% | -197.0 | -83.0 | 1000 | +5.309 |
| 22 | martin-bianchi | martinbianchi0 | 0 | -106.083 | -104.532 | 0.1% | -200.0 | -83.0 | 1000 | +5.806 |
| R | salim | athinasalimm | — | -106.224 | -102.868 | 0.0% | -183.0 | -83.0 | 1000 | +5.947 |
| 23 | frangiavarini-exp12 | frangiavarini | 0 | -106.306 | -103.634 | 0.0% | -182.0 | -83.0 | 1000 | +6.029 |
| 24 | vanafa | VANAFA | 0 | -106.377 | -102.934 | 0.0% | -172.0 | -83.0 | 1000 | +6.100 |
| R | tomas-castro | tommycass | — | -106.729 | -102.804 | 0.0% | -171.0 | -83.0 | 1000 | +6.452 |
| 25 | valeriano | Isivaleriano | 0 | -106.790 | -107.256 | 0.7% | -200.0 | -84.0 | 1000 | +6.513 |
| R | fium-V1 | tomasbenavidez | — | -107.063 | -103.426 | 0.0% | -196.0 | -84.0 | 1000 | +6.786 |
| R | Wachinators-v1 | ginerJuanUdesa | — | -107.249 | -104.198 | 0.0% | -194.0 | -83.0 | 1000 | +6.972 |
| 26 | gonzalezds | mariagonzalezdelsolar | 0 | -107.371 | -102.788 | 0.0% | -170.0 | -83.0 | 1000 | +7.094 |
| R | domabot3 | Sdomato | — | -107.403 | -105.288 | 0.0% | -179.0 | -84.0 | 1000 | +7.126 |
| R | lein3 | matilein | — | -107.460 | -102.700 | 0.0% | -173.0 | -83.0 | 1000 | +7.183 |
| R | Alan-Schadan | Alanschad | — | -107.569 | -103.778 | 0.0% | -176.0 | -83.0 | 1000 | +7.292 |
| 27 | sally-m | athinasalimm | 0 | -107.668 | -103.626 | 0.0% | -199.0 | -83.0 | 1000 | +7.391 |
| R | lein2 | matilein | — | -107.947 | -103.168 | 0.0% | -160.0 | -83.0 | 1000 | +7.670 |
| 28 | sb3zoo | Gabo-Tor | 0 | -108.171 | -105.530 | 0.2% | -200.0 | -83.0 | 1000 | +7.894 |
| R | domabot4 | Sdomato | — | -108.277 | -104.536 | 0.0% | -181.0 | -83.0 | 1000 | +8.000 |
| 29 | viaggio | FelipeViaggioFL | 0 | -108.386 | -103.134 | 0.0% | -188.0 | -83.0 | 1000 | +8.109 |
| R | fium-V2 | tomasbenavidez | — | -109.136 | -105.960 | 0.1% | -200.0 | -84.0 | 1000 | +8.859 |
| 30 | Meteoro | FacundoFirpo | 0 | -110.196 | -104.878 | 0.1% | -200.0 | -83.0 | 1000 | +9.919 |
| 31 | matbr | mateobramer | 0 | -110.346 | -106.632 | 0.0% | -183.0 | -83.0 | 1000 | +10.069 |
| R | domabot | Sdomato | — | -111.638 | -105.518 | 0.3% | -200.0 | -83.0 | 1000 | +11.361 |
| 32 | fium-V5 | tomasbenavidez | 0 | -114.239 | -110.174 | 0.0% | -196.0 | -83.0 | 1000 | +13.962 |
| R | agusamblard-motor | agusamblard | — | -114.273 | -105.262 | 0.3% | -200.0 | -83.0 | 1000 | +13.996 |
| R | Sloppeitors-v1 | ginerJuanUdesa | — | -114.968 | -112.556 | 0.1% | -200.0 | -83.0 | 1000 | +14.691 |
| R | Wachinators-v4 | ginerJuanUdesa | — | -115.062 | -112.304 | 0.5% | -200.0 | -83.0 | 1000 | +14.785 |
| R | Larpest-v1 | ginerJuanUdesa | — | -115.433 | -112.778 | 0.2% | -200.0 | -83.0 | 1000 | +15.156 |
| R | Larpest-v2 | ginerJuanUdesa | — | -116.442 | -114.852 | 0.1% | -200.0 | -83.0 | 1000 | +16.165 |
| 33 | auto-cipre | CiprianoOss | 0 | -116.572 | -112.482 | 0.0% | -174.0 | -83.0 | 1000 | +16.295 |
| R | Larper-v1 | ginerJuanUdesa | — | -116.984 | -115.168 | 0.2% | -200.0 | -83.0 | 1000 | +16.707 |
| R | Wachinator-v1 | ginerJuanUdesa | — | -125.074 | -122.782 | 1.0% | -200.0 | -83.0 | 1000 | +24.797 |
| 34 | ion_h_RL_TP2 | 72Ion | 0 | -148.168 | -140.578 | 4.1% | -200.0 | -125.0 | 1000 | +47.891 |

## GP Motor débil

_El motor rinde entre 8% y 12% menos._

| # | Auto | Escudería | Pts | Media | IQM | Sin llegar | Min | Max | Episodios | Dif. al 1° |
|---|------|-----------|----:|-------|-----|-----------:|-----|-----|-----------|-----------|
| 1 | Larpest-v5 | ginerJuanUdesa | 25 | -110.524 | -110.532 | 0.0% | -194.0 | -92.0 | 1000 | — |
| R | agusamblard-motor | agusamblard | — | -110.550 | -110.592 | 0.0% | -126.0 | -92.0 | 1000 | +0.026 |
| 2 | nixons | Anaholcman | 18 | -110.650 | -110.746 | 0.0% | -122.0 | -92.0 | 1000 | +0.126 |
| R | Alan-Schadan-v4 | Alanschad | — | -110.780 | -111.018 | 0.0% | -176.0 | -92.0 | 1000 | +0.256 |
| R | fium-V2 | tomasbenavidez | — | -110.867 | -111.010 | 0.0% | -125.0 | -92.0 | 1000 | +0.343 |
| R | Larpest-v4 | ginerJuanUdesa | — | -110.959 | -110.844 | 0.0% | -199.0 | -92.0 | 1000 | +0.435 |
| R | Wachinators-v3 | ginerJuanUdesa | — | -111.037 | -110.846 | 0.0% | -191.0 | -92.0 | 1000 | +0.513 |
| 3 | Alan-Schadan-v3 | Alanschad | 15 | -111.131 | -111.112 | 0.0% | -197.0 | -92.0 | 1000 | +0.607 |
| R | Wachinators-v2 | ginerJuanUdesa | — | -111.238 | -110.910 | 0.1% | -200.0 | -92.0 | 1000 | +0.714 |
| 4 | valentino-pettazi-5 | ValenPettaz1 | 12 | -112.123 | -111.516 | 0.0% | -180.0 | -92.0 | 1000 | +1.599 |
| R | Alan-Schadan-v2 | Alanschad | — | -112.278 | -111.942 | 0.1% | -200.0 | -92.0 | 1000 | +1.754 |
| R | valentino-pettazi | ValenPettaz1 | — | -112.549 | -110.862 | 0.0% | -171.0 | -92.0 | 1000 | +2.025 |
| R | bravo-andres-r2 | Andresbravo9 | — | -112.686 | -111.022 | 0.1% | -200.0 | -92.0 | 1000 | +2.162 |
| 5 | agusamblard-v4 | agusamblard | 10 | -113.436 | -111.512 | 0.4% | -200.0 | -92.0 | 1000 | +2.912 |
| R | bravo-andres-r5 | Andresbravo9 | — | -114.266 | -110.616 | 0.4% | -200.0 | -92.0 | 1000 | +3.742 |
| R | naoagent | naomicouriel | — | -114.634 | -110.542 | 0.4% | -200.0 | -92.0 | 1000 | +4.110 |
| R | bravo-andres-r1 | Andresbravo9 | — | -114.705 | -111.036 | 0.0% | -194.0 | -92.0 | 1000 | +4.181 |
| R | valentino-pettazi-4 | ValenPettaz1 | — | -114.846 | -110.730 | 0.6% | -200.0 | -92.0 | 1000 | +4.322 |
| R | naoagent-ensemble | naomicouriel | — | -115.473 | -110.828 | 0.6% | -200.0 | -92.0 | 1000 | +4.949 |
| 6 | DeCruz | BrunoDC-dev | 8 | -115.643 | -111.288 | 0.2% | -200.0 | -92.0 | 1000 | +5.119 |
| R | domabot4 | Sdomato | — | -115.935 | -110.858 | 0.0% | -186.0 | -92.0 | 1000 | +5.411 |
| R | SilverArrow | VANAFA | — | -116.054 | -111.094 | 0.3% | -200.0 | -92.0 | 1000 | +5.530 |
| 7 | Franco-Colapinto | famatodlr | 6 | -116.096 | -111.902 | 0.0% | -182.0 | -92.0 | 1000 | +5.572 |
| 8 | lein | matilein | 4 | -116.266 | -110.862 | 0.2% | -200.0 | -92.0 | 1000 | +5.742 |
| R | fium-V4 | tomasbenavidez | — | -116.694 | -112.252 | 0.4% | -200.0 | -93.0 | 1000 | +6.170 |
| 9 | espero-no-ser-ultimo | Tadeo-Casiraghi | 2 | -117.494 | -111.386 | 0.1% | -200.0 | -93.0 | 1000 | +6.970 |
| 10 | tomas-castro-equilibrado | tommycass | 1 | -117.999 | -110.830 | 0.1% | -200.0 | -92.0 | 1000 | +7.475 |
| R | ivan-de-pineda-107 | RamaMusic | — | -118.047 | -110.864 | 0.0% | -195.0 | -92.0 | 1000 | +7.523 |
| R | valentino-pettazi-2 | ValenPettaz1 | — | -118.077 | -111.790 | 0.3% | -200.0 | -92.0 | 1000 | +7.553 |
| R | ivan-de-pineda-106 | RamaMusic | — | -118.243 | -110.816 | 0.2% | -200.0 | -92.0 | 1000 | +7.719 |
| R | ivan-de-pineda-104 | RamaMusic | — | -118.274 | -110.740 | 0.3% | -200.0 | -92.0 | 1000 | +7.750 |
| R | domabot3 | Sdomato | — | -118.370 | -111.886 | 0.0% | -167.0 | -92.0 | 1000 | +7.846 |
| R | ivan-de-pineda-105 | RamaMusic | — | -118.723 | -111.188 | 0.3% | -200.0 | -92.0 | 1000 | +8.199 |
| 11 | domabot2 | Sdomato | 0 | -118.738 | -111.758 | 0.2% | -200.0 | -92.0 | 1000 | +8.214 |
| R | ivan-de-pineda-103 | RamaMusic | — | -118.976 | -110.844 | 0.3% | -200.0 | -92.0 | 1000 | +8.452 |
| R | valentino-pettazi-3 | ValenPettaz1 | — | -119.103 | -111.314 | 0.3% | -200.0 | -92.0 | 1000 | +8.579 |
| 12 | maxi | maxividela2577 | 0 | -119.282 | -112.610 | 0.4% | -200.0 | -93.0 | 1000 | +8.758 |
| 13 | joaco-di-cola | joaco1212004 | 0 | -119.523 | -113.392 | 2.2% | -200.0 | -92.0 | 1000 | +8.999 |
| R | ivan-de-pineda-101 | RamaMusic | — | -120.693 | -113.274 | 0.3% | -200.0 | -92.0 | 1000 | +10.169 |
| R | bravo-andres-r4 | Andresbravo9 | — | -120.740 | -114.480 | 0.0% | -194.0 | -92.0 | 1000 | +10.216 |
| R | Larpest-v3 | ginerJuanUdesa | — | -121.039 | -114.000 | 0.1% | -200.0 | -92.0 | 1000 | +10.515 |
| 14 | zoffi | florzoffi | 0 | -121.367 | -114.872 | 7.1% | -200.0 | -92.0 | 1000 | +10.843 |
| 15 | mateofreire | mateofreire | 0 | -122.323 | -112.370 | 1.0% | -200.0 | -92.0 | 1000 | +11.799 |
| R | tomas-castro | tommycass | — | -122.620 | -118.376 | 0.0% | -193.0 | -92.0 | 1000 | +12.096 |
| 16 | ivan-de-pineda-102 | RamaMusic | 0 | -123.804 | -114.862 | 2.2% | -200.0 | -92.0 | 1000 | +13.280 |
| 17 | sgroba | Santi2065 | 0 | -124.057 | -113.460 | 1.6% | -200.0 | -93.0 | 1000 | +13.533 |
| 18 | frangiavarini-exp12 | frangiavarini | 0 | -124.562 | -115.994 | 1.4% | -200.0 | -93.0 | 1000 | +14.038 |
| R | salim | athinasalimm | — | -125.186 | -119.948 | 0.0% | -195.0 | -93.0 | 1000 | +14.662 |
| R | ivan-de-pineda-es-inocente-sin-features | RamaMusic | — | -125.251 | -117.268 | 2.9% | -200.0 | -92.0 | 1000 | +14.727 |
| 19 | viaggio | FelipeViaggioFL | 0 | -125.442 | -114.484 | 0.2% | -200.0 | -94.0 | 1000 | +14.918 |
| 20 | sally-m | athinasalimm | 0 | -125.624 | -120.458 | 0.1% | -200.0 | -92.0 | 1000 | +15.100 |
| R | lein2 | matilein | — | -126.332 | -123.906 | 0.0% | -193.0 | -92.0 | 1000 | +15.808 |
| 21 | vanafa | VANAFA | 0 | -126.354 | -120.288 | 0.5% | -200.0 | -93.0 | 1000 | +15.830 |
| 22 | auto-cipre | CiprianoOss | 0 | -126.476 | -122.788 | 0.0% | -154.0 | -99.0 | 1000 | +15.952 |
| 23 | bravo-andres | Andresbravo9 | 0 | -126.512 | -121.298 | 0.5% | -200.0 | -92.0 | 1000 | +15.988 |
| R | Alan-Schadan | Alanschad | — | -126.532 | -119.804 | 0.7% | -200.0 | -93.0 | 1000 | +16.008 |
| R | ivan-de-pineda-es-inocente-con-features | RamaMusic | — | -126.765 | -119.776 | 1.5% | -200.0 | -92.0 | 1000 | +16.241 |
| 24 | naoagent-greedy | naomicouriel | 0 | -126.818 | -120.192 | 1.6% | -200.0 | -93.0 | 1000 | +16.294 |
| R | naoagent-greedy3 | naomicouriel | — | -126.967 | -121.108 | 0.9% | -200.0 | -92.0 | 1000 | +16.443 |
| 25 | valeriano | Isivaleriano | 0 | -127.281 | -114.172 | 3.9% | -200.0 | -102.0 | 1000 | +16.757 |
| 26 | jazgeller | jazgeller | 0 | -127.327 | -120.268 | 0.1% | -200.0 | -93.0 | 1000 | +16.803 |
| R | ivan-de-pineda-es-inocente-sin-cos | RamaMusic | — | -127.381 | -120.494 | 0.8% | -200.0 | -92.0 | 1000 | +16.857 |
| R | lein3 | matilein | — | -127.464 | -126.000 | 0.0% | -192.0 | -92.0 | 1000 | +16.940 |
| 27 | gonzalezds | mariagonzalezdelsolar | 0 | -127.507 | -123.486 | 0.0% | -186.0 | -93.0 | 1000 | +16.983 |
| R | naoagent-greedy2 | naomicouriel | — | -128.727 | -122.904 | 0.9% | -200.0 | -92.0 | 1000 | +18.203 |
| 28 | leon-alderete | joaquinleondev | 0 | -129.705 | -122.852 | 2.3% | -200.0 | -93.0 | 1000 | +19.181 |
| R | fium-V3 | tomasbenavidez | — | -130.158 | -122.592 | 0.4% | -200.0 | -92.0 | 1000 | +19.634 |
| 29 | Meteoro | FacundoFirpo | 0 | -130.904 | -120.308 | 6.0% | -200.0 | -93.0 | 1000 | +20.380 |
| R | DeCruz_v2 | BrunoDC-dev | — | -132.224 | -129.800 | 0.4% | -200.0 | -92.0 | 1000 | +21.700 |
| R | Wachinators-v1 | ginerJuanUdesa | — | -132.833 | -128.554 | 1.3% | -200.0 | -92.0 | 1000 | +22.309 |
| R | Sloppeitors-v1 | ginerJuanUdesa | — | -133.096 | -132.672 | 0.2% | -200.0 | -92.0 | 1000 | +22.572 |
| R | agusamblard | agusamblard | — | -133.343 | -125.230 | 4.9% | -200.0 | -93.0 | 1000 | +22.819 |
| R | Larpest-v1 | ginerJuanUdesa | — | -133.534 | -134.252 | 0.3% | -200.0 | -92.0 | 1000 | +23.010 |
| 30 | sb3zoo | Gabo-Tor | 0 | -133.939 | -128.688 | 0.6% | -200.0 | -93.0 | 1000 | +23.415 |
| R | tomasbenavidez | tomasbenavidez | — | -134.285 | -128.850 | 1.6% | -200.0 | -93.0 | 1000 | +23.761 |
| R | Wachinators-v4 | ginerJuanUdesa | — | -134.931 | -134.988 | 0.3% | -200.0 | -92.0 | 1000 | +24.407 |
| 31 | martin-bianchi | martinbianchi0 | 0 | -135.643 | -130.480 | 0.3% | -200.0 | -94.0 | 1000 | +25.119 |
| R | Larpest-v2 | ginerJuanUdesa | — | -137.880 | -139.908 | 0.5% | -200.0 | -92.0 | 1000 | +27.356 |
| R | Larper-v1 | ginerJuanUdesa | — | -138.459 | -140.650 | 0.5% | -200.0 | -92.0 | 1000 | +27.935 |
| R | domabot | Sdomato | — | -138.948 | -133.360 | 0.6% | -200.0 | -111.0 | 1000 | +28.424 |
| 32 | matbr | mateobramer | 0 | -140.219 | -136.596 | 0.2% | -200.0 | -99.0 | 1000 | +29.695 |
| R | fium-V1 | tomasbenavidez | — | -140.761 | -142.958 | 0.7% | -200.0 | -92.0 | 1000 | +30.237 |
| 33 | fium-V5 | tomasbenavidez | 0 | -141.502 | -145.612 | 0.1% | -200.0 | -92.0 | 1000 | +30.978 |
| R | Wachinator-v1 | ginerJuanUdesa | — | -144.886 | -148.320 | 0.0% | -191.0 | -92.0 | 1000 | +34.362 |
| 34 | ion_h_RL_TP2 | 72Ion | 0 | -154.574 | -147.024 | 10.1% | -200.0 | -134.0 | 1000 | +44.050 |

## GP Otra pista

_La montaña cambia de forma: cos(f·x) con f entre 2.6 y 2.8 (en vez de 3)._

| # | Auto | Escudería | Pts | Media | IQM | Sin llegar | Min | Max | Episodios | Dif. al 1° |
|---|------|-----------|----:|-------|-----|-----------:|-----|-----|-----------|-----------|
| R | Larpest-v2 | ginerJuanUdesa | — | -95.299 | -95.470 | 0.0% | -108.0 | -82.0 | 1000 | −0.396 |
| R | Larper-v1 | ginerJuanUdesa | — | -95.338 | -95.552 | 0.0% | -108.0 | -82.0 | 1000 | −0.357 |
| R | Larpest-v1 | ginerJuanUdesa | — | -95.592 | -96.014 | 0.0% | -109.0 | -82.0 | 1000 | −0.103 |
| 1 | fium-V5 | tomasbenavidez | 25 | -95.695 | -96.184 | 0.0% | -108.0 | -82.0 | 1000 | — |
| R | lein2 | matilein | — | -95.981 | -96.168 | 0.0% | -109.0 | -82.0 | 1000 | +0.286 |
| R | Wachinators-v4 | ginerJuanUdesa | — | -96.035 | -96.482 | 0.0% | -110.0 | -82.0 | 1000 | +0.340 |
| R | Sloppeitors-v1 | ginerJuanUdesa | — | -96.114 | -96.658 | 0.0% | -109.0 | -82.0 | 1000 | +0.419 |
| R | Wachinator-v1 | ginerJuanUdesa | — | -96.259 | -97.350 | 0.0% | -108.0 | -82.0 | 1000 | +0.564 |
| R | lein3 | matilein | — | -96.393 | -96.448 | 0.0% | -113.0 | -83.0 | 1000 | +0.698 |
| R | Wachinators-v1 | ginerJuanUdesa | — | -96.415 | -97.494 | 0.0% | -109.0 | -82.0 | 1000 | +0.720 |
| R | fium-V1 | tomasbenavidez | — | -97.121 | -97.652 | 0.0% | -111.0 | -83.0 | 1000 | +1.426 |
| R | tomas-castro | tommycass | — | -97.286 | -98.346 | 0.0% | -110.0 | -82.0 | 1000 | +1.591 |
| R | DeCruz_v2 | BrunoDC-dev | — | -97.651 | -99.442 | 0.0% | -109.0 | -82.0 | 1000 | +1.956 |
| R | fium-V3 | tomasbenavidez | — | -98.192 | -100.480 | 0.0% | -110.0 | -82.0 | 1000 | +2.497 |
| 2 | bravo-andres | Andresbravo9 | 18 | -98.226 | -100.384 | 0.0% | -110.0 | -82.0 | 1000 | +2.531 |
| R | bravo-andres-r4 | Andresbravo9 | — | -98.854 | -101.302 | 0.0% | -110.0 | -82.0 | 1000 | +3.159 |
| R | naoagent-greedy2 | naomicouriel | — | -98.919 | -101.578 | 0.0% | -109.0 | -82.0 | 1000 | +3.224 |
| 3 | gonzalezds | mariagonzalezdelsolar | 15 | -98.962 | -100.764 | 0.0% | -112.0 | -83.0 | 1000 | +3.267 |
| 4 | naoagent-greedy | naomicouriel | 12 | -98.967 | -101.634 | 0.0% | -110.0 | -82.0 | 1000 | +3.272 |
| R | Larpest-v3 | ginerJuanUdesa | — | -99.044 | -101.890 | 0.0% | -110.0 | -82.0 | 1000 | +3.349 |
| R | ivan-de-pineda-es-inocente-sin-cos | RamaMusic | — | -99.134 | -102.084 | 0.0% | -109.0 | -82.0 | 1000 | +3.439 |
| R | naoagent-greedy3 | naomicouriel | — | -99.197 | -101.904 | 0.0% | -110.0 | -82.0 | 1000 | +3.502 |
| 5 | leon-alderete | joaquinleondev | 10 | -99.202 | -101.910 | 0.0% | -110.0 | -82.0 | 1000 | +3.507 |
| 6 | ivan-de-pineda-102 | RamaMusic | 8 | -99.342 | -102.606 | 0.0% | -110.0 | -82.0 | 1000 | +3.647 |
| 7 | sally-m | athinasalimm | 6 | -99.412 | -101.678 | 0.0% | -111.0 | -83.0 | 1000 | +3.717 |
| R | ivan-de-pineda-es-inocente-sin-features | RamaMusic | — | -99.473 | -102.166 | 0.0% | -111.0 | -82.0 | 1000 | +3.778 |
| R | ivan-de-pineda-es-inocente-con-features | RamaMusic | — | -99.569 | -102.144 | 0.0% | -111.0 | -83.0 | 1000 | +3.874 |
| R | tomasbenavidez | tomasbenavidez | — | -100.060 | -102.298 | 0.0% | -122.0 | -83.0 | 1000 | +4.365 |
| 8 | vanafa | VANAFA | 4 | -100.162 | -102.492 | 0.0% | -113.0 | -83.0 | 1000 | +4.467 |
| R | ivan-de-pineda-101 | RamaMusic | — | -100.175 | -103.304 | 0.0% | -111.0 | -82.0 | 1000 | +4.480 |
| 9 | frangiavarini-exp12 | frangiavarini | 2 | -100.200 | -103.320 | 0.0% | -111.0 | -83.0 | 1000 | +4.505 |
| 10 | Meteoro | FacundoFirpo | 1 | -100.551 | -103.898 | 0.0% | -111.0 | -83.0 | 1000 | +4.856 |
| 11 | mateofreire | mateofreire | 0 | -101.106 | -104.210 | 0.0% | -114.0 | -82.0 | 1000 | +5.411 |
| R | ivan-de-pineda-105 | RamaMusic | — | -101.108 | -105.178 | 0.0% | -111.0 | -82.0 | 1000 | +5.413 |
| R | Alan-Schadan | Alanschad | — | -101.159 | -103.448 | 0.0% | -114.0 | -83.0 | 1000 | +5.464 |
| 12 | viaggio | FelipeViaggioFL | 0 | -101.387 | -105.796 | 0.0% | -112.0 | -82.0 | 1000 | +5.692 |
| 13 | auto-cipre | CiprianoOss | 0 | -101.474 | -103.940 | 0.0% | -117.0 | -82.0 | 1000 | +5.779 |
| R | ivan-de-pineda-106 | RamaMusic | — | -101.539 | -105.534 | 0.0% | -113.0 | -82.0 | 1000 | +5.844 |
| 14 | tomas-castro-equilibrado | tommycass | 0 | -101.662 | -105.994 | 0.0% | -113.0 | -82.0 | 1000 | +5.967 |
| R | ivan-de-pineda-103 | RamaMusic | — | -101.690 | -105.754 | 0.0% | -113.0 | -82.0 | 1000 | +5.995 |
| R | ivan-de-pineda-107 | RamaMusic | — | -101.930 | -106.220 | 0.0% | -113.0 | -82.0 | 1000 | +6.235 |
| R | salim | athinasalimm | — | -102.124 | -104.612 | 0.0% | -144.0 | -84.0 | 1000 | +6.429 |
| 15 | jazgeller | jazgeller | 0 | -102.260 | -104.368 | 0.0% | -119.0 | -83.0 | 1000 | +6.565 |
| 16 | Franco-Colapinto | famatodlr | 0 | -102.281 | -107.276 | 0.0% | -114.0 | -82.0 | 1000 | +6.586 |
| R | valentino-pettazi-3 | ValenPettaz1 | — | -102.321 | -106.012 | 0.0% | -115.0 | -83.0 | 1000 | +6.626 |
| R | SilverArrow | VANAFA | — | -102.383 | -107.198 | 0.0% | -115.0 | -82.0 | 1000 | +6.688 |
| R | ivan-de-pineda-104 | RamaMusic | — | -102.476 | -107.082 | 0.0% | -114.0 | -82.0 | 1000 | +6.781 |
| R | valentino-pettazi-2 | ValenPettaz1 | — | -102.821 | -107.686 | 0.0% | -115.0 | -82.0 | 1000 | +7.126 |
| 17 | domabot2 | Sdomato | 0 | -102.947 | -107.528 | 0.0% | -115.0 | -83.0 | 1000 | +7.252 |
| 18 | sgroba | Santi2065 | 0 | -102.965 | -105.862 | 0.0% | -117.0 | -83.0 | 1000 | +7.270 |
| R | domabot4 | Sdomato | — | -103.230 | -107.998 | 0.0% | -114.0 | -82.0 | 1000 | +7.535 |
| R | naoagent-ensemble | naomicouriel | — | -103.321 | -107.904 | 0.0% | -116.0 | -83.0 | 1000 | +7.626 |
| R | domabot3 | Sdomato | — | -103.450 | -107.510 | 0.3% | -200.0 | -82.0 | 1000 | +7.755 |
| 19 | maxi | maxividela2577 | 0 | -103.585 | -107.732 | 0.0% | -118.0 | -83.0 | 1000 | +7.890 |
| R | naoagent | naomicouriel | — | -103.726 | -108.442 | 0.0% | -115.0 | -82.0 | 1000 | +8.031 |
| 20 | espero-no-ser-ultimo | Tadeo-Casiraghi | 0 | -103.944 | -108.434 | 0.0% | -116.0 | -83.0 | 1000 | +8.249 |
| 21 | lein | matilein | 0 | -104.051 | -108.690 | 0.0% | -115.0 | -83.0 | 1000 | +8.356 |
| 22 | DeCruz | BrunoDC-dev | 0 | -104.448 | -108.368 | 0.0% | -121.0 | -83.0 | 1000 | +8.753 |
| R | bravo-andres-r5 | Andresbravo9 | — | -104.469 | -108.840 | 0.0% | -119.0 | -83.0 | 1000 | +8.774 |
| R | domabot | Sdomato | — | -104.832 | -108.060 | 0.0% | -121.0 | -83.0 | 1000 | +9.137 |
| R | bravo-andres-r1 | Andresbravo9 | — | -105.173 | -108.482 | 0.6% | -200.0 | -83.0 | 1000 | +9.478 |
| R | valentino-pettazi-4 | ValenPettaz1 | — | -106.426 | -110.196 | 0.1% | -200.0 | -83.0 | 1000 | +10.731 |
| R | agusamblard | agusamblard | — | -106.427 | -107.062 | 0.6% | -200.0 | -85.0 | 1000 | +10.732 |
| 23 | agusamblard-v4 | agusamblard | 0 | -108.313 | -110.108 | 1.1% | -200.0 | -82.0 | 1000 | +12.618 |
| R | bravo-andres-r2 | Andresbravo9 | — | -109.398 | -109.426 | 3.1% | -200.0 | -83.0 | 1000 | +13.703 |
| 24 | valeriano | Isivaleriano | 0 | -109.701 | -111.716 | 2.2% | -200.0 | -84.0 | 1000 | +14.006 |
| R | valentino-pettazi | ValenPettaz1 | — | -109.825 | -110.946 | 1.8% | -200.0 | -83.0 | 1000 | +14.130 |
| 25 | valentino-pettazi-5 | ValenPettaz1 | 0 | -110.999 | -111.124 | 2.8% | -200.0 | -84.0 | 1000 | +15.304 |
| 26 | sb3zoo | Gabo-Tor | 0 | -111.205 | -112.318 | 0.7% | -200.0 | -83.0 | 1000 | +15.510 |
| 27 | zoffi | florzoffi | 0 | -111.519 | -109.972 | 4.8% | -200.0 | -83.0 | 1000 | +15.824 |
| 28 | martin-bianchi | martinbianchi0 | 0 | -112.161 | -110.708 | 0.1% | -200.0 | -86.0 | 1000 | +16.466 |
| R | fium-V4 | tomasbenavidez | — | -112.716 | -113.488 | 1.4% | -200.0 | -85.0 | 1000 | +17.021 |
| R | Alan-Schadan-v2 | Alanschad | — | -112.926 | -111.050 | 4.7% | -200.0 | -84.0 | 1000 | +17.231 |
| 29 | joaco-di-cola | joaco1212004 | 0 | -114.668 | -120.210 | 0.0% | -130.0 | -84.0 | 1000 | +18.973 |
| R | Larpest-v4 | ginerJuanUdesa | — | -115.515 | -109.502 | 8.6% | -200.0 | -83.0 | 1000 | +19.820 |
| 30 | Alan-Schadan-v3 | Alanschad | 0 | -117.224 | -112.124 | 8.2% | -200.0 | -83.0 | 1000 | +21.529 |
| R | Wachinators-v2 | ginerJuanUdesa | — | -117.841 | -109.372 | 11.4% | -200.0 | -83.0 | 1000 | +22.146 |
| 31 | Larpest-v5 | ginerJuanUdesa | 0 | -118.195 | -110.728 | 10.8% | -200.0 | -82.0 | 1000 | +22.500 |
| R | Alan-Schadan-v4 | Alanschad | — | -118.661 | -112.358 | 9.5% | -200.0 | -83.0 | 1000 | +22.966 |
| R | Wachinators-v3 | ginerJuanUdesa | — | -121.371 | -110.858 | 13.9% | -200.0 | -83.0 | 1000 | +25.676 |
| R | agusamblard-motor | agusamblard | — | -124.975 | -111.512 | 17.5% | -200.0 | -82.0 | 1000 | +29.280 |
| 32 | nixons | Anaholcman | 0 | -125.123 | -111.872 | 17.2% | -200.0 | -83.0 | 1000 | +29.428 |
| R | fium-V2 | tomasbenavidez | — | -128.591 | -113.772 | 19.5% | -200.0 | -83.0 | 1000 | +32.896 |
| 33 | matbr | mateobramer | 0 | -140.896 | -137.290 | 2.6% | -200.0 | -91.0 | 1000 | +45.201 |
| 34 | ion_h_RL_TP2 | 72Ion | 0 | -145.736 | -141.406 | 0.0% | -179.0 | -129.0 | 1000 | +50.041 |
