# Data Science Assignment: eCommerce Transactions

## Overview

This repository contains the complete implementation and reports for the Data Science assignment focused on eCommerce Transactions. The project consists of three tasks:

1. **Exploratory Data Analysis (EDA) and Business Insights**
2. **Lookalike Model Development**
3. **Customer Segmentation and Clustering**

Each task is aimed at deriving actionable insights, building predictive models, and implementing effective clustering techniques to support data-driven decision-making.

---

## Tasks Description

### Task 1: Exploratory Data Analysis (EDA) and Business Insights

#### Objective
Perform EDA on the provided dataset to uncover meaningful patterns, trends, and actionable insights. The analysis focuses on understanding customer behaviors, product performance, and transactional trends.

#### Process
- Analyzed customer demographics and regional distribution.
- Identified top-selling products and their revenue contributions.
- Examined seasonal trends in customer signups and transaction patterns.
- Highlighted high-value customers for loyalty-focused strategies.

#### Key Insights
- Regional distribution highlights potential areas for market penetration.
- Top-selling products contribute disproportionately to revenue.
- Seasonal trends indicate spikes in activity during holidays.
- High-value customers generate the majority of the revenue.

---

### Task 2: Lookalike Model

#### Objective
Develop a model that recommends three similar customers for any given customer based on their profile and transaction history.

#### Process
- Merged customer profile and transactional data to create aggregated features.
- Used cosine similarity to calculate similarity scores between customers.
- Generated recommendations for the first 20 customers (CustomerID: C0001 - C0020).

#### Model Highlights
- Similarity computation is based on features like TotalSpend and Quantity.
- Recommendations are tailored to match customers with similar purchasing behaviors.

---

### Task 3: Customer Segmentation and Clustering

#### Objective
Perform customer segmentation using clustering techniques to identify distinct groups based on transactional behavior.

#### Process
- Used KMeans clustering to segment customers into four clusters.
- Evaluated cluster performance using Davies-Bouldin Index and Silhouette Score.
- Visualized clusters using PCA for dimensionality reduction.

#### Clustering Metrics
- **Number of Clusters**: 4
- **Davies-Bouldin Index**: 0.78
- **Silhouette Score**: 0.65

#### Cluster Insights
- **Cluster 0**: High-value customers with frequent, large transactions.
- **Cluster 1**: Low-spending customers with minimal transactions.
- **Cluster 2**: Moderate spenders with steady purchase patterns.
- **Cluster 3**: Customers focused on high-value, premium products.

---

## How to Run

### Prerequisites
- Python 3.8 or above.
  
### Libraries:
- pandas
- numpy
- matplotlib
- seaborn
- scikit-learn

### Instructions

1. Clone the repository:
   ```bash
   git clone <repository_link>
   cd <repository_folder>
