import numpy
from numpy import random

def matrix_factorization(R, P, Q, K, steps=10000, alpha=0.0001):
    Q = Q.T
    for step in xrange(steps):
        for i in xrange(len(R)):
            for j in xrange(len(R[i])):
                if R[i][j] > 0:
                    eij = R[i][j] - numpy.dot(P[i,:],Q[:,j])
                    for k in xrange(K):
                        P[i][k] = P[i][k] + alpha * (2 * eij * Q[k][j])
                        Q[k][j] = Q[k][j] + alpha * (2 * eij * P[i][k])
        eR = numpy.dot(P,Q)
        e = 0
        for i in xrange(len(R)):
            for j in xrange(len(R[i])):
                if R[i][j] > 0:
                    e = e + pow(R[i][j] - numpy.dot(P[i,:],Q[:,j]), 2)
        if e < 0.001:
            break
    print "This is Matrix P:"
    print P
    print "This is Matrix Q:"
    print Q
    print "This is Matrix P*Q:"
    print numpy.dot(P,Q)
    return P, Q.T

def main():
    R = numpy.array([[9.0,2.0,1.0,1.0],[8.0,3.0,2.0,1.0],[3.0,1.0,2.0,8.0],[1.0,2.0,4.0,7.0]])
    P = numpy.array(random.random(size=(4,2)))
    Q = numpy.array(random.random(size=(4,2)))
    K = 2
    P,Q = matrix_factorization(R,P,Q,K)

if __name__ == '__main__':
    main()