# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 2.8

#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:

# Remove some rules from gmake that .SUFFIXES does not remove.
SUFFIXES =

.SUFFIXES: .hpux_make_needs_suffix_list

# Suppress display of executed commands.
$(VERBOSE).SILENT:

# A target that is always out of date.
cmake_force:
.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /usr/bin/cmake

# The command to remove a file.
RM = /usr/bin/cmake -E remove -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /root/gr-ncofdm

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /root/gr-ncofdm/build

# Include any dependencies generated for this target.
include lib/CMakeFiles/gnuradio-ncofdm.dir/depend.make

# Include the progress variables for this target.
include lib/CMakeFiles/gnuradio-ncofdm.dir/progress.make

# Include the compile flags for this target's objects.
include lib/CMakeFiles/gnuradio-ncofdm.dir/flags.make

lib/CMakeFiles/gnuradio-ncofdm.dir/ncofdm_carrier_allocator_impl.cc.o: lib/CMakeFiles/gnuradio-ncofdm.dir/flags.make
lib/CMakeFiles/gnuradio-ncofdm.dir/ncofdm_carrier_allocator_impl.cc.o: ../lib/ncofdm_carrier_allocator_impl.cc
	$(CMAKE_COMMAND) -E cmake_progress_report /root/gr-ncofdm/build/CMakeFiles $(CMAKE_PROGRESS_1)
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Building CXX object lib/CMakeFiles/gnuradio-ncofdm.dir/ncofdm_carrier_allocator_impl.cc.o"
	cd /root/gr-ncofdm/build/lib && /usr/bin/c++   $(CXX_DEFINES) $(CXX_FLAGS) -o CMakeFiles/gnuradio-ncofdm.dir/ncofdm_carrier_allocator_impl.cc.o -c /root/gr-ncofdm/lib/ncofdm_carrier_allocator_impl.cc

lib/CMakeFiles/gnuradio-ncofdm.dir/ncofdm_carrier_allocator_impl.cc.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/gnuradio-ncofdm.dir/ncofdm_carrier_allocator_impl.cc.i"
	cd /root/gr-ncofdm/build/lib && /usr/bin/c++  $(CXX_DEFINES) $(CXX_FLAGS) -E /root/gr-ncofdm/lib/ncofdm_carrier_allocator_impl.cc > CMakeFiles/gnuradio-ncofdm.dir/ncofdm_carrier_allocator_impl.cc.i

lib/CMakeFiles/gnuradio-ncofdm.dir/ncofdm_carrier_allocator_impl.cc.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/gnuradio-ncofdm.dir/ncofdm_carrier_allocator_impl.cc.s"
	cd /root/gr-ncofdm/build/lib && /usr/bin/c++  $(CXX_DEFINES) $(CXX_FLAGS) -S /root/gr-ncofdm/lib/ncofdm_carrier_allocator_impl.cc -o CMakeFiles/gnuradio-ncofdm.dir/ncofdm_carrier_allocator_impl.cc.s

lib/CMakeFiles/gnuradio-ncofdm.dir/ncofdm_carrier_allocator_impl.cc.o.requires:
.PHONY : lib/CMakeFiles/gnuradio-ncofdm.dir/ncofdm_carrier_allocator_impl.cc.o.requires

lib/CMakeFiles/gnuradio-ncofdm.dir/ncofdm_carrier_allocator_impl.cc.o.provides: lib/CMakeFiles/gnuradio-ncofdm.dir/ncofdm_carrier_allocator_impl.cc.o.requires
	$(MAKE) -f lib/CMakeFiles/gnuradio-ncofdm.dir/build.make lib/CMakeFiles/gnuradio-ncofdm.dir/ncofdm_carrier_allocator_impl.cc.o.provides.build
.PHONY : lib/CMakeFiles/gnuradio-ncofdm.dir/ncofdm_carrier_allocator_impl.cc.o.provides

lib/CMakeFiles/gnuradio-ncofdm.dir/ncofdm_carrier_allocator_impl.cc.o.provides.build: lib/CMakeFiles/gnuradio-ncofdm.dir/ncofdm_carrier_allocator_impl.cc.o

lib/CMakeFiles/gnuradio-ncofdm.dir/add_cp_sync_impl.cc.o: lib/CMakeFiles/gnuradio-ncofdm.dir/flags.make
lib/CMakeFiles/gnuradio-ncofdm.dir/add_cp_sync_impl.cc.o: ../lib/add_cp_sync_impl.cc
	$(CMAKE_COMMAND) -E cmake_progress_report /root/gr-ncofdm/build/CMakeFiles $(CMAKE_PROGRESS_2)
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Building CXX object lib/CMakeFiles/gnuradio-ncofdm.dir/add_cp_sync_impl.cc.o"
	cd /root/gr-ncofdm/build/lib && /usr/bin/c++   $(CXX_DEFINES) $(CXX_FLAGS) -o CMakeFiles/gnuradio-ncofdm.dir/add_cp_sync_impl.cc.o -c /root/gr-ncofdm/lib/add_cp_sync_impl.cc

