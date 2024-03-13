


import gmsh
    

L=0.00025

J=1.31*(10**1) # A/m2
sigma=4.1*(10**7)

u=((J**2)/sigma)
# We start by giving some nice shortcuts for some namespaces

# If sys.argv is passed to gmsh.initialize(), Gmsh will parse the command line
# in the same way as the standalone Gmsh app:
gmsh.initialize()

gmsh.option.setNumber("General.Terminal", 1)

gmsh.model.add("microgripper")

#define points 
gmsh.model.geo.addPoint(0, 0.000002, 0, 0.00001, 1) 
gmsh.model.geo.addPoint(0, 0.000022, 0, 0.00001, 2) 
gmsh.model.geo.addPoint(0.000020, 0.000022, 0, 0.00001, 3)
gmsh.model.geo.addPoint((0.000020+L)-0.000007, 0.000022, 0, 0.00001, 4) 
gmsh.model.geo.addPoint((0.000020+L)-0.000007, 0.000029, 0, 0.00001, 5) 
gmsh.model.geo.addPoint(0.000020, 0.000029, 0, 0.00001, 6) 
gmsh.model.geo.addPoint(0, 0.000029, 0, 0.00001, 7) 
gmsh.model.geo.addPoint(0, 0.000049, 0, 0.00001, 8) 
gmsh.model.geo.addPoint(0.000020, 0.000049, 0, 0.00001, 9) 
gmsh.model.geo.addPoint(0.000020, 0.000036, 0, 0.00001, 10) 
gmsh.model.geo.addPoint((0.000020+L), 0.000036, 0, 0.00001, 11) 
gmsh.model.geo.addPoint((0.000020+L), 0.000029, 0, 0.00001, 12) 
gmsh.model.geo.addPoint((0.000020+L), 0.000022, 0, 0.00001, 13) 
gmsh.model.geo.addPoint((0.000020+L), 0, 0, 0.00001, 14) 
gmsh.model.geo.addPoint(0.000060, 0, 0, 0.00001, 15) 
gmsh.model.geo.addPoint(0.000060, 0.000016, 0, 0.00001, 16) 
gmsh.model.geo.addPoint(0.000020, 0.000016, 0, 0.00001, 17) 
gmsh.model.geo.addPoint(0.000020, 0.000002, 0, 0.00001, 18) 

gmsh.model.geo.addPoint((0.000020+L)+0.000430, 0.000036, 0, 0.00001, 19) 
gmsh.model.geo.addPoint((0.000020+L)+0.000440, 0.0000485, 0, 0.00001, 20) 
gmsh.model.geo.addPoint((0.000020+L)+0.000450, 0.0000485, 0, 0.00001, 21) 
gmsh.model.geo.addPoint((0.000020+L)+0.000435, 0.000029, 0, 0.00001, 22) 
gmsh.model.geo.addPoint((0.000020+L)-0.000007, 0.000036, 0, 0.00001, 23) 
gmsh.model.geo.addPoint(0.000060, 0.000022, 0, 0.00001, 24) 

#Lines connecting the points
gmsh.model.geo.addLine(1, 2, 1) 
gmsh.model.geo.addLine(2, 3, 2) 
gmsh.model.geo.addLine(3, 24, 3) 
gmsh.model.geo.addLine(24, 4, 4) 
gmsh.model.geo.addLine(4, 5, 5) 
gmsh.model.geo.addLine(5, 6, 6) 
gmsh.model.geo.addLine(6, 7, 7) 
gmsh.model.geo.addLine(7, 8, 8) 
gmsh.model.geo.addLine(8, 9, 9) 
gmsh.model.geo.addLine(9, 10, 10) 
gmsh.model.geo.addLine(10, 23, 11)
gmsh.model.geo.addLine(23, 11, 12) 
gmsh.model.geo.addLine(11, 12, 13) 
gmsh.model.geo.addLine(12, 13, 14) 
gmsh.model.geo.addLine(13, 14, 15) 
gmsh.model.geo.addLine(14, 15, 16) 
gmsh.model.geo.addLine(15, 16, 17) 
gmsh.model.geo.addLine(16, 17, 18) 
gmsh.model.geo.addLine(17, 18, 19) 
gmsh.model.geo.addLine(18, 1, 20) 
gmsh.model.geo.addLine(11, 19, 21) 
gmsh.model.geo.addLine(19, 20, 22) 
gmsh.model.geo.addLine(20, 21, 23) 
gmsh.model.geo.addLine(21, 22, 24) 
gmsh.model.geo.addLine(22, 12, 25) 
gmsh.model.geo.addLine(5, 12, 26) 
gmsh.model.geo.addLine(4, 13, 27)
gmsh.model.geo.addLine(17, 3, 28) 
gmsh.model.geo.addLine(16, 24, 29) 
gmsh.model.geo.addLine(6, 10, 30) 


gmsh.model.geo.addCurveLoop([8, 9, 10, -30, 7], 31) 
gmsh.model.geo.addPlaneSurface([31], 32) 
gmsh.model.geo.addCurveLoop([11, 12, 13, -26, 6, 30], 33) 
gmsh.model.geo.addPlaneSurface([33], 34) 
gmsh.model.geo.addCurveLoop([14, -27, 5, 26], 35)
gmsh.model.geo.addPlaneSurface([35], 36) 
gmsh.model.geo.addCurveLoop([15, 16, 17, 29, 4, 27], 37) 
gmsh.model.geo.addPlaneSurface([37], 38) 
gmsh.model.geo.addCurveLoop( [18, 28, 3, -29], 39) 
gmsh.model.geo.addPlaneSurface([39], 40) 
gmsh.model.geo.addCurveLoop([19, 20, 1, 2, -28], 41) 
gmsh.model.geo.addPlaneSurface([41], 42) 
gmsh.model.geo.addCurveLoop([21, 22, 23, 24, 25, -13], 43) 
gmsh.model.geo.addPlaneSurface([43], 44) 


gmsh.model.geo.extrude([(2,32), (2,34), (2,36), (2, 38), (2, 40), (2, 42), (2, 44)], 0, 0, 0.000020)


gmsh.model.addPhysicalGroup(2, [71, 206], 240)  #Gold Anchor Surface
gmsh.model.addPhysicalGroup(2, [179, 157, 125, 103], 241)  #Gold Surface


gmsh.model.geo.extrude([(2,71), (2, 206), (2, 179), (2, 157), (2, 125), (2, 103)], 0, 0, 0.0000003) 



gmsh.model.addPhysicalGroup(3, [8, 9], 404) #Gold Anchor
gmsh.model.addPhysicalGroup(3, [10, 13, 11, 12], 405)  #Gold 
gmsh.model.addPhysicalGroup(3, [1, 6], 406)  #Polymer Anchor
gmsh.model.addPhysicalGroup(3, [5, 2, 4, 3, 7], 407)  #Polymer


####

