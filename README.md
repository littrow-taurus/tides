# Tides
Tides computing using Darwin/Doodson modelization.

## Models
We use harmonics in a selection of principal ones guided on following documentations:
- [Lecture 1: Introduction to ocean tides, Myrl Hendershott](https://www.whoi.edu/cms/files/lecture01_21351.pdf)
- [Theory of tides - Wikipedia](https://en.wikipedia.org/wiki/Theory_of_tides)
- [Chapitre 4 Le potentiel générateur des marées](http://fabien.lefevre.free.fr/These_HTML/doc0004.htm)

More complex models with many more harmonics are described here:
- [The Harmonic Development of the Tide-generating Potential](https://royalsocietypublishing.org/doi/pdf/10.1098/rspa.1921.0088)
- [Precession-Nutations and Tidal Potential](https://articles.adsabs.harvard.edu/pdf/1971CeMec...4..190M)
- [Transformation between the International Terrestrial Reference System and the Geocentric Celestial Reference System (10 August 2012)](https://iers-conventions.obspm.fr/content/chapter5/icc5.pdf)
Those models can be used during further evolutions to improve models.

The admited order of importance of harmonics is:
1. M2
2. S2
3. N2
4. K1
5. M4
6. O1
7. M6
8. MK3
9. S4
10. MN4
11. nu2
12. S6
13. mu2
14. 2N2
15. OO1
16. lambda2
17. S1
18. M1
19. J1
20. Mm
21. Ssa
22. Sa
23. MSf
24. Mf
25. rau1
26. Q1
27. T2
28. R2
29. 2Q1
30. P1
31. 2SM2
32. M3
33. L2
34. 2MK3
35. K2
36. M8
37. MS4
Source: [Theory of tides - Wikipedia](https://en.wikipedia.org/wiki/Theory_of_tides)

## Documentation
- [Project setup](doc/setup.md)

## Bibliography
- [Theory of tides - Wikipedia](https://en.wikipedia.org/wiki/Theory_of_tides)
- [Is there an official recommended expression for Doodson arguments? - StackExchange](https://astronomy.stackexchange.com/questions/48303/is-there-an-official-recommended-expression-for-doodson-arguments)
- [Chapitre 4 Le potentiel générateur des marées](http://fabien.lefevre.free.fr/These_HTML/doc0004.htm)
- [Lecture 1: Introduction to ocean tides, Myrl Hendershott](https://www.whoi.edu/cms/files/lecture01_21351.pdf)
- [Transformation between the International Terrestrial Reference System and the Geocentric Celestial Reference System](https://iers-conventions.obspm.fr/content/chapter5/icc5.pdf)
- [Download tide gauge data - data.shom.fr](https://data.shom.fr/donnees/refmar/111/download)
  We use *Validated (delayed mode)*