#include "BPR_node_embed.h"
#include <omp.h>
#include<iostream>
#include<fstream>
#include<vector>
#include<string>

BPR_node_embed::BPR_node_embed() {
    char negative_method[15] = "no_degrees";
    pnet.SetNegativeMethod(negative_method);
}
BPR_node_embed::~BPR_node_embed() {
}

void BPR_node_embed::LoadEdgeList(string filename, bool undirect) {
    pnet.LoadEdgeList(filename, undirect);
}

void BPR_node_embed::SaveWeights(string model_name){

    cout << "Save Model:" << endl;
    ofstream model(model_name);
    if (model)
    {
        model << pnet.MAX_vid << " " << dim << endl;
        for (long vid=0; vid!=pnet.MAX_vid; vid++)
        {
            model << pnet.vertex_hash.keys[vid];
            for (int d=0; d<dim; ++d)
                model << " " << w_vertex[vid][d];
            model << endl;
        }
        cout << "\tSave to <" << model_name << ">" << endl;
    }
    else
    {
        cout << "\tfail to open file" << endl;
    }
}

void BPR_node_embed::Init(int dim,string embed_path) {
    //cout<<"hi"<<endl;
    vector<vector<double>> data;
    data.resize(235868);
    ifstream infile;
    infile.open(embed_path);
    for(long i = 0;i<235868;i++){
        data[i].resize(128);
        for(int j = 0;j<128;j++){
            infile >>data[i][j];
            //cout<<data[i][j]<<endl;
        }
    }
    infile.close();
    this->dim = dim;
    cout << "Model Setting:" << endl;
    cout << "\tdimension:\t\t" << dim << endl;
    //for(int i =0;i<128;i++)
    //    cout<<data[0][i]<<endl;
    w_vertex.resize(pnet.MAX_vid);

    for (long vid=0; vid<pnet.MAX_vid; ++vid)
    {
        w_vertex[vid].resize(dim);
        for (int d=0; d<dim;++d){
            //w_vertex[vid][d] = (rand()/(double)RAND_MAX - 0.5) / dim;
            /*char s1[128];
            strcpy(s1,pnet.vertex_hash.keys[vid]);
            //cout<<s1<<endl;
            s1[0] = ' ';
            s1[1] = ' ';
            w_vertex[vid][d] = data[stol(s1)][d];*/
            w_vertex[vid][d] = data[stol(pnet.vertex_hash.keys[vid])][d];
        }
    }

}


void BPR_node_embed::Train(int sample_times, int negative_samples, double alpha, double reg, int workers){

    omp_set_num_threads(workers);

    cout << "Model:" << endl;
    cout << "\t[BPR]" << endl;

    cout << "Learning Parameters:" << endl;
    cout << "\tsample_times:\t\t" << sample_times << endl;
    cout << "\talpha:\t\t\t" << alpha << endl;
    //cout << "\tregularization:\t\t" << reg << endl;
    cout << "\tworkers:\t\t" << workers << endl;

    cout << "Start Training:" << endl;

    unsigned long long total_sample_times = (unsigned long long)sample_times*1000000;
    double alpha_min = alpha * 0.0001;
    double alpha_last;

    unsigned long long current_sample = 0;
    unsigned long long jobs = total_sample_times/workers;

#pragma omp parallel for
    for (int worker=0; worker<workers; ++worker)
    {

        long v1, v2, v3;
        unsigned long long count = 0;
        double _alpha = alpha;

        while (count<jobs)
        {
            v1 = pnet.SourceSample();
            v2 = pnet.TargetSample(v1);
            v3 = pnet.NegativeSample();

            pnet.UpdateBPRPair(w_vertex, w_vertex, v1, v2, v3, dim, reg, _alpha);

            count ++;
            if (count % MONITOR == 0)
            {
                _alpha = alpha* ( 1.0 - (double)(current_sample)/total_sample_times );
                current_sample += MONITOR;
                if (_alpha < alpha_min) _alpha = alpha_min;
                alpha_last = _alpha;
                printf("\tAlpha: %.6f\tProgress: %.3f %%%c", _alpha, (double)(current_sample)/total_sample_times * 100, 13);
                fflush(stdout);
            }
        }

    }
    printf("\tAlpha: %.6f\tProgress: 100.00 %%\n", alpha_last);

}

