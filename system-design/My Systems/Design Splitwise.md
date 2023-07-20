## **Requirements**

1. Users should be able to create and join groups with their friends and family.
2. Users should be able to add expenses to a group and specify which users participated in the expense.
3. The application should automatically calculate how much each user owes or is owed for each expense based on the sharing settings.
4. Users should be able to make payments towards their debts using various payment methods.
5. Users should be able to view their balances and transaction history with other users.
6. The application should be available as a web and mobile application.

## **API Contracts**

Here are some example API contracts for Splitwise:

1. User API
    - **`/users`** (GET): Get a list of all users.
    - **`/users/:id`** (GET): Get details of a specific user by ID.
    - **`/users`** (POST): Create a new user.
    - **`/users/:id`** (PUT): Update an existing user by ID.
    - **`/users/:id`** (DELETE): Delete a user by ID.
2. Group API
    - **`/groups`** (GET): Get a list of all groups.
    - **`/groups/:id`** (GET): Get details of a specific group by ID.
    - **`/groups`** (POST): Create a new group.
    - **`/groups/:id`** (PUT): Update an existing group by ID.
    - **`/groups/:id`** (DELETE): Delete a group by ID.
3. Expense API
    - **`/expenses`** (GET): Get a list of all expenses.
    - **`/expenses/:id`** (GET): Get details of a specific expense by ID.
    - **`/expenses`** (POST): Create a new expense.
    - **`/expenses/:id`** (PUT): Update an existing expense by ID.
    - **`/expenses/:id`** (DELETE): Delete an expense by ID.
4. Payment API
    - **`/payments`** (GET): Get a list of all payments.
    - **`/payments/:id`** (GET): Get details of a specific payment by ID.
    - **`/payments`** (POST): Create a new payment.
    - **`/payments/:id`** (PUT): Update an existing payment by ID.
    - **`/payments/:id`** (DELETE): Delete a payment by ID.

## **Database Design**

Here is an example database schema for Splitwise:

1. Users table:
    - user_id (primary key)
    - name
    - email
    - password
2. Groups table:
    - group_id (primary key)
    - name
3. GroupMembers table:
    - group_id (foreign key to Groups.group_id)
    - user_id (foreign key to Users.user_id)
4. Expenses table:
    - expense_id (primary key)
    - description
    - amount
    - group_id (foreign key to Groups.group_id)
5. ExpenseParticipants table:
    - expense_id (foreign key to Expenses.expense_id)
    - user_id (foreign key to Users.user_id)
    - share
6. Payments table:
    - payment_id (primary key)
    - expense_id (foreign key to Expenses.expense_id)
    - user_id (foreign key to Users.user_id)
    - amount
    - payment_method_id
7. PaymentMethods table:
    - payment_method_id (primary key)
    - name
8. Debts table:
    - debt_id (primary key)
    - user_owed_id (foreign key to Users.user_id)
    - user_owing_id (foreign key to Users.user_id)
    - amount

## **Algorithms**

Here is an algorithm for calculating how much each user owes or is owed for an expense:

1. Retrieve the expense details and participants from the database.
2. Calculate the total amount of the expense.
3. Calculate the total number of shares in the expense.
4. Calculate the amount per share by dividing the total amount by the total shares.
5. For each participant:
    - Calculate the participant's share of the expense based on their specified share percentage.
    - Subtract any payments made by the participant.
    - Calculate the net balance for each participant.
6. Store the net balances in the Debts table in the database.

Here is an example implementation of the algorithm in Python:

```python
def calculate_balances(expense):
    total_amount = expense.amount
    total_shares = sum(expense.shares)
    per_share = total_amount / total_shares
    balances = {}
    for i in range(len(expense.users)):
        balance = expense.shares[i] * per_share - expense.payments[i]
        balances[expense.users[i]] = balance
    return balances
```

In this algorithm, the **`expense`** object represents an expense with the amount, shares, users, and payments. The algorithm calculates the balance owed by each user and returns a dictionary of balances.

## **Capacity Estimation**

To estimate the capacity required for Splitwise, we need to consider factors such as user base, daily active users, concurrent requests, and database load. Let's assume the following estimates:

- Users: 1 million
- Daily active users: 100,000
- Concurrent requests: 10,000
- Database load: 10 read requests per second, 5 write requests per second

1. **User Base**: 1 million active users.
2. **Workload**: 100,000 daily transactions.
3. **Concurrent Users**: 10,000 concurrent users.
4. **Request Patterns**: 60% read operations, 40% write operations.
5. **Performance Goals**: Maximum response time of 500 milliseconds, throughput of 1,000 transactions per second.
6. **Infrastructure and Resources**:
    - CPU and Memory: Start with a baseline of 4 CPU cores and 8GB RAM.
    - Database: Estimate database size based on average transaction size and user data.
    - Networking: Ensure sufficient network bandwidth to handle the traffic.

Let's make some assumptions for the back-of-the-envelope estimation:

- Each transaction involves an average of 10 database read/write operations.
- The average transaction size is 1 KB.
- Network bandwidth of 1 Gbps is sufficient.
- Each server can handle 250 concurrent users.

Based on these assumptions, we can estimate the required resources:

1. **CPU and Memory**:
    - Since each transaction involves 10 database operations, we can estimate that each transaction takes approximately 50 milliseconds (500 milliseconds divided by 10 operations).
    - To achieve a throughput of 1,000 transactions per second, we would need at least 20 CPU cores (1,000 transactions per second divided by 50 milliseconds per transaction).
    - Allocate a minimum of 32GB RAM to support the increased CPU capacity.
