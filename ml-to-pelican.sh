#!/bin/sh
for x in $(find . -type f -iname "*.md"); do
	sed -i '1s/\[tor\]/Title:\ /' $x
	sed -i '/To:\ torservers@xxxxxxxxxxxxx/d' $x
	sed -i '/\<moritz@xxxxxxxxxxxxx\>/d' $x
	sed -i 's/From:/Author:/' $x
	sed -i -e 's:Date\: ..., \([0-9][0-9]\) \([a-zA-Z]\{3\}\) \([0-9]\{4\}\) .*$:Date\: \3-\2-\1:' $x
	sed -i '3s/Jan/01/' $x
	sed -i '3s/Feb/02/' $x
	sed -i '3s/Mar/03/' $x
	sed -i '3s/Apr/04/' $x
	sed -i '3s/May/05/' $x
	sed -i '3s/Jun/06/' $x
	sed -i '3s/Jul/07/' $x
	sed -i '3s/Aug/08/' $x
	sed -i '3s/Sep/09/' $x
	sed -i '3s/Oct/10/' $x
	sed -i '3s/Nov/11/' $x
	sed -i '3s/Dec/12/' $x
done
