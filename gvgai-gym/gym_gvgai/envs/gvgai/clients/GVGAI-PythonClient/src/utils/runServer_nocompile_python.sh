#!/bin/bash

# Got an java.net.BindException: Address already in use (Bind failed) from the server?
# Maybe a process is running at that port. Check: lsof -i tcp:<port>

game_id=$1
server_dir_prefix=$2
games_prefix=$2
visuals=$3
port=$4

DIRECTORY='./logs'
if [ ! -d "$DIRECTORY" ]; then
  mkdir ${DIRECTORY}
fi

#Point at the folder that contains 'examples/'
server_dir="${server_dir_prefix}/src"
build_folder='server-out'

rm -rf ${build_folder}
mkdir -p ${build_folder}
find "$server_dir" -name "*.java" | sed 's/\(.*\)/"\1"/g' > sources.txt
javac -d ${build_folder} @sources.txt

if [ "${visuals}" = "True" ]; then
    exec java -classpath ${build_folder} tracks.singleLearning.utils.JavaServer -gameId ${game_id} -gamesDir "${games_prefix}" -visuals -portNum ${port} > ${DIRECTORY}/output_server_redirect.txt 2> ${DIRECTORY}/output_server_redirect_err.txt
else
    exec java -classpath ${build_folder} tracks.singleLearning.utils.JavaServer -gameId ${game_id} -gamesDir "${games_prefix}" -portNum ${port} > ${DIRECTORY}/output_server_redirect.txt 2> ${DIRECTORY}/output_server_redirect_err.txt
fi