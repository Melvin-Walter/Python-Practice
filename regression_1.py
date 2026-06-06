import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
X = np.linspace(0, 200, 200).reshape(-1, 1)
noise = (np.random.randn(200) * 6).reshape(-1, 1)
y = (2 * X + 3) + noise 

X_train = X[0:int(len(X)*0.75)]
X_test = X[int(len(X)*0.75):]
y_train = y[0:int(len(y)*0.75)]
y_test = y[int(len(y)*0.75):]

model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

residuals = y_test - y_pred

std_data = np.std(residuals)
mean_data = np.mean(residuals)
z_score_data = (residuals - mean_data)/std_data
print(np.max(z_score_data))

# plt.figure(figsize=(15,7))
# plt.plot(X_test.flatten(), y_pred.flatten(), color="blue")
# plt.plot(X_test.flatten(), y_test.flatten(), color="red")
# plt.show()