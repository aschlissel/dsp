# Matrix Algebra

import numpy as np                               
                                                 
A = np.array([1, 2, 3, 2, 7, 4]).reshape(2, 3)   
B = np.array([1, -1, 0, 1]).reshape(2, 2)        
C = np.array([5, -1, 9, 1, 6, 0]).reshape(3, 2)  
D = np.array([3, -2, -1, 1, 2, 3]).reshape(2, 3) 
u = np.array([6, 2, -3, 5])                      
v = np.array([3, 5, -1, 4])                      
w = np.array([1, 8, 0, 5]).reshape(4, 1)         
a = 6                                            
                                                 
#Part 1: Matrix Dimensions                       
                                                 
#1.1                                             
print A.shape                                    
#2x3                                             
                                                 
#1.2                                             
print B.shape                                    
#2x2                                             
                                                 
#1.3                                             
print C.shape                                    
#3x2                                             
                                                 
#1.4                                             
print D.shape                                    
#2x3                                             
                                                 
#1.5                                             
print u.shape                                    
#1x4                                             
                                                 
#1.6                                             
print w.shape                                    
#4x1                                             
                                                 
                                                 
#Part 2: Vector Operations                       
                                                 
#2.1                                             
print u + v                                      
#[ 9  7 -4  9]                                   
                                                 
#2.2                                             
print u - v                                      
#[ 3 -3 -2  1]                                   
                                                 
#2.3                                             
print a*u                                        
#[ 36  12 -18  30]                               
                                                 
#2.4                                             
print np.dot(u, v)                               
#51                                              
                                                 
#2.5                                             
print np.linalg.norm(u)                          
#8.60232526704        
                                                 
                                                 
#Part 3: Matrix Operations                       
                                                 
#3.1                                             
print A + C                                     
#not defined                                     
                                                 
#3.2                                             
print A - C.transpose()                          
#[[-4 -7 -3]                                     
# [3  6  4]]                                     
                                                 
#3.3                                             
print C.transpose() + 3*D                        
#[[14  3  3]                                     
# [2  7  9]]                                     
                                                 
#3.4                                             
print np.dot(B, A)                               
#[[-1 -5 -1]                                     
# [2  7  4]]                                     
                                                 
#3.5                                             
print np.dot(B, A.transpose())                   
#not defined                                     
                                                 
                                                 
#Optional                                        
                                                 
#3.6                                             
print np.dot(B, C)                               
#not defined                                     
                                                 
#3.7                                             
print np.dot(C, B)                               
#[[ 5 -6]                                        
# [ 9 -8]                                        
# [ 6 -6]]                                       
                                                 
#3.8                                             
print B**4                                       
#[[1 1]                                          
# [0 1]]                                         
                                                 
#3.9                                             
print np.dot(A, A.transpose())                   
#[[14 28]                                        
# [28 69]]                                       
                                                 
#3.10                                            
print np.dot(D.transpose(), D)                   
#[[10 -4  0]                                     
# [-4  8  8]                                     
# [ 0  8 10]]                                    
                                                 
                                                 
