# OceanHackWeek22 Project
## Nutrients Clustering on H.O.T
Clusters in profiles of nutrients and their correlation with phytoplankton communities

---
### Collaborators

Laurel Meke  
Nate Lauffenburger  
Xinjin Li  
Mariam Garcia  
Sara Delawalla  

---
### Goals

We aimed to:  
Identify clusters in the distribution of nutrients across a certain location 
Identify clusters in the distribution of nutrients from mid depth to surface level waters 
Identify patterns between the clusters of nutrients, concentrations of chlorophyll, and species of phytoplankton present 
Tie in any connection between the nutrient profiles to chlorophyll’s depth profile 

### Datasets

We use Bottle Data HOT from https://simonscmap.com/catalog/datasets/HOT_Bottle_ALOHA. This data collection contains bottle data from the Hawaii Ocean
Time-series (HOT) program for the time period 1988 until 2008.

![image](https://user-images.githubusercontent.com/73109234/185674008-c4ff834c-a9fb-4f21-8d78-026efb698208.png)

data were downloaded from Ocean Data View. 

### Workflow

1. Data Pre-processing[Subset + Nutrients vs. Depth] 
2. Dimension Reduction [PCA] 
3. Clustering Analysis [Gaussian Mixture Model / KMeans] 
4. Data Visualization 
4.1 T-SNE (T-distributed Stochastic Neighbor Embedding) 
4.2 Chlorophyll vs. cluster labels 
5. Supervised Learning 