lib/CMakeFiles/gnuradio-ncofdm.dir/add_cp_sync_impl.cc.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/gnuradio-ncofdm.dir/add_cp_sync_impl.cc.i"
	cd /root/gr-ncofdm/build/lib && /usr/bin/c++  $(CXX_DEFINES) $(CXX_FLAGS) -E /root/gr-ncofdm/lib/add_cp_sync_impl.cc > CMakeFiles/gnuradio-ncofdm.dir/add_cp_sync_impl.cc.i

lib/CMakeFiles/gnuradio-ncofdm.dir/add_cp_sync_impl.cc.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/gnuradio-ncofdm.dir/add_cp_sync_impl.cc.s"
	cd /root/gr-ncofdm/build/lib && /usr/bin/c++  $(CXX_DEFINES) $(CXX_FLAGS) -S /root/gr-ncofdm/lib/add_cp_sync_impl.cc -o CMakeFiles/gnuradio-ncofdm.dir/add_cp_sync_impl.cc.s

lib/CMakeFiles/gnuradio-ncofdm.dir/add_cp_sync_impl.cc.o.requires:
.PHONY : lib/CMakeFiles/gnuradio-ncofdm.dir/add_cp_sync_impl.cc.o.requires

lib/CMakeFiles/gnuradio-ncofdm.dir/add_cp_sync_impl.cc.o.provides: lib/CMakeFiles/gnuradio-ncofdm.dir/add_cp_sync_impl.cc.o.requires
	$(MAKE) -f lib/CMakeFiles/gnuradio-ncofdm.dir/build.make lib/CMakeFiles/gnuradio-ncofdm.dir/add_cp_sync_impl.cc.o.provides.build
.PHONY : lib/CMakeFiles/gnuradio-ncofdm.dir/add_cp_sync_impl.cc.o.provides

lib/CMakeFiles/gnuradio-ncofdm.dir/add_cp_sync_impl.cc.o.provides.build: lib/CMakeFiles/gnuradio-ncofdm.dir/add_cp_sync_impl.cc.o

lib/CMakeFiles/gnuradio-ncofdm.dir/ShortPNcorr_impl.cc.o: lib/CMakeFiles/gnuradio-ncofdm.dir/flags.make
lib/CMakeFiles/gnuradio-ncofdm.dir/ShortPNcorr_impl.cc.o: ../lib/ShortPNcorr_impl.cc
	$(CMAKE_COMMAND) -E cmake_progress_report /root/gr-ncofdm/build/CMakeFiles $(CMAKE_PROGRESS_3)
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Building CXX object lib/CMakeFiles/gnuradio-ncofdm.dir/ShortPNcorr_impl.cc.o"
	cd /root/gr-ncofdm/build/lib && /usr/bin/c++   $(CXX_DEFINES) $(CXX_FLAGS) -o CMakeFiles/gnuradio-ncofdm.dir/ShortPNcorr_impl.cc.o -c /root/gr-ncofdm/lib/ShortPNcorr_impl.cc

lib/CMakeFiles/gnuradio-ncofdm.dir/ShortPNcorr_impl.cc.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/gnuradio-ncofdm.dir/ShortPNcorr_impl.cc.i"
	cd /root/gr-ncofdm/build/lib && /usr/bin/c++  $(CXX_DEFINES) $(CXX_FLAGS) -E /root/gr-ncofdm/lib/ShortPNcorr_impl.cc > CMakeFiles/gnuradio-ncofdm.dir/ShortPNcorr_impl.cc.i

lib/CMakeFiles/gnuradio-ncofdm.dir/ShortPNcorr_impl.cc.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/gnuradio-ncofdm.dir/ShortPNcorr_impl.cc.s"
	cd /root/gr-ncofdm/build/lib && /usr/bin/c++  $(CXX_DEFINES) $(CXX_FLAGS) -S /root/gr-ncofdm/lib/ShortPNcorr_impl.cc -o CMakeFiles/gnuradio-ncofdm.dir/ShortPNcorr_impl.cc.s

lib/CMakeFiles/gnuradio-ncofdm.dir/ShortPNcorr_impl.cc.o.requires:
.PHONY : lib/CMakeFiles/gnuradio-ncofdm.dir/ShortPNcorr_impl.cc.o.requires

