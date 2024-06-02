This distributed web infrastructure attempts at reducing the traffic to the primary server through the distribution of the load to a replicated server, balancing the load between server 1 and 2. 

The load balancer has an algorithm that works, using each of the servers behind the load balancer, according to the weights. It ensures the server’s processing time remains equally distributed. The weights are adjusted on the go. 

The HAProxy load balancer enables an active-active that distributes workload across all the nodes, preventing any of the single nodes from overloading. There are several other nodes available to serve, improving the response time In active-passive setup, not all nodes are active. 
The master-slave cluster configures one server, making it the primary server and the other server is the replica of the primary server. The primary server performs read/write requests, while the replica server only performs read requests
The primary node is responsible for the write operations on a write while the replica node processes read operations, thereby decreasing read traffic to the primary node. . 
Issues
It has multiple SPOF, Id the primary MySQl server is down, the site cant make changes to the site. 
The data transmitted over the network isn't encrypted, so hackers can spy on the network. 

There isn't monitoring of the server as they aren't being monitored 
