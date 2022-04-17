import random
import math
import csv
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
    



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
        iterations = 0
        if (n is None):
            n = math.inf

        while (iterations < n):
            
            iterations = iterations + 1
            print("Iteration "  + str(iterations))
            #declare old center 
            oldCenters = []
            for i in range(len(centers)):
                oldCenters.append([])
                for j in range(len(centers[i])):
                    oldCenters[i].append([j])

            #copy data into oldCenters by value
            for i in range(len(centers)):
                for j in range(len(centers[i])):
                    oldCenters[i][j] = centers[i][j]

            print (oldCenters)

            #for each row in the data, do this
            for i in range(len(data)):
                
                closestCluster = 0
                closestClusterDistance = math.inf
                #for each center, do this
                for j in range(len(centers)):
                    #calculate distance between this point and the center
                    
                    #reset the closestDistance
                    currentDistance = 0
                    #For each column, do this
                    currentColumn = 0
                    for column in columns:

                        currentDistance = currentDistance + (data[i][column] - centers[j][currentColumn])**2
                        currentColumn = currentColumn + 1
                        
                    #after adding all these together, square root the value
                    currentDistance = currentDistance ** (1/2)
                    

                    #if the currentDistance calculated here is less than the minimum, the data point is assigned to this one
                    if currentDistance < closestClusterDistance:
                        closestCluster = j
                        closestClusterDistance = currentDistance
                        
                        

                #append the point to whichever cluster is closest
                clusters[closestCluster].append(data[i])

            #Now that we have our rows placed in clusters, calculate new cluster center
            #reset center's values
            for i in range(len(centers)):
                for j in range(len(centers[i])):
                    centers[i][j] = 0



            #for each cluster, do this
            for i in range(len(clusters)):
                #for each row in a cluster, do this
                for j in range(len(clusters[i])):
                    #for each column we care about in the row, do this
                    currentColumn = 0
                    for column in columns:
                        centers[i][currentColumn] = centers[i][currentColumn] + clusters[i][j][column]
                        currentColumn = currentColumn + 1
                    
                
            #after adding everything up, divide by the length of the clusters to get the average
                    
            for i in range(len(centers)):
                for j in range(len(centers[i])):
                    if (len(clusters[i]) != 0):
                        centers[i][j] = centers[i][j] / len(clusters[i])

            #print (centers)

            #compare old center to this if eps is not none
            if (eps is not None):
                
                distanceMoved = 0
                averageDistanceMoved = 0
                for i in range(len(centers)):
                    for j in range(len(centers[i])):
                        distanceMoved = distanceMoved + (centers[i][j] - oldCenters[i][j])**2 
                    distanceMoved = distanceMoved**(1/2)
                    #print(distanceMoved)

                    averageDistanceMoved = averageDistanceMoved + distanceMoved
                        
                averageDistanceMoved = averageDistanceMoved / len(centers)
                #print (averageDistanceMoved)
                if (averageDistanceMoved < eps):
                    break

    # This function has to return a list of k cluster centers (lists of floats of the same length as columns)
    return centers
    pass
    
# DO NOT CHANGE THE FOLLOWING LINE
def kmedoids(data, k, distance, centers=None, n=None, eps=None):
# DO NOT CHANGE THE PRECEDING LINE
    # This function has to return a list of k cluster centroids (data instances!)
    pass

#stolen from testcases.py
def plot(data, centers, x, y, scale=None):
    def dist(point,center):
        return math.sqrt((point[x] - center[0])**2 + (point[y] - center[1])**2)
    xs, ys, colors = [], [], []
    for d in data:
        mind = None 
        cluster = None 
        for i,c in enumerate(centers):
            delta = dist(d, c)
            if mind is None or delta < mind:
                mind = delta
                cluster = i
        xs.append(d[x])
        ys.append(d[y])
        colors.append(cluster)
        
    cxs, cys, ccolors = [], [], []
    for i,c in enumerate(centers):
        cxs.append(c[0])
        cys.append(c[1])
        ccolors.append(i)
    if scale is None:
        fr = min(min(xs), min(ys), min(cxs), min(cys))
        to = max(max(xs), max(ys), max(cys), max(cys))
        range = (to-fr)
        fr -= 0.01*range
        to += 0.01*range
    else:
        fr,to = scale
    plt.scatter(xs, ys, c=colors)
    plt.scatter(cxs, cys, c=ccolors, marker = "+")
    plt.xlim((fr,to))
    plt.ylim((fr,to))
    plt.show()

def show_centers(centers):
    for i,c in enumerate(centers):
        print(f"   cluster center {i+1}: {tuple(c)}")

def main():
    #import the data from the csv
    csvdata = pd.read_csv("spotify.csv")

    #declare data as a list
    data = []

    #for each row in csvdata, make a row in data
    for i in range(len(csvdata)):
        data.append([])
        data[i] = csvdata.loc[i]

    

    columns = [2, 4]
    centers = lloyds(data, 3, columns, None, 100, .001)
    plot(data, centers, 1, 2, scale=(0,1))
    show_centers(centers)

if __name__ == '__main__':
    main()