lib/CMakeFiles/gnuradio-ncofdm.dir/ShortPNcorr_impl.cc.o.provides: lib/CMakeFiles/gnuradio-ncofdm.dir/ShortPNcorr_impl.cc.o.requires
	$(MAKE) -f lib/CMakeFiles/gnuradio-ncofdm.dir/build.make lib/CMakeFiles/gnuradio-ncofdm.dir/ShortPNcorr_impl.cc.o.provides.build
.PHONY : lib/CMakeFiles/gnuradio-ncofdm.dir/ShortPNcorr_impl.cc.o.provides

lib/CMakeFiles/gnuradio-ncofdm.dir/ShortPNcorr_impl.cc.o.provides.build: lib/CMakeFiles/gnuradio-ncofdm.dir/ShortPNcorr_impl.cc.o

lib/CMakeFiles/gnuradio-ncofdm.dir/stream2fftvector_impl.cc.o: lib/CMakeFiles/gnuradio-ncofdm.dir/flags.make
lib/CMakeFiles/gnuradio-ncofdm.dir/stream2fftvector_impl.cc.o: ../lib/stream2fftvector_impl.cc
	$(CMAKE_COMMAND) -E cmake_progress_report /root/gr-ncofdm/build/CMakeFiles $(CMAKE_PROGRESS_4)
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Building CXX object lib/CMakeFiles/gnuradio-ncofdm.dir/stream2fftvector_impl.cc.o"
	cd /root/gr-ncofdm/build/lib && /usr/bin/c++   $(CXX_DEFINES) $(CXX_FLAGS) -o CMakeFiles/gnuradio-ncofdm.dir/stream2fftvector_impl.cc.o -c /root/gr-ncofdm/lib/stream2fftvector_impl.cc

lib/CMakeFiles/gnuradio-ncofdm.dir/stream2fftvector_impl.cc.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/gnuradio-ncofdm.dir/stream2fftvector_impl.cc.i"
	cd /root/gr-ncofdm/build/lib && /usr/bin/c++  $(CXX_DEFINES) $(CXX_FLAGS) -E /root/gr-ncofdm/lib/stream2fftvector_impl.cc > CMakeFiles/gnuradio-ncofdm.dir/stream2fftvector_impl.cc.i

lib/CMakeFiles/gnuradio-ncofdm.dir/stream2fftvector_impl.cc.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/gnuradio-ncofdm.dir/stream2fftvector_impl.cc.s"
	cd /root/gr-ncofdm/build/lib && /usr/bin/c++  $(CXX_DEFINES) $(CXX_FLAGS) -S /root/gr-ncofdm/lib/stream2fftvector_impl.cc -o CMakeFiles/gnuradio-ncofdm.dir/stream2fftvector_impl.cc.s

lib/CMakeFiles/gnuradio-ncofdm.dir/stream2fftvector_impl.cc.o.requires:
.PHONY : lib/CMakeFiles/gnuradio-ncofdm.dir/stream2fftvector_impl.cc.o.requires

lib/CMakeFiles/gnuradio-ncofdm.dir/stream2fftvector_impl.cc.o.provides: lib/CMakeFiles/gnuradio-ncofdm.dir/stream2fftvector_impl.cc.o.requires
	$(MAKE) -f lib/CMakeFiles/gnuradio-ncofdm.dir/build.make lib/CMakeFiles/gnuradio-ncofdm.dir/stream2fftvector_impl.cc.o.provides.build
.PHONY : lib/CMakeFiles/gnuradio-ncofdm.dir/stream2fftvector_impl.cc.o.provides

lib/CMakeFiles/gnuradio-ncofdm.dir/stream2fftvector_impl.cc.o.provides.build: lib/CMakeFiles/gnuradio-ncofdm.dir/stream2fftvector_impl.cc.o

lib/CMakeFiles/gnuradio-ncofdm.dir/LongPNcorr_impl.cc.o: lib/CMakeFiles/gnuradio-ncofdm.dir/flags.make
lib/CMakeFiles/gnuradio-ncofdm.dir/LongPNcorr_impl.cc.o: ../lib/LongPNcorr_impl.cc
	$(CMAKE_COMMAND) -E cmake_progress_report /root/gr-ncofdm/build/CMakeFiles $(CMAKE_PROGRESS_5)
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Building CXX object lib/CMakeFiles/gnuradio-ncofdm.dir/LongPNcorr_impl.cc.o"
	cd /root/gr-ncofdm/build/lib && /usr/bin/c++   $(CXX_DEFINES) $(CXX_FLAGS) -o CMakeFiles/gnuradio-ncofdm.dir/LongPNcorr_impl.cc.o -c /root/gr-ncofdm/lib/LongPNcorr_impl.cc

