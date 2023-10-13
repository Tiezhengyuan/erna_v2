"""
download data from NCIB FTP
"""
import os
from ftplib import FTP
from django.conf import settings
from annot.models import Specie

from process.utils import Dir, HandleJson
from .connect_ftp import ConnectFTP
from .connect_ftp2 import ConnectFTP2

ANATOMY_GROUPS = ['archaea', 'bacteria', 'fungi', 'invertebrate', 'plant',
    'protozoa', 'vertebrate_mammalian', 'vertebrate_other', 'viral', ]

class ConnectNCBI(ConnectFTP):
    endpoint = 'ftp.ncbi.nlm.nih.gov'

    def __init__(self):
        super(ConnectNCBI, self).__init__(self.endpoint)
        ref_dir = getattr(settings, 'REFERENCES_DIR')
        self.dir_local = os.path.join(ref_dir, "NCBI")
    
    def download_gene_data(self):
        '''
        download /gene/DATA including subdirectories and files
        '''
        local_files = self.download_tree(
            local_name = os.path.join('NCBI', 'gene', 'DATA'),
            ftp_path = 'gene/DATA',
            file_pattern = '.gz'
        )
        return local_files

    def download_pubmed(self):
        '''
        download /PubMed including subdirectories and files
        '''
        ConnectFTP2.download_tree(
            ftp_endpoint = self.endpoint,
            ftp_path = '/pubmed',
            pattern = '.gz',
            local_path = self.dir_local
        )

    def download_assembly_summary(self):
        '''
        download assembly_summary.txt
        '''
        res = {}
        for antonomy in ANATOMY_GROUPS:
            outdir = os.path.join(self.dir_local, 'assembly_summary', antonomy)
            Dir(outdir).init_dir()
            local_file = self.download_file(
                ftp_path = f'genomes/refseq/{antonomy}/',
                file_name = 'assembly_summary.txt',
                local_path = outdir
            )
            res[antonomy] = local_file
        return res

    def load_species(self):
        '''
        work on model Specie
        1. delete all
        2. load species from assembly_summary
        '''
        # truncate all data
        Specie.objects.all().delete()

        # retrieve data from json
        n = {}
        names = ['taxid', 'organism_name', 'group']
        for antonomy in ANATOMY_GROUPS:
            n[antonomy] = []
            json_file = os.path.join(self.dir_local, 'assembly_summary',\
                antonomy, 'assembly_summary.json')
            obj = HandleJson(json_file).read_json()
            print(obj)
            for _, summary in obj:
                data = dict([(n, summary[n]) for n in names])
                if data['organism_name'] not in n[antonomy]:
                    Specie.objects.create(**data)
                    n[antonomy].append(data['organism_name'])
            n[antonomy] = len(n[antonomy])
        return n


