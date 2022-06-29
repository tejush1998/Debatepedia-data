# Debatepedia-data

This code is updated version of data extraction in https://github.com/PrekshaNema25/DiverstiyBasedAttentionMechanism . Since that code no longer works. 

### To crawl the data from scratch :
* The model will extract the data for the categories mentioned in file debatepedia_categories
* sh extract_data.sh
* python make_folds.py ../../data <number_of_folds> <new_dir_for_10_folds> 
* By default run : python make_folds.py ../../data 10 ../../data
