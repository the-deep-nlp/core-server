## Generate Embeddings and Predictions

Import and use the class `ClassificationModelOutput` from the script `generate_outputs.py` 
to generate the embeddings and predictions of the excerpts. This input expects a 
dataframe with fields `entry_id`, `excerpts` and optional fields `sectors`,
`subpillars_1d`, `subpillars_2d`. These optional fields are the ground truths
set by the users when creating the entry in Deep.

The outputs returns a dataframe with fields like `entry_id`, `embeddings`,
`sectors_pred`, `subpillars_2d_pred`, `subpillars_1d_pred`, `age_pred`,
`gender_pred`, `affected_groups_pred`, `specific_needs_groups_pred`,
`severity_pred`.

In this imported class, we can pass arguments to get only the embeddings or
predictions or both.

## Calculate Model Performance metrics 
Once we have the embeddings and predicted tags on each category and grouth 
truths fetched from the deep database, prepare a dataframe consisting of 
following columns `entry_id`, `excerpt`, `project_id`, `sectors`, `subpillars_1d`,
`subpillars_2d`, `sectors_pred`, `subpillars_1d_pred`, `subpillars_2d_pred`.

There are several methods/functions that can be called in this script which
computes the performance metrics on project basis, tag basis, overall project
basis etc by importing and using the class `ModelPerformance` from the script 
`model_performance.py`

## Calculate Feature Drift For feature drift, first calculate the Embeddings
Using the class imported from the script `generate_output.py` and using the 
class `FeatureDrift` from the script `featuredrift.py` to calculate the 
feature drift on the project level. For this, we need to prepare
two dataframes, one dataframe which is a reference one using the embeddings of
the excerpts from the training data(this remains fixed) and dataframe
consisting of the `project_id` and `embeddings` of the excerpts from the
production/new data.
