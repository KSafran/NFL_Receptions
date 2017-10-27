# For fun, let's create our own exponential smoother
# We will estimate alpha using poisson nll
# poisson nll = sum(x_i log(lambda_i) - lambda_i) for all i
# lambda is our estimated poisson parameter, x_i is the true 
# number of receptions

import numpy as np
from scipy.optimize import minimize

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

def exponential_smooth_pois_error(actual_values, alpha):
	''' given a series and alpha this returns the 
	poisson error of the exponentially weighted 
	averages

	actual_values -- a series to expentially smooth
	alpha -- smoothing parameter
	'''
	predictions = exponential_series(actual_values, alpha)
	error = poisson_nll(predictions, actual_values)
	return(error)

# We need a function of just alpha for optimization
def function_from_series(actual_values):
	'''returns a poisson error function given a series
	'''
	def output_fun(alpha):
		return(exponential_smooth_pois_error(actual_values, alpha))
	return(output_fun)

# Wrapping this all into one neat little function
def simple_pois_exp_smooth(series):
	optimize_me_capn = function_from_series(series)
	return(minimize(optimize_me_capn, 0.5))