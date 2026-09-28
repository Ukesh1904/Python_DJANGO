excuted_args = set()

def privilage(func):
    def inner(user, *args, **kwargs):
        if user not in  excuted_args:
            excuted_args.add(user)
            if user.lower() == "ayush":
                return func(user, *args, **kwargs)
            else:
                print("You are not allowed to access the function.")
        else:
            print("The function has already been executed for this user.")
    return inner

@privilage 
def is_admin(user, *args, **kwargs):
    print("Welcome Admin: ", user)

is_admin("ayush")
is_admin("ram")
is_admin("shyam")
is_admin("ram")
is_admin("shyam")
is_admin("ayush")