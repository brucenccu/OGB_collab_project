#ifndef HBPR_NODE_EMBED_H
#define HBPR_NODE_EMBED_H

#include "../proNet.h"

/*****
 * HBPR_NODE_EMBED
 * **************************************************************/

class HBPR_node_embed {

    public:
        
        HBPR_node_embed();
        ~HBPR_node_embed();
        
        proNet pnet;

        // parameters
        int dim;                // representation dimensions
        vector< vector<double> > w_vertex;
        vector< vector<double> > w_context;

        // data function
        void LoadEdgeList(string, bool);
        void LoadFieldMeta(string);
        void SaveWeights(string);
        
        // model function
        void Init(int,string);
        void Train(int, int, double, int);

};


#endif
