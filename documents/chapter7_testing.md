# Testings and Experiment ##

## Testings and Experiment Scope ##

<!-- [Describe an overview of your test process and experiment scope, including its test processes, test focuses and objectives, and selected test criteria at the component (e.g. unit testing) and system (e.g. integration testing) levels. This section must include textual description accompanied with figures and/or tables.] -->

The testing plan for the project was broken into three focal areas: unit testing of all verilog modules, communication testing between the host PC and the FPGA development board, and lastly, integration testing involving captures from other development boards.

### Verilog Modules ###

The verilog testing followed the standard RTL testing method. First a testbench is written for functional verification of the module then the module is synthesized and tested on an FPGA. This testing method was done for every major module through each layer of abstraction. This starts at a unit level test and moves up to the full chip test. Modules with a small amount of inputs were tested exhaustively, while modules with a large input set were tested with both directed testing to test edge cases and random testing to increase coverage.
The functional verification was used to ensure the module acted as expected in every case it might be in. With FPGA’s the turnaround time from changing code to a uploading a bitstream onto the board is very large. Using functional verification helps find any bugs in the logic of the module in a much faster way. Functional verification is ran on a hardware simulator hosted on a pc. This simulation allows a testbench to be written to examine all the signals and verify their state. This also provides waveforms that can be used to see the state of the module and the timing each signal changes.
Hardware verification is required due to the fact that hardware does not always act the same way as the simulation. With hardware there can be issues with delays, metastable states, or other issues that can arise when running on a non simulated test environment. When the module is in hardware it is much more difficult to debug, so hardware test is not done until functional verification has been brought to a satisfactory level for that module.

### PC-to-FPGA Communication ###

### Systems Integration and Sampling Tests ###

After extensive unit testing of individual verilog modules, a final top level test was built to simulate communication from a PC host to initiate a capture. Sample input data was generated for the simulation at random. By monitoring internal modules, verification of proper functionality was observed, leading the way to hardware validation.

Hardware validation was performed by attaching leads from the PMODs on the Nexys4 DDR to pins on a SJOne development board. The SJOne board has at its core has LPC1758 CPU along with many onboard components, including a SPI FLASH memory module. Hardware validation was accomplished by generating transfers of data from the SJOne board and confirming through Sigrok’s decoder that the correct data was being transferred.  

## Testings and Experiment Approach ##

<!-- [Describe the selected test strategies, test methods and techniques, as well as selected test coverage criteria. Test design content and test design summary could be included here, such as test case distribution and summary. These results must tie back to the requirements stated earlier.  This section must include textual description accompanied with figures and/or tables.] -->



## Testing and Experiment Results and Analysis ##

<!-- [Describe testing and experiment results and analysis. For example, test execution and test result summary, performance test result analysis, test coverage, bug distribution report, and so on. This section must include textual description accompanied with figures and/or tables.] -->

\newpage