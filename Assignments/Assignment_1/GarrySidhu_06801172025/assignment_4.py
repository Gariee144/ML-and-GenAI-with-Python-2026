# ans:1
# Gender	SubscriptionType	WatchHoursPerWeek	DevicesUsed	FavoriteGenre	AdClicks	MonthlySpend	SubscriptionRenewed
# 1001	22	Female	Basic	8	4	Action	13	353	No
# 1002	55	Male	Premium	8	2	Action	14	317	Yes
# 1003	49	Male	Premium	7	3	Drama	16	309	No
# 1004	39	Female	VIP	    18	4	Sci-Fi	45	833	Yes
# 1005	38	Female	VIP	    17	1	Drama	24	804	Yes

# ans:2
# Rows: 750
# Columns: 10
 
# ans:3
# UserID
# Age
# Gender
# SubscriptionType
# WatchHoursPerWeek
# DevicesUsed
# FavoriteGenre
# AdClicks
# MonthlySpend
# SubscriptionRenewed

# ans:4
# Numerical Features
# UserID
# Age
# WatchHoursPerWeek
# DevicesUsed
# AdClicks
# MonthlySpend
# Categorical Features
# Gender
# SubscriptionType
# FavoriteGenre
# SubscriptionRenewed

# ans:5
# Column	Missing Values
# All Columns	0
# Result: No missing values found in the dataset.

# ans:6
# Average Age = 41.82 years

# ans:7
# Average Watch Hours = 14.24 hours/week

# ans:8
# Average Monthly Spending = ₹689.91

# ans:9
# Subscription Type	Count
# Basic	342
# Premium	279
# VIP	129

#  ans:10
# Renewed = 347 users
# Total Users = 750
# Renewal Percentage = 46.27%

# ans:11
import pandas as pd
df=pd.read_csv("Dataset 2.csv")
from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
df["Gender"] = le.fit_transform(df["Gender"])
df["SubscriptionType"] = le.fit_transform(df["SubscriptionType"])
df["FavoriteGenre"] = le.fit_transform(df["FavoriteGenre"])
df["SubscriptionRenewed"] = le.fit_transform(df["SubscriptionRenewed"])

# ans:12
X = df.drop("SubscriptionRenewed", axis=1)
y = df["SubscriptionRenewed"]

# ans:13
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.20,
    random_state=42
)

# ans:14
from sklearn.tree import DecisionTreeClassifier
dt = DecisionTreeClassifier(random_state=42)
dt.fit(X_train, y_train)

# ans:15

# Decision Tree Accuracy = 56.67%
from sklearn.metrics import accuracy_score
accuracy = accuracy_score(y_test, y_pred)

# ans:16
# Confusion Matrix:
# Actual / Predicted	No	Yes
# No	50	32
# Yes	33	35

# Matrix Form:

# [[50 32]
#  [33 35]]
# Interpretation
# 50 users correctly predicted as not renewing.
# 35 users correctly predicted as renewing.
# 32 users wrongly predicted as renewing.
# 33 users wrongly predicted as not renewing.

# The model makes correct predictions for 85 out of 150 test users.

# ans:17
from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train, y_train)

# ans:18
# Model	Accuracy
# Decision Tree	56.67%
# KNN (K=5)	60.00%
# Conclusion

# KNN performed slightly better than Decision Tree on this dataset.

# ans:19
from sklearn.linear_model import LinearRegression
lr = LinearRegression()
lr.fit(X_train_reg, y_train_reg)
# Target variable:
y = df["MonthlySpend"]

# ans:20
# Using the first user's data as a sample:
# Predicted Monthly Spending = ₹391.39

prediction = lr.predict(new_user)
# Interpretation
# The model estimates that a user with similar characteristics would spend approximately ₹391 per month on Netflix.
# Business Reflection Questions
# 1. Which factors appear to influence subscription renewal the most?
# According to the Decision Tree feature importance:

# MonthlySpend
# Age
# WatchHoursPerWeek
# AdClicks
# User activity-related features

# Users who spend more and watch more content are generally more likely to renew.

# 2. Why is subscription renewal a classification problem?

# Because the output has two categories:

# Yes (Renewed)
# No (Not Renewed)

# The model predicts a class label, not a numerical value.

# 3. Why is monthly spending a regression problem?

# Monthly spending is a continuous numerical value (₹200, ₹500, ₹1000, etc.).

# Regression algorithms are used when predicting numeric quantities.

# 4. Which algorithm performed better for renewal prediction?
# Algorithm	Accuracy
# Decision Tree	56.67%
# KNN	60.00%

# KNN performed better because it achieved higher accuracy.

# 5. How could Netflix use these predictions to improve customer retention?

# Netflix could:

# Identify users likely to cancel subscriptions.
# Offer personalized discounts and promotions.
# Recommend content based on viewing history.
# Send renewal reminders.
# Improve engagement through targeted marketing campaigns.
# Create loyalty rewards for long-term subscribers.

# These actions can increase customer satisfaction and improve subscription renewal rates.

# Complete Python Program
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LinearRegression
from sklearn.metrics import accuracy_score, confusion_matrix

df = pd.read_excel("Dataset 2.xlsx")

print(df.head())
print(df.shape)
print(df.columns)

for col in df.select_dtypes(include='object').columns:
    le = LabelEncoder()
    df[col] = le.fit_transform(df[col])

X = df.drop("SubscriptionRenewed", axis=1)
y = df["SubscriptionRenewed"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

dt = DecisionTreeClassifier(random_state=42)
dt.fit(X_train, y_train)

y_pred = dt.predict(X_test)

print("Decision Tree Accuracy:",
      accuracy_score(y_test, y_pred))

print(confusion_matrix(y_test, y_pred))

knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train, y_train)

knn_pred = knn.predict(X_test)

print("KNN Accuracy:",
      accuracy_score(y_test, knn_pred))

X_reg = df.drop("MonthlySpend", axis=1)
y_reg = df["MonthlySpend"]

X_train_r, X_test_r, y_train_r, y_test_r = train_test_split(
    X_reg, y_reg, test_size=0.2, random_state=42
)

lr = LinearRegression()
lr.fit(X_train_r, y_train_r)

print("Predicted Spending:",
      lr.predict(X_reg.iloc[[0]]))