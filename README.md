# STAR_WARS_EXPLORER
## The Star Wars API


Simple application for retrieving data about character from https://swapi.dev website. Data about characters is stored in csv files and metadata is stored in sqlite3 database

### Things that can be improved:
1. Resloving of TODOs left in the project
2. Fetch button should be disabled until fetching will be finished
3. fetch_collection function in utils.py could be extended with buffering. Now it is writing to file every 10 records.
4. addition of tests for fetch_collection with mocked requests, addition of behaviour for status_code different than 200
5. usage of petl could be wrapped in some functions/class in order for data to be easier managed.
6. DEBUG parameter was left set on True. It should be changed to False for deployment purpose
7. media/collections - I choose media directory for this csv "database" but maybe it should be changed to something more meaningful. Especially if this application is going to be scaled then some common place for storing collections should be used
8. Petl queries should be analysed because there is a space for improvment
9. Logging should be added to utils.py
10. Addition of SSL/HTTPS if it should be deployed.
11. Form for filtering could be added
