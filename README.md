# SCA-optimized-Microgripper
With the development of miniaturization technology, micro-electromechanical system (MEMS) electrothermal microgrippers have been widely used owing to their compact size, ease of manufacturing, and low production cost. Since most of these systems are governed by partial differential equations (PDEs), modeling of microgrippers poses a significant challenge for designers. To reduce the overall computational complexity, it is common practice to model the microgripper system using the finite element method (FEM). During the design process, the geometric and analytical properties of the microgripper influence the system dynamics to a great extent, and this work focuses on studying the effects of such parameter changes. In low-voltage applications, the performance of the microgripper is influenced by the geometrical variations, and the air gap. Hence, for the modeling of the microgripper, actuator arm lengths, and the gap between the arms are chosen as the two main geometric design parameters, while the input current density is considered as the analytical design parameter. In this work, the optimized design parameter values for maximum possible displacement are obtained with the use of sine cosine algorithm (SCA). Furthermore, an averaging operation is proposed for efficiently designing the MEMS electrothermal microgripper, and the efficacy of the proposed design methodology is demonstrated through simulation studies. [DOI: 10.1115/1.4052668]

Download both Gmsh and the SDK with pip: 'pip install --upgrade gmsh' 
 
Woo hoo!!!!

Now you are all set to run this code. 😅

project_micro gives the values of displacement and generated temperature for one parameter input (Length of the actuator) through calling_proj

project_micro2 gives the values of displacement and generated temperature for two parameters input (Length and width of the actuator) through calling_proj

SCA_Microgripper gives the optimized values of the Microgripper parameters
