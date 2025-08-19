Using ArrayFire on Linux
========================

Once you have :ref:`installed <Linux>` ArrayFire on your system, the next thing to do is set up your build system. On Linux, you can create ArrayFire projects using almost any editor, compiler, or build system. The only requirements are that you include the ArrayFire header directories and link with the ArrayFire library you intend to use i.e. CUDA, OpenCL, oneAPI, CPU, or Unified backends.

.. _bigpicture:

The big picture
###############

On Linux, we recommend installing ArrayFire to :literal:`/opt/arrayfire` directory. The installer will populate files in the following sub-directories:

.. code-block:: text

    include/arrayfire.h         - Primary ArrayFire include file
    include/af/*.h              - Additional include files
    lib/libaf*                  - CPU, CUDA, oneAPI, and OpenCL libraries (.a, .so)
    lib/libforge*               - Visualization library
    lib/libcu*                  - CUDA backend dependencies
    lib/libOpenCL.so            - OpenCL ICD Loader library
    share/ArrayFire/cmake/*     - CMake config (find) scripts
    share/ArrayFire/examples/*  - All ArrayFire examples

Because ArrayFire follows standard installation practices, you can use basically any build system to create and compile projects that use ArrayFire. Among the many possible build systems on Linux we suggest using ArrayFire with either CMake or Makefiles with CMake being our preferred build system.

Prerequisite software
#####################

To build ArrayFire projects you will need a compiler

**Fedora, Centos and Redhat**

Install EPEL repo (not required for Fedora)

.. code-block:: text

    yum install epel-release
    yum update

Install build dependencies

.. code-block:: text

    yum install gcc gcc-c++ cmake3 make

**Debian and its derivatives**

Install common dependencies

.. code-block:: text

    apt install build-essential cmake cmake-curses-gui

CMake
We recommend that the CMake build system be used to create ArrayFire projects. As `discussed above <bigpicture>`, ArrayFire ships with a series of CMake scripts to make finding and using our library easy.

First create a file called :literal:`CMakeLists.txt` in your project directory:

.. code-block:: text

    cd your-project-directory
    touch CMakeLists.txt

and populate it with the following code:

.. code-block:: text

    find_package(ArrayFire)
    add_executable(<my_executable> [list your source files here])

    # To use Unified backend, do the following.
    # Unified backend lets you choose the backend at runtime
    target_link_libraries(<my_executable> ArrayFire::af)

where :literal:`my_executable` is the name of the executable you wish to create. See the `CMake documentation <https://cmake.org/documentation/>`_ for more information on how to use CMake. To link with a specific backend directly, replace the :literal:`ArrayFire::af` with the following for their respective backends.

* :literal:`ArrayFire::afcpu` for CPU backend.
* :literal:`ArrayFire::afcuda` for CUDA backend.
* :literal:`ArrayFire::afoneapi` for oneAPI backend.
* :literal:`ArrayFire::afopencl` for OpenCL backend.

Next we need to instruct CMake to create build instructions and then compile. We suggest using CMake's out-of-source build functionality to keep your build and source files cleanly separated. To do this open the CMake GUI.

.. code-block:: text

    cd your-project-directory
    mkdir build
    cd build
    cmake ..
    make

NOTE: If you have installed ArrayFire to a non-standard location, CMake can still help you out. When you execute CMake specify the path to ArrayFire installation root as :literal:`ArrayFire_DIR` variable.

For example, if ArrayFire were installed locally to :literal:`/home/user/ArrayFire` then you would modify the :literal:`cmake` command above to contain the following definition:

.. code-block:: text

    cmake -DArrayFire_DIR=/home/user/ArrayFire ..

You can also specify this information in the :literal:`ccmake` command-line interface.


Makefiles
#########

Building ArrayFire projects with Makefiles is fairly similar to CMake except you must specify all paths and libraries manually.

As with any :literal:`make` project, you need to specify the include path to the directory containing :literal:`arrayfire.h` file. This should be :literal`-I /opt/arrayfire/include` if you followed our installation instructions.

Similarly, you will need to specify the path to the ArrayFire library using the :literal:`-L` option (e.g. :literal:`-L/opt/arrayfire/lib`) followed by the specific ArrayFire library you wish to use using the :literal:`-l` option (for example :literal:`-lafcpu`, :literal:`-lafopencl`, :literal:`-lafoneapi`, :literal:`-lafcuda`, or :literal:`-laf` for the CPU, OpenCL, oneAPI, and CUDA, and unified backends, respectively.

Here is a minimal example Makefile which uses ArrayFire's CPU backend:

.. code-block:: text

    LIBS=-lafcpu
    LIB_PATHS=-L/opt/arrayfire/lib
    INCLUDES=-I/opt/arrayfire/include
    CC=g++ $(COMPILER_OPTIONS)
    COMPILER_OPTIONS=-std=c++11 -g

    all: main.cpp Makefile
        $(CC) main.cpp -o test $(INCLUDES) $(LIBS) $(LIB_PATHS)