set(CMAKE_C_FLAGS "${CMAKE_C_FLAGS} -std=gnu11 -O3 -Wall")


set(CMAKE_C_FLAGS  "${CMAKE_C_FLAGS} -Werror")

add_executable(yang2c 
               cmn_crc.c)

target_link_libraries(yang2c yang)
