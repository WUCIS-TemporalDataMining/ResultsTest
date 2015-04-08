library(ggplot2)
ggQQ = function(lm) {
  # extract standardized residuals from the fit
  d <- data.frame(std.resid = rstandard(lm))
  # calculate 1Q/4Q line
  y <- quantile(d$std.resid[!is.na(d$std.resid)], c(0.25, 0.75))
  x <- qnorm(c(0.25, 0.75))
  slope <- diff(y)/diff(x)
  int <- y[1L] - slope * x[1L]
  
  p <- ggplot(data=d, aes(sample=std.resid)) +
    stat_qq(shape=1, size=3) +           # open circles
    labs(title="Normal Q-Q",             # plot title
         x="Theoretical Quantiles",      # x-axis label
         y="Standardized Residuals") +   # y-axis label
    geom_abline(slope = slope, intercept = int, linetype="dashed")  # dashed reference line
  return(p)
}