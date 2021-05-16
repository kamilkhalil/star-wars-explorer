# STAR_WARS_EXPLORER
## The Star Wars API


Simple application for retrieving data about character from https://swapi.dev website. Data about characters is stored in csv files and metadata is stored in sqlite3 database

### Things that can be improved:
1. Resloving of TODOs left in the project
2. Fetch button should be disabled until fetching will be finished
3. addition of tests for fetch_collection, addition of behaviour for status_code different than 200
4. usage of petl could be wrapped in some functions/class in order for data to be easier managed.
5. DEBUG parameter was left set on True. It should be changed to False for deployment purpose
6. media/collections - I choose media directory for this csv "database" but maybe it should be changed to something more meaningful
7. Petl queries should be analysed because there is a space for improvment
8. Logging should be added
9. Addition of SSL/HTTPS if it should be deployed.
10. Form for filtering could be added
