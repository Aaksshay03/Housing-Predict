# -*- coding: utf-8 -*-
"""Housing Price Prediction.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1_DEqAIElsrOOUATnC5OBRkLC45jIYpn4
"""

#import Libraries

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import LabelEncoder, MinMaxScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.svm import SVR
from sklearn.model_selection import GridSearchCV, RandomizedSearchCV
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error

# Load the Data Set

df = pd.read_csv('/content/Housing.csv')

# Exploratory Data Analysis
df.head()

df.info()

df.describe()

df.isna().sum()

# Data Visualisation

# Transforming price to millions for better readability
df['price_millions'] = df['price'] / 1e6

plt.figure(figsize=(10, 6))
sns.histplot(df['price_millions'], kde=True, color='skyblue', edgecolor='black')

plt.title('Distribution of House Prices', fontsize=16)
plt.xlabel('Price (in millions)', fontsize=12)
plt.ylabel('Frequency', fontsize=12)

plt.xticks(fontsize=10)
plt.yticks(fontsize=10)

plt.tight_layout()
plt.show()

"""This histogram shows a slightly right-skewed distribution of house prices. The majority of houses are priced between 3 million USD and 5 million USD, while a small number of high-priced properties create the skew.
This type of distribution is typical in housing markets, where most properties are mid-priced, with a few luxury homes at the higher end of the market.
"""

plt.figure(figsize=(8, 5))

ax = sns.countplot(x=df['mainroad'], hue=df['mainroad'], palette='pastel', dodge=False, edgecolor='black', order=['yes', 'no'])

for p in ax.patches:
    ax.annotate(f'{int(p.get_height())}',
                (p.get_x() + p.get_width() / 2., p.get_height() + 3),
                ha='center', fontsize=10)
# The following line was incorrectly indented. Corrected the indentation to align with other lines in the block.
plt.title("Distribution of Mainroad", fontsize=16, fontweight='bold')
plt.xlabel("Mainroad", fontsize=14, labelpad=10)
plt.ylabel("Count", fontsize=14, labelpad=10)

plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.grid(axis='y', linestyle='--', alpha=0.7)

plt.legend([], [], frameon=False)

plt.tight_layout()
plt.show()

plt.figure(figsize=(8, 5))

ax = sns.countplot(x=df['guestroom'], hue=df['guestroom'], palette='pastel', dodge=False, edgecolor='black', order=['yes', 'no'])

for p in ax.patches:
    ax.annotate(f'{int(p.get_height())}',
                (p.get_x() + p.get_width() / 2., p.get_height() + 3),
                ha='center', fontsize=10)

plt.title("Distribution of Guestroom", fontsize=16, fontweight='bold')
plt.xlabel("Guestroom", fontsize=14, labelpad=10)
plt.ylabel("Count", fontsize=14, labelpad=10)

plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.grid(axis='y', linestyle='--', alpha=0.7)

plt.legend([], [], frameon=False)

plt.tight_layout()

plt.figure(figsize=(8, 5))

ax = sns.countplot(x=df['basement'], hue=df['basement'], palette='pastel', dodge=False, edgecolor='black', order=['yes', 'no'])

for p in ax.patches:
    ax.annotate(f'{int(p.get_height())}',
                (p.get_x() + p.get_width() / 2., p.get_height() + 3),
                ha='center', fontsize=10)

plt.title("Distribution of Basement", fontsize=16, fontweight='bold')
plt.xlabel("Basement", fontsize=14, labelpad=10)
plt.ylabel("Count", fontsize=14, labelpad=10)

plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.grid(axis='y', linestyle='--', alpha=0.7)

plt.legend([], [], frameon=False)

plt.tight_layout()
plt.show()

plt.figure(figsize=(8, 5))

ax = sns.countplot(x=df['hotwaterheating'], hue=df['hotwaterheating'], palette='pastel', dodge=False, edgecolor='black', order=['yes', 'no'])

for p in ax.patches:
    ax.annotate(f'{int(p.get_height())}',
                (p.get_x() + p.get_width() / 2., p.get_height() + 3),
                ha='center', fontsize=10)

plt.title("Distribution of Hot Water Heating", fontsize=16, fontweight='bold')
plt.xlabel("Hot Water Heating", fontsize=14, labelpad=10)
plt.ylabel("Count", fontsize=14, labelpad=10)

plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.grid(axis='y', linestyle='--', alpha=0.7)

plt.legend([], [], frameon=False)

plt.tight_layout()
plt.show()

plt.figure(figsize=(8, 5))

ax = sns.countplot(x=df['airconditioning'], hue=df['airconditioning'], palette='pastel', dodge=False, edgecolor='black', order=['yes', 'no'])

for p in ax.patches:
    ax.annotate(f'{int(p.get_height())}',
                (p.get_x() + p.get_width() / 2., p.get_height() + 3),
                ha='center', fontsize=10)

plt.title("Distribution of Air Conditioning", fontsize=16, fontweight='bold')
plt.xlabel("Air Conditioning", fontsize=14, labelpad=10)
plt.ylabel("Count", fontsize=14, labelpad=10)

plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.grid(axis='y', linestyle='--', alpha=0.7)

plt.legend([], [], frameon=False)

plt.tight_layout()
plt.show()

plt.figure(figsize=(8, 5))

ax = sns.countplot(x=df['prefarea'], hue=df['prefarea'], palette='pastel', dodge=False, edgecolor='black', order=['yes', 'no'])

for p in ax.patches:
    ax.annotate(f'{int(p.get_height())}',
                (p.get_x() + p.get_width() / 2., p.get_height() + 3),
                ha='center', fontsize=10)

plt.title("Distribution of Preferred Area", fontsize=16, fontweight='bold')
plt.xlabel("Preferred Area", fontsize=14, labelpad=10)
plt.ylabel("Count", fontsize=14, labelpad=10)

plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.grid(axis='y', linestyle='--', alpha=0.7)

plt.legend([], [], frameon=False)

plt.tight_layout()
plt.show()

plt.figure(figsize=(8, 5))

ax = sns.countplot(x=df['furnishingstatus'], hue=df['furnishingstatus'], palette='pastel', dodge=False, edgecolor='black', order=['unfurnished', 'semi-furnished', 'furnished'])

for p in ax.patches:
    ax.annotate(f'{int(p.get_height())}',
                (p.get_x() + p.get_width() / 2., p.get_height() + 3),
                ha='center', fontsize=10)

plt.title("Distribution of Furnishing Status", fontsize=16, fontweight='bold')
plt.xlabel("Furnishing Status", fontsize=14, labelpad=10)
plt.ylabel("Count", fontsize=14, labelpad=10)

plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.grid(axis='y', linestyle='--', alpha=0.7)

plt.legend([], [], frameon=False)

plt.tight_layout()
plt.show()

plt.figure(figsize=(8, 5))

ax = sns.countplot(x=df['bedrooms'], hue=df['bedrooms'], palette='pastel', dodge=False, edgecolor='black')

for p in ax.patches:
    ax.annotate(f'{int(p.get_height())}',
                (p.get_x() + p.get_width() / 2., p.get_height() + 3),
                ha='center', fontsize=10)

plt.title("Distribution of Bedrooms", fontsize=16, fontweight='bold')
plt.xlabel("Number of Bedrooms", fontsize=14, labelpad=10)
plt.ylabel("Count", fontsize=14, labelpad=10)

plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.grid(axis='y', linestyle='--', alpha=0.7)

plt.legend([], [], frameon=False)

plt.tight_layout()
plt.show()

plt.figure(figsize=(8, 5))

ax = sns.countplot(x=df['bathrooms'], hue=df['bathrooms'], palette='pastel', dodge=False, edgecolor='black')

for p in ax.patches:
    ax.annotate(f'{int(p.get_height())}',
                (p.get_x() + p.get_width() / 2., p.get_height() + 3),
                ha='center', fontsize=10)

plt.title("Distribution of Bathrooms", fontsize=16, fontweight='bold')
plt.xlabel("Number of Bathrooms", fontsize=14, labelpad=10)
plt.ylabel("Count", fontsize=14, labelpad=10)

plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.grid(axis='y', linestyle='--', alpha=0.7)

plt.legend([], [], frameon=False)

plt.tight_layout()
plt.show()

plt.figure(figsize=(8, 5))

ax = sns.countplot(x=df['stories'], hue=df['stories'], palette='pastel', dodge=False, edgecolor='black')

