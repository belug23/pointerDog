Rigth now it's a starting project so it's nothing!

#PointerDog

pointerDog is a collection of tool and a website to collect information about your servers to help you find what is wrong, hping to find it before clients call. The project is made in python Pyramid and has  parts to be installed on servers and a part to be installed as a service.

I tried centreon and Nagios and I found it to complex for what it is, I look at Cabot and it's missing some key elements. I've looked at Logstash and tought it would be nice to combine it with something like Nagios and combine log analysing with event happening. So I told my self, le make something that you'll use and maybe others will come.

On top of that I'm a DevOp, I like it when everything is running smoothly, so I can code more! I do like neat UX and think that there's not enough neat interfaces for sysadmins.

#Requirements

- Python3
- Python3-dev
- Mongodb-server
- Install the modules from requirements.txt (It may be splitted one for the website and one for the server side apps)


# The application design is MVCA

Ok, MVCA is made up, since it's not yet a standard, but it's Model View Controller Abstarction. So you take a standard MVC and put all your bussiness logic in an abstraction, a set of class and function outside of MVC. So all your logic is independent of what your app is and when migrating from html pages to javascript REST api, you don't need to rewrite your logic, just the way you handle the http request. Plus it's easier for the tests monster and to debug.

Exemple :

    Action : Add a new Computer.
    Controller : Get the resquest, grab the needed information [POST, current user] and create a new Computer Object.
    Computer Object (Abstraction) : Take all the data he recived, validate it, interact with the model and return result (Positive or negative)
    Controller : get the result, make the response and render if needed.

It's simple, and it answer most of the questions that looks like "Do I put that in the controller or in the model?"

So thanks to Alex Gaynor for this talk : http://youtu.be/yvjmAYmYOj0 that came right a the good moment for this project.

#TODO

- Write tests for all what follows.
- ICMP : Make a ICMP library to watch if servers ar up.
- ICMP relay : Make a offsite ICMP watcher to make sure that it's not only your network that is down.. [Think about this more Belug!]
- HTTP and HTTPS watcher : To check if webservers are still up.
- Website watcher : Check if websites are still responding, may be by watching the OPTION request?
- Database watcher : Check if the database is still up.... [Maybe on client side!]
- Mail{relay, box, filter, ...} watcher : Look at all te part of mail service to determine if everything is working good.
- System updates watchers : Check for updates for the OS, if possible get the changelog to help sysadmin have the knowledge of what the are doing. [This will need to be multiple packages to support all the platforms redhat based, debian based, arch based, BSD based... , Windows?, Mac? Solaris?]
- System watcher : Disk space, load, memory, installed softwares, IP adresses, network load and uptime.
- Virtualenv | rvm watcher : Valide the state of those environements to check if there's update to do.
- Log catcher : Client side script in a cron job to collect logs and send it to pointerDog.
- Log analyser : Small web interface to setup de logs to get and the format to parse it.
- Log parser : Parse logs using REGEX made by the user and record it in Mongodb.
- Alert system : Send mails, sms or anything possible to the Sysadmin to warn it.
- REST Api : To build external tools for monitoring.
- Look for a neat design for the website interfaces.
- Resume Page : To display wath is happening on your network at the moment.
- Configuration pages : To setup the logs, the watchers and the parsers.
- Log viewer : Web interface to show the logs and filter the result.
- Log filtering tool : Easy to to add filters to your log. (Start with a tool on top of the page to add a manual filter, than double clic on a cell to filer for the content. i.e : Search in mail logs for a faulty entry for "toto@example.com" then double click on the the QUEUE ID and to filter only what happend to this transaction and remove the frist filter to see full detail of the transaction)
- Event Analyser : Addon to the log viewer to combine result from a log file with other logs and event that happends on the network.
  - Example:
    - Event : Apache stopped responding. Show logs from apache and system of the minutes before  to catch what happend
    - Website got hacked : Show access and error logs to determine entry points.
    - Mail server Queue is huge : Show who send to how many when, to help see is a user was hacked.
    - Website busted bandwith limit : Calculate the download size for file from logs and show them in decreasing orders.
- Make depolyements packages : make it easy to install.

# Reporting Issue

At the start I'll have a lot of issues for all the todos. If you find a bug, please report it with more than less information if applicable:
- OS version (Name and kernel)
- Python version
- Service version (Apache, nginx or postfix)
- Error logs and backtracks
- Anything you thing could be usefull
- In a neat and ordered Issue post please

# Contributors checklist

If you'd like to help. You welcome just follow those small steps :
- Fork it
- Make a branch per feature
- Make tests and run them for wath you added
- Do your changes. (Yes after writing the tests)
- Comment what you did if it's not explicite. (Yes it's after making the changes, I know must of us don't write comments on the fly)
- If it's not explicite please make it.
- If this add User side stuff, please add documentation. (I'm lazy and don't want to write doc for what you added...)
- Add your name to contrubutors list (Please make it at the same time as your contribution, it could be nice not to have pull request only for a name, I know it's important for you, so don't forget it!)
- Make a pull request.
- I may argue a little and review your code.
- If all is good, Yeah pointerDog is now better thanks to you! I'll be very thankful!

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
