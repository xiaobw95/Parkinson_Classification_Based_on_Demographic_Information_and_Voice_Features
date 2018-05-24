# Parkinson_Classification_Based_on_Demographic_Information_and_Voice_Features

Using demographic information and GeMAPS extracted features of voice to classify a patient diagnosed with Parkinson’s disease. I started with demogrphics data (~80% negative cases), testing different classification methods (achieved ~90% accuracy), and then went on combining with voice features (~60% negative cases). Finally, I used a hierarchical regularized logistic regression and achieved 90% accuracy and 86% recall. 

Also, I packed the combined data to a simple neural network (single hidden layer with some dropout, mini batch and scale adjustment), I set the estimated parameter of logistic regression with demographic data as initial weights and it turned out to be a tiny improvement (achieved ~90% accuracy and ~80% callback).

## Organization

-   `README.md`: This file, describing the content project.

-   `doc`: Documents and analysis

    -   `Analysis.pdf`: this is my main analysis.

-   `src`: Any R scripts (`.R`) and Python scripts (`.py`) used in the analysis.

-   `data`: Input data used in the analysis. Files in this directory should be treated as read only.


## Dependence

R packages for this project:

```r
# List of the packages this project depends on
packages <- c("mlbench","e1071","randomForest","xgboost","glmnet","party","effects")
if(!require(packages)){
  install.packages(packages)
  require(packages)
}
```

Python requirements for this project:

- python 2.7
- numpy==1.12.1
- scipy==0.19.0

## Data

The data used for this analysis was collected by Sage Bionetworks through the [mPower research study](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4776701/pdf/sdata201611.pdf). The voice activity in the application recorded the user’s voice making the sound ‘aaah’ for 10 seconds. The audio samples collected via the mobile application were converted into over 58,000 json files with the help of the pyAudioAnalysis library. I am only used demographic data and GeMAPS extracted features of the voices.

## Main Results

- Analysis of Demographic Information
    |Method|Accuracy|Recall|
    |---|---|---|
    |logistic|0.91|0.68|
    |SVM|0.91|0.64|
    |Naive Bayes|0.91|0.81|
    |Random Forest|0.92|0.74|
    |XGBoost|0.91|0.75|
    
- Combining with Voice Features
    |Method|Accuracy|Recall|
    |---|---|---|
    |Baseline1-Demographics|0.891|0.786|
    |Baseline2-Voice|0.719|0.476|
    |Regularized Logistic|0.893|0.787|
    |Hierarchical Regularized Logistic|0.901|0.863|


## Build

- R: Open `src/R/Analysis.Rmd` and knit the file.
- Python: run `src/Python/parkinson.py`
