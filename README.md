# eRNA_v2

eRNA_v2 is upgraded from eRNA which is a tool in Perl with GUI interface (Yuan, T., Huang, X., Dittmar, R.L. et al. eRNA: a graphic user interface-based tool optimized for large data analysis from high-throughput RNA sequencing. BMC Genomics 15, 176 (2014). https://doi.org/10.1186/1471-2164-15-176).

eRNA_v2 is a web applicaton for mRNA-seq data analysis. The app aims at fullfilling RNA-seq data analysis at enterprise level.
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


Source codes of eRNAv2 are composed of multiple  repositories:
- Front-end app (Vue3-JS): https://github.com/Tiezhengyuan/ernav2_frontend/
- Back-end app (Djnago4-Python3): https://github.com/Tiezhengyuan/ernav2_backend/
- DataModel: https://github.com/Tiezhengyuan/ernav2_seqdata
- FileProcess: https://github.com/Tiezhengyuan/bio_file
- SequenceProcess: https://github.com/Tiezhengyuan/bio_sequence
- Download and process omics data: https://github.com/Tiezhengyuan/bio_omics
- Utils: https://github.com/Tiezhengyuan/bio_utils


# Deployment

The app is developed in Linux. Front-end, back-end and data processing are decoupled. It is ok to deploy the three components into different VM depending on the scale of data analysis and complexity of user group.

# References


#mirna docker

```
cd mirna/emirna_frontend
```

```
yarn install
yarn build
```

build image
```
docker-compose build
```

launch instance of container
```
docker-compose up
```