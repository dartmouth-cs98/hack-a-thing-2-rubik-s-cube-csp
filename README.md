# hack-a-thing-2-rubik-s-cube-csp
hack-a-thing-2-rubik-s-cube-csp created by GitHub Classroom

####README

###Project Description

  In this project I attempted to build a program that modeled a Rubik's Cube as a constraint satisfaction problem and then
  attempted to solve this problem via hillclimbing.  In the final version their are three methods used by the program to attempt
  to solve the problem.  One is a search which iterates over the space that exists three moves down from the current state and
  selects the set of moves that results in the highest amount of constraints being satisfied.  The second is a search identical to the
  first except that instead of choosing the move set that will result in the most constraints being satisfied, this search
  greedily choose the set of moves that will result in the most new constraints being satisfied.  The third method is simply
  a set of two randomly chosen moves.  This is done to help the program break out of local maxima it may become trapped in.
  
  ###What I Learned
  
  I undertook this project knowing that a Rubik's Cube is not well suited to being solves as a CSP, since it is somewhat resistant to
  hillclimbing methods and there is no way to check for things like arc consistency since all states of a Rubiks Cube can 
  lead to a correct state.  I did this because I wanted to attack the challenge as a sort of mini research project where I 
  would attempt to optimize a CSP approach until it could solve the cube.  Over the course of my effort I learned about incorporating
  different methods, in this case a tree search, into the CSP problem so that I could progress further.  I also learned about the 
  value of data gathering, while I did not have the time or resources to create explicit tables mapping how my success changed as 
  I altered different variables, I was able to get a a general idea of how they were related from observation.
  
  ###What Did Not Work
  
  Unfortunately I was not able to get the program to fully solve the problem.  In my system there are a total of 2916 constrainst that need
  to be satified for the cube to be fully solved.  The furthest my program ever got was 2556 constraints satisfied.  For context,
  the randomly mixed cubes tend to have around 2000 constraints satified.  While I never got close to a full solution, my score
  did imporve over time, (my first attempts never got further than around 2350 contraints).  There were two possible solutions
  I thought of but did not have the time or equipment to test.  One was simply expand the search space more than 3 moves down.  
  I could not implement this with my computer as any search past three moves became intractible.  My other thought was to break the 
  problem into parts.  The most common algorithms to solve a Rubik's Cube break the problem into distinct stage, so I thought
  it might be possible to model each stage as a seperarte CSP with its own contraints, and see if the stages could be progressed 
  through in that manner
