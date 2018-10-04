# Project Requirements #

## Domain and Business Requirements ##

<!-- [Use UML 2 activity diagram to draw process summary diagram and a set of process decomposition diagrams. Draw a domain class diagram of business classes with attributes; draw a set of state machine diagrams for key business classes.] -->

|The device MUST...|
|Follow the USB interface standards for voltage and communication|
|Not interfere with the operation of the device it is sampling from|


## System (or Component) Functional Requirements ##

<!-- [List an organized set of statements of what the system does.  Use “shall” and “should” statements to recognize what was mandatory and optional respectively.  Note, if any, which requirements have changed from 195A. This section must include textual description accompanied with tables.] -->

|The device MUST...|
|------------------|
|Support a minimum of 8 channels of data capture|
|Provide storage for the entire capture before sending it to the host PC|
|Be able to transmit opcodes via USB to the logic analyzer|

|Sigrok Must...|
|-------------|
|Be able to receive data from logic analyzer|
|Be able to display the results of a capture on screen for the user|

|The Device SHOULD...|
|------------|
|Support a maximum of 16 channels of data capture|
|Allow for streaming a capture to the host PC|

## Non-functional Requirements ##
<!-- [List an organized set of statements describing requirements placed on the system, e.g., performance, capacity, availability, compliance to standards, security, etc.  This section must include textual description accompanied with tables. Ensure these requirements (as well as those stated in Section 3.2) can be measured in Chapter 7 on testing.  For example, “The system shall be fast” is not an appropriate requirement, but The system commands shall deliver .9 second response time in the first 3 months 99 percent of the time as measured end-to-end.] -->

|The device MUST…|
|-----------|
|Capture signals at a minimum speed of 50MHz|
|The logic analyzer MUST implement communication to a host PC using USB 2.0 communication|
|Be 3.3v tolerant|
|Trigger at the appropriate signal parameters specified by the user in sigrok|
|Work with a host PC running Windows 10 and sigrok|
|Return the capture signals to the host PC without any additional noise|


|The device SHOULD…|
|-----------|
|Capture signals at a speeds up to  200Mhz|
|The logic analyzer SHOULD implement communication to a host PC using USB 2.0 or USB 3.0|
|Be open source compliant|
|Have software written for it that is clear, well written, and maintainable for future open-sourced work|
|Have software written for it in a way so that extending the features for future versions can be easily done|
|Work on Windows 10, Ubuntu, and MacOS|
|Be adaptable to use for other FPGA products and manufacturers|

## Context and Interface Requirements ##
<!-- [Specify the context environments supporting your development, testing, and deployment of your project results. You also need to describe the interface requirements for your hardware/software components and system.] -->

The context of the project includes all the HDL code and hardware required to operate the Nexys 4 DDR FPGA board, as well as the sampling probes used to collect data from the device under test. The context also includes the USB connection to the host machine. Context and interface requirements also include the system drivers to support the logic analyzer, as well as the interface requirements for using the sigrok API by.

## Technology and Resource Requirements ##
<!-- [List the requirements for hardware (devices, components, systems, etc.) and software (compiler, database, middleware, etc.), technologies. This section must include textual description accompanied with tables.] -->

The hardware requirements for this project include the Nexys 4 DDR as well as a host PC running the Windows 10 operating system. Future work will support multiple operating systems and possibly other FPGA devices as well. With the project being used with an FPGA at its core, there are many technologies released by the FPGA developer (in this case Xilinx) that are necessary, including the Vivado suite of tools and the Memory Interface Generator provided within.

\newpage