lib/CMakeFiles/gnuradio-ncofdm.dir/LongPNcorr_impl.cc.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/gnuradio-ncofdm.dir/LongPNcorr_impl.cc.i"
	cd /root/gr-ncofdm/build/lib && /usr/bin/c++  $(CXX_DEFINES) $(CXX_FLAGS) -E /root/gr-ncofdm/lib/LongPNcorr_impl.cc > CMakeFiles/gnuradio-ncofdm.dir/LongPNcorr_impl.cc.i

lib/CMakeFiles/gnuradio-ncofdm.dir/LongPNcorr_impl.cc.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/gnuradio-ncofdm.dir/LongPNcorr_impl.cc.s"
	cd /root/gr-ncofdm/build/lib && /usr/bin/c++  $(CXX_DEFINES) $(CXX_FLAGS) -S /root/gr-ncofdm/lib/LongPNcorr_impl.cc -o CMakeFiles/gnuradio-ncofdm.dir/LongPNcorr_impl.cc.s

lib/CMakeFiles/gnuradio-ncofdm.dir/LongPNcorr_impl.cc.o.requires:
.PHONY : lib/CMakeFiles/gnuradio-ncofdm.dir/LongPNcorr_impl.cc.o.requires

lib/CMakeFiles/gnuradio-ncofdm.dir/LongPNcorr_impl.cc.o.provides: lib/CMakeFiles/gnuradio-ncofdm.dir/LongPNcorr_impl.cc.o.requires
	$(MAKE) -f lib/CMakeFiles/gnuradio-ncofdm.dir/build.make lib/CMakeFiles/gnuradio-ncofdm.dir/LongPNcorr_impl.cc.o.provides.build
.PHONY : lib/CMakeFiles/gnuradio-ncofdm.dir/LongPNcorr_impl.cc.o.provides

lib/CMakeFiles/gnuradio-ncofdm.dir/LongPNcorr_impl.cc.o.provides.build: lib/CMakeFiles/gnuradio-ncofdm.dir/LongPNcorr_impl.cc.o

lib/CMakeFiles/gnuradio-ncofdm.dir/FreqOffCalc_impl.cc.o: lib/CMakeFiles/gnuradio-ncofdm.dir/flags.make
lib/CMakeFiles/gnuradio-ncofdm.dir/FreqOffCalc_impl.cc.o: ../lib/FreqOffCalc_impl.cc
	$(CMAKE_COMMAND) -E cmake_progress_report /root/gr-ncofdm/build/CMakeFiles $(CMAKE_PROGRESS_6)
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Building CXX object lib/CMakeFiles/gnuradio-ncofdm.dir/FreqOffCalc_impl.cc.o"
	cd /root/gr-ncofdm/build/lib && /usr/bin/c++   $(CXX_DEFINES) $(CXX_FLAGS) -o CMakeFiles/gnuradio-ncofdm.dir/FreqOffCalc_impl.cc.o -c /root/gr-ncofdm/lib/FreqOffCalc_impl.cc

lib/CMakeFiles/gnuradio-ncofdm.dir/FreqOffCalc_impl.cc.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/gnuradio-ncofdm.dir/FreqOffCalc_impl.cc.i"
	cd /root/gr-ncofdm/build/lib && /usr/bin/c++  $(CXX_DEFINES) $(CXX_FLAGS) -E /root/gr-ncofdm/lib/FreqOffCalc_impl.cc > CMakeFiles/gnuradio-ncofdm.dir/FreqOffCalc_impl.cc.i

lib/CMakeFiles/gnuradio-ncofdm.dir/FreqOffCalc_impl.cc.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/gnuradio-ncofdm.dir/FreqOffCalc_impl.cc.s"
	cd /root/gr-ncofdm/build/lib && /usr/bin/c++  $(CXX_DEFINES) $(CXX_FLAGS) -S /root/gr-ncofdm/lib/FreqOffCalc_impl.cc -o CMakeFiles/gnuradio-ncofdm.dir/FreqOffCalc_impl.cc.s

lib/CMakeFiles/gnuradio-ncofdm.dir/FreqOffCalc_impl.cc.o.requires:
.PHONY : lib/CMakeFiles/gnuradio-ncofdm.dir/FreqOffCalc_impl.cc.o.requires

lib/CMakeFiles/gnuradio-ncofdm.dir/FreqOffCalc_impl.cc.o.provides: lib/CMakeFiles/gnuradio-ncofdm.dir/FreqOffCalc_impl.cc.o.requires
	$(MAKE) -f lib/CMakeFiles/gnuradio-ncofdm.dir/build.make lib/CMakeFiles/gnuradio-ncofdm.dir/FreqOffCalc_impl.cc.o.provides.build
.PHONY : lib/CMakeFiles/gnuradio-ncofdm.dir/FreqOffCalc_impl.cc.o.provides

lib/CMakeFiles/gnuradio-ncofdm.dir/FreqOffCalc_impl.cc.o.provides.build: lib/CMakeFiles/gnuradio-ncofdm.dir/FreqOffCalc_impl.cc.o

