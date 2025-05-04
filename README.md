# Predict H1N1 and Seasonal Flu Vaccines

## Overview

This is a practice competition hosted at [DrivenData](https://www.drivendata.org/competitions/66/flu-shot-learning/). It aims at predicting whether people got H1N1 and seasonal flu vaccines using information they shared about their backgrounds, opinions, and health behaviors. This is a multilabel problem as two target variables, 1. whether respondent received H1N1 flu vaccine, and 2. whether respondent received seasonal flu vaccine, will be predicted.

## Implication

Helping the government to target and encourage citizens whom are less likely to get the vaccines in order to increase vaccination, so as to provide immunization for more individuals, and enough immunization in a community can further reduce the spread of diseases through "herd immunity."

## Author

Jackie Chan (jackiecareer89@gmail.com)


## Data

*   Data is provided courtesy of the United States [National Center for Health Statistics](https://www.cdc.gov/nchs/index.html?CDC_AA_refVal=https%3A%2F%2Fwww.cdc.gov%2Fnchs%2Findex.htm)
*   Data cleaning and preprocessing
    * Features with ordinal data will be scaled by normalization because there are several ranges, such as 0-3, 0-2, 1-5, etc.. After scaling, I will assume the greater the number, the more likely the respondent will take the vaccine.
    *  For most numerical features, each feature only contains <3.6% missing values. While the second most missing values are in 'doctor_recc_h1n1' and 'doctor_recc_seasonal' columns, which are 8% respectively. Lastly, 'health_insurance' has the most of missing values, containing 46%.
        * Except 'health_insurance', the missing values will be imputed with mode
        * For 'health_insurance', the missing values will be treated as a new category
    * For categorical features, 7 out of 12 columns contains missing values. Most of them contains less than 8%. For 'income_poverty', 'employment_industry' and 'employment_occupation' columns, missing values will be treated as new group because they contain 17%, 50% and 50% missing values respectively
        * One-hot-encoding will be applied since those categorical features are nominal data


## Methods

*   Description of the methods used (e.g., machine learning algorithms, statistical techniques)
    * 
*   Explanation of the feature engineering process
    * 
*   Model evaluation metrics
    * ROC AUC

## Results

*   Summary of the key findings
    * 
*   Visualizations of the results
    * 
*   Discussion of the limitations of the study
    * 

## Usage

Instructions on how to set up the project, run the code, and reproduce the results.

### Prerequisites

*   Python 3.x
*   Pip
*   Virtualenv (optional)

### Installation

1.  Clone the repository:

    ```bash
    git clone https://github.com/funnychan01/predict_h1n1_and_seasonal_flu_vaccines
    ```

2.  Create a virtual environment:

    ```bash
    virtualenv venv
    source venv/bin/activate
    ```

3.  Install the dependencies:

    ```bash
    pip install -r requirements.txt
    ```

### Running the code

1.  Run the notebooks in the `notebooks/` directory.
2.  Run the scripts in the `src/` directory.
