# 📊 Machine Learning Template Constructor (MLTC)
The Machine Learning Template Constructor (MLTC) is a CLI tool designed to streamline the process of setting up machine learning projects by providing a structured way to select, merge, and utilize a variety of Jupyter notebook templates. These templates cover different stages of the machine learning project lifecycle, from problem definition to model evaluation.

## 🔧 How to Use
To use MLTC, follow these steps:

1. **Install Dependencies**: Ensure that you have Python installed on your system along with the required libraries. You may need to install `click`, `nbformat`, and any other libraries used by the templates.

2. **Clone the Repository**: Clone this repository to your local machine to get started. This will include the MLTC tool and the available notebook templates.

3. **Navigate to the MLTC Directory**: Open a terminal and navigate to the directory where you cloned the MLTC repository.

4. **Run the Tool**: Execute the tool using the following command:
   ```bash
   poetry run mltc --templates-dir <path_to_templates_directory> --output-path <path_to_output_notebook>
   ```
   `<path_to_templates_directory>`: This is the path to the directory containing the Jupyter notebook templates. By default, it points to the templates directory within the MLTC repository.
   `<path_to_output_notebook>`: This is the path where the merged notebook will be saved. By default, it creates an mltc.ipynb file in the root of the MLTC repository.

5. **Select Templates**: The tool will display a list of available notebook templates. Enter the indices of the notebooks you wish to merge, separated by spaces (e.g., 1 2 3).

6. **Merged Notebook**: Once the selected templates are merged, the output notebook will be saved at the specified path. Open this notebook in Jupyter or your preferred notebook editor to start working on your machine learning project.

## 🧠 Templates
These templates are created to serve as my personal starting point for machine learning projects. They help me quickly set up experiments and ensure consistency in my workflow, whether I'm working on a new project or revisiting an old one.

As of now, the following templates are available, each designed to address a specific stage of the machine learning project lifecycle. Feel free to use, modify, or extend these templates to suit your needs, the templates are located in the [`mltc/templates`](/mltc/templates/) directory. 

### 1. Problem Definition
[`mltc > templates > problem-definition > problem-definition.ipynb`](/mltc/templates/problem-definition/problem-definition.ipynb)

This template is used to define the problem statement and objectives of the machine learning project. It includes sections for:

- **Sources:** Listing the sources of any relevant background information used throughout the notebook.
- **Problem Statement:** Defining the problem that the notebook aims to solve.
- **Objectives:** Listing the specific objectives that the notebook aims to achieve.
- **Data Description:** Describing the dataset used in the notebook.

### 2. Setup
[`mltc > templates > setup > setup.ipynb`](/mltc/templates/setup/setup.ipynb)

This template is used to set up the machine learning project. It includes sections for:

- **Importing Libraries:** Importing the necessary Python libraries for the project.
- **Loading Data:** Loading the dataset into a Pandas DataFrame, the source can be anything depending on the project (e.g. CSV, SQL, etc.).

### 3. Preprocessing
[`mltc > templates > preprocessing > data-preparation.ipynb`](/mltc/templates/preprocessing/data-preparation.ipynb)

This template is used to preprocess the data before training the machine learning model. It includes sections for:

- **Preview Data:** Displaying an overview of the dataset, including the first few rows and column names.
- **Remove Unvaluable Columns:** Removing columns that are not useful for the analysis.
- **Check for Missing Data:** Identifying missing values in the dataset and deciding how to handle them.
- **Check Unique Value Count:** Checking the number of unique values for each column to determine the imputation technique.
- **Determine Imputation Technique:** Deciding on the imputation technique for each feature based on the data distribution.
- **Impute Missing Values:** Imputing missing values using the chosen imputation technique.
- **Find & Remove Outliers:** Identifying and removing outliers from the dataset.
- **Convert Formats:** Converting data into a suitable format for the machine learning model.
- **Verify Preprocessed Data:** Verifying that the data has been preprocessed successfully.

### 4. Data Analysis
[`mltc > templates > data-analysis > data-exploration.ipynb`](/mltc/templates/data-analysis/data-exploration.ipynb)

This template is used to analyze the data and identify patterns, trends, and relationships between variables. It includes sections for:

- **Understand the Distribution of Data:** Analyzing the distribution of numerical features using histograms, density plots, and box plots.
- **Visualize Data Distribution:** Creating visualizations to understand the distribution of data for numerical features.
- **Analyze Categorical Variables:** Visualizing the distribution of categorical variables using bar plots and count plots.
- **Explore Relationships Between Variables:** Investigating relationships between variables using correlation analysis, scatter plots, and pair plots.
- **Identify Patterns and Trends:** Identifying patterns and trends in the data, such as time series analysis, group analysis, and statistical testing.
- **Statistical Testing:** Conducting hypothesis tests and checking assumptions for statistical models.
- **Finalize EDA:** Summarizing the insights gained from exploratory data analysis and outlining the next steps for feature engineering and model selection.

### 5. Modelling
[`mltc > templates > modelling > binary-classification.ipynb`](/mltc/templates/modelling/binary-classification.ipynb)

This template is used to train and evaluate binary classification models. It includes sections for:

- **Prepare the Data:** Defining the target and features, splitting the data into training, validation, and test sets.
- **Train and Evaluate:** Training and evaluating different binary classification models, such as logistic regression, decision trees, random forests, and support vector machines.
- **Compare Models:** Comparing the performance of different models based on metrics like accuracy, precision, recall, F1 score, and ROC AUC.
- **Evaluate Best Model:** Evaluating the best-performing model on the test set and interpreting the ROC curve and AUC score.
- **Document Findings and Next Steps:** Summarizing the performance metrics of the final model, discussing its strengths and weaknesses, and providing insights into how the model can be used in practice.

[`mltc > templates > modelling > multi-class-multi-label-classification.ipynb`](/mltc/templates/modelling/multi-class-multi-label-classification.ipynb)

This template is used to train and evaluate multi-class and multi-label classification models. It includes sections for:

- **Prepare the Data:** Defining the target and features, splitting the data into training, validation, and test sets.
- **Train and Evaluate:** Training and evaluating different multi-class and multi-label classification models, such as logistic regression, decision trees, random forests, and support vector machines.
- **Compare Models:** Comparing the performance of different models based on metrics like accuracy, precision, recall, F1 score, and macro/micro-averaged metrics.
- **Evaluate Best Model:** Evaluating the best-performing model on the test set and interpreting the confusion matrix, classification report, and other relevant metrics.
- **Document Findings and Next Steps:** Summarizing the performance metrics of the final model, discussing its strengths and weaknesses, and providing insights into how the model can be used in practice.

## 🔮 Possible Improvements   
- Add more templates, including clustering, regression, time series, reinforcement learning, natural language processing, and computer vision. 
- Include actual code in the templates, rather than just placeholders.

   > 💭 This opens up the possibility of using AI to generate the code based on the template, in a predefined structure.
   > Function-calling could be used to construct the notebook, with the user only needing to provide the data.

## 📊 Current State of the Project
This repository is a work in progress. If you have any ideas, suggestions, or improvements, feel free to reach out or open an issue in the GitHub repository.