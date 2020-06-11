# Brainstorm

## Tracking nature of transactions
+ Add a field to the transactions table [type] which would be have choices [credit] [debit].
+ How does a transaction work?
  + Debit transaction?
    +  Withdrawal?
       +  The user goes to the dashboard, inputs [amount] to withdraw,
       +  a debit transaction is raised whose [transaction_amount] is equal to the [amount] given,
       +  and beneficiary is [Self],
       +  if that [amount] + [fee] can be deducted from his [account_balance],
          +  it is deducted from the [account],
          +  and [transaction] is saved
       +  else
          +  [transaction] is NOT saved
          +  raise an insufficient balance error
    +  Transfer?
       +  The user goes to the dashboard and selects the [beneficiary] or creates a new beneficiary if none,
       +  inputs [amount] to transfer,
       +  a debit [transaction] is raised whose [transaction_amount] is equal to the [amount] given,
       +  and beneficiary if [beneficiary],
       +  if that [amount] + [fee] can be deducted from his [account_balance],
          +  it is deducted from the [account],
          +  and [transaction] is saved
       +  else
          +  transaction is NOT saved
          +  raise an insufficient balance error
  +  Credit Transaction?
     +  A credit request is sent in with an [amount] and [account]
     +  if [account] exists,
        +  a credit transaction is raised whose [transaction_amount] is equal to the [amount] in the request
        +  and beneficiary is [Self],
        +  the [account] is credited with the given [amount]
        +  the [transaction] is saved.
     +  else
        +  raise a 404 account not found error