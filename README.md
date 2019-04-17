# CloudComputingHW4
## Hadoop Python Map Reduce
This repo is used to count the number of each type of vehicle that was involved in an accident in New York City 
based on the data at https://data.cityofnewyork.us/Public-Safety/NYPD-Motor-Vehicle-Collisions/h9gi-nx95.
This code is ran using the hadoop-streaming jar and the mapper and reducer python scripts in this repository.
An example of the expected output can be found in output.txt.

## Running
1. Put the data set on hadoop with `hadoop fs -put /path/to/nyc.data /home/<username>/`
2. Make sure you are in the root directory of this repo
3. Run the command to start the job

```hadoop jar /usr/hdp/3.1.0,0-78/hadoop-mapreduce/hadoop-streaming.jar -file mapper.py -mapper mapper.py -file reducer.py -input reducer.py -input /path/to/nyc.data -output /path/to/output```

4. Check the output with `hadoop fs -cat /path/to/output/part-00000 | less`
