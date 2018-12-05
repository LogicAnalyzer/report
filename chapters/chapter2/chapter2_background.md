# Background and Related Work #

## Background and Technologies ##

<!-- [Provide the necessary background of this project, including concepts and knowledge (e.g design patterns, asynchronous programming, project estimation, scientific and mathematical theories), along with technologies (e.g. PHP, MySQL). In addition, provide an updated table of courses you have taken that you applied to the project and how you applied them.] -->

While going through our course work at San Jose State, we have used logic analyzers for various projects and assignments. We were not satisfied with the performance and user experience with any of the analyzers we used, so we decided it would be a good project to build our own to our specifications.

| Course 									| Description | 
| --- 										| ------- |
| Digital Design I 							| This course taught us the basics of digital logic and was heavily hands on. This was also our first experience using logic analyzers. |
| Digital Design II 						| This course was our first Verilog course which introduced us to our development board, as well as the concepts of RTL design. |
| Computer Architecture and Design 			| This was our capstone RTL design course, having us create a reduced instruction set MIPS I CPU from scratch. |
| Microprocessor Design 					| This course was our first Microprocessor course, where we spent hands on time interfacing with a microprocessor. During this time we started to notice the downfalls of current logic analyzers on the market.|
| Real-Time Embedded System Engineering 	| This course was our capstone Microprocessor course, teaching the fundamentals of good system design, which has helped us in designing our system. |
| Software Engineering I 					| This course introduced us to various software engineering topics including project management, which has helped us a lot on this project. |
Table: Relevant Courses

Verification methodologies and tools, such as UVM and SystemVerilog, were excellent in testing the many modules required in the FPGA design. They were also useful to help speed the verification process along as development time is extremely short.

On the user’s side, the Sigrok interface and system drivers have been created to allow the client computer to recognize and connect via USB to the logic analyzer. The software/hardware integration will be a major hurdle, especially at the target speeds. Initially using standard UART over USB communication on the development board will give us a working model that we will be able to interface to the Cypress FX-3 controller at a later time.

<!-- ## Literature Search ##

Verification of digital designs requires specialized tools called logic analyzers. Logic analyzers allow for multiple digital signals to be read at the same time which allows for multiple signal communications protocols to be debugged. Through our research, we learned about an important limiting theorem, the Nyquist rate [@Nyquist1928], and how that will determine our maximum data rate. State of the art logic analyzers can read multiple gigabytes of data per second across tens of different digital signals. Our project will not be cutting edge. We will be creating a budget specific, entry-level logic analyzer that will read 16 digital signals and send that signal to a personal computer to be displayed.

Through our research we have found books and articles discussing printed circuit boards, low-voltage high-frequency digital signaling, USB 3.0 test systems, FPGA data acquisition. These articles and books have helped us solidify our understanding of these systems, and we will be using them continuously in the design and implementation of our project. We will inevitably need to research more on specific topics as we get further into the design cycle. 
-->

<!-- [Similarly, present your updated literature search adding to those that you explained in Chapter 1 of 195A workbook.] --> 

## State-of-the-art ##

<!-- [A smaller, one page summary follows the literature review. Please refer to ‘State-of-the-Art Summary’ section in Chapter 1 of 195A workbook. You should provide an updated state-of-the-art summary here.]  -->

The state of the art logic analyzers used today in industry can capture millions of samples across hundreds of channels or read signals changing at over 50 GHz. These logic analyzers are stand-alone units that have dedicated general purpose computers built into them running standard operating systems such as Microsoft Windows. Research that is currently being done in this field is mostly on increasing the speed of capture in these devices. We haven't been able to find many academic papers on this subject, which leads us to believe that the research is being done in-house and being kept as a trade secret. These devices are so specialized that there are only two companies producing high-speed logic analyzers, with one of them being the clear market leader. Performance increases in this specific market segment come from tangential research. For example, increased silicon performance for high-speed radio frequency signaling could be directly applied to the application specific integrated circuits used in these products.

The products that are competing at the top of the market are being sold for over 50 thousand dollars. This is due to the thousands of engineering hours required to design and implement these high-speed devices, and the extremely low volume that these devices are produced in. The electronics industry uses these devices to measure and test new products and designs. Without these tools, the speed increases that we have seen every year for the past thirty years would have been impossible. New designs must be verified before they are released for production, and as speeds have increased capturing the signal has become more complicated.

The Nyquist-Shannon sampling theorem states in order to accurately read an electronic signal at a given speed, you need to sample that signal at twice the speed[@Nyquist1928]. This speed requirement means that the industry needs to have equipment that can capture at least twice the speed they are designing at. This problem becomes a chicken and egg situation, where the current equipment needs to be designed, but it can't be tested with any of the equipment that is currently available.
