bank_balance = 4583.11
withdraw_amount = 250

if withdraw_amount <= bank_balance
    bank_balance -= withdraw_amount
    print("Withdrew ", withdraw_amount, " from your account")
end
