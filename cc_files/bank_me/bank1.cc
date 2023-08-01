#include <iostream>
#include <string>
#include <map>

class BankAccount {
private:
    int accountNumber;
    std::string accountHolderName;
    double balance;

public:
    BankAccount(int accNum, const std::string& name, double initialBalance)
        : accountNumber(accNum), accountHolderName(name), balance(initialBalance) {}

    int getAccountNumber() const { return accountNumber; }
    const std::string& getAccountHolderName() const { return accountHolderName; }
    double getBalance() const { return balance; }

    void deposit(double amount) { balance += amount; }
    bool withdraw(double amount) {
        if (balance >= amount) {
            balance -= amount;
            return true;
        }
        return false;
    }
};

class BankingSystem {
private:
    std::map<int, BankAccount> accounts;
    int nextAccountNumber;

public:
    BankingSystem() : nextAccountNumber(1000) {}

    int createAccount(const std::string& name, double initialBalance) {
        int newAccountNumber = nextAccountNumber++;
        BankAccount newAccount(newAccountNumber, name, initialBalance);
        accounts.insert({ newAccountNumber, newAccount });
        return newAccountNumber;
    }

    BankAccount* findAccount(int accountNumber) {
        auto it = accounts.find(accountNumber);
        return (it != accounts.end()) ? &it->second : nullptr;
    }
};

int main() {
    BankingSystem bankingSystem;

    int accountNumber = bankingSystem.createAccount("John Doe", 1000.0);
    std::cout << "Account created with number: " << accountNumber << std::endl;

    BankAccount* account = bankingSystem.findAccount(accountNumber);
    if (account) {
        std::cout << "Account holder: " << account->getAccountHolderName() << std::endl;
        std::cout << "Balance: " << account->getBalance() << std::endl;

        account->deposit(500.0);
        std::cout << "Deposited 500.0" << std::endl;
        std::cout << "Balance: " << account->getBalance() << std::endl;

        if (account->withdraw(200.0)) {
            std::cout << "Withdrawn 200.0" << std::endl;
            std::cout << "Balance: " << account->getBalance() << std::endl;
        } else {
            std::cout << "Insufficient balance for withdrawal." << std::endl;
        }
    } else {
        std::cout << "Account not found." << std::endl;
    }

    return 0;
}
