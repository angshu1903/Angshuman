import numpy as np 
from sklearn.linear_model import LinearRegression
X = np.array([[2],[3], [4],[5],[6] ,[7],[10],[11] ,[20],[30]])  # Input data
y = np.array([2,4,4,5,5,6,8,8,9,9])  # Target data
model = LinearRegression()
model.fit(X, y)
new_data = np.array([[22],[25],[35],[40]])
predictions = model.predict(new_data)
print("Predicted values from the given data:", predictions)
#PREDICTING OTHER POINTS FROM A SERIES OF DATA OF A GIVEN MASS POINTS AND THE NUMBER OF FOLDS
#THE TOTAL MASS HAS BEEN KEPT CONSTANT