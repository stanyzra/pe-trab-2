# -*- coding: utf-8 -*-
"""
Created on Mon Sep 26 14:01:51 2022

@author: Collection-Acer01
"""
MEDIUMIDH = 550
HIGHTIDH = 700
VERYHIGHTIDH = 800

class verifier:
    def isLow(self,data):
        return data<MEDIUMIDH
    def isMedium(self,data):
        return data<HIGHTIDH
    def isHight(self,data):
        return data<VERYHIGHTIDH
    def isVeryHight(self,data):
        return data>=VERYHIGHTIDH

def getTotal(line):
    sum=0
    for value in line:
        sum=sum+value
    return sum  
def calcProbaility(transitionMatrix):
    probMatrix = [
        [0,0,0,0],
        [0,0,0,0],
        [0,0,0,0],
        [0,0,0,0],
    ]
    i=0
    for line in transitionMatrix:
        total = getTotal(line)
        j=0
        for value in line:
            probMatrix[i][j]=value/total
            j=j+1
        i=i+1
    print()
    print("[")
    for line in probMatrix:
        print(line)
    print("]")
        
        
def classifyData(matrix):
    year1900 = [0,0,0,0]
    year2000 = [0,0,0,0]
    verifierData = verifier()
    for line in matrix:
        for i in range(len(line)):
            if line[i].isnumeric():
                value = int(line[i])
                if(verifierData.isLow(value)):
                    if(i==1):
                         year1900[0] =  year1900[0] + 1
                    else:
                         year2000[0] =  year2000[0] + 1
                elif(verifierData.isMedium(value)):
                    if(i==1):
                         year1900[1] =  year1900[1] + 1
                    else:
                         year2000[1] =  year2000[1] + 1
                elif(verifierData.isHight(value)):
                    if(i==1):
                         year1900[2] =  year1900[2] + 1
                    else:
                         year2000[2] =  year2000[2] + 1
                elif(verifierData.isVeryHight(value)):
                    if(i==1):
                         year1900[3] =  year1900[3] + 1
                    else:
                         year2000[3] =  year2000[3] + 1
    print(year1900)
    print(year2000)
    return year1900,year2000

def processData(matrix):
    transitionMatrix = [
        [0,0,0,0],
        [0,0,0,0],
        [0,0,0,0],
        [0,0,0,0],
    ]
    verifierData = verifier()
    for line in matrix:
        idh1900 = int(line[1])
        idh2000 = int(line[2])  
        if(verifierData.isLow(idh1900)):
            if(verifierData.isLow(idh2000)):
                transitionMatrix[0][0]=transitionMatrix[0][0]+1
            elif(verifierData.isMedium(idh2000)):
                transitionMatrix[0][1]=transitionMatrix[0][1]+1
            elif(verifierData.isHight(idh2000)):
                transitionMatrix[0][2]=transitionMatrix[0][2]+1
            elif(verifierData.isVeryHight(idh2000)):
                transitionMatrix[0][3]=transitionMatrix[0][3]+1   
        elif(verifierData.isMedium(idh1900)):
            if(verifierData.isLow(idh2000)):
                    transitionMatrix[1][0]=transitionMatrix[1][0]+1
            elif(verifierData.isMedium(idh2000)):
                    transitionMatrix[1][1]=transitionMatrix[1][1]+1
            elif(verifierData.isHight(idh2000)):
                    transitionMatrix[1][2]=transitionMatrix[1][2]+1
            elif(verifierData.isVeryHight(idh2000)):
                    transitionMatrix[1][3]=transitionMatrix[1][3]+1         
        elif(verifierData.isHight(idh1900)):
            if(verifierData.isLow(idh2000)):
                    transitionMatrix[2][0]=transitionMatrix[2][0]+1
            elif(verifierData.isMedium(idh2000)):
                    transitionMatrix[2][1]=transitionMatrix[2][1]+1
            elif(verifierData.isHight(idh2000)):
                    transitionMatrix[2][2]=transitionMatrix[2][2]+1
            elif(verifierData.isVeryHight(idh2000)):
                    transitionMatrix[2][3]=transitionMatrix[2][3]+1           
        elif(verifierData.isVeryHight(idh1900)):
            if(verifierData.isLow(idh2000)):
                    transitionMatrix[3][0]=transitionMatrix[3][0]+1
            elif(verifierData.isMedium(idh2000)):
                    transitionMatrix[3][1]=transitionMatrix[3][1]+1
            elif(verifierData.isHight(idh2000)):
                    transitionMatrix[3][2]=transitionMatrix[3][2]+1
            elif(verifierData.isVeryHight(idh2000)):
                    transitionMatrix[3][3]=transitionMatrix[3][3]+1   
    print("[")
    for line in transitionMatrix:
        print(line)
    print("]")
    return transitionMatrix
def readDataBase():
    file = open("./hdi-database-from-1990-to-2000.csv")
    fileLines = file.readlines()
    databaseMatrix = []
    
    for line in fileLines:
        splittedLine = line.split(",")
        if (splittedLine[1] != '' and splittedLine[2] != ''):
            splittedLine[2] = splittedLine[2].replace('\n','')    
            databaseMatrix.append(splittedLine)
        
    file.close()
    return databaseMatrix
    

def main():
    dataMatrix = readDataBase()
    dataMatrix.pop(0)
    classifyData(dataMatrix)
    transitionMatrix = processData(dataMatrix)
    calcProbaility(transitionMatrix)
    

if __name__ == "__main__":
    main()
    