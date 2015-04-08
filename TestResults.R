##
## Import results from Google Docs CSV.
##

library(stringr)
library(magrittr)
library(ggplot2)
library(dplyr)
library(e1071)
source("ggQQ.R")

results <- read.csv("Results - Sheet1.csv", stringsAsFactors=FALSE)

## Add consistent row-names.
results=cbind(name=results[rep(seq(1,172,4),each=4),1],results)

## Set names.
colnames(results)[1:2]=c("Dataset","Transform")

## Remove % symbols, cast as numeric.
results$KNN.Train %<>% str_replace(.,pattern = '%',replacement = '') %>% as.numeric()
results$KNN.Test %<>% str_replace(.,pattern = '%',replacement = '') %>% as.numeric()

## Rename Series Names to something more informative.
results[!grepl(pattern = '(Mirroring)|(Haar Wavelet)|(Daubechies Wavelet)',results$Transform),2]="Original"

## Boxplot
ggplot(results,aes(Transform,KNN.Test))+geom_boxplot()+ylab("Test % Accuracy")

## Show histograms of each Test Set.
ggplot(results,aes(x=KNN.Test))+geom_histogram()+facet_wrap(~Transform)+ylab("Frequency")+xlab("Test % Accuracy")

## Numerical Summary:
results %>% select(Transform,KNN.Test) %>% group_by(Transform) %>% summarise_each(funs(mean,sd,skewness)

## QQ Normality Plots
ggQQ(lm(KNN.Test~Transform,data=results))

## Create the factor structure needed for ANOVA
results$Transform = as.factor(results$Transform)
aovmod = aov(KNN.Test~Transform,data = results)

## Type I Summary
summary(aovmod)

## Print Type III residual SS
drop1(aovmod,~.,test="F")