lib/CMakeFiles/gnuradio-ncofdm.dir/DyThresAdjust_impl.cc.o: lib/CMakeFiles/gnuradio-ncofdm.dir/flags.make
lib/CMakeFiles/gnuradio-ncofdm.dir/DyThresAdjust_impl.cc.o: ../lib/DyThresAdjust_impl.cc
	$(CMAKE_COMMAND) -E cmake_progress_report /root/gr-ncofdm/build/CMakeFiles $(CMAKE_PROGRESS_7)
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Building CXX object lib/CMakeFiles/gnuradio-ncofdm.dir/DyThresAdjust_impl.cc.o"
	cd /root/gr-ncofdm/build/lib && /usr/bin/c++   $(CXX_DEFINES) $(CXX_FLAGS) -o CMakeFiles/gnuradio-ncofdm.dir/DyThresAdjust_impl.cc.o -c /root/gr-ncofdm/lib/DyThresAdjust_impl.cc

lib/CMakeFiles/gnuradio-ncofdm.dir/DyThresAdjust_impl.cc.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/gnuradio-ncofdm.dir/DyThresAdjust_impl.cc.i"
	cd /root/gr-ncofdm/build/lib && /usr/bin/c++  $(CXX_DEFINES) $(CXX_FLAGS) -E /root/gr-ncofdm/lib/DyThresAdjust_impl.cc > CMakeFiles/gnuradio-ncofdm.dir/DyThresAdjust_impl.cc.i

lib/CMakeFiles/gnuradio-ncofdm.dir/DyThresAdjust_impl.cc.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/gnuradio-ncofdm.dir/DyThresAdjust_impl.cc.s"
	cd /root/gr-ncofdm/build/lib && /usr/bin/c++  $(CXX_DEFINES) $(CXX_FLAGS) -S /root/gr-ncofdm/lib/DyThresAdjust_impl.cc -o CMakeFiles/gnuradio-ncofdm.dir/DyThresAdjust_impl.cc.s

lib/CMakeFiles/gnuradio-ncofdm.dir/DyThresAdjust_impl.cc.o.requires:
.PHONY : lib/CMakeFiles/gnuradio-ncofdm.dir/DyThresAdjust_impl.cc.o.requires

lib/CMakeFiles/gnuradio-ncofdm.dir/DyThresAdjust_impl.cc.o.provides: lib/CMakeFiles/gnuradio-ncofdm.dir/DyThresAdjust_impl.cc.o.requires
	$(MAKE) -f lib/CMakeFiles/gnuradio-ncofdm.dir/build.make lib/CMakeFiles/gnuradio-ncofdm.dir/DyThresAdjust_impl.cc.o.provides.build
.PHONY : lib/CMakeFiles/gnuradio-ncofdm.dir/DyThresAdjust_impl.cc.o.provides

lib/CMakeFiles/gnuradio-ncofdm.dir/DyThresAdjust_impl.cc.o.provides.build: lib/CMakeFiles/gnuradio-ncofdm.dir/DyThresAdjust_impl.cc.o

lib/CMakeFiles/gnuradio-ncofdm.dir/ShortPNdetector_impl.cc.o: lib/CMakeFiles/gnuradio-ncofdm.dir/flags.make
lib/CMakeFiles/gnuradio-ncofdm.dir/ShortPNdetector_impl.cc.o: ../lib/ShortPNdetector_impl.cc
	$(CMAKE_COMMAND) -E cmake_progress_report /root/gr-ncofdm/build/CMakeFiles $(CMAKE_PROGRESS_8)
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Building CXX object lib/CMakeFiles/gnuradio-ncofdm.dir/ShortPNdetector_impl.cc.o"
	cd /root/gr-ncofdm/build/lib && /usr/bin/c++   $(CXX_DEFINES) $(CXX_FLAGS) -o CMakeFiles/gnuradio-ncofdm.dir/ShortPNdetector_impl.cc.o -c /root/gr-ncofdm/lib/ShortPNdetector_impl.cc

lib/CMakeFiles/gnuradio-ncofdm.dir/ShortPNdetector_impl.cc.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/gnuradio-ncofdm.dir/ShortPNdetector_impl.cc.i"
	cd /root/gr-ncofdm/build/lib && /usr/bin/c++  $(CXX_DEFINES) $(CXX_FLAGS) -E /root/gr-ncofdm/lib/ShortPNdetector_impl.cc > CMakeFiles/gnuradio-ncofdm.dir/ShortPNdetector_impl.cc.i

