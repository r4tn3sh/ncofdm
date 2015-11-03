INCLUDE(FindPkgConfig)
PKG_CHECK_MODULES(PC_NCOFDM ncofdm)

FIND_PATH(
    NCOFDM_INCLUDE_DIRS
    NAMES ncofdm/api.h
    HINTS $ENV{NCOFDM_DIR}/include
        ${PC_NCOFDM_INCLUDEDIR}
    PATHS ${CMAKE_INSTALL_PREFIX}/include
          /usr/local/include
          /usr/include
)

FIND_LIBRARY(
    NCOFDM_LIBRARIES
    NAMES gnuradio-ncofdm
    HINTS $ENV{NCOFDM_DIR}/lib
        ${PC_NCOFDM_LIBDIR}
    PATHS ${CMAKE_INSTALL_PREFIX}/lib
          ${CMAKE_INSTALL_PREFIX}/lib64
          /usr/local/lib
          /usr/local/lib64
          /usr/lib
          /usr/lib64
)

INCLUDE(FindPackageHandleStandardArgs)
FIND_PACKAGE_HANDLE_STANDARD_ARGS(NCOFDM DEFAULT_MSG NCOFDM_LIBRARIES NCOFDM_INCLUDE_DIRS)
MARK_AS_ADVANCED(NCOFDM_LIBRARIES NCOFDM_INCLUDE_DIRS)

