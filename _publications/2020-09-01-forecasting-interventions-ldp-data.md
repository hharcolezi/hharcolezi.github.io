---
title: "Forecasting the number of firefighter interventions per region with local-differential-privacy-based data"
collection: publications
permalink: /publication/forecasting-interventions-ldp-data
date: 2020-09-01
venue: 'Computers & Security'
---


[Download paper here](http://hharcolezi.github.io/files/2020_COSE_LDP_FIREMEN.pdf)

Abstract: Statistical studies on the number and types of firefighter interventions by region are essential to improve service to the population. It is also a preliminary step if we want to predict these interventions in order to optimize the placement of human and material resources of fire departments, for example. However, this type of data is sensitive and must be treated with the utmost care. In order to avoid any leakage of information, one can think of anonymizing them using Differential Privacy (DP), a safe method by construction. This work focuses on predicting the number of firefighter interventions in certain localities while respecting the strong concept of DP. A local Differential Privacy approach was first used to anonymize location data. Statistical estimators were then applied to reconstruct a synthetic data set that is uncorrelated from the users. Finally, a supervised learning approach using extreme gradient boosting was used to make the predictions. Experiments have shown that the anonymization-prediction method is very accurate: the introduction of noise to sanitize the data does not affect the quality of the predictions, and the predictions faithfully reflect what happened in reality.

Recommended citation: Arcolezi, H. H., Couchot, J.-F., Cerna, S., Guyeux, C., Royer, G., Bouna, B. Al, & Xiao, X. (2020). Forecasting the Number of Firefighters Interventions per Region with Local-Differential-Privacy-Based Data. Computers & Security, 96, 101888. https://doi.org/10.1016/j.cose.2020.101888

bibtex: @article{Arcolezi2020,
  doi = {10.1016/j.cose.2020.101888},
  url = {https://doi.org/10.1016/j.cose.2020.101888},
  year = {2020},
  month = sep,
  publisher = {Elsevier BV},
  volume = {96},
  pages = {101888},
  author = {H{\'{e}}ber H. Arcolezi and Jean-Fran{\c{c}}ois Couchot and Selene Cerna and Christophe Guyeux and Guillaume Royer and B{\'{e}}chara Al Bouna and Xiaokui Xiao},
  title = {Forecasting the number of firefighter interventions per region with local-differential-privacy-based data},
  journal = {Computers {\&} Security}
}
