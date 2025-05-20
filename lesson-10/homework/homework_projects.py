
from datetime import datetime

# ---------------- Homework 1: ToDo List ----------------
class Task:
    def __init__(self, title, description, due_date, status="Incomplete"):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.status = status

    def mark_complete(self):
        self.status = "Complete"

    def __str__(self):
        return f"{self.title} | {self.description} | Due: {self.due_date} | Status: {self.status}"

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def mark_task_complete(self, title):
        for task in self.tasks:
            if task.title == title:
                task.mark_complete()

    def list_all_tasks(self):
        return [str(task) for task in self.tasks]

    def list_incomplete_tasks(self):
        return [str(task) for task in self.tasks if task.status != "Complete"]


# ---------------- Homework 2: Blog System ----------------
class Post:
    def __init__(self, title, content, author):
        self.title = title
        self.content = content
        self.author = author
        self.created = datetime.now()

    def __str__(self):
        return f"{self.title} by {self.author} at {self.created.strftime('%Y-%m-%d %H:%M')}:\n{self.content}"

class Blog:
    def __init__(self):
        self.posts = []

    def add_post(self, post):
        self.posts.append(post)

    def list_all_posts(self):
        return [str(post) for post in self.posts]

    def posts_by_author(self, author):
        return [str(post) for post in self.posts if post.author == author]

    def delete_post(self, title):
        self.posts = [post for post in self.posts if post.title != title]

    def edit_post(self, title, new_content):
        for post in self.posts:
            if post.title == title:
                post.content = new_content

    def latest_posts(self, count=3):
        return [str(post) for post in sorted(self.posts, key=lambda p: p.created, reverse=True)[:count]]


# ---------------- Homework 3: Banking System ----------------
class Account:
    def __init__(self, account_number, holder_name, balance=0.0):
        self.account_number = account_number
        self.holder_name = holder_name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            return True
        return False

    def __str__(self):
        return f"Account {self.account_number} | {self.holder_name} | Balance: ${self.balance:.2f}"

class Bank:
    def __init__(self):
        self.accounts = []

    def add_account(self, account):
        self.accounts.append(account)

    def find_account(self, account_number):
        for acc in self.accounts:
            if acc.account_number == account_number:
                return acc
        return None

    def deposit_to_account(self, account_number, amount):
        acc = self.find_account(account_number)
        if acc:
            acc.deposit(amount)

    def withdraw_from_account(self, account_number, amount):
        acc = self.find_account(account_number)
        if acc:
            return acc.withdraw(amount)
        return False

    def transfer(self, from_acc, to_acc, amount):
        sender = self.find_account(from_acc)
        receiver = self.find_account(to_acc)
        if sender and receiver and sender.withdraw(amount):
            receiver.deposit(amount)
            return True
        return False

    def display_all_accounts(self):
        return [str(acc) for acc in self.accounts]