#define points
gmsh.model.geo.addPoint(0, 0.000102, 0, 0.00001, 175) 
gmsh.model.geo.addPoint(0, 0.000082, 0, 0.00001, 176) 
gmsh.model.geo.addPoint(0.000020, 0.000082, 0, 0.00001, 177) 
gmsh.model.geo.addPoint((0.000020+L)-0.000007, 0.000082, 0, 0.00001, 178) 
gmsh.model.geo.addPoint((0.000020+L)-0.000007, 0.000075, 0, 0.00001, 179) 
gmsh.model.geo.addPoint(0.000020, 0.000075, 0, 0.00001, 180) 
gmsh.model.geo.addPoint(0, 0.000075, 0, 0.00001, 181) 
gmsh.model.geo.addPoint(0, 0.000055, 0, 0.00001, 182) 
gmsh.model.geo.addPoint(0.000020, 0.000055, 0, 0.00001, 183)
gmsh.model.geo.addPoint(0.000020, 0.000068, 0, 0.00001, 184) 
gmsh.model.geo.addPoint((0.000020+L), 0.000068, 0, 0.00001, 185) 
gmsh.model.geo.addPoint((0.000020+L), 0.000075, 0, 0.00001, 186) 
gmsh.model.geo.addPoint((0.000020+L), 0.000082, 0, 0.00001, 187) 
gmsh.model.geo.addPoint((0.000020+L), 0.000104, 0, 0.00001, 188) 
gmsh.model.geo.addPoint(0.000060, 0.000104, 0, 0.00001, 189) 
gmsh.model.geo.addPoint(0.000060, 0.000088, 0, 0.00001, 190) 
gmsh.model.geo.addPoint(0.000020, 0.000088, 0, 0.00001, 191) 
gmsh.model.geo.addPoint(0.000020, 0.000102, 0, 0.00001, 192)

gmsh.model.geo.addPoint((0.000020+L)+0.000430, 0.000068, 0, 0.00001, 193) 
gmsh.model.geo.addPoint((0.000020+L)+0.000440, 0.0000555, 0, 0.00001, 194) 
gmsh.model.geo.addPoint((0.000020+L)+0.000450, 0.0000555, 0, 0.00001, 195) 
gmsh.model.geo.addPoint((0.000020+L)+0.000435, 0.000075, 0, 0.00001, 196) 
gmsh.model.geo.addPoint((0.000020+L)-0.000007, 0.000068, 0, 0.00001, 197) 
gmsh.model.geo.addPoint(0.000060, 0.000082, 0, 0.00001, 198) 

#Add connecting lines

gmsh.model.geo.addLine(182, 183, 408) 
gmsh.model.geo.addLine(183, 184, 409) 
gmsh.model.geo.addLine(184, 180, 410) 
gmsh.model.geo.addLine(180, 181, 411) 
gmsh.model.geo.addLine(181, 182, 412) 
gmsh.model.geo.addLine(184, 197, 413) 
gmsh.model.geo.addLine(197, 185, 414) 
gmsh.model.geo.addLine(185, 186, 415) 
gmsh.model.geo.addLine(186, 179, 416) 

gmsh.model.geo.addLine(179, 180, 418) 
gmsh.model.geo.addLine(176, 175, 419) 
gmsh.model.geo.addLine(175, 192, 420) 
gmsh.model.geo.addLine(192, 191, 421) 
gmsh.model.geo.addLine(191, 190, 422) 
gmsh.model.geo.addLine(190, 189, 423) 
gmsh.model.geo.addLine(189, 188, 424) 
gmsh.model.geo.addLine(188, 187, 425) 
gmsh.model.geo.addLine(187, 186, 426) 
gmsh.model.geo.addLine(187, 178, 427) 
gmsh.model.geo.addLine(178, 179, 428) 
gmsh.model.geo.addLine(178, 198, 429) 
gmsh.model.geo.addLine(198, 190, 430) 
gmsh.model.geo.addLine(198, 177, 431) 
gmsh.model.geo.addLine(177, 191, 432) 
gmsh.model.geo.addLine(177, 176, 433) 
gmsh.model.geo.addLine(185, 193, 434) 
gmsh.model.geo.addLine(193, 194, 435) 
gmsh.model.geo.addLine(194, 195, 436) 
gmsh.model.geo.addLine(195, 196, 437) 
gmsh.model.geo.addLine(196, 186, 438) 


gmsh.model.geo.addCurveLoop([411, 412, 408, 409, 410], 439) 
gmsh.model.geo.addPlaneSurface([439], 440) 
gmsh.model.geo.addCurveLoop([413, 414, 415, 416, 418, -410], 442) 
gmsh.model.geo.addPlaneSurface([442], 443) 
gmsh.model.geo.addCurveLoop([427, 428, -416, -426], 444) 
gmsh.model.geo.addPlaneSurface([444], 445) 
gmsh.model.geo.addCurveLoop([424, 425, 427, 429, 430, 423], 446) 
gmsh.model.geo.addPlaneSurface([446], 447) 
gmsh.model.geo.addCurveLoop([422, -430, 431, 432], 448) 
gmsh.model.geo.addPlaneSurface([448], 449) 
gmsh.model.geo.addCurveLoop([420, 421, -432, 433, 419], 450) 
gmsh.model.geo.addPlaneSurface([450], 451) 
gmsh.model.geo.addCurveLoop([438, -415, 434, 435, 436, 437], 452) 
gmsh.model.geo.addPlaneSurface([452], 453) 

gmsh.model.geo.extrude([(2,440), (2,443), (2,445), (2,447), (2,449), (2,451), (2,453)], 0, 0, 0.000020) ;

gmsh.model.addPhysicalGroup(2, [480, 615], 648)  #Gold anchor surface
gmsh.model.addPhysicalGroup(2, [588, 566, 534, 512], 649)  #Gold surface


gmsh.model.geo.extrude([(2,480), (2,615), (2,588), (2,566), (2,534), (2,512)], 0, 0, 0.0000003)

gmsh.model.addPhysicalGroup(3, [22, 21], 812)   # Gold Anchor
gmsh.model.addPhysicalGroup(3, [23, 24, 25, 26], 813)    #Gold
gmsh.model.addPhysicalGroup(3, [14, 19], 814)   #Polymer Anchor
gmsh.model.addPhysicalGroup(3, [18, 15, 16, 17, 20], 815)    #Polymer


#####
gmsh.model.geo.synchronize()

#type of meshing, here we are doing 3D meshing thats why 3

gmsh.model.mesh.generate(3)

gmsh.write("microgripper.msh2") #saving mesh file

gmsh.fltk.run();

gmsh.finalize()

###########################################################################################################################################################

import numpy as np # Importing numpy library
#name = input("Enter file name: ") # Inputting a file name
#if len(name) < 1 : print("Enter a valid file name")
handle = open("microgripper.msh2") # open file for reading text
mylines = list() # Creating an empty list with name mylines
des_lst_node = list() # Creating an empty list with name des_lst_node
des_lst_ele = list() # Creating an empty list with name des_lst_ele
counter = 0;
for line in handle:                  # For each line in the file with file handle "handle",
    mylines.append(line.rstrip()) # strip newline and add to list.
    counter = counter+1
    if line.rstrip() == '$Nodes' :
        start_index_node = counter-1 # Index of line $Nodes
    if line.rstrip() == '$EndNodes' :
        end_index_node = counter-1 # Index of line $EndNodes
    if line.rstrip() == '$Elements' :
        start_index_ele = counter-1 # Index of line $Elements
    if line.rstrip() == '$EndElements' :
        end_index_ele = counter-1 # Index of line $EndElements
des_lst_node = mylines[start_index_node+2:end_index_node] # Creating a new list with data between $Nodes and $EndNodes.
# Also, this command removes the immediate number followed by $Nodes line
des_lst_ele = mylines[start_index_ele+2:end_index_ele] # Creating a new list with data between $Elements and $EndElements.
# Also, this command removes the immediate number followed by $Nodes line


