# -*- coding: utf-8 -*-
"""
Created on Mon Sep 26 14:01:51 2022

@author: Collection-Acer01
"""

def main():
    file = open("./hdi-database-from-1990-to-2000.csv")
    fileLines = file.readlines()
    databaseMatrix = []
    
    for line in fileLines:
        splittedLine = line.split(",")
        if (splittedLine[1] != '' and splittedLine[2] != ''):    
            databaseMatrix.append(splittedLine)
        
    file.close()

if __name__ == "__main__":
    main()
    