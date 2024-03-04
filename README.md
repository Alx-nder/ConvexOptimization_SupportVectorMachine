1. Use Matlab’s quadprog() function or Python’s CVXOPT package to implement the linearly nonseparable (soft margin) SVM in its dual form and test its functionality with the data set generated as shown below. For 𝐶𝐶 = 0.1 and 𝐶𝐶 = 100, plot the samples, margin hyperplanes, and the decision boundary. Also, on the plot, identify and give the count of the support vectors and the misclassified samples.  

2. Compare the computational efficiency of your implementation of SVM with one in Matlab or Python that employs the SMO approach. Present this comparison as a plot of the number of training samples versus execution time.   

rng(100); 
class1=mvnrnd([1 3],[1 0; 0 1],60); 
class2=mvnrnd([4 1],[2 0; 0 2],40);  

For those programming in Python, the dataset is provided in the attached Excel file. 
  
