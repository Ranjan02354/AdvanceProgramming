import java.util.ArrayList;

class Account {

    private String accountNumber;
    private String ownerName;
    private double balance;

    public Account(String accountNumber, String ownerName, double balance) {
        this.accountNumber = accountNumber;
        this.ownerName = ownerName;
        this.balance = balance;
    }

    // Constructor chaining
    public Account(String accountNumber, String ownerName) {
        this(accountNumber, ownerName, 0.0);
    }

    public String getAccountNumber() {
        return accountNumber;
    }

    public String getOwnerName() {
        return ownerName;
    }

    public double getBalance() {
        return balance;
    }

    public void setOwnerName(String ownerName) {
        this.ownerName = ownerName;
    }

    protected void setBalance(double balance) {
        this.balance = balance;
    }

    public void deposit(double amount) {
        if (amount <= 0) {
            throw new IllegalArgumentException("Deposit amount must be positive.");
        }

        balance += amount;
        System.out.println("Deposited Rs." + amount + " successfully.");
    }

    public void withdraw(double amount) {
        if (amount <= 0) {
            throw new IllegalArgumentException("Withdrawal amount must be positive.");
        }

        if (amount > balance) {
            throw new IllegalArgumentException(
                    "Insufficient balance. Available: Rs." + balance);
        }

        balance -= amount;
        System.out.println("Withdrawn Rs." + amount + " successfully.");
    }

    public void display() {
        System.out.println("Account Number : " + accountNumber);
        System.out.println("Owner Name     : " + ownerName);
        System.out.println("Balance        : Rs." + balance);
    }
}

class SavingsAccount extends Account {

    private double interestRate;

    public SavingsAccount(String accountNumber, String ownerName,
                          double balance, double interestRate) {
        super(accountNumber, ownerName, balance);
        this.interestRate = interestRate;
    }

    // Constructor chaining
    public SavingsAccount(String accountNumber, String ownerName,
                          double interestRate) {
        this(accountNumber, ownerName, 0.0, interestRate);
    }

    public double getInterestRate() {
        return interestRate;
    }

    @Override
    public void display() {
        super.display();

        double interest = (getBalance() * interestRate) / 100;

        System.out.println("Interest Rate  : " + interestRate + "%");
        System.out.println("Interest Earned: Rs." + interest);
        System.out.println("Account Type   : Savings Account");
    }
}

class CurrentAccount extends Account {

    private double overdraftLimit;

    public CurrentAccount(String accountNumber, String ownerName,
                          double balance, double overdraftLimit) {
        super(accountNumber, ownerName, balance);
        this.overdraftLimit = overdraftLimit;
    }

    // Constructor chaining
    public CurrentAccount(String accountNumber, String ownerName,
                          double overdraftLimit) {
        this(accountNumber, ownerName, 0.0, overdraftLimit);
    }

    public double getOverdraftLimit() {
        return overdraftLimit;
    }

    // Override withdrawal to support overdraft
    @Override
    public void withdraw(double amount) {

        if (amount <= 0) {
            throw new IllegalArgumentException(
                    "Withdrawal amount must be positive.");
        }

        if (amount > getBalance() + overdraftLimit) {
            throw new IllegalArgumentException(
                    "Exceeds overdraft limit. Max withdrawable: Rs."
                            + (getBalance() + overdraftLimit));
        }

        setBalance(getBalance() - amount);

        System.out.println("Withdrawn Rs." + amount + " successfully.");
    }

    @Override
    public void display() {
        super.display();
        System.out.println("Overdraft Limit: Rs." + overdraftLimit);
        System.out.println("Account Type   : Current Account");
    }
}

public class Assignment9 {

    public static void main(String[] args) {

        SavingsAccount savings =
                new SavingsAccount("SAV001", "Riya Sharma", 10000, 4.5);

        CurrentAccount current =
                new CurrentAccount("CUR001", "Arjun Mehta", 5000, 2000);

        // Demonstrate polymorphism
        ArrayList<Account> accounts = new ArrayList<>();
        accounts.add(savings);
        accounts.add(current);

        System.out.println("All Accounts:");

        for (Account account : accounts) {
            account.display();
            System.out.println();
        }

        try {
            savings.deposit(5000);
            savings.withdraw(3000);

            current.deposit(1000);
            current.withdraw(6500);

        } catch (IllegalArgumentException e) {
            System.out.println("Error: " + e.getMessage());
        }

        System.out.println("\nUpdated Account Details:\n");

        savings.display();
        System.out.println();

        current.display();
    }
}