# STAR_WARS_EXPLORER
## The Star Wars API


Simple application for retrieving data about character from https://swapi.dev website. Data about characters is stored in csv files and metadata is stored in sqlite3 database

### Things that can be improved:
1. Resloving of TODOs left in the project (excpetion handling, data validation, problems encountered with petl)
2. DEBUG parameter was left set on True. It should be changed to False for deployment purpose
3. media/collection - I choose media directory for this csv "database" but maybe it should be changed to something more meaningful
4. Petl queries should be analysed because there is a space for improvment
5. Logging should be added
6. Addition of SSL/HTTPS if it should be deployed.
7. Addition of django forms (at least for filter form)