lib/CMakeFiles/gnuradio-ncofdm.dir/ShortPNdetector_impl.cc.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/gnuradio-ncofdm.dir/ShortPNdetector_impl.cc.s"
	cd /root/gr-ncofdm/build/lib && /usr/bin/c++  $(CXX_DEFINES) $(CXX_FLAGS) -S /root/gr-ncofdm/lib/ShortPNdetector_impl.cc -o CMakeFiles/gnuradio-ncofdm.dir/ShortPNdetector_impl.cc.s

lib/CMakeFiles/gnuradio-ncofdm.dir/ShortPNdetector_impl.cc.o.requires:
.PHONY : lib/CMakeFiles/gnuradio-ncofdm.dir/ShortPNdetector_impl.cc.o.requires

lib/CMakeFiles/gnuradio-ncofdm.dir/ShortPNdetector_impl.cc.o.provides: lib/CMakeFiles/gnuradio-ncofdm.dir/ShortPNdetector_impl.cc.o.requires
	$(MAKE) -f lib/CMakeFiles/gnuradio-ncofdm.dir/build.make lib/CMakeFiles/gnuradio-ncofdm.dir/ShortPNdetector_impl.cc.o.provides.build
.PHONY : lib/CMakeFiles/gnuradio-ncofdm.dir/ShortPNdetector_impl.cc.o.provides

lib/CMakeFiles/gnuradio-ncofdm.dir/ShortPNdetector_impl.cc.o.provides.build: lib/CMakeFiles/gnuradio-ncofdm.dir/ShortPNdetector_impl.cc.o

lib/CMakeFiles/gnuradio-ncofdm.dir/add_cp_underlay_impl.cc.o: lib/CMakeFiles/gnuradio-ncofdm.dir/flags.make
lib/CMakeFiles/gnuradio-ncofdm.dir/add_cp_underlay_impl.cc.o: ../lib/add_cp_underlay_impl.cc
	$(CMAKE_COMMAND) -E cmake_progress_report /root/gr-ncofdm/build/CMakeFiles $(CMAKE_PROGRESS_9)
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Building CXX object lib/CMakeFiles/gnuradio-ncofdm.dir/add_cp_underlay_impl.cc.o"
	cd /root/gr-ncofdm/build/lib && /usr/bin/c++   $(CXX_DEFINES) $(CXX_FLAGS) -o CMakeFiles/gnuradio-ncofdm.dir/add_cp_underlay_impl.cc.o -c /root/gr-ncofdm/lib/add_cp_underlay_impl.cc

lib/CMakeFiles/gnuradio-ncofdm.dir/add_cp_underlay_impl.cc.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/gnuradio-ncofdm.dir/add_cp_underlay_impl.cc.i"
	cd /root/gr-ncofdm/build/lib && /usr/bin/c++  $(CXX_DEFINES) $(CXX_FLAGS) -E /root/gr-ncofdm/lib/add_cp_underlay_impl.cc > CMakeFiles/gnuradio-ncofdm.dir/add_cp_underlay_impl.cc.i

lib/CMakeFiles/gnuradio-ncofdm.dir/add_cp_underlay_impl.cc.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/gnuradio-ncofdm.dir/add_cp_underlay_impl.cc.s"
	cd /root/gr-ncofdm/build/lib && /usr/bin/c++  $(CXX_DEFINES) $(CXX_FLAGS) -S /root/gr-ncofdm/lib/add_cp_underlay_impl.cc -o CMakeFiles/gnuradio-ncofdm.dir/add_cp_underlay_impl.cc.s

lib/CMakeFiles/gnuradio-ncofdm.dir/add_cp_underlay_impl.cc.o.requires:
.PHONY : lib/CMakeFiles/gnuradio-ncofdm.dir/add_cp_underlay_impl.cc.o.requires

lib/CMakeFiles/gnuradio-ncofdm.dir/add_cp_underlay_impl.cc.o.provides: lib/CMakeFiles/gnuradio-ncofdm.dir/add_cp_underlay_impl.cc.o.requires
	$(MAKE) -f lib/CMakeFiles/gnuradio-ncofdm.dir/build.make lib/CMakeFiles/gnuradio-ncofdm.dir/add_cp_underlay_impl.cc.o.provides.build
.PHONY : lib/CMakeFiles/gnuradio-ncofdm.dir/add_cp_underlay_impl.cc.o.provides

lib/CMakeFiles/gnuradio-ncofdm.dir/add_cp_underlay_impl.cc.o.provides.build: lib/CMakeFiles/gnuradio-ncofdm.dir/add_cp_underlay_impl.cc.o