for item in range(len(des_lst_node)) :
    # print('==================================== Node list ==================================')
    # print('Element of list des_lst_node before spliting: \n', des_lst_node[item])
    des_lst_node[item] = des_lst_node[item].split() # Splits the each element of list des_lst_node
    # print('Element of list des_lst_node after spliting; \n', des_lst_node[item])
    des_lst_node[item] = des_lst_node[item][1:len(des_lst_node[item])] # Removing first number in each element of list
    # print('Element of list des_lst_node after removing first number in element: \n', des_lst_node[item])
    # print('==================================== End of Node list ===========================')
for item in range(len(des_lst_ele)) :
    # print('==================================== Elements list ==============================')
    # print('Element of list des_lst_ele before spliting: \n', des_lst_ele[item])
    des_lst_ele[item] = des_lst_ele[item].split() # Splits the each element of list des_lst_ele
    # print('Element of list des_lst_ele after spliting; \n', des_lst_ele[item])
    des_lst_ele[item] = des_lst_ele[item][3:len(des_lst_ele[item])] # Removing first number in each element of list
    # print('Element of list des_lst_ele after removing first number in element: \n', des_lst_ele[item])
    # print('================================ End of Elements list ===========================')
des_arr_node = np.array(des_lst_node) #Converting list to numpy array
des_arr_ele = np.array(des_lst_ele) #Converting list to numpy array
# print('====================== Required numpy array out of Nodes list =====================')
# print(des_arr_node) # prints the required numpy array out of the numeric data extracted from text file
# print('============================= End of Nodes list ===================================')
# print('===================== Required numpy array out of Elements list ===================')
# print(des_arr_ele) # prints the required numpy array out of the numeric data extracted from text file
# print('============================= End of Elements list ===============================')

##########################################################################################################################################################

N=np.empty(shape=((len(des_arr_node)),3))

for i in range(len(des_arr_node)):
     N[i][0]= (des_arr_node[i][0]) 
     N[i][1]= (des_arr_node[i][1]) 
     N[i][2]= (des_arr_node[i][2]) 
     
# print(N)


##########################################################################################################################################################

BB=np.array([]) 
B0=np.array([])
for i in range(len(des_arr_ele)):
    if (len(des_arr_ele[i])==5):
        BB=np.append(BB, [des_arr_ele[i]])
    else:
        B0=np.append(B0, des_arr_ele[i])
           
BB=BB.reshape(-1,5)
# print(BB)

B0=B0.reshape(-1,6)
# print(B0)


B1=np.empty(shape=((len(BB)),5))

for i in range(len(BB)):
     B1[i][0]= (BB[i][0]) 
     B1[i][1]= (BB[i][1]) 
     B1[i][2]= (BB[i][2]) 
     B1[i][3]= (BB[i][3]) 
     B1[i][4]= (BB[i][4])  
# print(B1)

B=np.empty(shape=((len(B0)),6), dtype = int)

for i in range(len(B0)):
     B[i][0]= (B0[i][0]) 
     B[i][1]= (B0[i][1]) 
     B[i][2]= (B0[i][2]) 
     B[i][3]= (B0[i][3]) 
     B[i][4]= (B0[i][4])
     B[i][5]= (B0[i][5])  
# print(B)

##########################################################################################################################################################

B2=np.copy(B1)

B2=B2[np.logical_not(np.logical_or(B2[:,0]==241, B2[:,0]==648))]

B2=B2[np.logical_not(B2[:,0]==649)]

# with np.printoptions(threshold=np.inf):
#     print(B2)
    
n1=np.empty(shape=((len(B2)),3), dtype = int)

for i in range(len(B2)):
     n1[i][0]= (B2[i][2]) 
     n1[i][1]= (B2[i][3]) 
     n1[i][2]= (B2[i][4]) 

# with np.printoptions(threshold=np.inf):
#     print(n1)
    

B3=np.copy(B1)

B3=B3[np.logical_not(np.logical_or(B3[:,0]==240, B3[:,0]==648))]

B3=B3[np.logical_not(B3[:,0]==649)]

# with np.printoptions(threshold=np.inf):
#     print(B3)
    
n2=np.empty(shape=((len(B3)),3), dtype = int)

for i in range(len(B3)):
     n2[i][0]= (B3[i][2]) 
     n2[i][1]= (B3[i][3]) 
     n2[i][2]= (B3[i][4]) 
# with np.printoptions(threshold=np.inf):
#     print(n2)
    
    
B4=np.copy(B1)

B4=B4[np.logical_not(np.logical_or(B4[:,0]==241, B4[:,0]==240))]

B4=B4[np.logical_not(B4[:,0]==649)]

# with np.printoptions(threshold=np.inf):
#     print(B4)
    
    
n3=np.empty(shape=((len(B4)),3), dtype = int)

for i in range(len(B4)):
     n3[i][0]= (B4[i][2]) 
     n3[i][1]= (B4[i][3]) 
     n3[i][2]= (B4[i][4]) 
# print(n3)
    
    
B5=np.copy(B1)

B5=B5[np.logical_not(np.logical_or(B5[:,0]==241, B5[:,0]==240))]

B5=B5[np.logical_not(B5[:,0]==648)]

# with np.printoptions(threshold=np.inf):
#     print(B5)


n4=np.empty(shape=((len(B5)),3), dtype = int)

for i in range(len(B5)):
     n4[i][0]= (B5[i][2]) 
     n4[i][1]= (B5[i][3]) 
     n4[i][2]= (B5[i][4]) 
# print(n4)

##############################################################################################################################################################################

B6=np.copy(B)

B6=B6[np.logical_not(np.logical_or(B6[:,0]==405, B6[:,0]==406))]

B6=B6[np.logical_not(np.logical_or(B6[:,0]==407, B6[:,0]==812))]

B6=B6[np.logical_not(np.logical_or(B6[:,0]==813, B6[:,0]==814))]

B6=B6[np.logical_not(B6[:,0]==815)]

# with np.printoptions(threshold=np.inf):
#     print(B6)
    
    
n5=np.empty(shape=((len(B6)),4), dtype = int)

for i in range(len(B6)):
     n5[i][0]= (B6[i][2]) 
     n5[i][1]= (B6[i][3]) 
     n5[i][2]= (B6[i][4])
     n5[i][3]= (B6[i][5]) 
# print(n5)
    
    
    
B7=np.copy(B)

B7=B7[np.logical_not(np.logical_or(B7[:,0]==404, B7[:,0]==406))]

B7=B7[np.logical_not(np.logical_or(B7[:,0]==407, B7[:,0]==812))]

B7=B7[np.logical_not(np.logical_or(B7[:,0]==813, B7[:,0]==814))]

B7=B7[np.logical_not(B7[:,0]==815)]

# with np.printoptions(threshold=np.inf):
#     print(B7)
    
n6=np.empty(shape=((len(B7)),4), dtype = int)

for i in range(len(B7)):
     n6[i][0]= (B7[i][2]) 
     n6[i][1]= (B7[i][3]) 
     n6[i][2]= (B7[i][4])
     n6[i][3]= (B7[i][5]) 

# with np.printoptions(threshold=np.inf):
#     print(n6)



    
B8=np.copy(B)

B8=B8[np.logical_not(np.logical_or(B8[:,0]==404, B8[:,0]==405))]

B8=B8[np.logical_not(np.logical_or(B8[:,0]==407, B8[:,0]==812))]

B8=B8[np.logical_not(np.logical_or(B8[:,0]==813, B8[:,0]==814))]

B8=B8[np.logical_not(B8[:,0]==815)]

# with np.printoptions(threshold=np.inf):
#     print(B8)


n7=np.empty(shape=((len(B8)),4), dtype = int)

