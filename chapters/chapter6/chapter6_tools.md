# Tools and Standards #

## Tools Used ##

<!-- [This section specifies the selected hardware/software tools for use. Please specify why you selected these tools, and where and how these tools were used.] -->

Due to this project focusing on open source and contributing to the open source ecosystem, we also heavily used open source tools to verify our work. From the version control software we used, to the hardware verification we did.

### Software ###

#### Git ####

Source code version control is an incredibly important part of every project, and for our projected we decided to go with git. Git is the most used version control software in the open source community and is widely used in industry as well. It only made sense to use something that other people would be familiar with using so that in the future they would be able to contribute to the project with very little friction. 

#### GitHub ####

Many open source projects are hosted on GitHub, and it made sense to also use them for hosting our senior project. GitHub allowed us to host multiple remote git repositories. GitHub also has project management which we used for tracking our progress and milestones. This project management integrates directly with our git commits which made keeping track of progress even easier. 

#### Cocotb ####

In order to verify our RTL design on the FPGA, we used an open source unit testing framework. This unit testing framework allowed us to write our tests in python and directly interface with our Verilog design files. The results of the tests are output in a standard xUnit xml format, which can be parsed by many testing software suites.

#### Icarus Verilog ####

We used an open source RTL synthesizer with Cocotb for the testing of our design. Cocotb requires a synthesizer to test the design and run the python tests, and Icarus Verilog is the only open source and free synthesizer. 

#### Jenkins ####

Jenkins is a continuous integration service that we used to constant check test our project as we made iterations. We configured Jenkins to build and test our project every time we pushed a commit to GitHub, and report back to GitHub if that commit passed or failed. Jenkins was also configured to show which tests passed and failed.

#### Vivado ####

Vivado is Xilinx's integrated development environment which is used to develop for their FPGAs. We used Vivado for generating bitstreams used to program our FPGA development board. There are no open source bitstream generation tools available for use with Xilinx's products, but Xilinx does have the only free generation tool. With Vivado, we were also able to see the utilization of our FPGA, and design around the constrains built into the hardware.


### Hardware ###

#### Logic Analyzer ####

In order to test our own logic analyzer out, we needed to test it against a known working logic analyzer and compare the input results. We used two other open source logic analyzers to accomplish this, the Open Bench Logic Sniffer and the DSLogic Pro. Both of these devices work with Sigrok which means we were able to test all three at the same time. This made it much easier to track down issues in our design.

#### Oscilloscope ####

We also used an oscilloscope for high speed timing and making sure that our logic analyzer was reading the correct inputs. Using an oscilloscope allowed us measure input waveform times and manually measure what the expected output should be based on the input signal. This was a much more theoretical and hands on approach to testing that our other methods.

## Standards ##
<!-- [This section describes the standards you used in your project. These standards could be related to hardware/software system and its components, requirements, design, interface, testing, protocols, documentation, and so on.] -->

### Version Control ###

We used version control for everything in our project. All of our code has been in git since the beginning as well as our documentation. We specifically used markdown syntax to write out documentation so that the documentation could be viewable on GitHub and that we could easily track our changes. 

### Test Driven Development ###

Unit testing was another important part of this project, and accounted for the second largest amount of time spent. By designing our project to use unit testing from the start, we were able to design our features by first writing tests of what we wanted the output to look like, and then developing the feature to pass the test. 

### Continuous Integration ###

By developing our project using test driven development, we needed some way to constantly and automatically test our code base. Continuous integration does exactly that which is why we developed the tools to continuously integrate our code base and return the tests results directly to GitHub. 


<!-- ### Black box testing ### -->
