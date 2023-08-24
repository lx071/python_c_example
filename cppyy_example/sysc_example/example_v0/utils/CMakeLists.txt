set(LIB_SOURCES
	
)

# Define the library
add_library(vp_components
    initiator.cpp
	target.cpp
	clkgen.cpp
	resetgen.cpp)
target_link_libraries(vp_components LINK_PUBLIC scc)
target_include_directories(vp_components PUBLIC ${CMAKE_CURRENT_SOURCE_DIR})

install(TARGETS vp_components
        RUNTIME DESTINATION ${CMAKE_INSTALL_BINDIR}
        LIBRARY DESTINATION ${CMAKE_INSTALL_LIBDIR}
        ARCHIVE DESTINATION ${CMAKE_INSTALL_LIBDIR}
        PUBLIC_HEADER DESTINATION ${CMAKE_INSTALL_INCLUDEDIR}
        )
install(DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}/
        DESTINATION ${CMAKE_INSTALL_INCLUDEDIR} # target directory
        FILES_MATCHING # install only matched files
        PATTERN "*.h" # select header files
        )


