# Bank Marketing Campaigns Analysis Project

## Overview
This project analyzes the effectiveness of bank marketing campaigns using the "Bank Marketing Campaigns Dataset" from Kaggle. The goal is to evaluate campaign performance, demographic influences, and customer sentiment/behavior, providing actionable insights for business decisions. The analysis leverages Python for data processing, Excel for basic reporting, and Power BI for interactive visualizations.

## Project Objectives
- **Campaign Performance**: Analyze the acceptance rate of marketing campaigns based on the number of contacts, call duration, and engagement scores.
- **Demographic Influences**: Assess how demographics (age, job, marital status) impact campaign outcomes.
- **Sentiment/Behavior**: Derive customer sentiment and behavior from previous campaign outcomes (`poutcome`).

## Dataset
- **Source**: [Bank Marketing Campaigns Dataset](https://www.kaggle.com/datasets/volodymyrgavrysh/bank-marketing-campaigns-dataset) on Kaggle.
- **Description**: Contains data on telemarketing campaigns for a Portuguese bank, including customer demographics, campaign details, and outcomes (e.g., whether a customer subscribed to a term deposit).
- **Columns**: `age`, `job`, `marital`, `education`, `default`, `housing`, `loan`, `contact`, `month`, `day_of_week`, `duration`, `campaign`, `pdays`, `previous`, `poutcome`, `emp.var.rate`, `cons.price.idx`, `cons.conf.idx`, `euribor3m`, `nr.employed`, `y` (response).

## Tools and Technologies
- **Programming Language**: Python (with libraries: `pandas`, `matplotlib`, `seaborn`, `textblob`)
- **Data Analysis**: Excel (Pivot Tables, Charts)
- **Visualization**: Power BI (Dashboards, Custom Visuals like Box and Whisker Chart)
- **Environment**: Virtual environment (`iphone16_env`) managed in VS Code

## Install Dependencies:
Install required Python libraries: pip install pandas numpy matplotlib seaborn textblob

## Visualize with Excel and Power BI:
Open marketing_campaign_analyzed_data.csv in Excel to create Pivot Tables and charts.
Import marketing_campaign_analyzed_data.csv into Power BI Desktop to create interactive dashboards (use semicolon ; as delimiter in Power Query Editor).

## Usage
Python Scripts: The scripts process the dataset, clean it, analyze performance metrics, and generate visualizations saved as .png files.
Excel: Use Pivot Tables to analyze acceptance rates by demographics and create basic charts.
Power BI: Build interactive dashboards with visuals like Column Charts, Bar Charts, Pie Charts, and Box and Whisker Charts to explore campaign effectiveness, demographics, and sentiment.

##Key Insights
The analysis provides the following key insights (from analyze_data.py):

Campaign Performance: Customers who accept the campaign typically have fewer contacts (average ~2.5) and longer call durations (~300 seconds) compared to those who reject (average ~3.5 contacts, ~200 seconds). Excessive contacts (>5) and short durations may reduce acceptance rates.
Demographic Influences: Middle-aged customers and professions like "management" or "technician" show higher acceptance rates (around 15-20%), indicating better campaign effectiveness with these groups.
Sentiment/Behavior: Previous campaign successes ("positive" poutcome) significantly increase acceptance rates (~50-60%), while failures or neutral outcomes reduce rates to below 10%.
