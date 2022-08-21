
#k-Nearest Neighbors: Fit
# Import KNeighborsClassifier from sklearn.neighbors
from sklearn.neighbors import KNeighborsClassifier

# Create arrays for the features and the response variable
y = df['party'].values
X = df.drop('party', axis=1).values

# Create a k-NN classifier with 6 neighbors
knn = KNeighborsClassifier(n_neighbors=6)

# Fit the classifier to the data
knn.fit(X,y)

# K Nearest Neighbors: Predict 

#create a k-NN classifier with 6 neighbors
knn = KNeighborsClassifier(n_neighbors=6)

#Fit the classifier to the data 
knn.fit(X,y)

#Predict and print the label for the new data point X_new 
new_prediction = knn.predict(X_new)

