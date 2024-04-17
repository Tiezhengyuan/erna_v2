# eRNA_v2

eRNA_v2 is upgraded from eRNA which is a tool in Perl with GUI interface (Yuan, T., Huang, X., Dittmar, R.L. et al. eRNA: a graphic user interface-based tool optimized for large data analysis from high-throughput RNA sequencing. BMC Genomics 15, 176 (2014). https://doi.org/10.1186/1471-2164-15-176).

eRNA_v2 is a web applicaton for mRNA-seq data analysis (https://www.fbridges.com/erna/erna_introduce). The app aims at fullfilling RNA-seq data analysis at enterprise level.
- Prcess sequencing data determined by mRNA-seq, miRNA-seq, and scRNA-seq etc.
- Manage raw data. fullfill processing up to thousands raw data.
- Allow multiple tasks. Up to hundreds projects inlcuding thousands tasks could be create managed.
- Network connection. The app can be accessed by team members at Group/Division/Department level.
- Inegrate genome annotations into bioinformatic pipelines.

Design and programming of eRNA_v2. 
- Front end is Vue3-JavaScript.
- Back end is Django4-Python3.
- Database is Sqlite/MySQL.
- Bioinformatics pipelines are Python3 tools.


eRNAv2 are composed of multiple modules, which could be deployed separately.
- mirna: that is used for miRNA-Seq data processing. 
    The document is available at https://www.fbridges.com/erna/mierna_install.
    The source code of front-end is at https://github.com/Tiezhengyuan/emirna_frontend.
    The source code of back-end is at https://github.com/Tiezhengyuan/emirna_backend.
- mrna: used for bulk mRNA-Seq (under testing)
- scrna: used for scRNA-Seq (under development)