#!/bin/bash
for i in {0..10..1}
do
	wget https://ftp.ncbi.nlm.nih.gov/blast/db/"nt.0$i.tar.gz"
done