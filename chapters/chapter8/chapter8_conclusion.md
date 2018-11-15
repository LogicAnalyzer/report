# Conclusions and Future Work #

We learned a lot from this project. Some of the biggest take aways were project management and scope. We originally had lofty goals for our project that required more time and effort than we had available during our last year at San Jose State University. We also decided that we wanted to create something that we were proud of, and chose difficult to implement features that would be difficult for 

## Future Work ##

There were many features that we would have liked to make it into our final project, but due to time we weren't able to implement. The following are in no particular order.
 
### Run Length Encoding ###

Run length encoding is a technique used to store more data in a fixed ammount of space. It leverages a simple compression algorithm that can signicant increase the number of samples for signals that are far apart. This feature wouild have been nice to implement to use even more of our available resources and support a feature that is available in sigrok.

### DD2/DD3 ###

Our development board has a DD2 memory chip onboard and it would have been nice to actually leverage the power of that chip for our project. We originally set out to use that memory for our project, and spent a lot of time trying to implement simple demos, but ultimately gave up and started to work on the more important aspects of the project. We never got back around to implemeting DDR support and that is something that would really differentiate our logic analyzer from others on the market.

### Pull request into libsigrok ###

We spent a lot of time and effort writing a hardware driver for our logic analyzer to interface with libsigrok. We would like to get our code in a state to submit a patch to the sigrok team to get our hardware driver into the mainline codebase for sigrok. 

### PCB design ###

One of our other main intentions with this project was to create a full hardware product, including a custom PCB. We still plan on doing this, but in the scope of this project we weren't able to accomplish this. Once we have finished adding the features we need, we plan on spending the time to design and manufacture a PCB for our device.

### 32 Channels ###

Our current design only supports 8 channels, but our design can easily be expanded to use 32 channels. We have been using 8 channels for development to make it easier to test and verify our design, but something we would like to change in the future it the ability to use up to 32 channels on our device.

### 250 MHz ###

The current sample rate of our logic analyzer is capped at 100MHz. We would like to increase the maximum speed to at least 250MHz to allow us to capture some of the high speed bus signals currently used in embedded systems. This would give our logic analyzer a feature that is currenlty not in the open-source market. 