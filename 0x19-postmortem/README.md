# Postmortem 

__Issue Summary:__

The duration of the outage lasted from 12:00 PST to 4:00 PST. The impact affected all clients as the root cause of the problem is that the Nginx was listening on the incorrect port and we need to change it to the correct port. It was mapped to port 8080 and needed to be mapped to port 80.

__Timeline:__

12:00 PST - A loud scream from the back of the office revealed one of our worst fears - an error message showing that once we curled the port, the connection was refused. And as all bad things tend to happen, it happened right before lunch break. 

12:30:00 PST - The issue lied in the Nginx installation in which it was listening to the incorrect port.

12:30:00 PST - Though the clocks were ticking and tummies were rumbling the team decided to power through and find the correct port to listen on while Chris ran out to grab tacos. 

1:30:45 PST - Full bellied and with a smile on our faces only a tall glass of Horchata and fish tacos could deliver, we made our way through the trenches to look for the issue. 

1:35:26 PST - We googled the error and follow some debugging steps, such as checking that our webserver is running which it was. We moved on to looking into our sites-enabled file.

1:45:34 PST - Issue is still unresolved. As we try to push through we realize we're not getting anywhere. Some of use ate too many tacos and it's now time for a coffee break with some Pan Dulce to truly be able to reflect on what the issue could be. 

1:55:35 PST - We're officially out of Pan Dulce.

2:00:16 PST - We have found the port we were listening on to be 8080, we decided to change our listening port to 80 using sed command restarted nginx. This worked. Everyone is finally at ease. 

__Root Cause and Resolution:__

The issue is that our NGINX was not listening to port 80. When we tried to curl the page we received a fail to connect to port 80. As soon as we realized the problem we made a script to use for any future changes such as this that may need to be made in the future.

__Corrective and preventative measures:__

Things that we can improve is testing things before commiting to certain changes.
curling the ports as we make changes to make sure all things are working appropriately.



