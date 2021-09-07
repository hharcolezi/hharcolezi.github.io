---
title: "Identifying the knee joint angular position under neuromuscular electrical stimulation via long short-term memory neural networks"
collection: publications
permalink: /publication/identification-angular-position-nmes-lstm
date: 2020-09-04
venue: 'Research on Biomedical Engineering'
---


[Download paper here](http://hharcolezi.github.io/files/2020_RBEB_LSTM_Identification.pdf)

Abstract: *Purpose* Recurrent neural networks (RNNs) offer a promising opportunity for identifying nonlinear systems. This paper investigates the effectiveness of the long short-term memory (LSTM) RNN architecture in the specific task of identifying the knee joint angular position under neuromuscular electrical stimulation (NMES). The standard RNN model referred to as SimpleRNN and the well-known multilayer perceptron (MLP) are used for comparison purposes. *Methods* Data from seven healthy and two paraplegic volunteers were experimentally acquired. These data were adequately scaled, encoded using three timestep values (1, 5, and 10), and divided into training, validation, and testing sets. These models were mainly evaluated using the root mean square error (RMSE) and training time metrics. *Results* The three NN models demonstrated very good fitting to data for all volunteers. The LSTM presented smaller RMSE for most of the individuals. This is even more notable when using 5 and 10 timesteps achieving half and one-third of the error from MLP and half of the error from the SimpleRNN. This higher utility comes with a substantial time-utility trade-off. *Conclusion* The results in this paper show that the LSTM worths deeper investigation to design control-oriented models to knee joint stimulation in closed-loop systems. Even though the LSTM takes more time for training due to a more complex architecture, time and computational costs could be increased if achieving better modeling of systems. Rather than mathematically modeling this system with several unique parameters per individual, the use of NNs is encouraged in this task where there exist high nonlinearities and time-varying parameters.

Recommended citation: Arcolezi, H.H., Nunes, W.R.B.M., Cerna, S. et al. Identifying the knee joint angular position under neuromuscular electrical stimulation via long short-term memory neural networks. Res. Biomed. Eng. 36, 511–526 (2020). https://doi.org/10.1007/s42600-020-00089-1

bibtex: @article{Arcolezi2020,
  doi = {10.1007/s42600-020-00089-1},
  url = {https://doi.org/10.1007/s42600-020-00089-1},
  year = {2020},
  month = sep,
  publisher = {Springer Science and Business Media {LLC}},
  volume = {36},
  number = {4},
  pages = {511--526},
  author = {H{\'{e}}ber H. Arcolezi and Willian R. B. M. Nunes and Selene Cerna and Rafael A. de Araujo and Marcelo Augusto Assun{\c{c}}{\~{a}}o Sanches and Marcelo Carvalho Minhoto Teixeira and Aparecido Augusto de Carvalho},
  title = {Identifying the knee joint angular position under neuromuscular electrical stimulation via long short-term memory neural networks},
  journal = {Research on Biomedical Engineering}
}