for i in range(len(B8)):
     n7[i][0]= (B8[i][2]) 
     n7[i][1]= (B8[i][3]) 
     n7[i][2]= (B8[i][4])
     n7[i][3]= (B8[i][5]) 

# with np.printoptions(threshold=np.inf):
#     print(n7)
    
    
B9=np.copy(B)

B9=B9[np.logical_not(np.logical_or(B9[:,0]==404, B9[:,0]==405))]

B9=B9[np.logical_not(np.logical_or(B9[:,0]==406, B9[:,0]==812))]

B9=B9[np.logical_not(np.logical_or(B9[:,0]==813, B9[:,0]==814))]

B9=B9[np.logical_not(B9[:,0]==815)]

# with np.printoptions(threshold=np.inf):
#     print(B9)

n8=np.empty(shape=((len(B9)),4), dtype = int)

for i in range(len(B9)):
     n8[i][0]= (B9[i][2]) 
     n8[i][1]= (B9[i][3]) 
     n8[i][2]= (B9[i][4])
     n8[i][3]= (B9[i][5]) 

# with np.printoptions(threshold=np.inf):
#     print(n8)



    
B10=np.copy(B)

B10=B10[np.logical_not(np.logical_or(B10[:,0]==404, B10[:,0]==405))]

B10=B10[np.logical_not(np.logical_or(B10[:,0]==406, B10[:,0]==407))]

B10=B10[np.logical_not(np.logical_or(B10[:,0]==813, B10[:,0]==814))]

B10=B10[np.logical_not(B10[:,0]==815)]

# with np.printoptions(threshold=np.inf):
#     print(B10)



n9=np.empty(shape=((len(B10)),4), dtype = int)

for i in range(len(B10)):
     n9[i][0]= (B10[i][2]) 
     n9[i][1]= (B10[i][3]) 
     n9[i][2]= (B10[i][4])
     n9[i][3]= (B10[i][5]) 

# with np.printoptions(threshold=np.inf):
#     print(n9)

    
B11=np.copy(B)

B11=B11[np.logical_not(np.logical_or(B11[:,0]==404, B11[:,0]==405))]

B11=B11[np.logical_not(np.logical_or(B11[:,0]==406, B11[:,0]==407))]

B11=B11[np.logical_not(np.logical_or(B11[:,0]==812, B11[:,0]==814))]

B11=B11[np.logical_not(B11[:,0]==815)]

# with np.printoptions(threshold=np.inf):
#     print(B11)
    
n10=np.empty(shape=((len(B11)),4), dtype = int)

for i in range(len(B11)):
     n10[i][0]= (B11[i][2]) 
     n10[i][1]= (B11[i][3]) 
     n10[i][2]= (B11[i][4])
     n10[i][3]= (B11[i][5]) 

# with np.printoptions(threshold=np.inf):
#     print(n10)

    
B12=np.copy(B)

B12=B12[np.logical_not(np.logical_or(B12[:,0]==404, B12[:,0]==405))]

B12=B12[np.logical_not(np.logical_or(B12[:,0]==406, B12[:,0]==407))]

B12=B12[np.logical_not(np.logical_or(B12[:,0]==812, B12[:,0]==813))]

B12=B12[np.logical_not(B12[:,0]==815)]

# with np.printoptions(threshold=np.inf):
#     print(B12)

n11=np.empty(shape=((len(B12)),4), dtype = int)

for i in range(len(B12)):
     n11[i][0]= (B12[i][2]) 
     n11[i][1]= (B12[i][3]) 
     n11[i][2]= (B12[i][4])
     n11[i][3]= (B12[i][5]) 

# with np.printoptions(threshold=np.inf):
#     print(n11)

    
B13=np.copy(B)

B13=B13[np.logical_not(np.logical_or(B13[:,0]==404, B13[:,0]==405))]

B13=B13[np.logical_not(np.logical_or(B13[:,0]==406, B13[:,0]==407))]

B13=B13[np.logical_not(np.logical_or(B13[:,0]==812, B13[:,0]==813))]

B13=B13[np.logical_not(B13[:,0]==814)]

# with np.printoptions(threshold=np.inf):
#     print(B13)


n12=np.empty(shape=((len(B13)),4), dtype = int)

for i in range(len(B13)):
     n12[i][0]= (B13[i][2]) 
     n12[i][1]= (B13[i][3]) 
     n12[i][2]= (B13[i][4])
     n12[i][3]= (B13[i][5]) 

# with np.printoptions(threshold=np.inf):
#     print(n12)

n13=np.empty(shape=((len(B)),4), dtype = int)
#n13 consists of element list
for i in range(len(B)):
     n13[i][0]= (B[i][2]) 
     n13[i][1]= (B[i][3]) 
     n13[i][2]= (B[i][4])
     n13[i][3]= (B[i][5]) 

# with np.printoptions(threshold=np.inf):
#     print(n13)    
######################################################################################################################3

nnodes=(len(N))

nels=len(n13)


choose=np.zeros((nnodes+1, 1), dtype=int)

for i in range(nnodes+1):
    if(i in n1)==True:
        choose[i]=1
    elif(i in n2)==True:
        choose[i]=1
    elif(i in n3)==True:
        choose[i]=11
    elif(i in n4)==True:
        choose[i]=11
    elif(i in n5)==True:
        choose[i]=1
    elif(i in n6)==True:
        choose[i]=1
    elif(i in n7)==True:
        choose[i]=0
    elif(i in n8)==True:
        choose[i]=0
    elif(i in n9)==True:
        choose[i]=11
    elif(i in n10)==True:
        choose[i]=11
    elif(i in n11)==True:
        choose[i]=2
    elif(i in n12)==True:
        choose[i]=2
    
# with np.printoptions(threshold=np.inf):
#      print(choose)
#choose 1 means the node id gold, 0 means node is in polymer
##########################################################################################

choose1=np.zeros((nels, 1), dtype=int)

for i in range(nels):
    
    if(any((n5[:]==n13[i]).all(1))==True):
        choose1[i]=1
    elif(any((n6[:]==n13[i]).all(1))==True):
        choose1[i]=1
    elif(any((n7[:]==n13[i]).all(1))==True):
        choose1[i]=0
    elif(any((n8[:]==n13[i]).all(1))==True):
        choose1[i]=0
    elif(any((n9[:]==n13[i]).all(1))==True):
        choose1[i]=11
    elif(any((n10[:]==n13[i]).all(1))==True):
        choose1[i]=11
    elif(any((n11[:]==n13[i]).all(1))==True):
        choose1[i]=2
    elif(any((n12[:]==n13[i]).all(1))==True):
        choose1[i]=2
        
# with np.printoptions(threshold=np.inf):
#     print(choose1)
        
# if choose1=1,11 element is gold, choose1=0,2 element is polymer

############################################################################################

bnodes=np.zeros((nnodes+1, 1), dtype=int)


for i in range(nnodes+1):
    if(i in n1)==True:
        bnodes[i,0]=1
    elif(i in n3)==True:
         bnodes[i,0]=1
    elif(i in n5)==True:
         bnodes[i,0]=1
    elif(i in n7)==True:
         bnodes[i,0]=1
    elif(i in n9)==True:
         bnodes[i,0]=1
    elif(i in n11)==True:
         bnodes[i,0]=1
    else:
         bnodes[i,0]=0
    
    
# print(bnodes)

# if bnode=1, it is in boundary, bnode=0 it is inside
#################################################################################################

#material properties

#initialize material constants
Cp=np.zeros((nels, 1))
rho=np.zeros((nels, 1))
k=np.zeros((nels, 1))
E=np.zeros((nels, 1))
nu=np.zeros((nels, 1))
G=np.zeros((nels, 1))


