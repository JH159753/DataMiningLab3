import random
import math
import csv
import pandas as pd
import numpy as np
    



# DO NOT CHANGE THE FOLLOWING LINE
def lloyds(data, k, columns, centers=None, n=None, eps=None):
# DO NOT CHANGE THE PRECEDING LINE

    if (n is None and eps is None):
        print("Lloyd's Algorithm needs to be given a stopping point (must have n or eps)")
    
    else:
        #first do all the one time things
        #initialize cluster centers?
        if centers is None:
            #random cluster centers
            centers = []
            
            for i in range(k):
                center = []

                for j in range(len(columns)):
                    #random.random() should return a value between 0 and 1 
                    center.append(random.random())
                centers.append(center)
            print(centers)
            

        #Clusters is a list of lists, and each list in it has the data instances of that cluster
        clusters = []
        #for each center that exists, create one more list in clusters
        for i in range(k):
            clusters.append([])

        #not one time things here

        #for each row in the data, do this
        for i in range(len(data)):
            
            closestCluster = 0
            closestClusterDistance = 100
            #for each center, do this
            for j in range(len(centers)):
                #calculate distance between this point and the center
                
                #reset the closestDistance
                currentDistance = 0
                #For each column, do this
                currentColumn = 0
                for column in columns:

                    currentDistance = currentDistance + (data.loc[i][column] - centers[j][currentColumn])**2
                    currentColumn = currentColumn + 1
                    
                #after adding all these together, square root the value
                currentDistance = currentDistance ** (1/2)
                

                #if the currentDistance calculated here is less than the minimum, the data point is assigned to this one
                if currentDistance < closestClusterDistance:
                    closestCluster = j
                    closestClusterDistance = currentDistance
                    
                    

            #append the point to whichever cluster is closest
            print(closestCluster)
            clusters[closestCluster].append(data.loc[i])


        print(clusters[0])
        
        
            



    # This function has to return a list of k cluster centers (lists of floats of the same length as columns)
    pass
    
# DO NOT CHANGE THE FOLLOWING LINE
def kmedoids(data, k, distance, centers=None, n=None, eps=None):
# DO NOT CHANGE THE PRECEDING LINE
    # This function has to return a list of k cluster centroids (data instances!)
    pass

def main():
    #import the data from the csv
    data = pd.read_csv("testdata.csv")
    #print(data)
    columns = [1, 2, 3, 4]
    lloyds(data, 2, columns, None, 10, None)

if __name__ == '__main__':
    main()