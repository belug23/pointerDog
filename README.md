#PointerDog

Rigth now it's a starting project so it's nothing!

pointerDog is a collection of tool and a website to collect information about your servers to help you find what is wrong, hping to find it before clients call. The project is made in python Pyramid and has  parts to be installed on servers and a part to be installed as a service.

I tried centreon and Nagios and I found it to complex for what it is, I look at Cabot and it's missing some key elements. I've looked at Logstash and tought it would be nice to combine it with something like Nagios and combine log analysing with event happening. So I told my self, le make something that you'll use and maybe others will come.

#Requirements

- Python3
- Python3-dev
- Mongodb-server
- Install the modules from requirements.txt (It may be splitted one for the website and one for the server side apps)

#TODO

- Write tests for all what follows.
- ICMP : Make a ICMP library to watch if servers ar up.
- ICMP relay : Make a offsite ICMP watcher to make sure that it's not only your network that is down.. [Think about this more Belug!]
- HTTP and HTTPS watcher : To check if webservers are still up.
- Website watcher : Check if websites are still responding, may be by watching the OPTION request?
- Database watcher : Check if the database is still up.... [Maybe on client side!]
- Mail{relay, box, filter, ...} watcher : Look at all te part of mail service to determine if everything is working good.
- System updates watchers : Check for updates for the OS, if possible get the changelog to help sysadmin have the knowledge of what the are doing. [This will need to be multiple packages to support all the platforms redhat based, debian based, arch based,... , Windows?, Mac? Solaris?]
- Log catcher : Client side script in a cron job to collect logs and send it to pointerDog.
- Log analyser : Small web interface to setup de logs to get and the format to parse it.
- Log parser : Parse logs using REGEX made by the user and record it in Mongodb.
- Log viewer : Web interface to show the logs and filter the result
- Event Analyser : Addon to the log viewer to combine result from a log file with other logs and event that happends on the network.
  - Example:
    - Event : Apache stopped responding. Show logs from apache and system of the minutes before  to catch what happend
    - Website got hacked : Show access and error logs to determine entry points.
    - Mail server Queue is huge : Show who send to how many when, to help see is a user was hacked.
    - Website busted bandwith limit : Calculate the download size for file from logs and show them in decreasing orders.
- Alert system : Send mails, sms or anything possible to the Sysadmin to warn it.
- REST Api : To build external tools for monitoring.
- Resume Page : To display wath is happening on your network at the moment.
- Configuration pages : To setup the logs, the watchers and the parsers.
- Make depolyements packages : make it easy to install.

# BSD License

Copyright (c) 2014, Alexandre Lessard AKA Belug
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:
    - Redistributions of source code must retain the above copyright
      notice, this list of conditions and the following disclaimer.
    - Redistributions in binary form must reproduce the above copyright
      notice, this list of conditions and the following disclaimer in the
      documentation and/or other materials provided with the distribution.
    - Neither the name of Alexandre Lessard nor the
      names of its contributors may be used to endorse or promote products
      derived from this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL Alexandre Lessard BE LIABLE FOR ANY
DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
(INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
(INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
