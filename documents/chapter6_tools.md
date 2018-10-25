# Tools and Standards #

## Tools Used ##

<!-- [This section specifies the selected hardware/software tools for use. Please specify why you selected these tools, and where and how these tools were used.] -->

Due to this project focusing on open source and contributing to the open source ecosystem, we also heavily used open source tools to verify our work. From the version control software we used, to the hardware verification we did.

### Git ###

Source code version control is an incredibly important part of every project, and for our projected we decided to go with git. Git is the most used version control software in the open source community and is widely used in industry as well. It only made sense to use something that other people would be familiar with using so that in the future they would be able to contribute to the project with very little friction. 

### Github ###

Many open source projects are hosted on Github, and it made sense to also use them for hosting our senior project. Github allowed us to host multiple remote git repositories. Github also has project management which we used for tracking our progress and milestones. This project management integrates directly with our git commits which made keeping track of progesses even easier. 

### Cocotb ###

In order to verify our RTL design on the FPGA, we used an open source unit testing framework. This unit testing framwork allowed us to write our tests in python and directly interface with our verilog design files. The results of the tests are output in a standard xUnit xml format, which can be parsed by many testing software suites.

### Icarus Verilog ###

We used an open source RTL synthesizer with Cocotb for the testing of our design. Cocotb requires a synthezer to test the design and run the python tests, and Icarus verilog is the only open source and free synthezier. 

### Jenkins ###


### Vivado ###


## Standards ##
<!-- [This section describes the standards you used in your project. These standards could be related to hardware/software system and its components, requirements, design, interface, testing, protocols, documentation, and so on.] -->

\newpage