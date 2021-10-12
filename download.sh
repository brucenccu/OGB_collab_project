#!/bin/bash

#mv ./node_embed_src/src_Makefile ./Makefile
#mv ./Makefile ./smore/src/
cp ./node_embed_src/src_Makefile ./smore/src/Makefile

#mv ./node_embed_src/cli_Makefile ./Makefile
#mv ./Makefile ./smore/cli
cp ./node_embed_src/cli_Makefile ./smore/cli/Makefile

#mv ./node_embed_src/BPR_node_embed* ./smore/src/model
#mv ./node_embed_src/cli_bpr_node_embed.cpp ./smore/cli
#mv ./smore/cli/cli_bpr_node_embed.cpp ./smore/cli/bpr_node_embed.cpp
#cp ./node_embed_src/cli_bpr_node_embed.cpp ./smore/cli
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
#mv ./node_embed_src/HPE_node_embed* ./smore/src/model
#mv ./node_embed_src/cli_hpe_node_embed.cpp ./smore/cli
#mv ./smore/cli/cli_hpe_node_embed.cpp ./smore/cli/hpe_node_embed.cpp

#mv ./node_embed_src/WARP_node_embed* ./smore/src/model
#mv ./node_embed_src/cli_warp_node_embed.cpp ./smore/cli
#mv ./smore/cli/cli_warp_node_embed.cpp ./smore/cli/warp_node_embed.cpp

#mv ./node_embed_src/HBPR_node_embed* ./smore/src/model
#mv ./node_embed_src/cli_hoprec_node_embed.cpp ./smore/cli
#mv ./smore/cli/cli_hoprec_node_embed.cpp ./smore/cli/hoprec_node_embed.cpp

#rm -rf node_embed_src

cd smore
make