2. **Database**:
    - Assuming an average transaction size of 1 KB, with 100,000 daily transactions, the total daily data processed would be approximately 100 MB (100,000 transactions multiplied by 1 KB).
    - Estimate the database size based on historical data or user data growth patterns. Let's assume a database size of 1 GB.
    - Ensure the database is optimized with appropriate indexing and caching mechanisms to handle the expected workload.
3. **Networking**:
    - With a network bandwidth of 1 Gbps, it can handle the required traffic volume. Ensure proper network optimization to handle concurrent connections.
4. **Scaling**:
    - To accommodate 10,000 concurrent users, we would need at least 40 application servers (10,000 concurrent users divided by 250 users per server). This assumes a load balancer distributes the traffic evenly across servers.
    - Implement auto-scaling mechanisms to dynamically add or remove servers based on demand.

Here's the complete code for the Simplify Debt feature in Java:

```java
import java.util.ArrayList;
import java.util.Comparator;
import java.util.List;
import java.util.stream.Collectors;

class User {
    private String name;
    private double balance;

    public User(String name, double balance) {
        this.name = name;
        this.balance = balance;
    }

    public String getName() {
        return name;
    }

    public double getBalance() {
        return balance;
    }

    public void updateBalance(double amount) {
        balance += amount;
    }
}

class Group {
    private List<User> users;

    public Group(List<User> users) {
        this.users = users;
    }

    public List<User> getUsers() {
        return users;
    }
}

class DebtCalculator {
    public static void calculateDebts(List<User> users) {
        // Calculate net amount owed by each user
        for (User user : users) {
            double netAmount = 0.0;
            for (User otherUser : users) {
                if (!user.equals(otherUser)) {
                    netAmount += calculateIndividualDebt(user, otherUser);
                }
            }
            user.updateBalance(netAmount);
        }
    }

    private static double calculateIndividualDebt(User debtor, User creditor) {
        // Retrieve transactions between the debtor and creditor from the database
        List<Transaction> transactions = retrieveTransactions(debtor, creditor);

        double totalDebt = 0.0;
        for (Transaction transaction : transactions) {
            if (transaction.getPayer().equals(debtor)) {
                totalDebt += transaction.getAmount();
            } else {
                totalDebt -= transaction.getAmount();
            }
        }

        return totalDebt;
    }

    private static List<Transaction> retrieveTransactions(User debtor, User creditor) {
        // Implement database query logic to retrieve transactions between debtor and creditor
        // Return the list of transactions
    }
}

class GroupTransaction {
    private List<String> participants;
    private double totalAmount;

    public GroupTransaction() {
        participants = new ArrayList<>();
        totalAmount = 0.0;
    }

    public void addDebt(User debtor, User creditor, double amount) {
        participants.add(debtor.getName() + " owes " + creditor.getName() + " $" + amount);
        totalAmount += amount;
    }

    public List<String> getParticipants() {
        return participants;
    }

    public double getTotalAmount() {
        return totalAmount;
    }
}

class DebtSimplifier {
    public static GroupTransaction simplifyDebt(Group group) {
        List<User> users = group.getUsers();

        // Calculate net amount owed by each user
        DebtCalculator.calculateDebts(users);

        // Sort users based on balances
        List<User> positiveBalances = users.stream()
                .filter(user -> user.getBalance() > 0)
                .sorted(Comparator.comparingDouble(User::getBalance))
                .collect(Collectors.toList());

        List<User> negativeBalances = users.stream()
                .filter(user -> user.getBalance() < 0)
                .sorted(Comparator.comparingDouble(User::getBalance).reversed())
                .collect(Collectors.toList());

        // Create GroupTransaction object
        GroupTransaction transaction = new GroupTransaction();

        // Allocate debts from positive balance users to negative balance users
        for (User debtor : positiveBalances) {
            for (User creditor : negativeBalances) {
                double amountToPay = Math.min(Math.abs(debtor.getBalance()), Math.abs(creditor.getBalance()));
                transaction.addDebt(debtor, creditor, amountToPay);
                debtor.updateBalance(-amountToPay);
                creditor.updateBalance(amountToPay);

                if (debtor.getBalance() == 0) {
                    break;
                }
            }
        }

        return transaction;
    }
}

public class Main {
    public static void main(String[] args) {
        // Create users
        User user1 = new User("Alice", -30.0);
        User user2 = new User("Bob", 10.0);
        User user3 = new User("Charlie", 20.0);
        User user4 = new User("David", 0.0);

        // Create group
        List<User> users = new ArrayList<>();
        users.add(user1);
        users.add(user2);
        users.add(user3);
        users.add(user4);

        Group group = new Group(users);

        // Simplify debt
        GroupTransaction transaction = DebtSimplifier.simplifyDebt(group);

        // Print simplified debt details
        System.out.println("Participants:");
        for (String participant : transaction.getParticipants()) {
            System.out.println(participant);
        }
        System.out.println("Total Amount: $" + transaction.getTotalAmount());
    }
}
```

In this code, we have the **`User`** class representing a user with their name and balance. The **`Group`** class represents a group with a list of users. The **`DebtCalculator`** class is responsible for calculating the net amount owed by each user. The **`GroupTransaction`** class represents the consolidated debt transaction, which keeps track of the participants and the total amount.

The **`DebtSimplifier`** class contains the **`simplifyDebt`** method that implements the debt simplification algorithm. It calculates the debts, sorts the users based on their balances, creates a **`GroupTransaction`** object, and allocates the debts from users with positive balances to users with negative balances.

In the **`Main`** class, we create users, form a group, call the **`simplifyDebt`** method, and print the participants and the total amount of the simplified debt.