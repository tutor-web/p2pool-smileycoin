Requirements:
-------------------------
Generic:
* Smileycoin >=3.0
* Python >=2.6
* Twisted >=10.0.0
* python-argparse (for Python =2.6)

Linux:
* sudo apt-get install python-zope.interface python-twisted python-twisted-web
* sudo apt-get install python-argparse # if on Python 2.6

Windows:
* Install Python 2.7: http://www.python.org/getit/
* Install Twisted: http://twistedmatrix.com/trac/wiki/Downloads
* Install Zope.Interface: http://pypi.python.org/pypi/zope.interface/3.8.0
* Install python win32 api: http://sourceforge.net/projects/pywin32/files/pywin32/Build%20218/
* Install python win32 api wmi wrapper: https://pypi.python.org/pypi/WMI/#downloads
* Unzip the files into C:\Python27\Lib\site-packages


In order to run P2Pool with the various pow-algorithms, you would need to build and install
each module.

Inside each module run the following command

Linux:

    sudo python setup.py install

Windows (mingw):
* Install MinGW: http://www.mingw.org/wiki/Getting_Started
* Install Python 2.7: http://www.python.org/getit/

In bash type this:

    C:\Python27\python.exe setup.py build --compile=mingw32 install



Running P2Pool:
-------------------------
To use P2Pool, you must be running your own local smileycoind. For standard
configurations, using P2Pool should be as simple as:

    python run_p2pool.py --net {network_name} 

Replace {network_name} with the following depending on the algorithm:

* Scrypt - smileycoinScrypt
* Skein - smileycoinSkein
* Groestl - smileycoinGroestl
* Qubit - smileycoinQubit

To make your node accessible from the internet, open the following ports on your router (both the worker port and peer-2-peer port please!):

* Scrypt Worker Port = 11330; Peer-2-Peer Port = 11320
* Skein: Worker Port = 11430; Peer-2-Peer Port = 11420
* Qubit: Worker Port = 11530; Peer-2-Peer Port = 11520
* Groestl: Worker Port = 11630; Peer-2-Peer Port = 11620

To run your mining program ui, point your browser to 127.0.0.1:worker_port

Run for additional options:

    python run_p2pool.py --help

