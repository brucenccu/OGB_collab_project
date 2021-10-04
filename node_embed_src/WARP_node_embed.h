#ifndef WARP_NODE_EMBED_H
#define WARP_NODE_EMBED_H

#include "../proNet.h"

/*****
 * WARP_NODE_EMBED
 * **************************************************************/

class WARP_node_embed {

    public:
        
        WARP_node_embed();
        ~WARP_node_embed();
        
        proNet pnet;

        // parameters
        int dim;                // representation dimensions
        vector< vector<double> > w_vertex;

        // data function
        void LoadEdgeList(string, bool);
        void SaveWeights(string);
        
        // model function
        void Init(int,string);
        void Train(int, int, double, double, int);

};


#endif