Cp_gold= 129 # specific heat of gold
rho_gold= 19300 # density of gold
k_gold=  310 # heat conductivity of gold

Cp_polymer=  1500 # specific heat of polymer
rho_polymer= 1200 # density of polymer
k_polymer= 0.2 # heat conductivity of polymer

E_polymer=4400000000 # in Pa Young's Modulus
E_gold=78000000000  # in Pa  Young's Modulus


nu_polymer=0.22
nu_gold=0.42


for e in range(nels):
    if(choose1[e]==1):
        Cp[e]=Cp_gold
        rho[e]=rho_gold
        k[e]=k_gold
        E[e]=E_gold
        nu[e]=nu_gold
    elif(choose1[e]==0):
        Cp[e]=Cp_polymer
        rho[e]=rho_polymer
        k[e]=k_polymer
        E[e]=E_polymer
        nu[e]=nu_polymer
    elif(choose1[e]==11):
        Cp[e]=Cp_gold
        rho[e]=rho_gold
        k[e]=k_gold
        E[e]=E_gold
        nu[e]=nu_gold
    elif(choose1[e]==2):
        Cp[e]=Cp_polymer
        rho[e]=rho_polymer
        k[e]=k_polymer
        E[e]=E_polymer
        nu[e]=nu_polymer
    
    G[e]=((0.5*E[e])/(1+nu[e]))
    
    
####################################################################################################


#initialize input vector
Q=np.zeros((nnodes+1, 1))  


J=1.31*(10**1) # A/m2
sigma=4.1*(10**7);  
#Q is the input vector
for i in range(nnodes+1):
    if(choose[i]==1):
        Q[i]=1
    elif(choose[i]==11):
        Q[i]=1
    else:
        Q[i]=0
        

#####################################################################################################
        
# Initializing the global coeffnt matrix ...
 
K = np.zeros((nnodes+1, nnodes+1), dtype=float)  #Inisializing K, Stiffness matix
C=np.zeros((nnodes+1, nnodes+1), dtype=float)  #Inisializing C, Thermal matix

    
#xcen = np.zeros(1,nels) ; ycen = xcen ; 

x=np.zeros((nnodes+1,1), float)
y=np.zeros((nnodes+1,1), float)
z=np.zeros((nnodes+1,1), float)

for i in range(nnodes):
     x[i+1]=N[i][0]
     y[i+1]=N[i][1]
     z[i+1]=N[i][2]
#Generating the e-th coeffnt matrix ...
    
ex=np.zeros((1,4), float)
ey=np.zeros((1,4), float)
ez=np.zeros((1,4), float)

for e in range(nels):
    # print(e)
    ex[0,0]=x[n13[e,0]]
    ex[0,1]=x[n13[e,1]]
    ex[0,2]=x[n13[e,2]]
    ex[0,3]=x[n13[e,3]]
    # print(ex)
    ey[0,0]=y[n13[e][0]] 
    ey[0,1]=y[n13[e][1]]
    ey[0,2]=y[n13[e][2]] 
    ey[0,3]=y[n13[e][3]]
    
    ez[0,0]=z[n13[e][0]] 
    ez[0,1]=z[n13[e][1]]
    ez[0,2]=z[n13[e][2]] 
    ez[0,3]=z[n13[e][3]]
    
    # #  ex and ey has the global coordinates of the three nodes of current element.

    a=np.array([[1,ex[0,0], ey[0,0], ez[0,0]],
                [1,ex[0,1], ey[0,1], ez[0,1]],
                [1,ex[0,2], ey[0,2], ez[0,2]],
                [1,ex[0,3], ey[0,3], ez[0,3]]])
     
    Vole = (1/6)*np.linalg.det(a)
    
    bet=np.zeros((1,4), float); 
    gam = np.zeros((1,4), float); 
    delt=np.zeros((1,4), float);
    
    
    bet[0,0]=(((ey[0,1]*ez[0,3])-(ey[0,3]*ez[0,1]))+((ey[0,2]*ez[0,1])-(ey[0,1]*ez[0,2]))+((ey[0,3]*ez[0,2])-(ey[0,2]*ez[0,3])));  
    bet[0,1]=(((ey[0,0]*ez[0,2])-(ey[0,2]*ez[0,0]))+((ey[0,2]*ez[0,3])-(ey[0,3]*ez[0,2]))+((ey[0,3]*ez[0,0])-(ey[0,0]*ez[0,3])));     
    bet[0,2]=(((ey[0,0]*ez[0,3])-(ey[0,3]*ez[0,0]))+((ey[0,1]*ez[0,0])-(ey[0,0]*ez[0,1]))+((ey[0,3]*ez[0,1])-(ey[0,1]*ez[0,3])));      
    bet[0,3]=(((ey[0,0]*ez[0,1])-(ey[0,1]*ez[0,0]))+((ey[0,1]*ez[0,2])-(ey[0,2]*ez[0,1]))+((ey[0,2]*ez[0,0])-(ey[0,0]*ez[0,2])));   
    
    gam[0,0]=(((ez[0,1]*ex[0,3])-(ez[0,3]*ex[0,1]))+((ez[0,2]*ex[0,1])-(ez[0,1]*ex[0,2]))+((ez[0,3]*ex[0,2])-(ez[0,2]*ex[0,3])));   
    gam[0,1]=(((ez[0,0]*ex[0,2])-(ez[0,2]*ex[0,0]))+((ez[0,2]*ex[0,3])-(ez[0,3]*ex[0,2]))+((ez[0,3]*ex[0,0])-(ez[0,0]*ex[0,3])));
    gam[0,2]=(((ez[0,0]*ex[0,3])-(ez[0,3]*ex[0,0]))+((ez[0,1]*ex[0,0])-(ez[0,0]*ex[0,1]))+((ez[0,3]*ex[0,1])-(ez[0,1]*ex[0,3])));
    gam[0,3]=(((ez[0,0]*ex[0,1])-(ez[0,1]*ex[0,0]))+((ez[0,1]*ex[0,2])-(ez[0,2]*ex[0,1]))+((ez[0,2]*ex[0,0])-(ez[0,0]*ex[0,2]))); 
   
    delt[0,0]=(((ex[0,1]*ey[0,3])-(ex[0,3]*ey[0,1]))+((ex[0,2]*ey[0,1])-(ex[0,1]*ey[0,2]))+((ex[0,3]*ey[0,2])-(ex[0,2]*ey[0,3])));   
    delt[0,1]=(((ex[0,0]*ey[0,2])-(ex[0,2]*ey[0,0]))+((ex[0,2]*ey[0,3])-(ex[0,3]*ey[0,2]))+((ex[0,3]*ey[0,0])-(ex[0,0]*ey[0,3])));
    delt[0,2]=(((ex[0,0]*ey[0,3])-(ex[0,3]*ey[0,0]))+((ex[0,1]*ey[0,0])-(ex[0,0]*ey[0,1]))+((ex[0,3]*ey[0,1])-(ex[0,1]*ey[0,3])));
    delt[0,3]=(((ex[0,0]*ey[0,1])-(ex[0,1]*ey[0,0]))+((ex[0,1]*ey[0,2])-(ex[0,2]*ey[0,1]))+((ex[0,2]*ey[0,0])-(ex[0,0]*ey[0,2]))); 
   
    Ke=np.empty((4,4),dtype=float)
    ec=np.empty((4,4),dtype=float)
    
    for i in range(4):
        for j in range(4):
            Ke[i,j]=(1/(36*Vole))*((bet[0,i]*bet[0,j])+(gam[0,i]*gam[0,j])+(delt[0,i]*delt[0,j]))
      
        
    Ke1=Ke*(k[e])
    ec[0,0]=(Vole/10)
    ec[1,1]=ec[0,0];
    ec[2,2]=ec[1,1];
    ec[3,3]=ec[2,2];
    
    ec[0,1]=(Vole/20);
    ec[1,0]=ec[0,1];
    
    ec[0,2]=(Vole/20);
    ec[2,0]=ec[0,2];
    
    ec[0,3]=(Vole/20);
    ec[3,0]=ec[0,3];
    
    ec[1,2]=(Vole/20);
    ec[2,1]=ec[1,2];
    
    
    ec[1,3]=(Vole/20);
    ec[3,1]=ec[1,3];
    
    ec[2,3]=(Vole/20);
    ec[3,2]=ec[2,3];
    
    ec1=(Cp[e]*rho[e])*ec
    
    
    for i in range(4):
        for j in range(4):
            K[n13[e,i], n13[e,j]]=K[n13[e,i], n13[e,j]]+Ke1[i,j]
            C[n13[e,i], n13[e,j]]=C[n13[e,i], n13[e,j]]+ec1[i,j]
            
