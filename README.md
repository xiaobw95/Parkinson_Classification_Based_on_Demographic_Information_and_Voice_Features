# Parkinson_Classification_Based_on_Demographics_Information_and_Voice_Features

Using demographics information and GeMAPS extracted features of voice to classify a patient diagnosed with Parkinson’s disease. I started with demogrphics data (~80% negative cases), testing different classification methods (achieved ~90% accuracy), and then went on combining with voice features (~60% negative cases). Finally, I packed the data to a simple neural network (single hidden layer with some dropout, mini batch and scale adjustment), I set the estimated parameter of logistic regression with demographics data as initial weights and it turned out to be a little improvement (achieved ~90% accuracy and ~80% callback).

## Organization

-   `README.md`: This file, describing the content project.

-   `doc`: Documents and analysis

    -   `Analysis_of_demographics_information.pdf`: this is my main analysis.

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

The data used for this analysis was collected by Sage Bionetworks through the mPower research study. The voice activity in the application recorded the user’s voice making the sound ‘aaah’ for 10 seconds. The audio samples collected via the mobile application were converted into over 58,000 json files with the help of the pyAudioAnalysis library. I am only used demographics data and GeMAPS extracted features of the voices.

## Build

R: Open `src/R/Analysis_of_demographics_information.Rmd` and knit the file.
Python: run `src/Python/parkinson.py`
