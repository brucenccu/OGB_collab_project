#!/bin/bash

#unzip hpe_node_embed_src.zip
#unzip ./hpe_node_embed_src/node_embed.zip
#mv ./hpe_node_embed_src/node_embed.txt .
mv ./hpe_node_embed_src/src_Makefile ./Makefile
mv ./Makefile ./smore/src/

mv ./hpe_node_embed_src/cli_Makefile ./Makefile
mv ./Makefile ./smore/cli

mv ./hpe_node_embed_src/HPE_node_embed* ./smore/src/model
mv ./hpe_node_embed_src/hpe_node_embed.cpp ./smore/cli

#mv ./hpe_node_embed_src/node_embed.txt .
rm -rf hpe_node_embed_src

cd smore
make