# print(np.linalg.det(K))            
#########################################################################################################################################################

K=np.delete(K, (0), axis=0)
K=K.reshape((nnodes,-1))
K=np.delete(K,(0), axis=1)
K=K.reshape((nnodes,-1))

C=np.delete(C,(0), axis=0)
C=C.reshape(nnodes,-1)
C=np.delete(C,(0), axis=1)
C=C.reshape((nnodes,-1))

Q=np.delete(Q, (0), axis=0)
Q=Q.reshape((nnodes,1))

choose=np.delete(choose,(0), axis=0)
choose=choose.reshape((nnodes,1))

bnodes=np.delete(bnodes,(0), axis=0)
bnodes=bnodes.reshape((nnodes,1))

#######################################################################################################################################################3

K1=np.copy(K)
C1=np.copy(C)
Fh=np.copy(Q)
for i in reversed(range(nnodes)):
    if(bnodes[i,0]==1):
        # print(i)
        K1=np.delete(K1, (i), axis=0)
        C1=np.delete(C1, (i), axis=0)
        Fh=np.delete(Fh, (i), axis=0)
        
        
##############################################################################################################################################################
        
Auu=np.copy(K1);
Aud=np.copy(K1);
Cuu=np.copy(C1);

for i in reversed(range(nnodes)):
    if(bnodes[i,0]==1):
        Auu=np.delete(Auu, (i), axis=1)
        Cuu=np.delete(Cuu, (i), axis=1)
    else:
        Aud=np.delete(Aud, (i), axis=1)
        
# print(np.linalg.det(Auu))        
################################################################################################################################################################

td=(np.ones((Aud.shape[1],1), dtype=float))*293;      

t=0.2;
h=0.01;
tf=int(t/h)

alpha=1;



tu=np.zeros((Auu.shape[1],1), dtype=float)

T1=np.zeros((Auu.shape[1],tf), dtype=float)



for i in range(len(tu)):   #initial value 
    tu[i,0]=293
    T1[i,0]=293
# print(tu)   

 

f=((Fh)*u-(Aud@td))

for i in range(1, tf):
    tu=(np.linalg.inv(Cuu+(alpha*h*Auu)))@(((Cuu-((1-alpha)*h*Auu))@(tu))+(h*((alpha*(f))+((1-alpha)*(f)))));

    T1[:,i]=(tu).T
    
    
# print(T1)


#######################################################################################################################################################################################

T2=np.zeros((nnodes,1), dtype=float)


p = 0 ;
   
for i in range(nnodes):
    if(bnodes[i,0]==1):
        # print(i)
        T2[i] = 293 
    elif(bnodes[i,0]==0):
         
         T2[i] = tu[p]  
         p=p+1
         # print(p)
         
        
# print(T2)


###############################################################################################################################################

That=np.zeros((nnodes,1), dtype=float)


for i in range(nnodes):
    if (choose[i]==0 or choose[i]==2):
        That[i]=T2[i];
    else:
        That[i]=0;
   
Thatmax=np.amax(That)
print("Max temp in polymer is %f" %(Thatmax))

#Thatmax is showing the maximum temperature in the polymer which should not be more than 140 degree C or 413K
#######################################################################################################################################################################################

T=np.zeros((nnodes,1), dtype=float)

for i in range(1, nnodes):
    T[i]=T2[i]


# print(T)


E_polymer1=4.4*(10**9) # in GPa
E_gold1=77.2*(10**9)  # in GPa

alp_polymer1=52*(10**(-6))
alp_gold1=14.4*(10**(-6))

poisson_polymer1=0.22
poisson_gold1=0.42

Ti=293

E1=np.zeros((nnodes,1), dtype=float)
alp1=np.zeros((nnodes,1), dtype=float)
poisson1=np.zeros((nnodes,1), dtype=float)
sigma_th=np.zeros((nnodes,1), dtype=float)

for i in range(nnodes):
    if(choose[i]==1):
        E1[i]=E_gold1
        alp1[i]=alp_gold1
        poisson1[i]=poisson_gold1
    elif(choose[i]==0):
        E1[i]=E_polymer1
        alp1[i]=alp_polymer1
        poisson1[i]=poisson_polymer1
    elif(choose[i]==11):
        E1[i]=E_gold1
        alp1[i]=alp_gold1
        poisson1[i]=poisson_gold1
    elif(choose[i]==2):
        E1[i]=E_polymer1
        alp1[i]=alp_polymer1
        poisson1[i]=poisson_polymer1
    
    sigma_th[i]= E1[i]*alp1[i]*(1/(1-poisson1[i]))*(Ti-T[i])


#sigma_th=np.delete(sigma_th, (0), axis=0)
# print(sigma_th)


##########################################################################################################################################################
# Initializing the global coeffnt matrix ...
 
K11=np.zeros((nnodes+1, nnodes+1), dtype=float)  #Inisializing K, Stiffness matix
K12=np.zeros((nnodes+1, nnodes+1), dtype=float)
K13=np.zeros((nnodes+1, nnodes+1), dtype=float)
K22=np.zeros((nnodes+1, nnodes+1), dtype=float)
K23=np.zeros((nnodes+1, nnodes+1), dtype=float)
K33=np.zeros((nnodes+1, nnodes+1), dtype=float)

Fd=np.zeros((nnodes+1,1), dtype=float);

Mass=np.zeros((nnodes+1, nnodes+1), dtype=float)


#xcen = np.zeros(1,nels) ; ycen = xcen ; 

x=np.zeros((nnodes+1,1), float)
y=np.zeros((nnodes+1,1), float)
z=np.zeros((nnodes+1,1), float)

for i in range(nnodes):
     x[i+1]=N[i][0]
     y[i+1]=N[i][1]
     z[i+1]=N[i][2]
#Generating the e-th coeffnt matrix ...
    
ex1=np.zeros((1,4), float)
ey1=np.zeros((1,4), float)
ez1=np.zeros((1,4), float)

