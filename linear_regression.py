from numpy import *

def mean_sq_error(b, m, data):
    squared_error = 0

    # calculate squared_error
    for i in range(len(data)):
        x = data[i, 0]
        y = data[i, 1]
        suqared_error += (y - (m * x + b))**2  #this will calculate squared error

    # for mean squared error, divide squared error by number of data points or len(data)
    return squared_error / float(len(data)) #float bc we want error to be precise

def gradient_descent(b_init, m_init, data, learning_rate):
    gradient_wrt_b = 0 #gradient wrt b_init
    gradient_wrt_m = 0 #gradient wrt m_init
    N = float(len(data))

    # compute gradients wrt b_init and m_init
    for i in range(len(data)):
        x = data[i, 0]
        y = data[i, 1]
        gradient_wrt_b += -(2/N) * (y - ((m_init * x) + b_init))
        gradient_wrt_m += -(2/N) * x * (y - ((m_init * x) + b_init))

    #update and return b_init and m_init to b_new and m_new respectively
    b_new = b_init - (learning_rate * gradient_wrt_b)
    m_new = m_init - (learning_rate * gradiet_wrt_m)
    return (b_new, m_new)

def run_gradient_descent(b_init, m_init, data, learning_rate, num_of_iterations):
    # b and m before running gradient descent
    b_final = b_init
    m_final = m_init

    # run gradient descent for the given number of iterations
    for i in range(num_of_iterations):
        (b_final, m_final) = gradient_descent(b_final, m_final, array(data), learning_rate)


    # return the final values of b and m
    return (b_final, m_final)

def main():
    # load data
    dataset = genfromtxt('dataset', delimeter = ',')

    # define hyperparameters
    learning_rate = 0.0001
    b_init = 0 # y-intercept
    m_init = 0 # slope of regression line
    num_of_iterations = 1000

    # start gradient descent
    print("Starting gradient descent at b = {0}, m = {1}, error = {2}".format(b_init, m_init, mean_sq_error(b_init, m_init, dataset)))
    print("Running...")
    (b_init, m_init) = run_gradient_descent(b_init, m_init, dataset, learning_rate, num_of_iterations)

    #print final results
    print("Gradient descent successful...")
    print("After {0} iterations, b = {1}, m = {2}, error = {3}".format(num_of_iterations, b_init, m_init, mean_sq_error(b_init, m_init, dataset))


if name == "__main()__":
    main()
