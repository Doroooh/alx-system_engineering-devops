This is a secured 3-server web infrastructure that’s monitored, secured and serves an encrypted traffic. 

The firewalls protect the network from unauthorized and unwanted users , acting as the intermediary between external and internal network, blocking incoming traffic with given criteria. 
The SSL certificate encrypts traffic between web servers and external networks, preventing man-in-the-middle attacks, to protect valuable information. The SSL certificate ensures identification, integrity and privacy. 
Monitoring clients monitors servers and the external network. It analyzes operation and performance of the servers, measuring the overall health. It ensures servers operate as they should. Monitoring tools provide  key metrics on the operations of the servers to the administrators. 
Issues
The SSL can terminate at the load balancer lever leaving traffic between load balancer and web servers, this is unencrypted. 
Having a single MySQL server is a challenge since it isn’t scalable, and often will be a point of failure for web infrastructure. 
Having the setup not easily scalable. Having servers with all the same components makes the components contend for resources in the server. 
