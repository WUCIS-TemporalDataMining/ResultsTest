##
## Import results from Google Docs CSV.
##

library(stringr)
library(magrittr)
library(ggplot2)

results <- read.csv("C:/Users/rrutherf/Downloads/Results - Sheet1.csv", stringsAsFactors=FALSE)

## Add consistent row-names.
results=cbind(name=results[rep(seq(1,172,4),each=4),1],results)

## Set names.
colnames(results)[1:2]=c("Dataset","Transform")

## Remove % symbols, cast as numeric.
results$KNN.Train %<>% str_replace(.,pattern = '%',replacement = '') %>% as.numeric()
results$KNN.Test %<>% str_replace(.,pattern = '%',replacement = '') %>% as.numeric()

## Rename Series Names to something more informative.
results[!grepl(pattern = '(Mirroring)|(Haar Wavelet)|(Daubechies Wavelet)',results$Transform),2]="Original"

## QQ Normality Plots
qplot(sample=results$KNN.Test,data=results,stat="qq",main = "QQ Plots",xlab = "Theoretical",ylab = "Observations",facets=~Transform)



## Create the factor structure needed for ANOVA
results$Transform = as.factor(results$Transform)
aovmod = aov(KNN.Test~Transform,data = results)

## Type I Summary
summary(aovmod)

## Print Type III residual SS
drop1(aovmod,~.,test="F")

