#!/bin/bash

echo -e "Compile the SMORe ......"
cp ./node_embed_src/src_Makefile ./smore/src/Makefile
cp ./node_embed_src/cli_Makefile ./smore/cli/Makefile

cp ./node_embed_src/BPR_node_embed.cpp ./smore/src/model/BPR_node_embed.cpp
cp ./node_embed_src/BPR_node_embed.h ./smore/src/model/BPR_node_embed.h
cp ./node_embed_src/cli_bpr_node_embed.cpp ./smore/cli/bpr_node_embed.cpp

cp ./node_embed_src/HPE_node_embed.cpp ./smore/src/model/HPE_node_embed.cpp
cp ./node_embed_src/HPE_node_embed.h ./smore/src/model/HPE_node_embed.h
cp ./node_embed_src/cli_hpe_node_embed.cpp ./smore/cli/hpe_node_embed.cpp

cp ./node_embed_src/WARP_node_embed.cpp ./smore/src/model/WARP_node_embed.cpp
cp ./node_embed_src/WARP_node_embed.h ./smore/src/model/WARP_node_embed.h
cp ./node_embed_src/cli_warp_node_embed.cpp ./smore/cli/warp_node_embed.cpp

cp ./node_embed_src/HBPR_node_embed.cpp ./smore/src/model/HBPR_node_embed.cpp
cp ./node_embed_src/HBPR_node_embed.h ./smore/src/model/HBPR_node_embed.h
cp ./node_embed_src/cli_hoprec_node_embed.cpp ./smore/cli/hoprec_node_embed.cpp

cd smore
make

echo -e "Download the dataset ..."
wget -O ./data.tar.gz "https://www.dropbox.com/s/snkpt7aihmesaws/data.tar.gz?dl=0"
tar zxvf ./data.tar.gz

echo -e "Download Successfully!"
