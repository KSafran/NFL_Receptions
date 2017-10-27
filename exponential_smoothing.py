# For fun, let's create our own exponential smoother
# We will estimate alpha using poisson nll
# poisson nll = sum(x_i log(lambda_i) - lambda_i) for all i
# lambda is our estimated poisson parameter, x_i is the true 
# number of receptions

import numpy as np

def poisson_nll(predictions, target):
	'''returns the poisson negative log likelihood 

	predictions -- a numpy array of predicted lambdas
	target -- a numpy array of actual values
	'''
	return(np.sum(predictions - target * np.log(predictions)))

# note, with the log we will have to make sure we never 
# predict 0. When we see 0 receptions we will have to 
# use 1/(ngames) as a substitute 

def exponential_series(actual_values, alpha):
	'''given a series and value of alpha, fill in 
	exponentially weighted average prediction
	'''
	output = []
	for i in range(len(actual_values)):
		if i == 0:
			current = actual_values[i]
		else:
			current = actual_values[i] * alpha + current * (1 - alpha)
		if current == 0:
			current = 1/(i + 1) # We can't have a zero here
		output.append(current)
	return(output)

def exponential_smooth_pois(series):
	''' given a series, this returns the optimal
	alpha for an exponential poisson smoother

	series -- a series to expentially smooth
	'''
		