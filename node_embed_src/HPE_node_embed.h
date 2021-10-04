#ifndef HPE_NODE_EMBED_H
#define HPE_NODE_EMBED_H

#include "LINE.h"

/*****
 * HPE_NODE_EMBED
 * **************************************************************/

class HPE_node_embed: public LINE {

    public:
        
        HPE_node_embed();
        ~HPE_node_embed();

        void SaveWeights(string);

        // model function
        void Init(int,string);
        void Train(int, int, int, double, double, int);

};


#endif
