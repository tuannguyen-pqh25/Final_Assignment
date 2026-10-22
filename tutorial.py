# # Final Assignment Tutorial — Telecom
# 
# This notebook is a reference walkthrough for the GCI World 2026 Winter final assignment.
# The dataset comes from **Company A**, an anonymous telecommunications service provider, and contains historical customer information across two linked tables (`Client.csv`, `Record.csv`).
# 
# Your task is to analyze this data, build a machine learning model whose output supports a concrete business proposal — not to build the best possible model.
# 
# **What this notebook walks through:**
# 1. Market context.
# 2. Loading and merging the two source tables.
# 3. EDA: shape, missingness, target distribution, and a worked feature example.
# 4. Problem Definition — choosing the target and the ML task.
# 5. Preprocessing — what EDA told us we have to do.
# 6. A baseline churn classifier.
# 7. Model evaluation and feature importance.
# 8. From model to business proposal.
# 
# > **Treat this as a reference, not a template.** The strongest submissions diverge from it: a different target, a different segment, a different lever. Originality is rewarded.

# ---
# 
# ## 1.Introduction & Market Analysis

# ### 1.1 Company context
# *Company A* is a wireless telecommunications operator. They have years of usage and billing data on roughly 100,000 customers but no in-house machine learning capability.
# 
# When a company commissions a business proposal, they usually arrive with a vague sense that *something* needs to improve — margins, retention, growth, customer satisfaction — but no clear view of which lever to pull, which segment to focus on, or even which question to start with. **Choosing the question is the analyst's first job, and the rest of the proposal stands or falls on it.** The dataset rarely points to a single obvious answer; it admits several, and which one you pursue determines the kind of recommendation you can make.
# 
# This dataset includes a binary `churn` flag — whether a customer left within 31–60 days after the observation date — and we use churn as the worked example throughout this notebook. But churn is one of many viable targets the data supports. **You may and should explore other targets** — revenue, usage, equipment lifecycle, segment-level behaviour. Pick the question whose answer best supports the proposal you want to make.

# ### 1.2 Why this market matters
# - Acquiring a new subscriber costs several times more than keeping one — retention, usage, and ARPU all translate directly into margin.
# - Mature, saturated markets grow by taking customers from competitors or lifting revenue per existing customer.
# - Behaviour signals (usage decline, complaints, equipment ageing) precede both churn and revenue compression by months.
# 
# **Questions to think about:**
# - What does the telecom market look like in your country or region — who are the major players, what local dynamics (regulation, technology shifts, new entrants) are reshaping churn, and what story can you tell about a specific market you know? A proposal grounded in a local market you can describe concretely is more compelling than one assembled from generic global figures.
# - What recent, citable sources can you find that quantify these claims for your target market? Uncited industry numbers will not strengthen your case.
# - What share of churn in this market is voluntary (customer-initiated) versus involuntary (non-payment, address change)? Which one can a model meaningfully address?

# ---
# 
# ## 2.Setup and Data Loading

# ### 2.1 Import libraries

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix

from xgboost import XGBClassifier, plot_importance

pd.set_option("display.max_columns", 120)

# ### 2.2 Connect to Google Drive
# 
# If you are running this notebook on Google Colab, mount your Drive and `cd` into the folder that contains the dataset.

# Run this cell only on Google Colab.
from google.colab import drive
drive.mount('/content/drive')

# **IMPORTANT**:<br>
# Change the path in the `%cd` command below to match the folder where this notebook is saved on Google Drive by **replacing "WhereThisNotebookIsLocated" with your actual folder path**.
# 
# Example:
# - You uploaded `Final Assignment` folder directly under MyDrive (the default folder when you open Google Drive)
#     - Change to "/content/drive/MyDrive/Final Assignment"
# 
# You can easily locate your notebook's directory by:
# 1. Open the Files panel on the left side of Colab
# 2. Navigate through the "drive" and "MyDrive" folders until you find your notebook's folders
# 3. Click the more actions icon (three vertical dots, ⁝) next to the folder name
# 4. Select the option "Copy path"

# ![tutorial.png](data:image/png;base64,...)