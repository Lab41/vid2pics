# vid2pics
consumes a video writes it out as a series of png files


# build the container:
docker build -f Dockerfile -t vid2pics .


# run against your data
docker run -v/somedir/withvids:/in -v/somedir/output:/out vid2pics
