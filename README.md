# Gophishpaste

This Python script allows you to copy email templates, landing pages, and SMTP sending profiles between different users in a GoPhish SQLite database. It provides a command-line interface for selecting and transferring these resources efficiently.
**Features**

1.Copy email templates from one user to another.

2.Transfer landing pages while checking for duplicate names.

3.Move SMTP sending profiles securely between users.

4.Prevents overwriting by checking for existing templates, pages, or profiles in the destination user account.

5.Uses a user-friendly table display with the tabulate library.
        
**Prerequisites**

1.Python 3.x installed on your machine.

2.Have access to gophish server and gophish Sqllite database.

3.Install the tabulate library for pretty-printed tables:
```


```
git clone

```

**Output**


```
╒════╤════════════╕
│ ID │ Username   │
╞════╪════════════╡
│ 1  │ admin      │
│ 2  │ testuser   │
╘════╧════════════╛
Enter the source userid
> 1
Enter the Destination userid
> 2
1. Email template
2. Landing pages
3. Sending profiles
4. Exit
>> 1
Email template
╒════╤════════════════╕
│ ID │ Name           │
╞════╪════════════════╡
│ 1  │ Welcome Email  │
│ 2  │ Password Reset │
╘════╧════════════════╛
Enter your email template ID (Enter b to back): 1
Template does not exist for the destination user. You can proceed.
The email template updated successfully
```
