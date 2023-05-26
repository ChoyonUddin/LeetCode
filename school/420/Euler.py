from re import I
from Walk import Walk
from Graph import Graph
import sys

sys.setrecursionlimit(100000)

class Euler(Graph):
    """
    COPYRIGHT SOPHIE QUIGLEY 2022
    THIS FILE IS NOT TO BE CIRCULATED, OR POSTED WITHOUT THE PERMISSION OF SOPHIE QUIGLEY
 
    Euler objects are Graph objects that contain Euler Circuits:
    They are guaranteed to be connected and all their vertices have even degree
    
    DO NOT MODIFY THIS CLASS EXCEPT TO ADD CODE FOR FINDING EULER USING CIRCUITS HIERHOLZER'S ALGORITHM
    """
	  
    @classmethod
    def fromFile(cls, filename):
        """
	      Instantiates list of Eulers read from a file.  
        The file format is described in Graph.fromFile
	
	      Note: Graph.fromFile() first reads the file and turns the information
        into an array of Graphs, which is converted here into an array of Eulers. 
	 
	      Parameters:
            str filename: name of file containing Euler objects
	
	      Returns a list of the Eulers described in the file that contain Euler circuits. 
	      """
        graphList = Graph.fromFile(filename)
        eulerList = []
        for graph in graphList:
          euler = Euler(graph)
          if euler != None:
            eulerList.append(euler)
        return eulerList
    
    def __init__(self, graph):
        """
        Creates a new Euler object from an existing graph
	
        Parameters:
          Graph graph: valid graph
        
        Returns:
          A new Euler object which is a copy of the original graph
          or none if the original graph does not contain an Euler circuit
	      """
        if graph.totalV < 1 or not graph.isConnected() :
          return None         

        super(Euler,self).__init__(graph.directed, graph.totalV, graph.edges)
        self.degreeV = [None]*graph.totalV
        self.__countDegreesV()
        if not self.__evenDegrees():
          return None


    def __countDegreesV(self):
        """
        Add an array keeping degree of each vertex
        """
        for v1 in range(self.totalV):
          self.degreeV[v1] = 0
          for v2 in range(self.totalV):
            self.degreeV[v1] += self.edges[v1][v2]
          # Loops need to be counted twice
          self.degreeV[v1] += self.edges[v1][v1]

    def __evenDegrees(self):
        """
        Returns True iff every vertex has an even degree
        """
        for v1 in range(self.totalV):
          if self.degreeV[v1] % 2 == 1:
            return False
        return True
    
    
    ########################  WRITE SOLUTION UNDERNEATH #############################
    #
    # findEulerH is a public method and its calling sequence should not be changed
    # __newCircuit is private and can be modified or replaced
    #
    #################################################################################
    
    def findEulerH(self):
        """
        Returns an Euler circuit for the Euler object using the Hierholzer's algorithm
        """
        eulerWalk = Walk(self.totalEdges()+1)

        for i in range(self.totalV):
          while self.degreeV[i]>0:
            Walkpath = Walk(1)
            Walkpath.addVertex(i)
            eulerWalk.insertCircuit(self.__newCircuit(0,i,Walkpath))

        return eulerWalk

    def __newCircuit(self, startV, currentV, circuit):
        """
        __newCircuit recursively creates a new circuit starting at vertex startV.

        Parameters:
             int startV: first vertex in circuit
             int currentV: vertex being currently added
             Walk circuit: circuit being grown

        Returns number of edges added into the circuit (and traversed)
        
        Side Effects: 
          - edges added to circuit are removed from unvisitedE
          - the degreeV of each affected vertex is decremented      
        """
        if circuit.totalV > 2 and startV == currentV:
            return circuit

        for i in range(self.totalV):
          if(self.unvisitedE[currentV][i] > 0):
            nextVertex = i
            startV = 0
      
            self.unvisitedE[currentV][nextVertex] -= 1
            self.unvisitedE[nextVertex][currentV] -= 1
            self.degreeV[currentV] -= 1
            self.degreeV[nextVertex] -= 1

            circuit.maxV += 1 
            circuit.vertices.append(0)
            circuit.addVertex(nextVertex)
            return self.__newCircuit(startV,nextVertex,circuit)
        return circuit
