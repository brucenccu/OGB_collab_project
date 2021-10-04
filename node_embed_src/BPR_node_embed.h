#ifndef BPR_NODE_EMBED_H
#define BPR_NODE_EMBED_H

#include "../proNet.h"

/*****
 * BPR
 * **************************************************************/

class BPR_node_embed {

    public:
        
        BPR_node_embed();
        ~BPR_node_embed();
        
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
