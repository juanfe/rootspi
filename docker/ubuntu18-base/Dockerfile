FROM ubuntu:18.04

COPY packages packages

RUN apt-get update -qq \
 && apt-get -y install debconf-utils apt-utils \
 && echo "Geographic area: 12" | debconf-set-selections \
 && apt-get install tzdata \
 && apt-get -y install $(cat packages) \
 && Rscript -e 'install.packages(c("RInside","Rcpp"), repos="https://cran.r-project.org")' \
 && localedef -i en_US -f UTF-8 en_US.UTF-8 \
 && rm -rf /var/lib/apt/lists/* /tmp/* /packages