for p in ax.patches:
    ax.annotate(f'{int(p.get_height())}',
                (p.get_x() + p.get_width() / 2., p.get_height() + 3),
                ha='center', fontsize=10)

plt.title("Distribution of Stories", fontsize=16, fontweight='bold')
plt.xlabel("Number of Stories", fontsize=14, labelpad=10)
plt.ylabel("Count", fontsize=14, labelpad=10)

plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.grid(axis='y', linestyle='--', alpha=0.7)

plt.legend([], [], frameon=False)

plt.tight_layout()
plt.show()

plt.figure(figsize=(8, 5))

ax = sns.countplot(x=df['parking'], hue=df['parking'], palette='pastel', dodge=False, edgecolor='black')

for p in ax.patches:
    ax.annotate(f'{int(p.get_height())}',
                (p.get_x() + p.get_width() / 2., p.get_height() + 3),
                ha='center', fontsize=10)

plt.title("Distribution of Parking Spaces", fontsize=16, fontweight='bold')
plt.xlabel("Number of Parking Spaces", fontsize=14, labelpad=10)
plt.ylabel("Count", fontsize=14, labelpad=10)

plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.grid(axis='y', linestyle='--', alpha=0.7)

plt.legend([], [], frameon=False)

plt.tight_layout()
plt.show()

plt.figure(figsize=(10, 6))

sns.scatterplot(x=df['area'], y=df['price_millions'], alpha=0.7, edgecolor='w')

sns.regplot(x=df['area'], y=df['price_millions'], scatter=False, color='red', line_kws={'linewidth': 2, 'alpha': 0.8})

plt.title("Relationship Between Area and Price", fontsize=16, fontweight='bold')
plt.xlabel("Area (in square feet)", fontsize=14, labelpad=10)
plt.ylabel("Price (in millions)", fontsize=14, labelpad=10)

plt.xticks(fontsize=12)
plt.yticks(fontsize=12)

plt.grid(True, linestyle='--', alpha=0.7)

plt.tight_layout()
plt.show()

"""The scatter plot illustrates the relationship between house prices and area. A positive trend is evident, where larger areas are generally associated with higher prices. This trend is captured by the upward-sloping red trendline.

There is a high density of houses within the area range of 2,000 to 7,000 square feet, suggesting that most properties in the dataset fall into this size category. Outliers are also visible, such as smaller houses with unusually high prices or larger houses with lower prices, which may indicate unique characteristics or market conditions.


"""

plt.figure(figsize=(10, 6))

sns.boxplot(x=df['bedrooms'], y=df['price_millions'], hue=df['bedrooms'], dodge=False, width=0.6, palette='coolwarm')

plt.title("Price vs. Number of Bedrooms", fontsize=16, fontweight='bold')
plt.xlabel("Number of Bedrooms", fontsize=14, labelpad=10)
plt.ylabel("Price (in millions)", fontsize=14, labelpad=10)

plt.xticks(fontsize=12)
plt.yticks(fontsize=12)

plt.legend([], [], frameon=False)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

"""The boxplot illustrates the relationship between house prices and the number of bedrooms. The median price increases consistently from houses with 1 to 5 bedrooms, reflecting a positive relationship between the number of bedrooms and price. However, for houses with 6 bedrooms, the median price drops slightly, indicating that larger houses may not always command higher prices.

Houses with 5 bedrooms exhibit the largest interquartile range (IQR), suggesting a wider variability in prices within this category. Additionally, houses with 3, 4, and 5 bedrooms show notable outliers in the upper range, which may represent luxury or high-end properties.
"""

plt.figure(figsize=(10, 6))

sns.boxplot(x=df['bathrooms'], y=df['price_millions'], hue=df['bathrooms'], dodge=False, width=0.6, palette='viridis')

plt.title("Price vs. Number of Bathrooms", fontsize=16, fontweight='bold')
plt.xlabel("Number of Bathrooms", fontsize=14, labelpad=10)
plt.ylabel("Price (in millions)", fontsize=14, labelpad=10)

plt.xticks(fontsize=12)
plt.yticks(fontsize=12)

plt.legend([], [], frameon=False)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

