Title: Torcollect - A tool to collect statistics from servers that run Tor bridges
Author: Daniel 
Date: 2014-04-02

For the last year i've been developing a tool that collects metrics from bridge servers. The specified application had to extract and collect the data from
each single server that is registered in the system and generate static HTML reports from the received data.

Torcollect is written in Python and uses paramiko to establish ssh connections to its designated servers. It also uses the module pygal to display the
recorded data graphically.

<https://github.com/torservers/torcollect>

Starting development i first developed a database scheme capable of storing all data we
need and even add a few additional features, for example the ability to stor, that
certain organizations were given specific bridges, so we can create reports that only concern
the bridges of those organizations. I continued with gathering some static data, like a
complete list of countries and their abbreviations and a collection of flag images for all
of them (thanks to koppi for assembling a great image library).

After completing the prerequisites i wrote some code to extract data from the bridge servers.
The processing of the data is mostly done on the side of the bridge server to minimize
the amount of transported data and thus increasing performance. Doing so, I struggled a little
with the permissions that Tor enforces on it's server files. I had to do a workaround, that
involves copying the relevant file to a location which the torcollect user has access to. This
has to happen everyday via a cronjob. I find this solution to be sufficient but not very pretty as
it complicates the process of introducing a new server to a torcollect system. Maybe someone 
from the Tor community has a better idea or I may come up with a better solution.
The data is being extraced by appropriately using grep and find. Then I wrote the "collector", 
which is a piece of code that enters the collected datasets into the according relations in the database.

After having the database collecting the data, I experimented with how to display the data.
The first thing i implemented was an overall graph of the bridge usage. I implemented it in
coffeescript, which generated a svg object in the DOM and puts it into the page. After I
experimented around a bit, i discovered the pygal library, which produces very beautiful graphs
with little effort, and changed the static HTML generator to use it. Further, I experimented 
with different efforts to display so called sparklines for each object that is represented in 
the daily reports (countries, bridges, pluggable transport protocols).

Sparklines are a bit tricky because the graphics that are generated sum up to huge amounts
of data. This resulted in roughly 7 MiB per HTTP call even when using gzip compression, which
obviously kills responsiveness of the site. I'd love to have this feature included, because
they simplify detecting sudden changes in the values significantly.

The latest feature I added was creating monthly reports from the collected data. Those monthly
reports can be created for either the whole system or only the bridges of a single organization.

My further efforts will be:

- Trying to create a debian package to install torcollect
- Simplifying the process of setting up more servers
- Creating a better user experience in the UI
