The project outlines a simple web infrastructure  for a single server to host a website that’s reachable through www.foobar.com. 
In simple web, there aren't firewalls or SSL certificates to protect the network of my server. 

The process entails mybrowser request on the www.foobar.com. The DNS sends a query, solving www.foobar.com to the IP address 8.8.8.8, sends to the servers. The server processes the request and sends back an ideal response. 
The server is a virtual or physical machine with IP 8.8.8. That will host my web infrastructure.The server is the central piece of virtual machine or hardware which runs the database, application and web server. 
Domain name, foobar.com and www. Is the subdomain pointing to the server’s IP address. 
DNS Record: In www.foobar.com, the www is an A record in DNS, that maps the domain or subdomain to the IP address of the server. 
Nginx is the web server that will handle my incoming HTTP requests and forward dynamic requests to the app server. 
The app ( application server) processes my dynamic request, running application logic and interacting with the database. 
The application files are the codebase containing my website's application logic. 
My database, MySQL, stores and manages data that’s needed by application.
The server uses HTTP and HTTPS protocols in communicating with mybrowser. It sends and receives data packets. 
Issues
SPOF is the single point of failure. If the server is down, the website will be unavailable.
Downtime during maintenance is updating a software requiring the server to be restarted, which causes temporary downtime. 
It's possible for the single server to be overwhelmed with high traffic that results in crashes or the slow response time. It cannot scale horizontally. 
