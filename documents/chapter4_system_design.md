# System Design #

## Architecture Design ##

<!-- [Describe a general architectural solution for your system.  This section must include textual description accompanied with diagrams.] -->

![System Architecture](images/architecture.png)

Figure 1. System Architecture Block Diagram

The centerpiece of the project is the Xilinx Spartan-7 FPGA. This device will perform an array of tasks required for logic analysis. All data lines will run through a buffer to allow high voltage tolerance and go directly into the FPGA for processing. The FPGA will perform any required pre-processing then either store the data locally or send it to the overflow DDR3 DRAM. This decision will be based on the user preferences, which will allow choosing between streaming the data or storing and sending in blocks.

The microcontroller is the next major piece of hardware in the design. The Cypress FX-3 microcontroller will be used to implement the USB-3.0 high-speed stream and block data transfer. The data transfer will be used to get the information from the FPGA to the PC and also to allow programming of the device. An EEPROM will be used to allow updating of the firmware driving the FPGA and FX-3 microcontroller. This ability to update the firmware is fundamental to the open source principles this project is based on allowing users to improve upon the initial design we release.

The final part of the system architecture is the PC user interface which will be displayed on the open source signal UI Sigrok. In order to be displayed on sigrok, the USB data transfer will have to go through a middleware to parse the data to allow Sigrok to display it.

## Interface and Component Design ##

<!-- [Draw the actual component diagram with textual description. This section must include textual description accompanied with diagrams] -->

## Structure and Logic Design ##

<!-- [Present the detailed structure and logic design for your hardware/software components and processes. This section must include textual description accompanied with diagrams. If scientific or mathematical fundamentals are used for your project algorithm, specify what kind of formula or theory has been applied.] -->

## Design Constraints, Problems, Trade-offs, and Solutions ##

### Design Constraints and Challenges ###

<!-- [Present your design constraints in different perspectives, such as economic, resources, society and environment, hardware/software, mathematical/scientific theories and safety and reliability.] -->

The main constraint we will be dealing with in this project is keeping the cost of manufacturing down. In order for this to be a successful project, our design must be cost competitive to other devices that are already out on the market. This constraint is defined by the features plan to support and how much they will cost to implement. Some of the features we wish to to support are USB 3.0, 100 MHz sampling, and a large amount of data storage. For some of these constraints the solution is fairly obvious, but for others we will be engineering around fundamental laws of physics.

Because this project is a hardware project, we need to be cognizant of component price. If our design is reliant on a particular component that we cannot afford to purchase, then we have failed at designing our project. We also need to make sure that the components we design into our project have sufficient availability to allow for anyone in the future to take our designs and reproduce the logic analyzer.

The software and firmware that we produce for this project must be licensed in an appropriate open source license. In this context, appropriate means that it complies with all of the open source code we include in our software, and that also aligns with our ambitions for the project. If we choose to license our software with a license that is incompatible with other code we could face legal issues, and if we choose a license that is too restrictive we could detract contributors to our project.

The tools we use to design our software, firmware, and hardware all need to available to the general public for free. The tools to contribute to this project should not cost the contributor anything. We also are aiming to use as much open source software as possible to guarantee the tools we use will continue to be free in the future.


### Design Solutions and Trade-offs ###

<!-- [Document your approaches to cope with the given constraints. Present your design trade-off decisions and solution selections to deal with these constraints and problems and challenges.] -->

We have decided to support the USB 3.0 protocol which will allow us to communicate with a host computer ten times faster than USB 2.0. While the USB controller we have decided to use is more expensive than a USB 2.0 controller, the speed that USB 3.0 provides is worth more than the extra cost. USB 3.0 will also allow for different data transfer modes that could both increase performance of the device, and increase the maximum capture length. We looked into using the much higher bandwidth format, Thunderbolt. The cost to implement would have been too high and the skills necessary to accomplish this would have been well outside of our current skills. This communication protocol is also only implemented on higher end hardware using only Intel CPUs. This would have limited the total market that our project was aimed for by a drastic amount, thus we decided to not go with this communication protocol.

We have chosen to target the sampling speed of 100 MHz because that is what similar devices on the market have achieved with similar hardware. We looked into supporting higher sampling speeds such as 500 MHz, but if we were going to support these speeds, we would need to design a much more robust system. Also, the components we would need to use would be more expensive.

We decided to design our project around the Xilinx Spartan-7 and the Cypress FX-3 due to their low costs with the features that we need. The Spartan-7 is Xilinx’s lowest cost FPGA line, which means there really isn’t a lower tier FPGA that we could use instead. The Spartan-7 is one of the most important parts of our design because it allows for all of the different components that we are planning to integrate to work, most of them right out of the box. The FPGA will also allow us to be flexible in the components we add, because it is almost infinitely changeable, and from our initial estimates, the Spartan-7 will be more than capable of handling anything we throw at it. We chose to use a Xilinx FPGA due to our previous experiences with using it in our coursework at San Jose State. The other FPGA manufacturers also don’t have a line of components that seemed competitive in terms of price and features against the Spartan-7.

The Cypress FX-3 is another important pillar of our design, allowing for the USB 3.0 communication, which was discussed above. We chose the FX-3 in particular because we were unable find any other USB 3.0 peripheral controllers that also had as much documentation and application notes as the FX-3 had. The number of products this chip is in is astounding, with many different open source devices using this chip in their designs. We also couldn’t find a competitor that could compete on price. While the cost of this controller is high in comparison to USB 2.0 controllers, it is still significantly less than other USB 3.0 controllers.

In terms of keeping component costs down and choosing components that will be readily available, choosing the Spartan-7 and FX-3 were no brainers. They are the lowest cost options in their markets and neither of them are marked as end of life. We also made sure to check component suppliers such as Digikey and Mouser to make sure that there are sufficient quantities available for purchase. We will do the same verification when selecting the remaining components of our hardware design as we get further in the project.

We haven’t decided on a software license yet, but we are leaning towards a GPL compliant license to allow for the most code interoperability. The client software we will be using for our project is licensed under GPL which means that any modifications we make to that source will need to adhere to GPL as well. By adhering to a GPL compliant license we will also guarantee that contributors will have access to our code base, regardless of what happens to the project.

For the tools we will be using in this project, we will do our hardware design in KiCad, a free open source EDA tool. We will also be using Xilinx’s free Vivado development environment to develop for the Spartan-7 and to develop for the Cypress FX-3, we will be using Cypress’s free EZ-USB suite. There are no real alternative for either of these suites and we must use them in order to develop for our chosen components. We cannot guarantee that these tools will be available in the future, but we can assume that they will continue to be available and free as long as these companies exist. At this point in time, Xilinx and Cypress have no reason to start charging for these tools, making it a safe choice to select these vendors.
\newpage