"""The boxplot illustrates the relationship between house prices and the number of bathrooms. Houses with 3 bathrooms exhibit the IQR, indicating greater variability in prices within this category. Additionally, houses with 3 bathrooms have the highest median price, although houses with 4 bathrooms technically have a higher value, this category only includes a single house, making it less representative.

Houses with 1 bathroom display a significant number of outliers in the upper price range. This is likely due to the high number of houses with 1 bathroom, as well as the presence of unique or luxury properties within this category.
"""

plt.figure(figsize=(10, 6))

sns.boxplot(x=df['stories'], y=df['price_millions'], hue=df['stories'], dodge=False, width=0.6, palette='Set2')

plt.title("Price vs. Number of Stories", fontsize=16, fontweight='bold')
plt.xlabel("Number of Stories", fontsize=14, labelpad=10)
plt.ylabel("Price (in millions)", fontsize=14, labelpad=10)

plt.xticks(fontsize=12)
plt.yticks(fontsize=12)

plt.legend([], [], frameon=False)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

"""The boxplot illustrates the relationship between house prices and the number of stories. The median price increases steadily from houses with 1 to 4 stories, indicating a positive correlation between the number of stories and price.

The interquartile ranges (IQRs) are similar across all categories, suggesting comparable variability in prices for houses with different numbers of stories. However, houses with 2 stories exhibit a large number of outliers in the upper price range, potentially representing luxury or high-value properties within this category.
"""

plt.figure(figsize=(10, 6))

sns.boxplot(
    x=df['furnishingstatus'],
    y=df['price_millions'],
    hue=df['furnishingstatus'],
    dodge=False,
    width=0.6,
    palette='pastel',
    order=['unfurnished', 'semi-furnished', 'furnished']
)

plt.title("Price vs. Furnishing Status", fontsize=16, fontweight='bold')
plt.xlabel("Furnishing Status", fontsize=14, labelpad=10)
plt.ylabel("Price (in millions)", fontsize=14, labelpad=10)

plt.legend([], [], frameon=False)

plt.xticks(fontsize=12)
plt.yticks(fontsize=12)

plt.grid(axis='y', linestyle='--', alpha=0.7)

plt.tight_layout()
plt.show()

"""The boxplot illustrates the relationship between house prices and furnishing status. Furnished houses have the highest median price, indicating that fully furnished homes tend to command a premium in the market. This category also exhibits the largest interquartile range (IQR), suggesting greater variability in prices for furnished properties.

All three categories display outliers, but the number varies significantly. Furnished houses have the fewest outliers, while Semi-Furnished houses display a high number of outliers, particularly in the upper price range. These outliers may represent luxury or unique properties within each category.
"""

plt.figure(figsize=(10, 6))

sns.boxplot(
    x=df['parking'],
    y=df['price_millions'],
    hue=df['parking'],
    dodge=False,
    width=0.6,
    palette='pastel'
)

plt.title("Price vs. Parking Spaces", fontsize=16, fontweight='bold')
plt.xlabel("Number of Parking Spaces", fontsize=14, labelpad=10)
plt.ylabel("Price (in millions)", fontsize=14, labelpad=10)

plt.xticks(fontsize=12)
plt.yticks(fontsize=12)

plt.grid(axis='y', linestyle='--', alpha=0.7)

plt.legend([], [], frameon=False)

plt.tight_layout()
plt.show()

"""The boxplot illustrates the relationship between house prices and the number of parking spaces. Houses with 0 parking spaces have the lowest median price, while houses with 2 parking spaces have the highest median price, indicating that additional parking spaces may add value to a property.

Houses with 1 parking space exhibit the largest interquartile range (IQR), suggesting a wider variability in prices within this category. 0, 2, and 3 parking spaces display outliers in the upper price range, with houses having 3 parking spaces showing outliers that are significantly beyond the maximum quartile of the boxplot, potentially representing luxury or high-value properties.

**Data Preprocessing**
"""

encoder = LabelEncoder()

encoding_col = ['furnishingstatus', 'prefarea', 'airconditioning',
                'hotwaterheating', 'basement', 'guestroom', 'mainroad']

for col in encoding_col:
    df[col] = encoder.fit_transform(df[col])

df.head()

plt.figure(figsize=(10, 10))
sns.heatmap(df.corr(), annot=True, fmt=".2f", linewidths=0.5, cbar=True)
plt.title("Correlation Heatmap")
plt.show()

