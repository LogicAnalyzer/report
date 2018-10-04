# System Design #

## Architecture Design ##

<!-- [Describe a general architectural solution for your system.  This section must include textual description accompanied with diagrams.] -->

![System Architecture](images/high_level.png){width=50%}

The centerpiece of the project is the Xilinx Artix-7 FPGA. This device performs an array of tasks required for logic analysis. The FPGA then stores a capture of the input data. 

The microcontroller is the next major piece of hardware in the design. The Cypress FX-3 microcontroller  This ability to update the firmware is fundamental to the open source principles this project is based on allowing users to improve upon the initial design we release.

The final part of the system architecture is the PC user interface which will be displayed on the open source signal UI Sigrok. In order to be displayed on sigrok, the USB data transfer will have to go through a middleware to parse the data to allow Sigrok to display it.

## Interface and Component Design ##

<!-- [Draw the actual component diagram with textual description. This section must include textual description accompanied with diagrams] -->

The design of most logic analyzers is relatively linear. Data comes in, gets processed, stored, and then returned to the requester for analysis. Our project adheres to this design as well. 

![Interface Design](images/flow_diagram.png){width=50%}

The right column of our interface design diagram shows the software components that we used to get the signals to display on Pulseview after getting them from our device. The middle column shows the hardware and software components needed to read in the logic signals and send the data the computer. Objects in blue are components that we designed and objects in green are components that are provided through third party software, or from our hardware manufacturers. 

## Structure and Logic Design ##

<!-- [Present the detailed structure and logic design for your hardware/software components and processes. This section must include textual description accompanied with diagrams. If scientific or mathematical fundamentals are used for your project algorithm, specify what kind of formula or theory has been applied.] -->

The structura

## Design Constraints, Problems, Trade-offs, and Solutions ##

### Design Constraints and Challenges ###

<!-- [Present your design constraints in different perspectives, such as economic, resources, society and environment, hardware/software, mathematical/scientific theories and safety and reliability.] -->

The main constraint we will be dealing with in this project is keeping the cost of manufacturing down. In order for this to be a successful project, our design must be cost competitive to other devices that are already out on the market. This constraint is defined by the features plan to support and how much they will cost to implement. Some of the features we wish to to support are USB 3.0, 100 MHz sampling, and a large amount of data storage. For some of these constraints the solution is fairly obvious, but for others we will be engineering around fundamental laws of physics.

Because this project is a hardware project, we need to be cognizant of component price. If our design is reliant on a particular component that we cannot afford to purchase, then we have failed at designing our project. We also need to make sure that the components we design into our project have sufficient availability to allow for anyone in the future to take our designs and reproduce the logic analyzer.

The software and firmware that we produce for this project must be licensed in an appropriate open source license. In this context, appropriate means that it complies with all of the open source code we include in our software, and that also aligns with our ambitions for the project. If we choose to license our software with a license that is incompatible with other code we could face legal issues, and if we choose a license that is too restrictive we could detract contributors to our project.

The tools we use to design our software, firmware, and hardware all need to available to the general public for free. The tools to contribute to this project should not cost the contributor anything. We also are aiming to use as much open source software as possible to guarantee the tools we use will continue to be free in the future.

### Design Solutions and Trade-offs ###

<!-- [Document your approaches to cope with the given constraints. Present your design trade-off decisions and solution selections to deal with these constraints and problems and challenges.] -->

We decided to support the USB 3.0 protocol which allowed us to communicate with a host computer ten times faster than USB 2.0. While the USB controller we are using is more expensive than a USB 2.0 controller, the speed that USB 3.0 provides is worth more than the extra cost. USB 3.0 also allows for different data transfer modes that both increases performance of the device, and increases the maximum capture length. We looked into using the much higher bandwidth format, Thunderbolt. The cost to implement would have been too high and the skills necessary to accomplish this would have been well outside of our current skills. This communication protocol is also only implemented on more professional hardware using only Intel CPUs. This would have limited the total marketability of our project by a drastic amount, thus we decided to not go with this communication protocol.

We chose to target the sampling speed of 100 MHz because that is what similar devices on the market have achieved with similar hardware. We looked into supporting higher sampling speeds such as 500 MHz, but if we were going to support these speeds, we would need to design a much more robust system. Also, the components we would need to use would be more expensive.

We decided to design our project around the Xilinx Artix-7 and the Cypress FX-3 due to their low costs with the features that we need. We also all had a Xilinx Artix-7 Development board that we used for our course work at San Jose State. The Artix-7 is one of Xilinx’s value optimized FPGA's, which gave us a lot of performance for a relatively low per unit price. Using a Xilinx FPGA also allowed us to use many of Xilinx's IPs right out of the box, without having to write our own from scratch. We did look into using other FPGA manufacturers, but none of them had a product that was close to the performance of our Artix-7 for the price were aiming to achieve.

The Cypress FX-3 is another important pillar of our design, allowing for USB 3.0 communication. We chose the FX-3 in particular because we were unable find any other USB 3.0 peripheral controllers that also had as much documentation and application notes as the FX-3 had. We also couldn’t find a competitor that could compete on price. While the cost of this controller is high in comparison to USB 2.0 controllers, it is still significantly less than other USB 3.0 controllers.

In terms of keeping component costs down and choosing components that will be readily available, choosing the Artix-7 and FX-3 were easy decisions. They are the some of the lowest cost options in their markets and neither of them are marked as end of life. We also made sure to check component suppliers such as Digikey and Mouser to make sure that there are sufficient quantities available for purchase.

For the tools we will be using in this project, we used Xilinx’s free Vivado development environment to develop for the Artix-7 and to develop for the Cypress FX-3, we used Cypress’s free EZ-USB suite. There are no real alternative for either of these suites and we had to use them to develop for our chosen components. We cannot guarantee that these tools will be available in the future, but we can assume that they will continue to be available and free as long as these companies exist.

\newpage