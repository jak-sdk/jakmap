jakmap - My JMAP server  

Having a stab at implementing https://jmap.io/spec-core.html

Python - Flask & Sqlalchemy

Goals  
- All state should be in the database or an object store, you should be able to run any number of instances of jakmap backed by the same database / object store combo for redundancy; scaling is secondary but would also benefit from this.
- Keep a generic interface to the db / object store. I'll likely start with Mysql / S3, but someone may want cassandra / cassandra, or sqlite / local mail files
