import gzip
import glob

import os.path
import config
source_dir = os.path.join(config.localunprocessedfolder,'barclays')
dest_dir = os.path.join(config.localunprocessedfolder,'barclays','Ready for daily processing')

for src_name in glob.glob(os.path.join(source_dir, '*.gz')):
    
    base = os.path.basename(src_name)

    dest_name = os.path.join(dest_dir, base[:-3])
    print base,dest_name
    with gzip.open(src_name, 'rb') as infile:
        with open(dest_name, 'wb') as outfile:
            for line in infile:
                outfile.write(line)
