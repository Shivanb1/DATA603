# <u>Database Management Systems and Data Models</u>

Since there has been a wide usage of unstructured data  (email, chats, photographs, and videos) in recent years, traditional RDBMS was no longer a viable solution for meeting all expectations due to its constraints. This necessitated better and more diverse data interaction options that are meant to increase availability at the price of consistency, which was made possible by NoSql because it overcomes RDBMS restrictions. Data models used by NoSql include key-value stores, columnar databases, document stores, and graph databases.

<br>

![title](images/datalake.jpeg)

### <u>KEY-VALUE STORES </u>

Key- value store - uses key value pairs where key is the unique identifier used to retrieve the it’s associated value. Eg dB: reddis, memecache, Riak.

### <u>DOCUMENT ORIENTED DATABASE</u>

Data here is stored in the form of documents. Each doc has a key it’s unique identifier and the doc itself is the value.
Unlike key value store, the data here each doc contains some kind of metadata that provides a degree of structure to data.
It comes with API or query lang to interact with data.
all the data in Document store Model is stored in one doc and not in tables unlike RDBMS.
Eg DB: Mango DB, Couchbase, Apache couch DB.

### <u>GRAPH DATABASE</u>

They fall as sub category of DOC store model. Here an extra layer layer is addrd to Doc model by highlighting the relations between individual docs. It uses 
Node (•): individual entity( record, doc etc) 
Property: relevant info related to nodes
Edge: it says how two nodes are related(—). Can be directed(shows direction •—>•) or undirected(shows no direction can be two ways •—•)
Eg DB: Neo4j, Arango DB, Orient DB.

### When Should NoSQL Databases Be Used?

Size is important, as is speed, schema-free design, and automated (or simple) replications and scalability.

## <u>OVERVIEW OF DATA LAKE</u>

A data lake is a successful data-driven design pattern for capturing a wide range of data kinds, both old and new, at big scale when it is properly structured. A data lake is defined as a system that allows for rapid ingestion of raw, detailed source data as well as on-the-fly processing of that data for exploration, analytics, and operations. Traditional, latent data methods are still possible.

Because lakes provide the kind of raw data that consumers require for data exploration and discovery-oriented forms of advanced analytics, organizations are embracing the data lake architecture pattern (whether on Hadoop or a relational database). A data lake can also serve as a central repository for both new and old data, allowing for cross-data analytics correlations.




### PRACTICES & PATTERNS OF DATA LAKE

A data lake can offer self-service data practices that both technical and business users require with the correct end-user tools. These methods extract company value from big data, other new data sources, and increasing enterprise data; these resources aren't only cost centers. A data lake can also be used to update and enhance data warehousing, analytics, data integration, and other data-driven applications.

Analytics, new self-service data practices, value from big data, and warehouse modernization are the top benefactors of data lakes, according to this report's survey. Lakes, on the other hand, pose challenges in Hadoop governance, integration, user skills, and security.


For half of data management experts, the data lake is top of mind, but it is not a pressing demand for the other half.

### Reference

https://tdwi.org/articles/2017/03/29/executive-summary-data-lakes.aspx 

https://www.dnsstuff.com/nosql-database-comparison
