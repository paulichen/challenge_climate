# -*- coding: utf-8 -*-
"""
Created on Sun Sep 16 10:14:54 2018

@author: paulichen
"""
 
INT_MAX = 10000
INT_MIN = 0
  
class Node: 
  
    def __init__(self, data): 
        self.data = data  
        self.left = None
        self.right = None
        
def check_binary_search_tree_(node): 
    return (is_BST_aux(node, INT_MIN, INT_MAX)) 
  
def is_BST_aux(node, valor_minimo, valor_maximo): 
    
    if node is None: 
        return True
  
    if node.data < valor_minimo or node.data > valor_maximo: 
        return False
  
    return (is_BST_aux(node.left, valor_minimo, node.data -1) and
          is_BST_aux(node.right, node.data+1, valor_maximo)) 
  