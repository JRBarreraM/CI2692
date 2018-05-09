library(plyr)
library(ggplot2)

# read raw data from file
raw.data = read.csv('data.csv', header = T)

# for making plots with facets (~ operator), need the to put data in proper format
data.avg = ddply(raw.data, c('type', 'name', 'size'), summarise, n = length(i), time = mean(time), error = 1.0 - mean(verification))
data.max = ddply(raw.data, c('type', 'name', 'size'), summarise, n = length(i), time = max(time), error = 1.0 - mean(verification))
data.avg$measure = 'avg'
data.max$measure = 'max'
data = rbind(data.avg, data.max)

# plots for search: different algorithms along avg and max running time
pdf('p1.pdf', height=5, width=5)
ggplot(data[data$type == 'search',], aes(x = log2(size), y = 1000 * time)) +
    geom_bar(stat = 'identity') +
    facet_grid(measure ~ name, scales = "free", space = "free") +
    xlab('log(Tamaño entrada)') +
    ylab('Tiempo en milisegundos') +
    ggtitle('Búsqueda en arreglo') +
    theme(plot.title = element_text(hjust = 0.5)) # center title
dev.off()

# plots for sorting: different algorithms along avg and max running time
pdf('p2.pdf', height=5, width=5)
ggplot(data[data$type == 'sorting',], aes(x = log2(size), y = 1000 * time)) +
    geom_bar(stat = 'identity') +
    facet_grid(measure ~ name, scales = "free", space = "free") +
    xlab('log(Tamaño entrada)') +
    ylab('Tiempo en milisegundos') +
    ggtitle('Ordenamiento') +
    theme(plot.title = element_text(hjust = 0.5)) # center title
dev.off()

