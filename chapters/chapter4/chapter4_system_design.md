# System Design #

## Architecture Design ##

<!-- [Describe a general architectural solution for your system.  This section must include textual description accompanied with diagrams.] -->

![System Architecture](images/high_level.png){width=50%}

The centerpiece of the project is the Xilinx Artix-7 FPGA. This device performs all of tasks required for logic analysis. The FPGA then stores a capture of the input data in system block memory. 

<!-- The microcontroller is the next major piece of hardware in the design. The Cypress FX-3 microcontroller  This ability to update the firmware is fundamental to the open source principles this project is based on allowing users to improve upon the initial design we release. -->

The final part of the system architecture is the PC user interface which will be displayed on the open source signal UI sigrok. In order to be displayed on sigrok, the USB data transfer has to go through a middleware to parse the data to allow sigrok to display it.

## Interface and Component Design ##

<!-- [Draw the actual component diagram with textual description. This section must include textual description accompanied with diagrams] -->

The design of most logic analyzers is relatively linear. Data comes in, gets processed, stored, and then returned to the requester for analysis. Our project adheres to this design as well. 

![Interface Design](images/flow_diagram.png){width=50%}

The right column of our interface design diagram shows the software components that we used to get the signals to display on pulseView after getting them from our device. The middle column shows the hardware and software components needed to read in the logic signals and send the data the computer. Objects in blue are components that we designed and objects in green are components that are provided through third party software, or from our hardware manufacturers. 

## Structure and Logic Design ##

<!-- [Present the detailed structure and logic design for your hardware/software components and processes. This section must include textual description accompanied with diagrams. If scientific or mathematical fundamentals are used for your project algorithm, specify what kind of formula or theory has been applied.] -->

As discussed in the previous section, our project has three main parts, the data acquisition and storage done on the FPGA, the data transfer done on the USB 3.0 controller, and the PC interface that takes that data and presents it to sigrok for user analysis. 

The logic signals coming in from the device under test are immediately sent into a trigger module that checks to see see if the device is ready to start capturing data. If the device is ready, it captures the data from the lines and stores it into a buffer. The FPGA then grabs data packets from the buffer and stores them along with the time at which they were captured, usually in microseconds after acquisition started. When the acquisition is done, the data is then sent to the USB controller to send the data to the PC.

The USB controller hardware takes care of all of the protocol handling required to get the data transferred to the PC, and the drivers provided by the manufacturer for various operating systems handle the receiving of the data packet as well. The way the data is packaged before sending it is the way the data comes out on the host machine. The data is then sent to an interface driver that converts the data into signals readable by sigrok.

The data translation is well laid out in sigrok's documentation. We also have a separate control program that interfaces with sigrok and pulseView that allows us to set up acquisition and trigger settings in the software and request a capture. These functions are all done inside of pulseView, facilitated by our custom interface driver. 

## Design Constraints, Problems, Trade-offs, and Solutions ##

### Design Constraints and Challenges ###

<!-- [Present your design constraints in different perspectives, such as economic, resources, society and environment, hardware/software, mathematical/scientific theories and safety and reliability.] -->

The main constraint we dealt with in this project was keeping the cost of manufacturing down. In order for this to be a successful project, our design must be cost competitive to other devices that are already out on the market. This constraint is defined by the features implemented. Some of the features we designed around were USB 3.0, 100 MHz sampling, and a large amount of data storage. For some of these constraints the solution was fairly obvious, but for others we were limited by fundamental laws of physics.

Due to this project being a hardware project, we needed to be cognizant of component price. If our design was reliant on a particular component that we cannot afford to purchase, then we would have failed at designing our project. We also needed to make sure that the components we designed into our project had sufficient availability to allow for anyone in the future to take our designs and reproduce the logic analyzer.

The software and firmware that we produced for this project are licensed in an appropriate open source license. In this context, appropriate means that it complies with all of the open source code we included in our software, and that also aligned with our ambitions for the project. If we chose to license our software with a license that was incompatible with other code we could face legal issues. If we chose a license that is too restrictive we could detract contributors to our project.

The tools we used to design our software, firmware, and hardware all needed to be available to the general public for free. The tools to contribute to this project do not cost contributors anything. We also aimed to use as much open source software as possible to guarantee the tools we used will continue to be free in the future.

### Design Solutions and Trade-offs ###

<!-- [Document your approaches to cope with the given constraints. Present your design trade-off decisions and solution selections to deal with these constraints and problems and challenges.] -->

We decided to support the USB 3.0 protocol which allowed us to communicate with a host computer ten times faster than USB 2.0. While the USB controller we used is more expensive than a USB 2.0 controller, the speed that USB 3.0 provided is worth more than the extra cost. USB 3.0 also allowed for different data transfer modes that both increased performance of the device, and increased the maximum capture length. We also looked into using the much higher bandwidth format, Thunderbolt. The cost to implement would have been too high and the skills necessary to accomplish this would have been well outside of our current skills. This communication protocol is also only implemented on more professional hardware using Intel CPUs. This would have limited the total marketability of our project by a drastic amount, thus we decided to not go with this communication protocol.

We chose to target the sampling speed of 100 MHz because that is similar to other devices on the market with similar hardware. We looked into supporting higher sampling speeds such as 500 MHz, but if we were going to support these speeds, we would have needed to design a much more robust system. Also, the components we would have needed to use would have be more expensive.

We decided to design our project around the Xilinx Artix-7 and the Cypress FX-3 due to their low costs with the features that we need. We also all had a Xilinx Artix-7 Development board that we used for our course work at San Jose State. The Artix-7 is one of Xilinx's value optimized FPGAs, which gave us a lot of performance for a relatively low per unit price. Using a Xilinx FPGA also allowed us to use many of Xilinx's IPs right out of the box, without having to write our own from scratch. We did look into using other FPGA manufacturers, but none of them had a product that was close to the performance of our Artix-7 for the price were aiming to achieve.

The Cypress FX-3 is another important pillar of our design, allowing for USB 3.0 communication. We chose the FX-3 in particular because we were unable find any other USB 3.0 peripheral controllers that also had as much documentation and application notes as the FX-3 had. We also could not find a competitor that could compete on price. While the cost of this controller is high in comparison to USB 2.0 controllers, it is still significantly less than other USB 3.0 controllers.

In terms of keeping component costs down and choosing components that were readily available, choosing the Artix-7 and FX-3 were easy decisions. They are some of the lowest cost options in their markets and neither of them were marked as end of life. We also made sure to check component suppliers such as Digikey and Mouser to make sure that there are sufficient quantities available for purchase.

For the tools we will be using in this project, we used Xilinx's free Vivado development environment to develop for the Artix-7 and to develop for the Cypress FX-3, we used Cypress’s free EZ-USB suite. There are no real alternative for either of these suites and we had to use them to develop for our chosen components. We cannot guarantee that these tools will be available in the future, but we could reasonably assume that they will continue to be available and free as long as these companies exist.
