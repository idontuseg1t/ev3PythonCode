# Logs


Main Reference: python-ev3dev-lang Documentation -  https://ev3dev-lang.readthedocs.io/projects/python-ev3dev/en/ev3dev-stretch/index.html <br>

30/08      
       Started Robot, missing some pieces <br>
       Cloned git repo of demo scripts <br>
       LED, sound tested and worked <br>
       
01/09      
      Completed base robot <br>
      Touch sensor added <br>
      Colour sensor added <br>
      Able to report colour <br>

02/09    
      Attempted to get gyro sensor to work. <br>
      Robot keeps turning after it has passed the specified degrees. <br>
      Working on program where robot goes around an object when it detects one in front of it. <br>
      Next lesson: will keep trying to find a solution for above problem. <br>
      
06/09  
      Found solution for gyro sensor: it was put on the wrong way. <br>
      Robot now spins around the specified degrees. <br>
      Robot now attempts to go around an object detected using the touch sensor with the help of the gyro sensor. <br>
      Made similar program to the one above but with ultrasonic sensor.<br>
      Robot tries to go around when it detects an object 6cm in front of it. <br>
      All available sensors have now been tested. <br>
      Next lesson: more work on the gyro sensor and maybe rebuilding robot. <br>
      also maybe next lesson: getting the servo motor to work. <br>
      
08/09  
      testing gyro sensor again <br>
      beginning to make script so robot can follow a line <br>
      basic script created: followLine.py <br>
      A lot can go wrong with the script above <br>
      Improvements to be made next lesson <br>

09/09  
       Still working with follow line script <br>
       Created square script and straight line script <br>
       still problems with follow line <br>
       considered script that utilises two colour sensors <br>
       
13/09  
       Lesson with sub teacher <br>
       no access to robots <br>
       cabinets can't be opened <br>
       found information relating to brick-to-brick communication and remote control <br>
       Using a brick to control another brick is known as "daisy chaining" <br>
       SSH Control: https://www.ev3dev.org/projects/2018/08/14/EV3D4-ssh-control/ <br>
       Connecting to computer via bluetooth: https://www.ev3dev.org/docs/tutorials/connecting-to-the-internet-via-bluetooth/ <br>
       Brick-to-brick info from offical doc: https://ev3dev-lang.readthedocs.io/projects/python-ev3dev/en/ev3dev-stretch/rpyc.html#networking <br>
       Other info regarding official ev3 client (NOT ev3dev related): https://bricks.stackexchange.com/questions/2483/communication-between-two-ev-3-bricks <br>
       RPyC (program for remote communication installed on ev3dev) doc: https://rpyc.readthedocs.io/en/latest/ <br>
       
15/09  
       Begin to implement ssh control for the robot <br>
       base script downloaded and modifications made to suit needs (see sshTest.py for details) <br>
       Remote control succeeded while robot was wired to the computer <br>
       wireless remote control to be implemented next <br>
       
16/09
       attempted to work on wireless remote control using ssh <br>
       encountered problems with bluetooth <br>
       attempted to change bluetooth client on host - did not work <br>
       Connection is shown to be active on the robot but it still does not respond <br>
       pinging websites does not work either <br>
       continue working next lesson <br>

07/10
       attempting to connect to bluetooth again <br>
       gave up on using gui, switched to just using the command line <br>
       success on the first try (this is why command line is superior to gui) <br>
       ssh connection established, able to remote control robot wirelessly <br>
       
       