"""The correlation heatmap indicates that features such as air conditioning, number of bathrooms, and area have the strongest correlations with house prices. While the correlations are not very strong, these features appear to be the most influential factors in determining property value within this dataset."""

# Dropping 'price' since we are using 'price_millions'
df = df.drop(columns=['price'], axis=1)

X = df.drop(columns=['price_millions'], axis=1)
y = df['price_millions']

scaler = MinMaxScaler()

X = scaler.fit_transform(X)

y = scaler.fit_transform(y.values.reshape(-1, 1))

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=50)

"""**Machine Learning Models**"""

ln_model = LinearRegression()
ln_model.fit(X_train, y_train)

y_pred = ln_model.predict(X_test)

ln_r2 = r2_score(y_test, y_pred)
ln_mae = mean_absolute_error(y_test, y_pred)
ln_mse = mean_squared_error(y_test, y_pred)
ln_rmse = np.sqrt(ln_mse)

print("Linear Regression Metrics:")
print("R² Score:", ln_r2)
print("Mean Absolute Error (MAE):", ln_mae)
print("Mean Squared Error (MSE):", ln_mse)
print("Root Mean Squared Error (RMSE):", ln_rmse)

"""**Decision Tree Regressor**"""

dt_model = DecisionTreeRegressor(random_state=50)
dt_model.fit(X_train, y_train)

y_pred = dt_model.predict(X_test)

dt_r2 = r2_score(y_test, y_pred)
dt_mae = mean_absolute_error(y_test, y_pred)
dt_mse = mean_squared_error(y_test, y_pred)
dt_rmse = np.sqrt(dt_mse)

print("Decision Tree Metrics:")
print("R² Score:", dt_r2)
print("Mean Absolute Error (MAE):", dt_mae)
print("Mean Squared Error (MSE):", dt_mse)
print("Root Mean Squared Error (RMSE):", dt_rmse)

"""**Random Forest Regressor**"""

from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import GridSearchCV

# Define the parameter grid for hyperparameter tuning
param_grid = {
    'n_estimators': [50, 100, 200],
    'max_depth': [None, 10, 20, 30],
    'min_samples_split': [2, 5, 10],
    'min_samples_leaf': [1, 2, 4],
    'max_features': ['sqrt', 'log2', None]
}

# Create the GridSearchCV object
grid_search = GridSearchCV(
    estimator=RandomForestRegressor(random_state=50),
    param_grid=param_grid,
    cv=5,
    scoring='r2',
    verbose=2,
    n_jobs=-1
)

# Fit the model to the training data
grid_search.fit(X_train, y_train.ravel())

# Get the best estimator and hyperparameters
best_rf_model = grid_search.best_estimator_
print("Best Hyperparameters for Random Forest:", grid_search.best_params_)

y_pred = best_rf_model.predict(X_test)

rf_r2 = r2_score(y_test, y_pred)
rf_mae = mean_absolute_error(y_test, y_pred)
rf_mse = mean_squared_error(y_test, y_pred)
rf_rmse = np.sqrt(rf_mse)

print("\nTuned Random Forest Metrics:")
print("R² Score:", rf_r2)
print("Mean Absolute Error (MAE):", rf_mae)
print("Mean Squared Error (MSE):", rf_mse)
print("Root Mean Squared Error (RMSE):", rf_rmse)

"""**Gradient Boosting Regressor**"""

# Hyper tuning the model
param_distributions = {
    'n_estimators': [100, 200, 300, 500],
    'learning_rate': [0.01, 0.05, 0.1, 0.2],
    'max_depth': [3, 5, 7, 10],
    'subsample': [0.6, 0.8, 1.0],
    'min_samples_split': [2, 5, 10, 20],
    'min_samples_leaf': [1, 2, 5, 10]
}

random_search = RandomizedSearchCV(
    estimator=GradientBoostingRegressor(random_state=50),
    param_distributions=param_distributions,
    n_iter=50,
    scoring='r2',
    cv=5,
    verbose=2,
    random_state=50,
    n_jobs=-1
)

random_search.fit(X_train, y_train.ravel())

best_gb_model = random_search.best_estimator_
print("Best Hyperparameters for Gradient Boosting:", random_search.best_params_)

y_pred = best_gb_model.predict(X_test)

