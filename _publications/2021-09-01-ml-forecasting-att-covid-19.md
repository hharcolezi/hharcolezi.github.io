---
title: "Machine learning-based forecasting of firemen ambulances’ turnaround time in hospitals, considering the COVID-19 impact"
collection: publications
permalink: /publication/ml-forecasting-att-covid-19
date: 2021-09-01
venue: 'Applied Soft Computing'
---


[Download paper here](http://hharcolezi.github.io/files/2021_ASOC_ATT.pdf)

Abstract: When ambulances’ turnaround time (TT) in emergency departments is prolonged, it not only affects the victim severely but also causes unavailability of resources in emergency medical services (EMSs) and, consequently, leaves a locality unprotected. This problem may worsen with abnormal situations, e.g., the current coronavirus disease 2019 (COVID-19) pandemic. Taking this into consideration, this paper presents a first study on the COVID-19 impact on ambulances’ TT by analyzing historical data from the Departmental Fire and Rescue Service of the Doubs (SDIS 25), in France, for three hospitals. Because the TTs of SDIS 25 ambulances increased, this paper also calculated and analyzed the number of breakdowns in services, which augmented due to shortage of ambulances that return on service in time. It is, therefore, vital to have a decision-support tool to better reallocate resources by knowing the time EMSs ambulances and personnel will be in use. Thus, this paper proposes a novel two-stage methodology based on machine learning (ML) models to forecast the TT of each ambulance in a given time and hospital. The first stage uses a multivariate model of regularly spaced time series to predict the average TT (AvTT) per hour, which considers temporal variables and external ones (e.g., COVID-19 statistics, weather data). The second stage utilizes a multivariate irregularly spaced time series model, which considers temporal variables of each ambulance departure, type of intervention, external variables, and the previously predicted AvTT as inputs. Four state-of-the-art ML models were considered in this paper, namely, Light Gradient Boosted Machine, Multilayer Perceptron, Long Short-Term Memory, and Prophet. As shown in the results, the proposed methodology provided remarkable results for practical purposes. The AvTT accuracies obtained for the three hospitals were 90.16%, 97.02%, and 93.09%. And the TT accuracies were 74.42%, 86.63%, and 76.67%, all with an error margin of +- 10 min.

Recommended citation: Cerna, S., Arcolezi, H. H., Guyeux, C., Royer-Fey, G., & Chevallier, C. (2021). Machine learning-based forecasting of firemen ambulances’ turnaround time in hospitals, considering the COVID-19 impact. Applied Soft Computing, 109, 107561. https://doi.org/10.1016/j.asoc.2021.107561

bibtex: @article{Cerna2021,
  doi = {10.1016/j.asoc.2021.107561},
  url = {https://doi.org/10.1016/j.asoc.2021.107561},
  year = {2021},
  month = sep,
  publisher = {Elsevier {BV}},
  volume = {109},
  pages = {107561},
  author = {Selene Cerna and H{\'{e}}ber H. Arcolezi and Christophe Guyeux and Guillaume Royer-Fey and C{\'{e}}line Chevallier},
  title = {Machine learning-based forecasting of firemen ambulances' turnaround time in hospitals,  considering the {COVID}-19 impact},
  journal = {Applied Soft Computing}
}
