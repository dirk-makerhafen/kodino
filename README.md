Kodino
======
Kodino is a python library to run Kodi/Xbmc addons without Kodi/Xbmc.
It works for most content providing plugins. It does not work for plugins that draw their own view.

It requires python2, because Kodi/Xbmc addons are python2 only. 

### Dependencys:
```Shell
    apt-get install redis-server ffmpeg python-bs4 unzip
```
```Shell
   pip install redis polib BeautifulSoup4 HTMLParser
```


### Installation:

To install Kodino, first clone this repository:
```Shell
    git clone xx
```

Then, update and upgrade the default repositorys
```Shell
    kodinoPlugins.py update
```
```Shell
    kodinoPlugins.py upgrade
```


### Commandline usage:
```Shell
    kodinoPlugins.py                       # Print this help
    kodinoPlugins.py update                # Download repositorys
    kodinoPlugins.py upgrade               # Download new addon version from repos
    kodinoPlugins.py installed <filter>    # List all installed addons, optional filter by addon id starts with <filter>
    kodinoPlugins.py available <filter>    # List all available addons, optional filter by addon id starts with <filter>
    kodinoPlugins.py install   <addon id>  # Install addon
    kodinoPlugins.py uninstall <addon id>  # Unistall addon   
```

To manually install repositorys/addons, extract/copy them into the plugins folder.     


### Python usages:
```Python
    import kodino
    kodino.plugins.update()
    kodino.plugins.upgrade()
    kodino.plugins.install("plugin.video.youtube")
```

* Get root directory, contains installed addons that provide video content:
```Python
    subitems = kodino.getSubItems()
```
```Python
    [ 
        KodinoItem(title= b'YouTube', isFolder= True, requireKeyboard= False),
        ... 
    ]
```

* Get some subitem, for example youtube:
```Python
    subitems = subitems[0].getSubItems()
```
```Python
    [
        KodinoItem(title= b'[B]Sign In[/B]', isFolder= True, requireKeyboard= False),
        KodinoItem(title= b'Popular right now', isFolder= True, requireKeyboard= False),
        KodinoItem(title= b'Search', isFolder= True, requireKeyboard= False),
        KodinoItem(title= b'Live', isFolder= True, requireKeyboard= False),
        KodinoItem(title= b'Settings', isFolder= True, requireKeyboard= False)
    ]
```

* Navigate to even more subfolders, for example youtubes search page. This returns an item that has requireKeyboard= True.
```Python
    subitems = subitems[2].getSubItems()
```
```Python
    [
        KodinoItem(title= b'[B]New Search[/B]', isFolder= True, requireKeyboard= True)
    ]
```

* Provide keyboard input for an items the has requireKeyboard= True:
```Python
    subitems = subitems.getSubItems("testing")
```
```Python
    [
        KodinoItem(title= b'[B]Channels[/B]', isFolder= True, requireKeyboard= False),
        KodinoItem(title= b'[B]Playlists[/B]', isFolder= True, requireKeyboard= False),
        KodinoItem(title= b'[B]Live[/B]', isFolder= True, requireKeyboard= False),
        KodinoItem(title= b"The Simpsons - Bart's Megaphone Testing", isFolder= False, requireKeyboard= False),
        KodinoItem(title= b'Testing Out Weird Girl Gadgets!', isFolder= False, requireKeyboard= False),
        ...
    ]
```

* Receive actual playback url for non folder items:
```Python
    playbackurl = subitems[3].getPlaybackUrl()
```
```Python
    'https://r3---sn-1gi7zn7e.googlevideo.com/videoplayback?lmt=1440151299790002&fvip=1&gir=yes&ei=Ui37WprwEMOugQeP26PYCA&requiressl=yes&ip=176.10.116.173&key=yt6&ms=au%2Conr&mv=m&mt=1526410494&id=a02c97b070be950e&mn=sn-1gi7zn7e%2Csn-hpa7znsz&mm=31%2C26&signature=D5789B43DABCD43D313407F8B8A31C9CCA008404.7F71C12E3C947D549CEC07A7DC81838649332A4D&ratebypass=yes&ipbits=0&clen=3363343&initcwndbps=593750&itag=18&pl=19&dur=52.337&source=youtube&expire=1526432178&c=WEB&mime=video%2Fmp4&sparams=clen%2Cdur%2Cei%2Cgir%2Cid%2Cinitcwndbps%2Cip%2Cipbits%2Citag%2Clmt%2Cmime%2Cmm%2Cmn%2Cms%2Cmv%2Cpl%2Cratebypass%2Crequiressl%2Csource%2Cexpire'
```

* Receive playback duration, this calls ffprobe on the playback url to determine the action playback length.
This may fail on some sources, in this case it returns 0. 
```Python
    duration = subitems[23].getDuration()
```
```Python
    52
```

### Other 

Method stubs are cutnpaste from https://github.com/romanvm/Kodistubs 