gb_r2 = r2_score(y_test, y_pred)
gb_mae = mean_absolute_error(y_test, y_pred)
gb_mse = mean_squared_error(y_test, y_pred)
gb_rmse = np.sqrt(gb_mse)

print("Optimised Gradient Boosting Metrics:")
print("R² Score:", gb_r2)
print("Mean Absolute Error (MAE):", gb_mae)
print("Mean Squared Error (MSE):", gb_mse)
print("Root Mean Squared Error (RMSE):", gb_rmse)

"""**Support Vector Regression**"""

# Hyper tuning the model
param_distributions = {
    'kernel': ['linear', 'rbf', 'poly', 'sigmoid'],
    'C': [0.1, 1, 10, 100, 1000],
    'epsilon': [0.001, 0.01, 0.1, 0.5],
    'gamma': ['scale', 'auto', 0.001, 0.01, 0.1]
}

random_search = RandomizedSearchCV(
    estimator=SVR(),
    param_distributions=param_distributions,
    n_iter=50,
    scoring='r2',
    cv=5,
    verbose=2,
    random_state=50,
    n_jobs=-1
)

random_search.fit(X_train, y_train.ravel())

best_svr_model = random_search.best_estimator_
print("Best Hyperparameters for SVR:", random_search.best_params_)

y_pred = best_svr_model.predict(X_test)

svr_r2 = r2_score(y_test, y_pred)
svr_mae = mean_absolute_error(y_test, y_pred)
svr_mse = mean_squared_error(y_test, y_pred)
svr_rmse = np.sqrt(svr_mse)

print("Optimised Support Vector Regressor Metrics:")
print("R² Score:", svr_r2)
print("Mean Absolute Error (MAE):", svr_mae)
print("Mean Squared Error (MSE):", svr_mse)
print("Root Mean Squared Error (RMSE):", svr_rmse)

"""**Evaluation**

The evaluation of multiple machine learning models, including hyperparameter-tuned versions of Random Forest, Gradient Boosting, and Support Vector Regressor (SVR), provided valuable insights into their performance for predicting housing prices. Metrics such as R² Score, Mean Absolute Error (MAE), Mean Squared Error (MSE), and Root Mean Squared Error (RMSE) were used to assess each model, highlighting their strengths and limitations.

Linear Regression performed well as a baseline model, achieving an R² Score of 0.762 and an RMSE of 0.0778. Its low MAE of 0.0633 indicates its reliability in explaining a significant portion of the variance in the data. However, as a simpler model, it may struggle to fully capture non-linear relationships compared to more advanced methods.

The Decision Tree Regressor performed poorly, with an R² Score of only 0.141 and an RMSE of 0.148, demonstrating its inability to generalise effectively on the test data. Its high MAE of 0.102 highlights significant prediction errors, making it unsuitable for this task without further tuning or constraints to mitigate overfitting.

The hyperparameter-tuned Random Forest Regressor demonstrated strong performance, achieving the highest R² Score of 0.763 and the lowest RMSE of 0.0778. Its low MAE of 0.0599 indicates its ability to make accurate predictions, solidifying its position as the best-performing model. Random Forest effectively balances complexity and generalisation, making it highly suitable for this dataset.

The optimised Gradient Boosting Regressor also performed well, achieving an R² Score of 0.755 and an RMSE of 0.0790. Although slightly less accurate than Random Forest, its low MAE of 0.0603 highlights its robustness. Gradient Boosting’s iterative approach helps capture complex relationships, making it a competitive alternative.

The optimised Support Vector Regressor (SVR) achieved an R² Score of 0.747 and an RMSE of 0.0804, performing comparably to Gradient Boosting. Its MAE of 0.0634 indicates reasonable prediction accuracy but slightly lags behind Random Forest and Gradient Boosting in overall performance. SVR remains a viable option for datasets where relationships are highly non-linear.


In conclusion, the hyperparameter-tuned Random Forest Regressor stands out as the best-performing model, offering the highest accuracy and lowest error metrics. Linear Regression remains a reliable baseline, while Gradient Boosting and SVR demonstrate their potential as competitive alternatives. The Decision Tree Regressor, however, is not suitable for this dataset without significant improvements. These results underscore the importance of testing and optimising multiple models to identify the most robust solution.
"""