lib/CMakeFiles/gnuradio-ncofdm.dir/LongPNcorrV2_impl.cc.o: lib/CMakeFiles/gnuradio-ncofdm.dir/flags.make
lib/CMakeFiles/gnuradio-ncofdm.dir/LongPNcorrV2_impl.cc.o: ../lib/LongPNcorrV2_impl.cc
	$(CMAKE_COMMAND) -E cmake_progress_report /root/gr-ncofdm/build/CMakeFiles $(CMAKE_PROGRESS_10)
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Building CXX object lib/CMakeFiles/gnuradio-ncofdm.dir/LongPNcorrV2_impl.cc.o"
	cd /root/gr-ncofdm/build/lib && /usr/bin/c++   $(CXX_DEFINES) $(CXX_FLAGS) -o CMakeFiles/gnuradio-ncofdm.dir/LongPNcorrV2_impl.cc.o -c /root/gr-ncofdm/lib/LongPNcorrV2_impl.cc

lib/CMakeFiles/gnuradio-ncofdm.dir/LongPNcorrV2_impl.cc.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/gnuradio-ncofdm.dir/LongPNcorrV2_impl.cc.i"
	cd /root/gr-ncofdm/build/lib && /usr/bin/c++  $(CXX_DEFINES) $(CXX_FLAGS) -E /root/gr-ncofdm/lib/LongPNcorrV2_impl.cc > CMakeFiles/gnuradio-ncofdm.dir/LongPNcorrV2_impl.cc.i

lib/CMakeFiles/gnuradio-ncofdm.dir/LongPNcorrV2_impl.cc.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/gnuradio-ncofdm.dir/LongPNcorrV2_impl.cc.s"
	cd /root/gr-ncofdm/build/lib && /usr/bin/c++  $(CXX_DEFINES) $(CXX_FLAGS) -S /root/gr-ncofdm/lib/LongPNcorrV2_impl.cc -o CMakeFiles/gnuradio-ncofdm.dir/LongPNcorrV2_impl.cc.s

lib/CMakeFiles/gnuradio-ncofdm.dir/LongPNcorrV2_impl.cc.o.requires:
.PHONY : lib/CMakeFiles/gnuradio-ncofdm.dir/LongPNcorrV2_impl.cc.o.requires

lib/CMakeFiles/gnuradio-ncofdm.dir/LongPNcorrV2_impl.cc.o.provides: lib/CMakeFiles/gnuradio-ncofdm.dir/LongPNcorrV2_impl.cc.o.requires
	$(MAKE) -f lib/CMakeFiles/gnuradio-ncofdm.dir/build.make lib/CMakeFiles/gnuradio-ncofdm.dir/LongPNcorrV2_impl.cc.o.provides.build
.PHONY : lib/CMakeFiles/gnuradio-ncofdm.dir/LongPNcorrV2_impl.cc.o.provides

lib/CMakeFiles/gnuradio-ncofdm.dir/LongPNcorrV2_impl.cc.o.provides.build: lib/CMakeFiles/gnuradio-ncofdm.dir/LongPNcorrV2_impl.cc.o

# Object files for target gnuradio-ncofdm
gnuradio__ncofdm_OBJECTS = \
"CMakeFiles/gnuradio-ncofdm.dir/ncofdm_carrier_allocator_impl.cc.o" \
"CMakeFiles/gnuradio-ncofdm.dir/add_cp_sync_impl.cc.o" \
"CMakeFiles/gnuradio-ncofdm.dir/ShortPNcorr_impl.cc.o" \
"CMakeFiles/gnuradio-ncofdm.dir/stream2fftvector_impl.cc.o" \
"CMakeFiles/gnuradio-ncofdm.dir/LongPNcorr_impl.cc.o" \
"CMakeFiles/gnuradio-ncofdm.dir/FreqOffCalc_impl.cc.o" \
"CMakeFiles/gnuradio-ncofdm.dir/DyThresAdjust_impl.cc.o" \
"CMakeFiles/gnuradio-ncofdm.dir/ShortPNdetector_impl.cc.o" \
"CMakeFiles/gnuradio-ncofdm.dir/add_cp_underlay_impl.cc.o" \
"CMakeFiles/gnuradio-ncofdm.dir/LongPNcorrV2_impl.cc.o"

# External object files for target gnuradio-ncofdm
gnuradio__ncofdm_EXTERNAL_OBJECTS =

