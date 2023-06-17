## Stocks App
[Link to cron job example](https://gutsytechster.wordpress.com/2019/06/24/how-to-setup-a-cron-job-in-django/#:~:text=Steps%20to%20setup%20a%20cron%20job%20in%20Django&text=Create%20a%20file%20anywhere%20within,will%20be%20your%20cron%20job.).

[Link to random example](https://www.programiz.com/python-programming/examples/random-number)

### Backend
#### Django
- Folders
  - Controllers
    - trade controller
    - user controller
  - Services
    - cron service
    - trade service (reads)
    - user service
      - init script, and populates the users collection if it is empty
  - Db
    - model, schema, interface
  - Configs
    - port
    - db connection

Services 
- cron job (A scheduled job that runs periodically)
  - Runs every 5 mins 
  - Gets all 10 pre-populated users
  - filter out liquidated users
  - For each,
    - get last wallet_balance
    - Generate random number
    - `random.randint(-100, 100);`
    - check if sum of randon number and wallet_balance is <= 0
      - set wallet_balance to 0
      - is_liquidated to true
    - Create a record for containing the ff:
      - user_id
      - trade_value (profit/loss)
      - wallet_balance
      - is_liquidated (true when the aggregated trade_output <= 100)
      - timestamp
    - Persist the record in you collection 
      - active records (.save() on the record)
      - repository (saving through a repository object)
- read operations
  - get all users
  - get a single user's trades (paginated)
  - get all users' trades (paginated)

### Frontend
Design your components
- React
  - Axios or Fetch api to do your api calls
  - graph/visualization library for React
