# Introduction #

## Project Goals and Objectives ##

<!-- [Describe what are the goals and objectives of the project.  In addition, it covers the context in which the project was placed.] -->

The goal of this project is to design and implement a high-speed USB 3.0 logic analyzer. All of the design files and source code will be released under an open source license. This project is intended to boost the ability of the hobbyist and education market for electronic design testing. In order to impact this sector the price must be kept low while the features of the logic analyzer still compete with incumbent market leaders.

One of the main features of this project is having high-speed data analysis. The projects goal is to achieve accurate analysis of signals between 100- 250 Mhz. In order to achieve this goal we must accomplish subgoals of high speed data storage, processing, and transmitting. This project will employ DDR3 DRAM for storage which has higher bandwidth with lower latency allowing faster storage of the data. USB 3.0 will allow faster transfer of data, making it possible to stream at high speeds due to its capability of reaching speeds up to 4.8 megabits per second far exceeding the expected recording speed of the logic analyzer. Implementing these two features will set the project up to achieve the high speed goal aimed for.

The second main feature of the this project is to be fully open sourced. This means barring the market modules used, every tool used and document created will be open for view and fair use by the community. This goal will allow the logic analyzer to continue to be maintained and improved after the project is complete. It also allows anyone who wants to reproduce the project to see all stages and steps that were taken to achieve success.

## Problem and Motivation ##

<!-- [Describe the problem, motivation, and needs of your project. You need to address why this project is important and what is the problem you have addressed.] -->

Logic analyzers are an important tool used in hardware development. Currently there is one market leader in the low cost USB logic analyzer sector and they recently doubled the prices of all of their products. Nothing about the product changed, only the price. There are several open source logic analyzer projects available, but those too have their own set of problems. The most recent open source logic analyzer design is poorly documented and doesn’t provide the necessary files to manufacture the product. Other popular projects are much older and use hardware that has become obsolete. While the logic analyzer portion is still functions, the hardware design could be improved with more modern components and interfaces.

## Project Application and Impact ##

<!-- [Describe the application of your project results, and its impacts to academic, industry, and society.] -->

Academic - Providing an open source logic analyzer project could allow for other academic projects the tools necessary to test new designs without relying on expensive industry tools. Academic projects could also refactor our open source logic analyzer to work with a specific application they are developing.

Industry - By providing a low cost logic analyzer that is completely free, hardware companies could integrate the logic analyzer into their own products which could aid in faster development times

Society - Low cost, open source hardware tools could decrease costs of products due to less expensive development costs. Some of these products could be life saving medical devices, safety critical devices, or other devices that require accurate testing. Reducing the cost of testing can reduce the cost of these important systems overall, expanding the impact across communities.

## Project Results and Deliverables ##

<!-- [Describe your actual project results (such as a system, and a component) and project deliverables (such as report, prototype, code, etc.).] -->

Report: A key deliverable will be the completion of this report. The report will include a thorough and detailed documentation of this project. The report will be written in a way to allow a person with no knowledge on the project, but complete industry knowledge to complete the project only using the information contained in the document. The report will also allow someone with no knowledge on the current state of the industry for logic analyzers to get a complete understanding through reading the report.

Source Code: All of the source code we write, including the USB device driver, sigrok device handler, verilog system implementation and  microcontroller software will be provided. This software should be able to be compiled and synthesized to program and use our product. We will also provide already compiled binaries for multiple platforms that can be used instead of compiling from source.

Design Files: We will provide the design files for our printed circuit board as well as the files necessary to manufacture the printed circuit board. We will also provide a complete bill of materials. Our intentions is that anyone can download the files, get the printed circuit board produce, and assemble the device if they wanted to.

Documentation: In addition to the source code and design files, we will provide extensive documentation that explain all of the components of the system. We believe this is an important component of a successful product and will allow for other people to contribute to the project in the future.

Prototype: We will have a prototype of our final design manufactured. This will include a printed circuit board and a case to house the circuit board. This will be a fully working prototype that can demonstrate all of the features of our project

## Project Report Structure ##

<!-- [Introduce the following sections of the document] -->

\newpage