lib/libgnuradio-ncofdm.so: lib/CMakeFiles/gnuradio-ncofdm.dir/ncofdm_carrier_allocator_impl.cc.o
lib/libgnuradio-ncofdm.so: lib/CMakeFiles/gnuradio-ncofdm.dir/add_cp_sync_impl.cc.o
lib/libgnuradio-ncofdm.so: lib/CMakeFiles/gnuradio-ncofdm.dir/ShortPNcorr_impl.cc.o
lib/libgnuradio-ncofdm.so: lib/CMakeFiles/gnuradio-ncofdm.dir/stream2fftvector_impl.cc.o
lib/libgnuradio-ncofdm.so: lib/CMakeFiles/gnuradio-ncofdm.dir/LongPNcorr_impl.cc.o
lib/libgnuradio-ncofdm.so: lib/CMakeFiles/gnuradio-ncofdm.dir/FreqOffCalc_impl.cc.o
lib/libgnuradio-ncofdm.so: lib/CMakeFiles/gnuradio-ncofdm.dir/DyThresAdjust_impl.cc.o
lib/libgnuradio-ncofdm.so: lib/CMakeFiles/gnuradio-ncofdm.dir/ShortPNdetector_impl.cc.o
lib/libgnuradio-ncofdm.so: lib/CMakeFiles/gnuradio-ncofdm.dir/add_cp_underlay_impl.cc.o
lib/libgnuradio-ncofdm.so: lib/CMakeFiles/gnuradio-ncofdm.dir/LongPNcorrV2_impl.cc.o
lib/libgnuradio-ncofdm.so: lib/CMakeFiles/gnuradio-ncofdm.dir/build.make
lib/libgnuradio-ncofdm.so: /usr/lib/x86_64-linux-gnu/libboost_filesystem.so
lib/libgnuradio-ncofdm.so: /usr/lib/x86_64-linux-gnu/libboost_system.so
lib/libgnuradio-ncofdm.so: /usr/local/lib/libgnuradio-runtime.so
lib/libgnuradio-ncofdm.so: /usr/local/lib/libgnuradio-pmt.so
lib/libgnuradio-ncofdm.so: /usr/local/lib/libgnuradio-filter.so
lib/libgnuradio-ncofdm.so: /usr/local/lib/libgnuradio-fft.so
lib/libgnuradio-ncofdm.so: lib/CMakeFiles/gnuradio-ncofdm.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --red --bold "Linking CXX shared library libgnuradio-ncofdm.so"
	cd /root/gr-ncofdm/build/lib && $(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/gnuradio-ncofdm.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
lib/CMakeFiles/gnuradio-ncofdm.dir/build: lib/libgnuradio-ncofdm.so
.PHONY : lib/CMakeFiles/gnuradio-ncofdm.dir/build

lib/CMakeFiles/gnuradio-ncofdm.dir/requires: lib/CMakeFiles/gnuradio-ncofdm.dir/ncofdm_carrier_allocator_impl.cc.o.requires
lib/CMakeFiles/gnuradio-ncofdm.dir/requires: lib/CMakeFiles/gnuradio-ncofdm.dir/add_cp_sync_impl.cc.o.requires
lib/CMakeFiles/gnuradio-ncofdm.dir/requires: lib/CMakeFiles/gnuradio-ncofdm.dir/ShortPNcorr_impl.cc.o.requires
lib/CMakeFiles/gnuradio-ncofdm.dir/requires: lib/CMakeFiles/gnuradio-ncofdm.dir/stream2fftvector_impl.cc.o.requires
lib/CMakeFiles/gnuradio-ncofdm.dir/requires: lib/CMakeFiles/gnuradio-ncofdm.dir/LongPNcorr_impl.cc.o.requires
lib/CMakeFiles/gnuradio-ncofdm.dir/requires: lib/CMakeFiles/gnuradio-ncofdm.dir/FreqOffCalc_impl.cc.o.requires
lib/CMakeFiles/gnuradio-ncofdm.dir/requires: lib/CMakeFiles/gnuradio-ncofdm.dir/DyThresAdjust_impl.cc.o.requires
lib/CMakeFiles/gnuradio-ncofdm.dir/requires: lib/CMakeFiles/gnuradio-ncofdm.dir/ShortPNdetector_impl.cc.o.requires
lib/CMakeFiles/gnuradio-ncofdm.dir/requires: lib/CMakeFiles/gnuradio-ncofdm.dir/add_cp_underlay_impl.cc.o.requires
lib/CMakeFiles/gnuradio-ncofdm.dir/requires: lib/CMakeFiles/gnuradio-ncofdm.dir/LongPNcorrV2_impl.cc.o.requires
.PHONY : lib/CMakeFiles/gnuradio-ncofdm.dir/requires

lib/CMakeFiles/gnuradio-ncofdm.dir/clean:
	cd /root/gr-ncofdm/build/lib && $(CMAKE_COMMAND) -P CMakeFiles/gnuradio-ncofdm.dir/cmake_clean.cmake
.PHONY : lib/CMakeFiles/gnuradio-ncofdm.dir/clean

lib/CMakeFiles/gnuradio-ncofdm.dir/depend:
	cd /root/gr-ncofdm/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /root/gr-ncofdm /root/gr-ncofdm/lib /root/gr-ncofdm/build /root/gr-ncofdm/build/lib /root/gr-ncofdm/build/lib/CMakeFiles/gnuradio-ncofdm.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : lib/CMakeFiles/gnuradio-ncofdm.dir/depend

