#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: sofiagonzalez
"""

import numpy as np

Sx = np.array( [[0,1],[1,0]] )
Sy = np.array( [[0,-1j],[1j,0]] )
Sz = np.array( [[1,0],[0,-1]] )
Id = np.array( [[1,0],[0,1]] )

def kron_list(op_list):
    term = op_list[0]
    for op in op_list[1:]:
        term = np.kron(term, op)
    return term

def ZZ(N):
    """
    Input: N is the number of sites in a 1D Ising model
    Output: Matrix for sum of Sz Sz terms, including an overall minus sign
    
    Computed using Kronecker product method
    """
    ZZ = np.zeros( (2**N,2**N), dtype = int )
    for i in range(N-1):
        operators = [Id]*i + [Sz,Sz] + [Id]*(N-2-i)
        term = kron_list(operators)
        ZZ += term
    return ZZ

def X(N):
    """
    Input: N is the number of sites in a 1D Ising model
    Output: Matrix for sum of Sx terms, including an overall minus sign
    
    Computed using Kronecker product method
    """
    X = np.zeros( (2**N,2**N), dtype = int )
    for i in range(N):
        operators = [Id]*i + [Sx] + [Id]*(N-1-i)
        term = kron_list(operators)
        X += term
    return X

def Z(N):
    """
    Input: N is the number of sites in a 1D Ising model
    Output: Matrix for sum of Sx terms, including an overall minus sign
    
    Computed using Kronecker product method
    """
    Z = np.zeros( (2**N,2**N), dtype = int )
    for i in range(N):
        operators = [Id]*i + [Sz] + [Id]*(N-1-i)
        term = kron_list(operators)
        Z += term
    return Z