for e in range(nels):
    # print(e)
    ex1[0,0]=x[n13[e,0]]
    ex1[0,1]=x[n13[e,1]]
    ex1[0,2]=x[n13[e,2]]
    ex1[0,3]=x[n13[e,3]]
    # print(ex1)
    ey1[0,0]=y[n13[e][0]] 
    ey1[0,1]=y[n13[e][1]]
    ey1[0,2]=y[n13[e][2]] 
    ey1[0,3]=y[n13[e][3]]
    
    ez1[0,0]=z[n13[e][0]] 
    ez1[0,1]=z[n13[e][1]]
    ez1[0,2]=z[n13[e][2]] 
    ez1[0,3]=z[n13[e][3]]
    
    # #  ex and ey has the global coordinates of the three nodes of current element.

    a1=np.array([[1, ex1[0,0], ey1[0,0], ez1[0,0]],
                 [1, ex1[0,1], ey1[0,1], ez1[0,1]],
                 [1, ex1[0,2], ey1[0,2], ez1[0,2]],
                 [1, ex1[0,3], ey1[0,3], ez1[0,3]]])
     
    Vole1 = (1/6)*np.linalg.det(a1)
    
    delta=(1-(3*(nu[e]**2))-(2*(nu[e]**3)))/(E[e]**3);         
    c11=(1-(nu[e])**2)/((E[e]**2)*delta); 
    c22=(1-(nu[e])**2)/((E[e]**2)*delta);
    c33=(1-(nu[e])**2)/((E[e]**2)*delta);
    c12=(nu[e]-((nu[e])**2))/((E[e]**2)*delta); 
    c13=(nu[e]-((nu[e])**2))/((E[e]**2)*delta); 
    c23=(nu[e]-((nu[e])**2))/((E[e]**2)*delta);
    c44=G[e]; 
    c55=c44; 
    c66=c44; 
    he=0.00001;
    
    bet1=np.zeros((1,4), float); 
    gam1 = np.zeros((1,4), float); 
    delt1=np.zeros((1,4), float);
    
    
    bet1[0,0]=(((ey1[0,1]*ez1[0,3])-(ey1[0,3]*ez1[0,1]))+((ey1[0,2]*ez1[0,1])-(ey1[0,1]*ez1[0,2]))+((ey1[0,3]*ez1[0,2])-(ey1[0,2]*ez1[0,3])));  
    bet1[0,1]=(((ey1[0,0]*ez1[0,2])-(ey1[0,2]*ez1[0,0]))+((ey1[0,2]*ez1[0,3])-(ey1[0,3]*ez1[0,2]))+((ey1[0,3]*ez1[0,0])-(ey1[0,0]*ez1[0,3])));     
    bet1[0,2]=(((ey1[0,0]*ez1[0,3])-(ey1[0,3]*ez1[0,0]))+((ey1[0,1]*ez1[0,0])-(ey1[0,0]*ez1[0,1]))+((ey1[0,3]*ez1[0,1])-(ey1[0,1]*ez1[0,3])));      
    bet1[0,3]=(((ey1[0,0]*ez1[0,1])-(ey1[0,1]*ez1[0,0]))+((ey1[0,1]*ez1[0,2])-(ey1[0,2]*ez1[0,1]))+((ey1[0,2]*ez1[0,0])-(ey1[0,0]*ez1[0,2])));   
    
    gam1[0,0]=(((ez1[0,1]*ex1[0,3])-(ez1[0,3]*ex1[0,1]))+((ez1[0,2]*ex1[0,1])-(ez1[0,1]*ex1[0,2]))+((ez1[0,3]*ex1[0,2])-(ez1[0,2]*ex1[0,3])));   
    gam1[0,1]=(((ez1[0,0]*ex1[0,2])-(ez1[0,2]*ex1[0,0]))+((ez1[0,2]*ex1[0,3])-(ez1[0,3]*ex1[0,2]))+((ez1[0,3]*ex1[0,0])-(ez1[0,0]*ex1[0,3])));
    gam1[0,2]=(((ez1[0,0]*ex1[0,3])-(ez1[0,3]*ex1[0,0]))+((ez1[0,1]*ex1[0,0])-(ez1[0,0]*ex1[0,1]))+((ez1[0,3]*ex1[0,1])-(ez1[0,1]*ex1[0,3])));
    gam1[0,3]=(((ez1[0,0]*ex1[0,1])-(ez1[0,1]*ex1[0,0]))+((ez1[0,1]*ex1[0,2])-(ez1[0,2]*ex1[0,1]))+((ez1[0,2]*ex1[0,0])-(ez1[0,0]*ex1[0,2]))); 
   
    delt1[0,0]=(((ex1[0,1]*ey1[0,3])-(ex1[0,3]*ey1[0,1]))+((ex1[0,2]*ey1[0,1])-(ex1[0,1]*ey1[0,2]))+((ex1[0,3]*ey1[0,2])-(ex1[0,2]*ey1[0,3])));   
    delt1[0,1]=(((ex1[0,0]*ey1[0,2])-(ex1[0,2]*ey1[0,0]))+((ex1[0,2]*ey1[0,3])-(ex1[0,3]*ey1[0,2]))+((ex1[0,3]*ey1[0,0])-(ex1[0,0]*ey1[0,3])));
    delt1[0,2]=(((ex1[0,0]*ey1[0,3])-(ex1[0,3]*ey1[0,0]))+((ex1[0,1]*ey1[0,0])-(ex1[0,0]*ey1[0,1]))+((ex1[0,3]*ey1[0,1])-(ex1[0,1]*ey1[0,3])));
    delt1[0,3]=(((ex1[0,0]*ey1[0,1])-(ex1[0,1]*ey1[0,0]))+((ex1[0,1]*ey1[0,2])-(ex1[0,2]*ey1[0,1]))+((ex1[0,2]*ey1[0,0])-(ex1[0,0]*ey1[0,2]))); 
   
    ek=np.empty((4,4),dtype=float)
    
    
    for i in range(4):
        for j in range(4):
            ek[i,j]=(1/(36*Vole1))*((bet1[0,i]*bet1[0,j])+(gam1[0,i]*gam1[0,j])+(delt1[0,i]*delt1[0,j]))
      
        
    
    ek11=he*((ek*c11)+(ek*c66)+(ek*c44));
    ek12=he*((ek*c12)+(ek*c66));
    ek13=he*((ek*c13)+(ek*c44));
    ek22=he*((ek*c22)+(ek*c66)+(ek*c55));
    ek23=he*((ek*c23)+(ek*c55));
    ek33=he*((ek*c33)+(ek*c55)+(ek*c44));
    
    
    
    em=np.empty((4,4),dtype=float)
    
    em[0,0]=(Vole1/10)
    em[1,1]=em[0,0];
    em[2,2]=em[1,1];
    em[3,3]=em[2,2];
    
    em[0,1]=(Vole1/20);
    em[1,0]=em[0,1];
    
    em[0,2]=(Vole1/20);
    em[2,0]=em[0,2];
    
    em[0,3]=(Vole1/20);
    em[3,0]=em[0,3];
    
    em[1,2]=(Vole1/20);
    em[2,1]=em[1,2];
    
    
    em[1,3]=(Vole1/20);
    em[3,1]=em[1,3];
    
    em[2,3]=(Vole1/20);
    em[3,2]=em[2,3];
    
    em1=(rho[e])*em
    
    em=np.empty((4,1),dtype=float)
    
    ef=(Vole1/4)*np.array([[1.0],
                           [1.0],
                           [1.0],
                           [1.0]])
    
      #Inisializing C, Thermal matix

    for i in range(4):
        for j in range(4):
            K11[n13[e,i], n13[e,j]]=K11[n13[e,i], n13[e,j]]+ek11[i,j]
            K12[n13[e,i], n13[e,j]]=K12[n13[e,i], n13[e,j]]+ek12[i,j]
            K13[n13[e,i], n13[e,j]]=K13[n13[e,i], n13[e,j]]+ek13[i,j]
            K22[n13[e,i], n13[e,j]]=K22[n13[e,i], n13[e,j]]+ek22[i,j]
            K23[n13[e,i], n13[e,j]]=K23[n13[e,i], n13[e,j]]+ek23[i,j]
            K33[n13[e,i], n13[e,j]]=K33[n13[e,i], n13[e,j]]+ek33[i,j]
            
            Mass[n13[e,i], n13[e,j]]=Mass[n13[e,i], n13[e,j]]+em1[i,j]
            Fd[n13[e,i]]= Fd[n13[e,i]]+ef[i]
            
            
    

