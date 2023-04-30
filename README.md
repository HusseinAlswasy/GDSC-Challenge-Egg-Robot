# Table of Contents

* [Introduction](#Introduction)
* [Problem](#Problem)
* [Directory Strategy](#Directory_Strategy)
* [Solution](#Solution)
    * [Algorithm 1 - Static Policy](#Alternative_1)
        * [Training Phase](#Training_Phase)
        * [Playing Phase](#Playing_Phase)
    * [Algorithm 2 - Dynamic Policy](#Alternative_2)
        * [Description](#Description_1)
    * [Algorithm 3 - Extended Dynamic Policy](#Alternative_3)
        * [Description](#Description_2)
* [Conclusion](#Conclusion)
* [Appendix A - Code and Documentation](#Appendix_A)
* [Appendix B - Instructions to Run the Code](#Appendix_B)
* [Appendix C - Video](#Appendix_C)

<a id='Introduction'></a>
# Introduction

After ten weeks of learning additional Artificial Intelligence techniques, which cover more traditional branches of AI, such as research, planning, knowledge, logic and reinforcement learning, we had the opportunity to put what we learned into practice. After interesting brainstorming and group discussions, we decided to go ahead with a project using reinforcement learning. We found a challenging project and the right size to carry out a solution in a reasonable time and resources. We then put our efforts into defining the problem, defining workarounds, coding and testing our algorithms, evaluating the results and preparing for the conclusion. Here's what we did.

<a id='Problem'></a>
# Problem

### Problem statement: Find the path for a robot to reach an end point (goal state) while avoiding randomly generated obstacles in a 2D space, using reinforcement learning methods.

<div align="center">
<img src="https://github.com/ravasconcelos/rl_obstacle_avoidance/blob/master/notebook/images/Problem Identification.jpg" alt="Drawing" style="width: 800px;"/>
<center><b>Figure 1. Problem Statement</b></center>
<center><i>Source: Term Project</i></center>
<center><i>.</i></center>
</div> 
 

We found an implementation of this challenge that uses other techniques, instead of reinforcement learning. Here is the link to the article that inspired us on this project. 

https://bayesianadventures.wordpress.com/2015/08/31/obstacle-avoidance-for-clever-robots/

For this project, the environment created by the original simulator is called "Robot World".

<div align="center">
<img src="https://github.com/ravasconcelos/rl_obstacle_avoidance/blob/master/notebook/images/bayesian_giphy.gif" alt="Drawing" style="width: 800px;"/>
<center><b>Figure 2. Original Bayesian algorithm simulation</b></center>
<center><i>Source: Term Project</i></center>
<center><i>.</i></center>
</div> 

In this Robot World, you can move around by clicking on the step button. After a new step, the robot will be in a new state. You can add new obstacles during the journey dynamically. The objective is to reach the goal point (G) without colliding with an obstacle. You can also define the starting and goal points. 

The original code implemented three important classes: Robot, Sonar and Sonar_Array. The first one controls the robot, its position, its movements, etc. The other two implement the controls to obtain information from all the sensors and allows the robot to uderstantd if there are obstacles in close range, define the alerts and define the actions that control whether the robot should continue on its path or need to make a turn to avoid an obstacle. This part of the code is where our main problem lies. 

- Can we use reinforcement learning to define an optimal policy to guide the robot's actions to avoid the obstacles and reach the goal? 
- Can we replace the original algorithm by a more efficient RL algorithm or RL is not the best solution for this problem? 
- Can we extrapolate this problem to a drone or to a more dynamic environment ? 

These were some questions that guided our project. 

The original code and simultador can be see and run in this link: <br>
http://www.codeskulptor.org/#user40_EEIxkOtKog_1.py

     
To effectively use the original code and simulator, we made some changes and adapted the Robot World. Our goal was to focus more on reinforcement learning algorithms than on other parts of the code. 
<div align="center">
<img src="https://github.com/ravasconcelos/rl_obstacle_avoidance/blob/master/notebook/images/new_simulator.png" alt="Drawing" style="width: 800px;"/>
<center><b>Figure 3. New Robot World Simulator</b></center>
<center><i>Source: New Robot World from Term Project</i></center>
<center><i>.</i></center>
</div> 

<a id='Directory_Strategy'></a>
# Directory Strategy

These are the repository directories and what you can find into each one:
1. root: readme file, constants and test data generator;
1. bayesian: refactored code used as base line for a robot able to avoid obstacles using sensors and math calculations;
1. dynamic_policy: reinforcement learning approach to solve obstacle avoidance problem using Monte Carlo policy dynamically calculated;
1. extended_dynamic_policy: reinforcement learning approach to solve obstacle avoidance problem using Monte Carlo policy dynamically calculated in a 5x5 grid of elements with 50x50px long;
1. naive: a robot that moves towards the goal whithout trying to avoid obstacles. Used for performance comparisson.
1. notebook: report file in a Jupyter Notebook file, presentation in pdf and ptt formats
1. static_policy: reinforcement learning approach to solve obstacle avoidance problem using Monte Carlo policy statically calculated;

# Solution

We tried different alternatives to solve the problem. To effectively use the original code and simulator, we made some changes and adapted the Robot World. Our main goal was to focus more on reinforcement learning algorithms than on other parts of the code, but we also adapted the original code to better compare the results of our alternatives. Below you can see our solution alternatives. 

<a id='Alternative_1'></a>

### Training Phase


To find an optimal policy to help our robot reach its goal without hitting obstacles, we made an operational decision and divided the New Robot World (500 x 500) in 100 4 x 4 position grids. With that, we created a strategy to find the best policy in a smaller grid, considering that we could have 15 different positions for one or two obstacles. We ran the Monte Carlo method to simulate thousands of episodes and value iteration to find optimal q-value for every state in 4 x 4 grid and determine the action based on epsilon soft policy algorithm. The generated master policy is a dictionary of states and actions for all 100 grids. 

<div align="center">
<img src="https://github.com/ravasconcelos/rl_obstacle_avoidance/blob/master/notebook/images/Training Phase.png" alt="Drawing" style="width: 800px;"/>
<center><b>Figure 5. Static Policy Algorithm - Training Phase</b></center>
<center><i>Source: Term Project</i></center>
<center><i>.</i></center>
</div>


After that initial phase to define master policy, we just copied the print of policy to the code that implement the playing stage which was adapted to run the New Robot World. Below you can find some parts of the code which we use to build our Master Policy. 



```

<a id='Playing_Phase'></a>
### Playing Phase

With the Master Policy trained, we adapted the original code of the Robot World to create our New Robot World. We included the Master Policy as a dictionary considering States and Actions. We also created two functions: find_location_onMap and policy_finder, which are use to obtain information of the robot and obstacles within a specific grid and define the optimal action according the these positions. 

Within the code where the original program understands what action the robot should take when it discovers an obstacle, we changed the code to call our policy_finder fuction, which find the robot and obstacle locations, and return the action that the robot must take, 
according to our Master Policy. 

  
<div align="center">
<img src="https://github.com/ravasconcelos/rl_obstacle_avoidance/blob/master/notebook/images/Algorithm 1.png" alt="Drawing" style="width: 800px;"/>
<center><b>Figure 6. Static Policy Algorithm - Playing Phase</b></center>
<center><i>Source: Term Project</i></center>
<center><i>.</i></center>
</div> 

You can now play with an initial version of the New Robot World by clicking on the step button and adding new obstacles. 

Here is the link to the New Robot World:

http://www.codeskulptor.org/#user47_JJSgNIMtcq_0.py

Following are parts of the code that were inserted or updated int the original simulator for the New Robot World.







```

Here is a simulation of our static policy algorithm

<div align="center">
<img src="https://github.com/ravasconcelos/rl_obstacle_avoidance/blob/master/notebook/images/bayesian_static_giphy.gif" alt="Drawing" style="width: 800px;"/>
<center><b>Figure 7. Static Policy simulation</b></center>
<center><i>Source: Term Project</i></center>
<center><i>.</i></center>
</div> 

The results of this algorithm were not good enough. We had too many assumptions like fix start and end points, no more than two obstacles per 4 x 4 grids, two different phases (training and playing) and we could only play the game online by clicking on the step button.  

<a id='Alternative_2'></a>
## Algorithm 2 - Dynamic Policy

For our second algorithm, we decided to keep the same strategy as algorithm 1 of dividing the original world of 500 x 500 into 100 4 x 4 grids. In this algorithm, we allowed dynamic start and end points and no fix number of obstacles within a 4 x 4 grid. 

<a id='Description'></a>
### Description

Following is the definition of the Markov Decision Process (MDP): 

States: all possible states within a 4 x 4 grid with 0 to 15 obstacles<br>
Start State: dynamic, defined when the episode starts<br>
Actions(s): Up, Down, Right and left<br>
T(s'|s; a): probability of reaching s' if action a is taken in state s = 0.95 (some uncertainty)<br>
Reward(s; a; s0): -1 without obsctacle, -5 when there is an obstacle<br>
End State: dynamic, defined when the episode starts <br>
Discount factor = 0.6<br>

To compare the performance to the original code and our solution, we converted the original code into Python 3, broked it in 4 Python programs to implement the three classes (Robot, Sonar and Sonar_Array) and utilitarian functions. This was important to run multiples episodes of the Robot in a batch mode. 

Our reinforcement learning strategy is now considering a dynamic policy. We implemented just one phase (playing), starting every episode without a policy. For every step (action) taken by our robot in the New Robot World, if a policy is not available for that state, a new policy is created using the same Monte Carlo method used in the alternative 1. Then the policy for that state is  stored. If the robot enters a state where a possible had been previously defined, then the robot uses that policy. The array with the policies is being appended as long as the robot moves step by step until it reaches the goal. 


<div align="center">
<img src="https://github.com/ravasconcelos/rl_obstacle_avoidance/blob/master/notebook/images/Algorithm 2.png" alt="Drawing" style="width: 800px;"/>
<center><b>Figure 8. Dynamic Policy Algorithm</b></center>
<center><i>Source: Term Project</i></center>
<center><i>.</i></center>
</div> 


Our new robot, supported now by reinforcement leanirng instead of bayesian methods, can run in the same graphical interface than the original robot. However, to compare the performance of the two robots, we create a code to run both robots simultaneous, with the same number and position of obstacles, and to capture the number of steps each robot takes to reach the goal after 200 episodes. Then, we can plot two graphs to compare the accuracy and effort of both robots. 



```

Here is a simulation of our dynamic policy algorithm. 

<div align="center">
<img src="https://github.com/ravasconcelos/rl_obstacle_avoidance/blob/master/notebook/images/dynamic_giphy.gif" alt="Drawing" style="width: 800px;"/>
<center><b>Figure 9. Dynamic Policy simulation</b></center>
<center><i>Source: Term Project</i></center>
<center><i>.</i></center>
</div> 

We achieved a better performance with the dynamic approach, but we had an intuition that our 4 x 4 grid was too small and we could be missing something important. We decided to test a third algorithm to try to get new answers for the problem. 

<a id='Alternative_3'></a>
## Algorithm 3 - Extended Dynamic Policy

For our third algorithm, we decided to keep the same strategy as algorithm 2 of dividing the original world of 500 x 500, but now we have choose dynamic 250 x 250 pixels grids. The agent would be always in the middle of the grid to define the police. In this algorithm, we allowed dynamic start and end points and no fix number of obstacles within a 250 x 250px grid. 

<a id='Description'></a>
### Description

Following is the definition of the Markov Decision Process (MDP): 

States: all possible states within a 20 x 20 grid with 0 to 400 obstacles<br>
Start State: dynamic, defined when the episode starts<br>
Actions(s): Up, Down, Right and left<br>
T(s'|s; a): probability of reaching s' if action a is taken in state s = 0.95 (some uncertainty)<br>
Reward(s; a; s0): -1 without obsctacle, -5 when there is an obstacle<br>
End State: dynamic, defined when the episode starts <br>
Discount factor = 0.6<br>

Our reinforcement learning strategy is now considering a dynamic policy. We implemented just one phase (playing), starting every episode without a policy. For every step (action) taken by our robot in the New Robot World (250 x 250px), if a policy is not available for that state, a new policy is created using the same Monte Carlo method. Instead of Monte-carlo in a grid of 4x4 , we are calculating a grid of 5x5. The Monte Carlo is much more expensive because the grid is larger. Then the policy for that state is  stored. If the robot enters a state where a possible new state had been previously defined, then the robot uses that policy. The array with the policies is being appended as long as the robot moves step by step until it reaches the goal.



```

Here is a simulation of our extended dynamic policy algorithm. 

<div align="center">
<img src="https://github.com/ravasconcelos/rl_obstacle_avoidance/blob/master/notebook/images/extended_dynamic_giphy.gif" alt="Drawing" style="width: 800px;"/>
<center><b>Figure 10. Extended Dynamic Policy simulation</b></center>
<center><i>Source: Term Project</i></center>
<center><i>.</i></center>
</div>

This algorithm was not as good as the dynamic policy, but was an important step in our learning process to understand the possibilities that reinforcement learning can provide us to solve problems. 


# Conclusion

The project offered us a great opportunity to put into practice what we learned during the course. We tried different approaches and ended up with the feeling that there are many additional alternatives and more experimentation that we can do. The following are some lessons learned and future work that can be done to improve our solution.

Lesson learned:
we should not solve continuous problems using discrete solutions


Possible extensions of the work include :
1. Use deep learning – q network to further increases the accuracy for the path navigation as done in the snake game (reference : https://github.com/maurock/snake-ga)
2. Use deep deterministic policy gradient for solving the problem in continuous domain (reference : https://www.youtube.com/watch?v=PngA5YLFuvU&t=187s)

<div align="center">
<img src="https://github.com/ravasconcelos/rl_obstacle_avoidance/blob/master/notebook/images/robot_movements.png" alt="Drawing" style="width: 800px;"/>
<center><b>Figure 16. An example with reinforcement learning</b></center>
<center><i>Source: Term Project</i></center>
</div> 

<a id='Appendix_A'></a>
# Appendix A - Code and Documentation

All the code prepared for this project is available on Github. Here is the link for the project. 

https://github.com/ravasconcelos/rl_obstacle_avoidance

Description:

In the root you can find the code to run the algorithms. 

Folders: 
1. notebook - this report and presentation
2. bayseian - Original Bayseian code transformed to Python 3 and prepared to run in a bacyh mode
3. static_policy - Code with implements the Static Policy algorithm
4. dynamic_policy - Code with implements the Dynamic Policy algorithm

<a id='Appendix_B'></a>
# Appendix B - Instructions to Run the Code

The instructions were written you are running Windows 10, WSL and bash. The commands may be different for other OS and terminal tool.
Before you start:
1. Ensure you have Python 3.7.7 installed
1. Install the libraries (pip install <library>):
    * matplotlib      3.3.0
    * numpy           1.19.1
    * SimpleGUITk     1.1.3
    * if needed, see the full list of libraries in the file pip_list
1. If running in WSL you may need to install Xming in order to use the SimpleGUITk    
    1. https://sourceforge.net/projects/xming/
    1. export DISPLAY=localhost:0

How to run the code:
1. Clone the GitHub repository
    1. git clone git@github.com:ravasconcelos/rl_obstacle_avoidance.git
    1. cd rl_obstacle_avoidance
1. Bayesian:
    1. cd bayesian
    1. to play using the UI:
        1. python play_baysian_obs_avoid.py
    1. to run the batch test:
        1. python play_baysian_obs_avoid.py
1. Dynamic Policy:
    1. cd dynamic_policy
    1. to play using the UI:
        1. python play_obstacle_avoidance.py.py
    1. to run the batch test:
        1. python run_dynamic_policy.py
1. Extended Dynamic Policy:
    1. cd extended_dynamic_policy
    1. to play using the UI:
        1. python play_obstacle_avoidance.py.py
    1. to run the batch test:
        1. python run_extended_dp.py.py        
