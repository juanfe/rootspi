FROM rootproject/root-ubuntu18-base

#COPY build.sh build.sh

#ARG uid

#RUN useradd --create-home --home-dir /home/builder/ --uid ${uid} --groups sudo builder && \
#RUN useradd --create-home --home-dir /home/builder/ --groups sudo builder && \
#    passwd --delete builder

#USER builder
#ENV HOME /home/builder
ENV PYTHONPATH /usr/local/lib/root

RUN apt-get clean \
 && apt-get autoclean \
 && Rscript -e 'install.packages("Rcpp",    repos="https://cran.r-project.org")' \
 && Rscript -e 'install.packages("RInside", repos="https://cran.r-project.org")' \
 && rm -rf /var/lib/apt/lists/*

RUN localedef -i en_US -f UTF-8 en_US.UTF-8

RUN git clone https://github.com/root-project/root /usr/src/root \
 && cd /tmp \
 && cmake /usr/src/root -DCMAKE_INSTALL_PREFIX=/usr/local -Dgnuinstall=ON \
 && cmake --build . -- -j$(nproc) \
 && cmake --build . --target install \
 && rm -rf /usr/src/root /tmp/* \
 && echo "/usr/local/lib/root" > /etc/ld.so.conf.d/cern_root.conf \
 && ldconfig
# && cmake /usr/src/root \
#	-Dall=ON \
#	-Dbonjour=OFF \
#	-Dbuiltin_afterimage=OFF \
#    -Dbuiltin_davix=ON \
#	-Dbuiltin_ftgl=OFF \
#	-Dbuiltin_gl2ps=OFF \
#	-Dbuiltin_glew=OFF \
#	-Dbuiltin_unuran=OFF \
#	-Dbuiltin_xrootd=ON \
#	-Dcastor=OFF \
#	-Dcxx14=ON \
#	-Ddcache=ON \
#	-Dfail-on-missing=ON \
#	-Dfortran=ON \
#	-Dgeocad=OFF \
#	-Dgviz=ON \
#	-Djemalloc=ON \
#	-Dkrb5=OFF \
#	-Dldap=OFF \
#	-Doracle=OFF \
#    -Dpgsql=ON \
#	-Dpythia6=ON \
#    -Dpython=ON \
#	-Droot7=ON \
#	-Dr=ON \
#    -Druby=OFF \
#	-Drpath=ON \
#    -Dsqlite=ON \
#	-Dvc=OFF \
#	-Dvdt=OFF \
#	-Dveccore=OFF \
# && cmake --build . -- -j$(nproc) \
# && cmake --build . --target install \
# && rm -rf /usr/src/root /tmp/*
