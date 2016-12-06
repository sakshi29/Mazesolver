import numpy as np
import cv2

## The readImage function takes a file path as argument and returns image in binary form.
def readImage(filePath):
   
    img=cv2.imread(filePath)
    gray=cv2.cvtColor(img , cv2.COLOR_BGR2GRAY)
    ret,binaryImage = cv2.threshold(gray,127,255,cv2.THRESH_BINARY)

    ###################################################
    return binaryImage

## The findNeighbours function takes a maze image and row and column coordinates of a cell as input arguments
## and returns a stack consisting of all the neighbours of the cell as output.
## Note :- Neighbour refers to all the adjacent cells one can traverse to from that cell provided only horizontal
## and vertical traversal is allowed.

def findNeighbours(img,row,column):
    neighbours = []
   
    ncol=(row*20)+9
    nrow=(column*20)+9
    
    if(img[ncol,nrow-9]==150):
        neighbours.append((row,column-1))

    if(img[ncol,nrow+10]==150):
        neighbours.append((row,column+1))
        
    if(img[ncol-9,nrow]==150):
        neighbours.append((row-1,column)) 
        
    if(img[ncol+10,nrow]==150):
        neighbours.append((row+1,column))  

    ###################################################
    return neighbours

##  colourCell function takes 4 arguments:-
##            img - input image
##            row - row coordinates of cell to be coloured
##            column - column coordinates of cell to be coloured
##            colourVal - the intensity of the colour.
##  colourCell basically highlights the given cell by painting it with the given colourVal. Care should be taken that
##  the function doesn't paint over the black walls and only paints the empty spaces. This function returns the image
##  with the painted cell.

def colourCell(img,row,column,colourVal):
    
    ncol=(row*20)
    nrow=(column*20)
    for i in range(nrow,nrow+20):
        for j in range(ncol,ncol+20):
            if(img[j,i]>127):
                img[j,i]=colourVal

    ###################################################
    return img

##  Function that accepts some arguments from user and returns the graph of the maze image.
def buildGraph(length,neighbours):  ## You can pass your own arguments in this space.
    graph = {}
   
    k=0
    #len_of_adj=len(neighbours)
    #print len_of_adj
    for i in range(0,length):
        for j in range(0,length):
            graphs={(i,j):neighbours[k]}
            #print graphs
            graph.update(graphs)
            k=k+1
    ###################################################
    
    return graph

##  Finds shortest path between two coordinates in the maze. Returns a set of coordinates from initial point
##  to final point.
def findPath(graph,start,end,length):=
    
   
    shortest=[]
    prev={}
    visited={}
    s=start
    for i in range(0,length):
        for j in range(0,length):
            v={(i,j):False}
            p={(i,j): -1}
            visited.update(v)
            prev.update(p)
            
    queue=[]
    queue.append(s)
    visited[s]=True
    
    while queue:
        s=queue.pop(0)
       
        #shortest.append(start)
        
        if(end == s):
            currentv=end
            while(prev[currentv]!= -1):
                shortest.append(currentv)
                currentv=prev[currentv]
            shortest.append(start)
            shortest=list(reversed(shortest))
            return shortest
        
        for i in graph[s]:
            if visited[i]== False:
                queue.append(i)
                visited[s]= True
                prev[i]=s
                
                      
    ###################################################
    

## This is the main function where all other functions are called. It accepts filepath
## of an image as input. You are not allowed to change any code in this function.
def main(filePath, flag = 0):                 
    img = readImage(filePath)      ## Read image with specified filepath.
    breadth = len(img)/20          ## Breadthwise number of cells
    length = len(img[0])/20           ## Lengthwise number of cells
    if length == 10:
        initial_point = (0,0)      ## Start coordinates for maze solution
        final_point = (9,9)        ## End coordinates for maze solution    
    else:
        initial_point = (0,0)
        final_point = (19,19)
        
    img2=img.copy() 

    neighbours=[]    
    for i in range(initial_point[0],final_point[0]+1):
        for j in range(initial_point[1],final_point[1]+1):
             img2 = colourCell(img2,i,j, 150)
             neighbours.append(findNeighbours(img2,i,j))
             
             
    print neighbours        
    graph = buildGraph( length,neighbours ) ## Build graph from maze image. Pass arguments as required.
    print graph
    shortestPath = findPath(graph,initial_point,final_point,length)  ## Find shortest path. Pass arguments as required.
    print shortestPath            
    string = str(shortestPath) + "\n"
    for i in shortestPath:         ## Loop to paint the solution path.
        img = colourCell(img, i[0], i[1], 200)
    if __name__ == '__main__':     
        return img
    else:
        if flag == 0:
            return string
        else:
            return graph

          
if __name__ == '__main__':
    filePath = 'maze00.jpg'        ## File path for test image
    img = main(filePath)           ## Main function call
    cv2.imshow('canvas', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()




