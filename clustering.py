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
            for i in range(k):
                center = []
                #need to turn Centers into a list to append things to it
                centers = []
                for j in range(len(columns)):
                    #random.random() should return a value between 0 and 1 
                    center.append(random.random())
                centers.append(center)
                print(centers)
            

        #Clusters is a list of lists, and each list in it has the data instances of that cluster
        clusters = []
        cluster = []
        #for each center that exists, create one more list in clusters
        for i in range(len(centers)):
            clusters.append(cluster)

        #not one time things here

        #for each item in the data, do this
        for i in range(len(data)):
            #set closestCluster to 0 and its distance to 1; maximum distance between two things here should be 1
            closestCluster = 0
            closestClusterDistance = 1
            #for each center, do this
            for j in range(len(center)):
                #calculate distance between this point and the center
                
                #reset the closestDistance
                currentDistance = 0
                #For each column, do this
                for k in range(len(columns)):
                    #add the value from the data at each column, squared
                    currentDistance = currentDistance + (data[i][columns][k])^2

                #after adding all these together, square root the value
                currentDistance = currentDistance ^ (1/2)

                #if the currentDistance calculated here is less than the minimum, the data point is assigned to this one
                if currentDistance < closestClusterDistance:
                    closestCluster = j

            #append the point to whichever cluster is closest
            clusters[closestCluster].append(data[i])

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