########################################################################################################################################################################################333

#########################################################################################################################################################

K11=np.delete(K11, (0), axis=0)
K11=K11.reshape((nnodes,-1))
K11=np.delete(K11,(0), axis=1)
K11=K11.reshape((nnodes,-1))

K12=np.delete(K12, (0), axis=0)
K12=K12.reshape((nnodes,-1))
K12=np.delete(K12,(0), axis=1)
K12=K12.reshape((nnodes,-1))

K13=np.delete(K13, (0), axis=0)
K13=K13.reshape((nnodes,-1))
K13=np.delete(K13,(0), axis=1)
K13=K13.reshape((nnodes,-1))

K22=np.delete(K22, (0), axis=0)
K22=K22.reshape((nnodes,-1))
K22=np.delete(K22,(0), axis=1)
K22=K22.reshape((nnodes,-1))

K23=np.delete(K23, (0), axis=0)
K23=K23.reshape((nnodes,-1))
K23=np.delete(K23,(0), axis=1)
K23=K23.reshape((nnodes,-1))

K33=np.delete(K33, (0), axis=0)
K33=K33.reshape((nnodes,-1))
K33=np.delete(K33,(0), axis=1)
K33=K33.reshape((nnodes,-1))


Mass=np.delete(Mass,(0), axis=0)
Mass=Mass.reshape(nnodes,-1)
Mass=np.delete(Mass,(0), axis=1)
Mass=Mass.reshape((nnodes,-1))

Fd=np.delete(Fd, (0), axis=0)
Fd=Fd.reshape((nnodes,1))


########################################################################################################################################################################################333

Fh1=Fd*(sigma_th)
P11=np.copy(K11)
P12=np.copy(K12)
P13=np.copy(K13)
P22=np.copy(K22)
P23=np.copy(K23)
P33=np.copy(K33)
M1=np.copy(Mass)  


for i in reversed(range(nnodes)):
    if(bnodes[i,0]==1 or choose[i]==1 or choose[i]==11):
        # print(i)
        P11=np.delete(P11, (i), axis=0)
        P12=np.delete(P12, (i), axis=0)
        P13=np.delete(P13, (i), axis=0)
        P22=np.delete(P22, (i), axis=0)
        P23=np.delete(P23, (i), axis=0)
        P33=np.delete(P33, (i), axis=0)
        Fh1=np.delete(Fh1, (i), axis=0)
        M1=np.delete(M1, (i), axis=0)
        
        
#######################################################################################################################################################################################################

K11uu=np.copy(P11);
K12uu=np.copy(P12);
K13uu=np.copy(P13);
K22uu=np.copy(P22);
K23uu=np.copy(P23);
K33uu=np.copy(P33);

Muu=np.copy(M1);

for i in reversed(range(nnodes)):
    if(bnodes[i,0]==1 or choose[i]==1 or choose[i]==11):
        K11uu=np.delete(K11uu, (i), axis=1)
        K12uu=np.delete(K12uu, (i), axis=1)
        K13uu=np.delete(K13uu, (i), axis=1)
        K22uu=np.delete(K22uu, (i), axis=1)
        K23uu=np.delete(K23uu, (i), axis=1)
        K33uu=np.delete(K33uu, (i), axis=1)
        Muu=np.delete(Muu, (i), axis=1)
    
        
# print(np.linalg.det(Auu))         
#####################################################################################################################################################3333333###########################################

Z1=np.zeros((Muu.shape[0], Muu.shape[0]))

S1=np.append(Muu, Z1, axis=1)
S2=np.append(S1, Z1, axis=1)
S3=np.append(Z1, Muu, axis=1)
S4=np.append(S3, Z1, axis=1)
S5=np.append(Z1, Z1, axis=1)
S6=np.append(S5, Muu, axis=1)

C6=np.append(S2, S4, axis=0)
Muu1=np.append(C6, S6, axis=0)

S7=np.append(K11uu, K12uu, axis=1)
S8=np.append(S7, K13uu, axis=1)
S9=np.append(K12uu, K22uu, axis=1)
S10=np.append(S9, K23uu, axis=1)
S11=np.append(K13uu, K23uu, axis=1)
S12=np.append(S11, K33uu, axis=1)

S13=np.append(S8, S10, axis=0)
Kuu=np.append(S13, S12, axis=0)


Duu=(0.02*Muu1)+(0.02*Kuu)

S15=np.append(Fh1, Fh1, axis=0)
Fh11=np.append(S15, Fh1, axis=0)

t1=0.2
h1=0.01
tf1=int(t1/h1)
alpha1=1

I=np.eye(len(Muu1))

Zn=np.zeros((Muu1.shape[0],Muu1.shape[1]), dtype=float)

Khat1=np.append(Zn, -I, axis=1)
Khat2=np.append(Kuu, Duu, axis=1)
Khat=np.append(Khat1, Khat2, axis=0)

Mhat1=np.append(I, Zn, axis=1)
Mhat2=np.append(Zn, Muu1, axis=1)
Mhat=np.append(Mhat1, Mhat2, axis=0)

Zi=np.zeros((Muu1.shape[0],1), dtype=float)
Fhat=np.append(Zi, Fh11, axis=0)


U=np.zeros((Mhat.shape[0],1), dtype=float)

U1=np.zeros((Mhat.shape[0],tf1), dtype=float)


for l in range(1, tf1):
    U=(np.linalg.inv(Mhat+(alpha1*h1*Khat)))@(((Mhat-((1-alpha1)*h1*Khat))@(U))+(h1*((alpha1*(Fhat))+((1-alpha1)*(Fhat)))));

    U1[:,l]=(U).T
    
    
# print(U1)

##################################################################################################################################################

Xx=np.zeros((Muu.shape[0], tf1), dtype=float)

# for k in range(len(Muu)):
#     Xx[k]=U[k]
    

# print(Xx)
    
X2=np.zeros((nnodes,tf1), dtype=float)


p1 = 0 ;
   
for i in range(nnodes):
    if(bnodes[i,0]==1 or choose[i]==1 or choose[i]==11 ):
        # print(i)
        X2[i,:] = np.zeros(tf1) 
    else:
         
         X2[i,:] = U1[p1,:]  
         p1=p1+1
         # print(p)
         

for i in range(nnodes):
       if(choose[i]==2):
           X2[i]=abs(X2[i]);
       else:
           X2[i]=X2[i]        
           

# with np.printoptions(threshold=np.inf):
#     print(X2)        


print(X2[21])   #maximum displacement with negative side
print(X2[89])   #maximum displacement
print("Max displacement at X2[89] in polymer is %f" %(X2[89]))
print("Min displacement at X2[89] in polymer is %f" %(X2[21]))
 



import matplotlib.pyplot as plt 



plt.plot(X2)
 
plt.plot(sigma_th)

plt.plot((U1[89,:]))
plt.plot(T1[98,:])