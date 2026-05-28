from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.preprocessing import PolynomialFeatures
from sklearn.ensemble import HistGradientBoostingRegressor, RandomForestRegressor
import joblib
housing = datasets.fetch_california_housing()

x = housing.data
y = housing.target
poly = PolynomialFeatures()
x = poly.fit_transform(x)

x_train, x_test, y_train, y_test = train_test_split(
    x, 
    y, 
    test_size=0.2,
    random_state = 432
    )


model = HistGradientBoostingRegressor(max_iter=350, learning_rate=0.05)

model.fit(x_train, y_train)
y_pred = model.predict(x_test)

r2 = r2_score(y_test, y_pred)
print(r2)

joblib.dump(model, "my_model.joblib")