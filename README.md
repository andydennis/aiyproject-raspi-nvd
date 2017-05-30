# Google/Raspberry Pi AIY Project - NVD reader

New action for the AIYProjects Voice Kit:

https://github.com/google/aiyprojects-raspbian

Reads the latest vulnerability from the NVD RSS feed.

Import or copy and paste the class into the actions.py

Then to the make_actor function add

``` actor.add_keyword(_('nvd latest'), NistLatest(say)) ```


Currently only supports reading the first item. 
