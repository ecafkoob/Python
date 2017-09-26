import numpy as np
from os import sys, path
import urllib2
import json
import sys

if __name__ == '__main__':
    gene_info_file = sys.argv[1]
    output_file = sys.argv[2]
    start = int(sys.argv[3])
    geneLen = int(sys.argv[4])
    res = np.loadtxt("jk.csv", dtype=int)
    outputStrings = []
    for i in range(start, start + geneLen):
        print (i + 1), '/', len(res)
        gids = res[i]
        url = 'http://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi?db=gene&id=' + repr(gids) + '&retmode=json'
        print(url)

        data = json.load(urllib2.urlopen(url))
        geneId = str(gids)
        zongjie = data['result'][str(gids)]['summary']
        if zongjie == '':
            continue
        description = data['result'][str(gids)]['description']
        maplocation = data['result'][str(gids)]['maplocation']
        name = data['result'][str(gids)]['name']
        outputStrings.append(name + '||||' + geneId + '||||' + description + '||||' + maplocation + '||||' + zongjie)
    np.savetxt(output_file, outputStrings, fmt='%s')
