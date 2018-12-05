# Conclusions and Future Work #

We learned a lot from this project. Some of the biggest takeaways were project management and scope. We originally had lofty goals for our project that required more time and effort than we had available during our last year at San Jose State University. We also decided that we wanted to create something that we were proud of, and chose difficult to implement features that would be difficult for a team of three to complete. 

## Future Work ##

There were many features that we would have liked to make it into our final project, but due to time we weren't able to implement. The following are in no particular order.
 
### USB 3.0 ###

Our original intent was to get USB 3.0 communciation working with our project, but other aspects of the proejct took longer than expected. The first thing that we want to add to this project in the future is the USB 3.0 interface that we worked on before switching over to just implementing and testing the logic analyzer. 

### Run Length Encoding ###

Run length encoding is a technique used to store more data in a fixed amount of space. It leverages a simple compression algorithm that can significant increase the number of samples for signals that are far apart. This feature would have been nice to implement to use even more of our available resources and support a feature that is available in sigrok.

### DD2/DD3 ###

Our development board has a DD2 memory chip on board and it would have been nice to actually leverage the power of that chip for our project. We originally set out to use that memory for our project, and spent a lot of time trying to implement simple demos, but ultimately gave up and started to work on the more important aspects of the project. We never got back around to implementing DDR support and that is something that would really differentiate our logic analyzer from others on the market.

### Pull request into libsigrok ###

We spent a lot of time and effort writing a hardware driver for our logic analyzer to interface with libsigrok. We would like to get our code in a state to submit a patch to the sigrok team to get our hardware driver into the mainline code base for sigrok. 

### PCB design ###

One of our other main intentions with this project was to create a full hardware product, including a custom PCB. We still plan on doing this, but in the scope of this project we weren't able to accomplish this. Once we have finished adding the features we need, we plan on spending the time to design and manufacture a PCB for our device.

### 32 Channels ###

Our current design only supports 8 channels, but our design can easily be expanded to use 32 channels. We have been using 8 channels for development to make it easier to test and verify our design, but something we would like to change in the future it the ability to use up to 32 channels on our device.

### 250 MHz ###

The current sample rate of our logic analyzer is capped at 100MHz. We would like to increase the maximum speed to at least 250MHz to allow us to capture some of the high speed bus signals currently used in embedded systems. This would give our logic analyzer a feature that is currently not in the open-source market. 