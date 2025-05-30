import pandas as pd
import corella
import sys

stopping_point = int(sys.argv[1])

# set pandas options
pd.set_option('display.max_columns', None)
pd.set_option('display.expand_frame_repr', False)
pd.set_option('max_colwidth', None) #;

# get occurrences and multimedia into data frames
occurrences = pd.read_csv("corella_user_guide/occurrences_dwc.csv")
multimedia = pd.read_csv("corella_user_guide/multimedia_occ.csv")

# create DwCA with multimedia
my_dwca = corella.dwca(occurrences=occurrences,multimedia=multimedia)
if stopping_point == 1:
    print(my_dwca.check_data())

# do this for last thing
occurrences = pd.read_csv("corella_user_guide/occurrences_dwc_clean.csv")
multimedia = pd.read_csv("corella_user_guide/multimedia_occ.csv")
my_dwca = corella.dwca(occurrences=occurrences,multimedia=multimedia)

# final report example
if stopping_point == 99:
    print(my_dwca.check_data())