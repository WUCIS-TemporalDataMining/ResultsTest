##
## Import results from Google Docs CSV.
##

library(stringr)
library(magrittr)

results <- read.csv("C:/Users/rrutherf/Downloads/Results - Sheet1.csv", stringsAsFactors=FALSE)

## Add consistent row-names.
results=cbind(name=results[rep(seq(1,172,4),each=4),1],results)

## Remove % symbols, cast as numeric.
results$KNN.Train %<>% str_replace(.,pattern = '%',replacement = '') %>% as.numeric()
results$KNN.Test %<>% str_replace(.,pattern = '%',replacement = '') %>% as.numeric()

