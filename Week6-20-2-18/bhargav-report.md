### Week6 20-02-18
Converted the required data into Mathematical form.

Trained classifiers on Number of assignees, Number of comments and the Author Association to predict the closing time

The Classifiers trained are :

  1. KNN(For n_neighbors = 1 to n_neighbors = 31, 10 FOLD CROSS VALIDATION)
  2. Decision trees(With max_depths 1 to 5)
  3. Random Forest Classifier
  4. Logistic Regression
  5. Support Vector Machine Classifier
 
 Made an Ensemble of the last 4 using the Soft Voting Classifier. To get an Accuracy of about 56% on 5-Class Classification.
  
  
