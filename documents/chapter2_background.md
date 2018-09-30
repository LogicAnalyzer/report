# Background and Related Work #

## Background and Technologies ##

<!-- [Provide the necessary background of this project, including concepts and knowledge (e.g design patterns, asynchronous programming, project estimation, scientific and mathematical theories), along with technologies (e.g. PhP, MySql). In addition, provide an updated table of courses you have taken that you applied to the project and how you applied them.] -->

From a hardware standpoint, internal components of the logic analyzer will require an understanding of memory interfacing with DDR3, in particular, how to interface with the Xilinx Series 7 FPGA family. Xilinx provides memory management tools to help facilitate these types of designs. Also, maximizing the throughput of the FX-3 microcontroller will require the understanding of new high-speed technologies on the market. Another important technology needed will be high-speed PCB design and fabrication methods for the final product.

Verification methodologies and tools, such as UVM and SystemVerilog, will be excellent in testing the many modules required in the FPGA design, and will be useful to help speed the verification process along as development time is extremely short..

On the user’s side, the Sigrok interface and system drivers will need to be created to allow the client computer to recognize and connect via USB to the logic analyzer. The software/hardware integration will be a major hurdle, especially at the target speeds, however there is sufficient documentation concerning the Cypress FX-3 to complete that requirement.

## Literature Search ##

<!-- [Similarly, present your updated literature search adding to those that you explained in Chapter 1 of 195A workbook.] -->

## State-of-the-art ##

<!-- [A smaller, one page summary follows the literature review. Please refer to ‘State-of-the-Art Summary’ section in Chapter 1 of 195A workbook. You should provide an updated state-of-the-art summary here.]  -->

The state of the art logic analyzers used today in industry can capture millions of samples across hundreds of channels or read signals changing at over 50 GHz. These logic analyzers are stand-alone units that have dedicated general purpose computers built into them running standard operating systems such as Microsoft Windows. Research that is currently being done in this field is mostly on increasing the speed of capture in these devices. We haven't been able to find many academic papers on this subject, which leads us to believe that the research is being done in-house and being kept as a trade secret. These devices are so specialized that there are only two companies producing high-speed logic analyzers, with one of them being the clear market leader. Performance increases in this specific market segment come from tangential research. For example, increased silicon performance for high-speed radio frequency signaling could be directly applied to the application specific integrated circuits used in these products.

The products that are competing at the top of the market are being sold for over 50 thousand dollars. This is due to the thousands of engineering hours required to design and implement these high-speed devices, and the extremely low volume that these devices are produced in. The electronics industry uses these devices to measure and test new products and designs. Without these tools, the speed increases that we have seen every year for the past thirty years would have been impossible. New designs must be verified before they are released for production, and as speeds have increased capturing the signal has become more complicated.

The Nyquist-Shannon sampling theorem states in order to accurately read an electronic signal at a given speed, you need to sample that signal at twice the speed. This speed requirement means that the industry needs to have equipment that can capture at least twice the speed they are designing at. This problem becomes a chicken and egg situation, where the current equipment needs to be designed, but it can't be tested with any of the equipment that is currently available.

\newpage