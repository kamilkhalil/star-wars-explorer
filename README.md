# STAR_WARS_EXPLORER
## The Star Wars API


Simple application for retrieving data about character from https://swapi.dev website. Data about characters is stored in csv files and metadata is stored in sqlite3 database

### Things that can be improved:
1. Resloving of TODOs left in the project (excpetion handling, data validation, problems encountered with petl)
2. Application was made in the name of rule "Make it work, make it right, make it fast" and it is somewhere between first and second step
3. DEBUG parameter was left set on True. It should be changed to False for deployment purpose
4. media/collection - I choose media directory for this csv "database" but maybe it should be changed to something more meaningful
5. Petl queries should be analysed because there is a space for improvment
6. Logging should be added
7. This application has just sample test. More of them should be added to cover all possible scenarios.
8. Addition of SSL/HTTPS if it should be deployed.
9. Addition of django forms (at least for filter form)
