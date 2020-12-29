# Starbucks Offers
Once every few days, Starbucks sends out an offer to users on the mobile app. An offer can be an advertisement for a drink or an actual offer such as a discount or a bogo (buy one get one for free).
Every offer has a validity period before it expires and if conditions are met, a reward after the completion of the offer.

The goal of this project is to find what characteristics of the offer and the users make the completion more likely and to predict which user is going to complete an offer.

## Index

1. [Requirements](#requirements)
3. [Project](#project)
4. [Files](#files)
5. [Acknowledgements](#acknowledgements)

<a name="requirements"></a>
### Requirements
The libraries used in this project are:

scikit-learn 0.22.1, pandas 1.0.1, numpy1.18.1, json 0.9.1, plotly 4.8.2, xgboost 0.9 and scipy 1.4.1

<a name="projects"></a>
### Project

This project answers the following questions:
1. Which offer type has the highest rate of completions after viewed?
2. Does income or age affect the completion rate?
3. Does reward or duration affect the completion rate?
4. Can we predict if a user is going to complete the offer?

You can find a quick digestable analysis [in this Medium post](https://mauts.medium.com/analysis-of-offers-in-starbucks-5eb9a8ed6ddf), the complete analysis can be found [here](https://github.com/MauricioTrejo/StarbucksOffers/blob/master/Analysis.ipynb)

<a name="files"></a>
### Files

This repository contains the following folders and files:

* [analysis](https://github.com/MauricioTrejo/StarbucksOffers/blob/master/Analysis.ipynb). Contains the complete analysis in an ipython notebook.
* [functions](https://github.com/MauricioTrejo/StarbucksOffers/blob/master/functions.py). Contains all the functions needed by the analysis notebook.
* [users' paths](https://github.com/MauricioTrejo/StarbucksOffers/blob/master/paths.pkl). Contains a dictionary with the users' path (from receiving the offer till completion).
* [best xgboost parameters](https://github.com/MauricioTrejo/StarbucksOffers/blob/master/xgboost_gridsearch_params.pkl) Contains the parameters of the best xgboost model.
* [portfolio table](https://github.com/MauricioTrejo/StarbucksOffers/blob/master/portfolio.json) Contains the portfolio table.
* [profile table](https://github.com/MauricioTrejo/StarbucksOffers/blob/master/profile.json) Contains the profile table.
* [transcript table](https://github.com/MauricioTrejo/StarbucksOffers/blob/master/transcript.json) Contains the transcript table.

<a name="acknowledgements"></a>
### Acknowledgements

We want to thank [Starbucks](https://www.starbucks.com/) for the data used in this project and [Udacity](https://www.udacity.com/) for the material in the Data Science Nanodegree.
